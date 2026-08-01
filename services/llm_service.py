"""
LLM service layer.
Abstracts away whether we're calling local Ollama (dev) or Groq API (prod).
"""
from config import config

class LLMServiceError(Exception):
    """Raised when an LLM provider (Ollama or Groq) call fails."""
    pass

def _ollama_generate(prompt: str, model: str, system: str = None) -> str:
    import ollama
    try:
        client = ollama.Client(host=config.OLLAMA_HOST)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        # Yaratıcılığı artırmak ve farklı çıktılar almak için temperature değerini 0.85 yapıyoruz
        resp = client.chat(model=model, messages=messages, options={"temperature": 0.85})
        return resp["message"]["content"]
    except ConnectionError:
        raise LLMServiceError(
            "Could not connect to Ollama. Make sure Ollama is running "
            "(try 'ollama serve') and the model is available."
        )
    except Exception as e:
        raise LLMServiceError(f"Ollama request failed: {e}")


def _groq_generate(prompt: str, system: str = None) -> str:
    from groq import Groq
    try:
        client = Groq(api_key=config.GROQ_API_KEY)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        # Yaratıcılığı artırmak ve farklı çıktılar almak için temperature değerini 0.85 yapıyoruz
        resp = client.chat.completions.create(
            model=config.GROQ_MODEL,
            messages=messages,
            temperature=0.85,
        )
        return resp.choices[0].message.content
    except Exception as e:
        raise LLMServiceError(f"Groq request failed: {e}")


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
    import random
    
    # Modelin her istekte farklı bakış açıları geliştirmesi için rastgele bir odak açısı seçiyoruz
    ANGLES = [
        "mobil öncelikli çözümler",
        "toplumsal fayda ve sürdürülebilirlik",
        "bireysel kullanım kolaylığı ve hız",
        "işletmeler arası (B2B) verimlilik ve SaaS model",
        "maliyet tasarrufu ve ekonomik çözümler",
        "yapay zeka otomasyonu ve zaman tasarrufu",
        "topluluk oluşturma ve sosyal etkileşim",
        "veri analitiği, kişiselleştirme ve tahminleme",
        "oyunlaştırma ve kullanıcı bağlılığı",
    ]
    angle = random.choice(ANGLES)

    system = (
        "Sen yaratıcı bir proje/startup fikri üretme asistanısın. "
        "Verilen tema hakkında somut ve uygulanabilir fikirler önerirsin. "
        "Kesinlikle Türkçe yanıt vermelisin. "
        "Sadece istenen listeyi dönmelisin — selamlama, kapanış, ek açıklama yok."
    )
    prompt = (
        f"Tema: {theme}\n"
        f"Bakış Açısı Odağı: Fikirleri özellikle '{angle}' perspektifinden ele alarak geliştir.\n\n"
        f"Bu tema için {n} adet özgün proje/startup fikri öner. "
        "Her bir fikri tek bir satırda ver: kısa bir başlık + bir cümlelik açıklama. "
        "Sadece numaralandırılmış bir liste (1. 2. 3. ...) olarak yanıt ver ve tam olarak "
        f"{n} adet fikir içersin. Listenin önüne veya arkasına hiçbir metin ekleme."
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


def chat_with_context(user_question: str, context_chunks: list[dict], history: list[dict], selected_idea: str) -> str:
    """
    Generate a chat response using retrieved RAG context and conversation history.

    Args:
        user_question: The current question from the user.
        context_chunks: List of relevant dictionaries retrieved from the RAG pipeline.
        history: Previous conversation turns, each as {"role": "user"/"assistant", "content": str}.
        selected_idea: The exact project/startup idea being discussed.

    Returns:
        A string containing the assistant's response.
    """
    if context_chunks:
        formatted_chunks = []
        for chunk in context_chunks:
            title = chunk.get("title", "Unknown Source")
            url = chunk.get("url", "")
            content = chunk.get("content", "")
            if url:
                formatted_chunks.append(f"Source: {title} ({url})\nContent: {content}")
            else:
                formatted_chunks.append(f"Content: {content}")
        context_text = "\n\n---\n\n".join(formatted_chunks)
    else:
        context_text = "Proje fikri ile ilgili henüz doğrudan taranmış internet kaynağı bulunamadı."

    system = (
        "Sen girişimcilik, iş geliştirme ve yazılım mimarisi alanında uzman, son derece yardımsever ve bilgili bir yapay zeka asistanısın.\n\n"
        f"Kullanıcının geliştirmek istediği proje fikri: '{selected_idea}'\n\n"
        "GÖREVİN VE ÇALIŞMA PRENSİPLERİN:\n"
        "1. Kullanıcının bu proje fikriyle ilgili sorduğu soruları yanıtla, beyin fırtınası yapmasına yardımcı ol, "
        "iş modeli (Canvas), teknik mimari, pazar analizi, özellikler ve yol haritası gibi konularda somut, yaratıcı ve geliştirici öneriler sun.\n"
        "2. Sana sağlanan 'BAĞLAM' (CONTEXT) verileri, bu proje fikriyle ilgili internetten taranmış gerçek araştırma sonuçlarıdır. "
        "Yanıtlarında bu bağlamdaki bilgileri temel al, doğruları referans göster ve bağlamdan sapmamaya özen göster (RAG).\n"
        "3. Eğer kullanıcının sorduğu soru veya istediği detaylar bağlamda yer almıyorsa, robotik bir şekilde 'bilmiyorum' demek yerine "
        "kendi genel kültürünü, iş geliştirme ve yazılım bilgini kullanarak kullanıcıya yol göster (normal bir LLM gibi davran). Ancak bu esnada "
        "kullanıcının seçtiği temel fikirden kopma ve gerçekçi pazar sınırları içerisinde kal.\n"
        "4. Her zaman kullanıcının soru sorduğu dilde yanıt ver (genellikle Türkçe)."
    )
    prompt = f"BAĞLAM (WEB ARAŞTIRMALARI):\n{context_text}\n\nKULLANICI SORUSU:\n{user_question}"

    messages = [{"role": "system", "content": system}]
    messages.extend(history)
    messages.append({"role": "user", "content": prompt})

    try:
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
    except ConnectionError:
        raise LLMServiceError(
            "Could not connect to Ollama. Make sure Ollama is running "
            "(try 'ollama serve') and the model is available."
        )
    except Exception as e:
        raise LLMServiceError(f"Chat request failed: {e}")


def generate_chat_title(user_message: str) -> str:
    """
    Generate a 3-4 word summary title for a chat based on the first user message.
    """
    system = "Sen bir asistan yazılımsın. Verilen kullanıcı mesajını özetleyen maksimum 3-4 kelimelik kısa ve net bir Türkçe başlık üret. Başlıkta tırnak işareti kullanma."
    prompt = f"Kullanıcı Mesajı: {user_message}\n\nKısa Başlık:"
    
    try:
        if config.is_dev:
            import ollama
            client = ollama.Client(host=config.OLLAMA_HOST)
            resp = client.chat(
                model=config.OLLAMA_CHAT_MODEL, 
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ]
            )
            title = resp["message"]["content"].strip()
        else:
            from groq import Groq
            client = Groq(api_key=config.GROQ_API_KEY)
            resp = client.chat.completions.create(
                model=config.GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ]
            )
            title = resp.choices[0].message.content.strip()
        
        # Temizleme
        title = title.replace('"', '').replace("'", "").strip()
        if len(title) > 40:
            title = title[:37] + "..."
        return title
    except Exception:
        # Hata durumunda mesajın ilk kelimelerini al
        words = user_message.split()
        return " ".join(words[:4]) + "..." if len(words) > 4 else user_message