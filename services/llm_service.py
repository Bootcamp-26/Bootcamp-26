"""
LLM service layer.
Abstracts away whether we're calling local Ollama (dev) or Groq API (prod).
"""
from config import config


def _ollama_generate(prompt: str, model: str, system: str = None) -> str:
    import ollama
    client = ollama.Client(host=config.OLLAMA_HOST)
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    resp = client.chat(model=model, messages=messages)
    return resp["message"]["content"]


def _groq_generate(prompt: str, system: str = None) -> str:
    from groq import Groq
    client = Groq(api_key=config.GROQ_API_KEY)
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    resp = client.chat.completions.create(
        model=config.GROQ_MODEL,
        messages=messages,
    )
    return resp.choices[0].message.content


def generate_ideas(theme: str, n: int = 5) -> list[str]:
    """
    Generate a list of idea suggestions based on a given theme.

    Args:
        theme: The topic/theme the user entered.
        n: Number of ideas to generate.

    Returns:
        A list of strings, each representing one idea
        (e.g. "Idea title - short description").
    """
    system = (
        "You are a creative idea generation assistant. "
        "Given a theme, suggest concrete and actionable ideas. "
        "You respond ONLY with the requested list — no greetings, "
        "no closing remarks, no follow-up questions, no extra commentary."
    )
    prompt = (
        f"Theme: {theme}\n\n"
        f"Suggest {n} original project/startup ideas for this theme. "
        "Give each idea as one line: a short title + one-sentence description. "
        "Respond ONLY with a numbered list (1. 2. 3. ...) of exactly "
        f"{n} items. Do not include any text before or after the list."
    )

    if config.is_dev:
        raw = _ollama_generate(prompt, config.OLLAMA_IDEA_MODEL, system)
    else:
        raw = _groq_generate(prompt, system)

    ideas = [
        line.strip()
        for line in raw.split("\n")
        if line.strip() and line.strip()[0].isdigit()
    ]
    return ideas


def chat_with_context(user_question: str, context_chunks: list[str], history: list[dict]) -> str:
    """
    Generate a chat response using retrieved RAG context and conversation history.

    Args:
        user_question: The current question from the user.
        context_chunks: List of relevant text chunks retrieved from the RAG pipeline.
        history: Previous conversation turns, each as {"role": "user"/"assistant", "content": str}.

    Returns:
        A string containing the assistant's response.
    """
    if context_chunks:
        context_text = "\n\n---\n\n".join(context_chunks)
    else:
        context_text = "No relevant sources were found for this question."

    system = (
        "You are an idea development assistant. Answer the user's questions "
        "about their selected idea using ONLY the context provided below, "
        "which was collected from the web. If the context does not contain "
        "enough information to answer, say so honestly instead of guessing."
    )
    prompt = f"CONTEXT:\n{context_text}\n\nQUESTION:\n{user_question}"

    messages = [{"role": "system", "content": system}]
    messages.extend(history)
    messages.append({"role": "user", "content": prompt})

    if config.is_dev:
        import ollama
        client = ollama.Client(host=config.OLLAMA_HOST)
        resp = client.chat(model=config.OLLAMA_CHAT_MODEL, messages=messages)
        return resp["message"]["content"]
    else:
        from groq import Groq
        client = Groq(api_key=config.GROQ_API_KEY)
        resp = client.chat.completions.create(model=config.GROQ_MODEL, messages=messages)
        return resp.choices[0].message.content