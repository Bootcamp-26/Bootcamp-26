"""
RAG (Retrieval-Augmented Generation) service.

This module is responsible for:
- Managing document storage in the vector database
- Generating embeddings
- Performing similarity search
- Retrieving relevant documents
- Managing session context
"""

import uuid

import chromadb
import ollama

from config import config
from services.llm_service import chat_with_context


chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="documents"
)

ollama_client = ollama.Client(host=config.OLLAMA_HOST)

def save_documents(documents: list[str], session_id: str) -> None:
    """
    Save processed documents into the vector database.
    """

    chunks = chunk_documents(documents)

    embeddings = generate_embeddings(chunks)

    ids = [str(uuid.uuid4()) for _ in chunks]
    metadatas = [{"session_id": session_id} for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def chunk_document(document: str) -> list[str]:
    """
    Split a document into overlapping chunks.
    """

    chunk_size = config.CHUNK_SIZE
    overlap = config.CHUNK_OVERLAP

    if chunk_size <= 0:
        raise ValueError("CHUNK_SIZE must be greater than 0")

    if overlap < 0:
        raise ValueError("CHUNK_OVERLAP cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("CHUNK_OVERLAP must be smaller than CHUNK_SIZE")

    chunks = []
    start = 0

    while start < len(document):
        end = start + chunk_size

        chunk = document[start:end]

        if chunk.strip():
            chunks.append(chunk)

        if end >= len(document):
            break

        start = end - overlap

    return chunks


def chunk_documents(documents: list[str]) -> list[str]:
    """
    Split multiple documents into overlapping chunks.
    """

    chunks = []

    for document in documents:
        chunks.extend(chunk_document(document))

    return chunks


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

def get_rag_response(query: str, session_id: str, history: list[dict]) -> str:
    """
    Orchestrate the RAG pipeline by retrieving documents and passing them to the LLM.
    """
    context_chunks = retrieve_documents(query, session_id)
    return chat_with_context(user_question=query, context_chunks=context_chunks, history=history)