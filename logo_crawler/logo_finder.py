import re
from abc import ABCMeta, abstractmethod
from typing import Optional

from bs4 import BeautifulSoup

from logo_crawler import HTMLPage
from logo_crawler.helpers import get_logger


logger = get_logger()

SIGNATURES = \
    [{"tag": "meta", "attr":{"property": "og:image", "itemprop": "image primaryImageOfPage"}, "to_get": "content"},
     {"tag": "meta", "attr":{"itemprop": "logo"}, "to_get": "content"},
     {"tag": "link", "attr":{"rel": "logo"}, "to_get": "src"},
     {"tag": "img", "attr":{"alt": "logo"}, "to_get": "src"},
     {"tag": "img", "attr":{"class_": "logo"}, "to_get": "src"},
     {"tag": "img", "attr":{"alt": re.compile(".*_logo")}, "to_get": "src"},
     {"tag": "img", "attr": {"alt": re.compile(".*-logo")}, "to_get": "src"}
    ]


class LogoFinderContract(metaclass=ABCMeta):

    @abstractmethod
    def search(self, html_page: HTMLPage, signatures: list):
        pass


class LogoFinder(LogoFinderContract):
    """
    Searches for logo image signatures on given HTML page
    """

    def search(self, html_page: HTMLPage, signatures: list = SIGNATURES) -> Optional[str]:
        result = None
        if not html_page.text:
            return

        for signature in signatures:
            soup = BeautifulSoup(html_page.text, 'html.parser')
            result = soup.find_all(signature["tag"], signature["attr"], limit=1)
            if not result:
                continue
            return result[0].get(signature["to_get"])

        if not result:
            logger.info(f"Didn't find logo for {html_page.url}")
            return
