# search.py
import requests
from dotenv import dotenv_values
from typing import Optional

env = dotenv_values(".env")


def google_search(query: str, results_file: Optional[str] = None) -> dict:
    response = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={
            "key": env.get("GOOGLE_CUSTOM_SEARCH_API_KEY"),
            "cx": env.get("GOOGLE_CUSTOM_SEARCH_ENGINE_ID"),
            "q": query,
        },
    )

    if results_file is not None:
        with open(results_file, "w", encoding="utf-8") as f:
            f.write(response.text)

    return response.json()
