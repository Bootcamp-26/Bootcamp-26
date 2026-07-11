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


chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="documents"
)

ollama_client = ollama.Client(host=config.OLLAMA_HOST)


def save_documents(documents: list[str]) -> None:
    """
    Save processed documents into the vector database.
    """

    chunks = chunk_documents(documents)

    embeddings = generate_embeddings(chunks)

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
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


def similarity_search(query_embedding: list[float], top_k: int = 5) -> list[str]:
    """
    Find the most relevant documents using vector similarity.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results["documents"][0]


def retrieve_documents(query: str, top_k: int = 5) -> list[str]:
    """
    Retrieve the most relevant documents from the vector database.
    """

    query_embedding = generate_embeddings([query])[0]

    return similarity_search(query_embedding, top_k)


def load_session_context(session_id: str) -> list[str]:
    """
    Load previous conversation context for a user session.
    """
    pass