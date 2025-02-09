# Group 28 - CSC 310 Project

This project was created as a requirement for the course **CSC 310 - Concurrency in Java**.

We were asked (using any programming language) to implement a multi-threaded program to crawl the internet and find relevant information, and return the information in a useful and understandable format. We were also asked to visualize the information in a meaningful way.

We chose to do this using Python, and the following libraries:

-   **threading:** To handle multi-threading
-   **matplotlib:** For visualisation

For retrieving the search results, we are using Google's Custom Search Engine API. As a result, we're limited to 100 free searches per day, but that should be sufficient for this project

### Getting started

-   Create a virtualenv, and then install the requirements
-   You'll also need some API keys, as described in the .env.template file. Once you have the keys, create a .env file at the root of the folder and place them there
