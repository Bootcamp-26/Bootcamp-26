"""
Web search service layer using Tavily API.
Function signature is finalized here; implementation is stubbed for now.
"""


def search_sources(idea: str, max_results: int = 6) -> list[dict]:
    """
    Search the web for sources relevant to a given idea.

    Args:
        idea: The idea/topic to search for.
        max_results: Maximum number of results to return.

    Returns:
        A list of dicts, each with the following keys:
            - "title": str, the page title
            - "url": str, the source URL
            - "content": str, the extracted text content
    """
    raise NotImplementedError("To be implemented in a future issue")