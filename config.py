"""
Central configuration module.
Reads environment variables and exposes dev/prod switching logic.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_ENV = os.getenv("APP_ENV", "dev")  # "dev" | "prod"

    # Ollama (dev)
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_IDEA_MODEL = os.getenv("OLLAMA_IDEA_MODEL", "gemma3:4b")
    OLLAMA_CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.1:8b")
    OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

    # Groq (prod)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    # Tavily
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

    # RAG parameters
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
    TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", 5))

    @property
    def is_dev(self) -> bool:
        return self.APP_ENV == "dev"


config = Config()