def build_google_search_url(keyword: str):
    """
    Returns a Google search URL for the given keyword

    :param keyword: The keyword to search for

    :return: The Google search URL
    """
    return "https://www.google.com/search?q=" + (
        "+".join([k.strip() for k in keyword.split()])
    )


def build_duckduckgo_search_url(keyword: str):
    """
    Returns a DuckDuckGo search URL for the given keyword

    :param keyword: The keyword to search for

    :return: The DuckDuckGo search URL
    """
    return "https://html.duckduckgo.com/html/?q=" + (
        "%20".join([k.strip() for k in keyword.split()])
    )
