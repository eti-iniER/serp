# Google obfuscates the HTML and CSS content of the search results, to discourage scrapers
# As a result, we need to manually find the CSS selectors of the relevant items in the search results pages
# Afterwards, we add them to this dictionary, to be used by the scraper

from pathlib import Path

GOOGLE_SELECTORS = {
    "result": "div.N54PNb.BToiNc",
    "title": "span.VuuXrf",
    "source": "cite.qLRx3b.tjvcx.GvPZzd.cHaqb",
    "url": "a",
    "summary": "div.VwiC3b.yXK7lf.p4wth.r025kc.hJNv6b.Hdw6tb span",
}

DUCKDUCKGO_SELECTORS = {
    "result": "div.result.results_links.results_links_deep.web-result",
    "title": "h2.result__title",
    "source": "a.result__url",
    "url": "a.result__url",
    "summary": "a.result__snippet",
}

CRIME_REPORTING_KEYWORDS = [
    "crime",
    "police",
    "law enforcement",
    "crime reporting",
    "crime statistics",
]

OUTPUT_FILENAME = f"data.html"
