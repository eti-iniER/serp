import requests
from dotenv import dotenv_values

env = dotenv_values(".env")


def google_search(query: str, results_file=None) -> dict:
    response = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={
            "key": env.get("GOOGLE_CUSTOM_SEARCH_API_KEY"),
            "cx": env.get("GOOGLE_CUSTOM_SEARCH_ENGINE_ID"),
            "q": query,
        },
    )

    if results_file:
        with open(results_file, "w") as f:
            f.write(response.text)

    return response.json()
