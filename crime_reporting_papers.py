from core import (
    google_search,
    parse_search_results,
    count_features,
    plot_feature_counts,
)

results_file = "sample_results.json"
raw_results = google_search("crime in nigeria", results_file)
parsed_results = parse_search_results(raw_results)

features = ["crime", "nigeria", "violence"]

results = count_features(parsed_results, features)
plot_feature_counts(results)
