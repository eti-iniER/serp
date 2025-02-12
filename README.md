# Group 28 - CSC 310 Project

This project was created as a requirement for the course **CSC 310 - Concurrency in Java**.

## 1. Crime reporting papers

We were asked (using _any_ programming language) to implement a multi-threaded program to crawl the internet and find relevant information on **crime reporting papers**, and return the information in a useful and understandable format. We were also asked to visualize the information in a meaningful way.

We chose to do this using Python (as it is the language we are most familiar with), and the following libraries:

-   **requests:** For making and managing HTTP requests
-   **concurrent:** To handle concurrency and multi-threading
-   **matplotlib:** For data visualisation

For retrieving the search results, we are using Google's Custom Search Engine API. As a result, we're limited to 100 free searches per day, but that should be sufficient for this project

### Methodology

The main functionality of this project is in the `core.crime_reporting_papers` module. Here is a brief description of the code in the various files:

-   `search.py`: Implements a simple saerch function that uses the Google Custom Search API to gather search results and returns a JSON object. This function can optionally write to a file (used during testing).

-   `analyze.py`: This is the heart of the project. It counts the features in each of the results from the SERP (using concurrency concepts such as **multithreading** and **thread pools**), and returns them for further processing.

-   `visualize.py`: This displays the results in an easy-to-understand chart, generated using Matplotlib. Here, the search results are sorted for better data communication.

The rest of the files, `__init__.py` and `types.py` are simple utility files, containing module imports and type declarations respectively

## 2. Deep learning journal papers

We were also asked to write a program to identify the headings and subheadings in papers about deep learning,
also using concurrency principles.

To do this, we used the following libraries:

-   **PyMuPDF:** For reading and extracting text from the PDF files
-   **os:** For parsing the directory and file systems
-   **concurrent:** To handle concurrency and multithreading

### Methodology

Again, the code for this task can be found in the `core.deep_learning_journals` module. Below is a brief description of the relevant files:

-   `analyze.py`: This contains the concurrent code to extract the headings from the PDFs. To identify headings from the text content of the PDF, we used a simple heuristic based on font size and font weight (that is, we expect headings to have bold text, or a relatively larger font size).

As for visualization, we decided to simply print the number of headings and their content to the console, since it was basic textual data.

## Running this code

-   Create a virtualenv, and then install the requirements as given in the `requirements.txt` file.
-   You'll also need some API keys, as described in the .env.template file. Once you have the keys, create a .env file at the root of the folder and place them there.
-   Now, you can run either `crime_reporting_papers.py` or `deep_learning_journals.py` to see the results.

## Credits

To test the PDF heading extraction program, we have included three sample papers, sourced from the Full-Access section of [Springer Nature Link](https://link.springer.com/). Their authors and collaborators, of course, receive all the credit for their content!
