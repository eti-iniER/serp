import scrapy
import logging
from .. import helpers
from ..constants import CRIME_REPORTING_KEYWORDS, DUCKDUCKGO_SELECTORS
from pathlib import Path

PARENT_FOLDER = Path(__file__).parent.resolve()
OUTPUT_PATH = PARENT_FOLDER / "crime_reporting_papers.html"

print = logging.info


class CrimeReportingPapersSpider(scrapy.Spider):
    name = "crime_reporting_papers"
    start_urls = [
        helpers.build_duckduckgo_search_url(keyword)
        for keyword in CRIME_REPORTING_KEYWORDS
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        logging.debug(f"\n\nParsing response from {response.url} \n\n")
        with open(OUTPUT_PATH, "a", encoding="utf-8") as output:
            for result in response.css(DUCKDUCKGO_SELECTORS["result"]):
                data = {
                    "title": result.css(DUCKDUCKGO_SELECTORS["title"]).get(),
                    "summary": result.css(DUCKDUCKGO_SELECTORS["summary"]).get(),
                }

                output.write(response.body)
                yield data
