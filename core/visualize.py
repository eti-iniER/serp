from typing import List
import matplotlib.pyplot as plt
import numpy as np
from core.types import SearchResultFeatureCounts

FONT_SIZE = 8
MAX_TITLE_LENGTH = 20


def truncate_text(text: str) -> str:
    """
    Truncates the given text to a maximum of MAX_TITLE_LENGTH characters.
    If the text is longer, it will be shortened and an ellipsis ("...") appended.
    """
    if len(text) > MAX_TITLE_LENGTH:
        return text[: MAX_TITLE_LENGTH - 3] + "..."
    return text


def plot_feature_counts(results: List[SearchResultFeatureCounts]) -> None:
    """
    Plots a horizontal grouped bar chart where:
      - The y-axis labels are the (possibly truncated) titles of the search results.
      - Each group (one search result) shows the counts for various features as horizontal bars.
      - The legend shows the feature names.
      - The search results are sorted by total feature count in descending order
        (i.e. the result with the most total feature count appears at the top).

    Within each group, the bars for the features are drawn touching one another,
    while there is space between groups.
    """
    # Sort the results by descending total feature count.
    sorted_results = sorted(
        results, key=lambda r: sum(r["feature_counts"].values()), reverse=True
    )

    # Compute the union of all feature names across results.
    all_features = set()
    for result in sorted_results:
        all_features.update(result["feature_counts"].keys())
    feature_names = sorted(all_features)

    n_results = len(sorted_results)
    n_features = len(feature_names)

    # Set up positions and bar heights.
    indices = np.arange(n_results)  # one per search result
    group_height = 0.8  # total vertical space allotted to a single group
    bar_height = group_height / n_features  # height for each feature bar

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the horizontal bars for each feature.
    for i, feature in enumerate(feature_names):
        # For each search result, get the count for this feature (defaulting to 0 if missing)
        counts = [result["feature_counts"].get(feature, 0) for result in sorted_results]
        # Compute the bottom positions for the bars in each group.
        bottom_positions = indices - group_height / 2 + i * bar_height
        ax.barh(
            bottom_positions, counts, height=bar_height, align="edge", label=feature
        )

    # Get and truncate the search result titles.
    titles = [result["search_result"]["title"] for result in sorted_results]
    truncated_titles = [truncate_text(title) for title in titles]
    # Use the center of each group (simply indices) for the tick positions.
    tick_positions = indices
    ax.set_yticks(tick_positions)
    ax.set_yticklabels(truncated_titles, va="center", fontsize=FONT_SIZE)

    # Add labels and legend.
    ax.set_ylabel("Search Result")
    ax.set_xlabel("Feature Count")
    ax.legend(title="Feature", fontsize=FONT_SIZE)

    plt.title("Feature Counts in Search Results")
    plt.tight_layout()

    # Invert the y-axis so the highest total feature count is on top.
    ax.invert_yaxis()

    plt.show()
