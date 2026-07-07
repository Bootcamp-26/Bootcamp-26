
"""
LLM service layer.
Abstracts away whether we're calling local Ollama (dev) or Groq API (prod).
Function signatures are finalized here; implementation is stubbed for now.
"""


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
    raise NotImplementedError("To be implemented in a future issue")


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
    raise NotImplementedError("To be implemented in a future issue")