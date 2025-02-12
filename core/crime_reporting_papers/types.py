from typing import TypedDict


class SearchResult(TypedDict):
    id: int
    title: str
    url: str
    summary: str
    source: str


class SingleSearchResultFeatureCount(TypedDict):
    str: int


class SearchResultFeatureCounts:
    search_result: SearchResult
    feature_counts: SingleSearchResultFeatureCount
