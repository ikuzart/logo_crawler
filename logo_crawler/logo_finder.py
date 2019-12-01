import re
from typing import Optional

from bs4 import BeautifulSoup

from logo_crawler import HTMLPage
from logo_crawler.helpers import get_logger


logger = get_logger()


SIGNATURES = \
    [{"tag": "meta", "attr":{"property": "og:image", "itemprop": "image primaryImageOfPage"},
      "to_get": "content", "weight": 0.9},
     {"tag": "meta", "attr":{"itemprop": "logo"}, "to_get": "content", "weight": 0.9},
     {"tag": "link", "attr":{"rel": "logo"}, "to_get": "src", "weight": 0.9},
     {"tag": "img", "attr":{"alt": "logo"}, "to_get": "src", "weight": 0.9},
     {"tag": "img", "attr":{"class_": "logo"}, "to_get": "src", "weight": 0.9},
     {"tag": "img", "attr":{"alt": re.compile(".*_logo")}, "to_get": "src", "weight": 0.5},
     {"tag": "img", "attr": {"alt": re.compile(".*-logo")}, "to_get": "src", "weight": 0.5},
     {"tag": "img", "attr":{"alt": re.compile(".*_logo_.*")}, "to_get": "src", "weight": 0.5},
     {"tag": "img", "attr": {"alt": re.compile(".*-logo_.*")}, "to_get": "src", "weight": 0.5}
    ]


class SocialMediaLogo:
    """
    Ideally we could have additional information associated with url like social networks.
    so we could obtain company logo from it, it have advantages of unified size and format.
    """
    pass


class LogoFinder:
    """
    Searches for logo image signatures on given HTML page, selects first with highest weight.
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
