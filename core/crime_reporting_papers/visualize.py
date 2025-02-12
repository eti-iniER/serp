# visualize.py
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from .types import *

FONT_SIZE = 8
MAX_TITLE_LENGTH = 20


def truncate_text(text: str) -> str:
    if len(text) > MAX_TITLE_LENGTH:
        return text[: MAX_TITLE_LENGTH - 3] + "..."
    return text


def plot_feature_counts(results: List[SearchResultFeatureCounts]):
    """
    Plots a horizontal grouped bar chart where:
      - The y-axis labels are the (possibly truncated) titles of the search results.
      - Each group (one search result) shows the counts for various features as horizontal bars.
      - The legend shows the feature names.
      - The search results are sorted by total feature count in descending order
        (i.e. the result with the most total feature count appears at the top).

    """
    # Sort the results by descending total feature count.
    sorted_results = sorted(
        results, key=lambda r: sum(r["feature_counts"].values()), reverse=True
    )

    all_features = set()
    for result in sorted_results:
        all_features.update(result["feature_counts"].keys())
    feature_names = sorted(all_features)

    n_results = len(sorted_results)
    n_features = len(feature_names)

    # Set up positions and bar heights.
    indices = np.arange(n_results)
    group_height = 0.8
    bar_height = group_height / n_features

    fig, ax = plt.subplots(figsize=(6, 6))

    # Plot the horizontal bars for each feature.
    for i, feature in enumerate(feature_names):

        counts = [result["feature_counts"].get(feature, 0) for result in sorted_results]

        bottom_positions = indices - group_height / 2 + i * bar_height
        ax.barh(
            bottom_positions, counts, height=bar_height, align="edge", label=feature
        )

    titles = [result["search_result"]["title"] for result in sorted_results]
    truncated_titles = [truncate_text(title) for title in titles]

    tick_positions = indices
    ax.set_yticks(tick_positions)
    ax.set_yticklabels(truncated_titles, va="center", fontsize=FONT_SIZE)

    ax.set_ylabel("Search Result")
    ax.set_xlabel("Feature Count")
    ax.legend(title="Feature", fontsize=FONT_SIZE)

    plt.title("Feature Counts in Search Results")
    plt.tight_layout()

    # Invert the y-axis so the highest total feature count is on top.
    ax.invert_yaxis()

    plt.show()
