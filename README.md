# Group 28 - CSC 310 Project

This project was created as a requirement for the course **CSC 310 - Concurrency in Java**.

We were asked (using _any_ programming language) to implement a multi-threaded program to crawl the internet and find relevant information, and return the information in a useful and understandable format. We were also asked to visualize the information in a meaningful way.

We chose to do this using Python (as it is the language we are most familiar with), and the following libraries:

-   **requests:** For making and managing HTTP requests
-   **concurrent:** To handle concurrency and multi-threading
-   **matplotlib:** For data visualisation

For retrieving the search results, we are using Google's Custom Search Engine API. As a result, we're limited to 100 free searches per day, but that should be sufficient for this project

## Methodology

The main functionality of this project is in the `core` module. Here is a brief description of the code in the various files:

-   `search.py`: Implements a simple saerch function that uses the Google Custom Search API to gather search results and returns a JSON object. This function can optionally write to a file (used during testing).

-   `analyze.py`: This is the heart of the project. It counts the features in each of the results from the SERP (using concurrency concepts such as **multithreading** and **thread pools**), and returns them for further processing.

-   `visualize.py`: This displays the results in an easy-to-understand chart, generated using Matplotlib. Here, the search results are sorted for better data communication.

The rest of the files, `__init__.py` and `types.py` are simple utility files, containing module imports and type declarations respectively

## Getting started

-   Create a virtualenv, and then install the requirements as given in the `requirements.txt` file.
-   You'll also need some API keys, as described in the .env.template file. Once you have the keys, create a .env file at the root of the folder and place them there.
-   Now, you can run either `crime_reporting_papers.py` or `deep_learning_journals.py` to see the results.
