"""
RAG (Retrieval-Augmented Generation) service.

This module is responsible for:
- Managing document storage in the vector database
- Generating embeddings
- Performing similarity search
- Retrieving relevant documents
- Managing session context
"""
from typing import Any
import uuid
import chromadb
import ollama
from config import config

chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="documents"
)

ollama_client = ollama.Client(host=config.OLLAMA_HOST)

def save_documents(documents: list[str], session_id: str) -> None:
    """
    Save processed documents into the vector database.
    """

    embeddings = generate_embeddings(documents)

    ids = [str(uuid.uuid4()) for _ in documents]
    metadatas = [{"session_id": session_id} for _ in documents]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def generate_embeddings(documents: list[str]) -> list[list[float]]:
    """
    Generate embeddings for the given documents.

    Args:
        documents: List of text documents.

    Returns:
        A list of embedding vectors.
    """

    response = ollama_client.embed(
        model=config.OLLAMA_EMBED_MODEL,
        input=documents,
    )

    return response["embeddings"]


def similarity_search(query_embedding: list[float], session_id: str, top_k: int = 5) -> list[str]:
    """
    Find the most relevant documents using vector similarity.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"session_id": session_id}
    )

    return results["documents"][0]


def retrieve_documents(query: str, session_id: str, top_k: int = 5) -> list[str]:
    """
    Retrieve the most relevant documents from the vector database.
    """

    query_embedding = generate_embeddings([query])[0]

    return similarity_search(query_embedding, session_id, top_k)

def load_session_context(session_id: str) -> list[str]:
    """
    Load previous conversation context for a user session.
    """
    pass