from langchain_community.tools.tavily_search import TavilySearchResults


def get_linkedin_url_search_tavily(query: str):
    """Search for a Linkedin URL"""
    search = TavilySearchResults()
    res = search.run(f"{query}")
    return res
