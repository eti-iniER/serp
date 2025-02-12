from core.crime_reporting_papers import *


def main():
    query = input("\n\nEnter your search query: ")
    features = input(
        "Enter the features/keywords you want to count, separated by commas: "
    ).split(",")

    results = google_search(query, "crime_reporting_papers.json")
    parsed_results = parse_search_results(results)

    feature_counts = count_features(parsed_results, features)

    print("Your data is ready! \n\n")
    plot_feature_counts(feature_counts)


if __name__ == "__main__":
    main()
