# analyze.py
from .types import *
import concurrent.futures


def parse_search_results(data) -> list[SearchResult]:
    search_results = data["items"]
    parsed_results: list[SearchResult] = []

    for index, result in enumerate(search_results):
        result_data: SearchResult = {
            "id": index,
            "title": result.get("title"),
            "url": result.get("link"),
            "summary": result.get("snippet"),
            "source": result.get("displayLink"),
        }

        parsed_results.append(result_data)

    return parsed_results


def count_features_in_search_result(
    result: SearchResult, features: list[str]
) -> SingleSearchResultFeatureCount:
    """
    Count the number of times each feature appears in the title and summary
    of a search result.
    """
    feature_count = {}

    for feature in features:
        count = 0
        count += result["title"].lower().count(feature.lower())
        count += result["summary"].lower().count(feature.lower())
        feature_count[feature] = count

    return feature_count


def count_features(
    results: list[SearchResult], features: list[str]
) -> list[SearchResultFeatureCounts]:
    """
    Count the features in each search result concurrently using a thread pool.

    This function submits a task for each search result that counts the features.
    It then collects the results into a list of dictionaries with keys
    "search_result" and "feature_counts".
    """
    result_feature_counts = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map each search result to a future that counts its features.
        future_to_result = {
            executor.submit(count_features_in_search_result, result, features): result
            for result in results
        }
        for future in concurrent.futures.as_completed(future_to_result):
            result_obj = future_to_result[future]
            feature_count = future.result()
            data = {"search_result": result_obj, "feature_counts": feature_count}
            result_feature_counts.append(data)

    return result_feature_counts
