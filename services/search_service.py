"""
Web search service layer using Tavily API.
"""
from tavily import TavilyClient
from config import config


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
    client = TavilyClient(api_key=config.TAVILY_API_KEY)
    response = client.search(
        query=idea,
        search_depth="advanced",
        max_results=max_results,
        include_answer=False,
    )

    results = []
    for r in response.get("results", []):
        results.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("content", ""),
        })
    return results