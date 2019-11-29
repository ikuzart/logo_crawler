import threading
from abc import ABCMeta, abstractmethod
from typing import Optional

import requests

from logo_crawler.helpers import get_logger
from logo_crawler.html_page import HTMLPage


logger = get_logger()


class DownloaderContract(metaclass=ABCMeta):
    @abstractmethod
    def download(self, url: str) -> Optional[HTMLPage]:
        pass


class Downloader(DownloaderContract):
    """Downloader gets url as a str and send request to this url and process response
       This realisation is straightforward, if we don't get response 200, just return None

       Ideally methods for dealing with each HTTP response should be realised as ability to use proxy, user_agents and
       cache.
    """
    @staticmethod
    def _get_response(url: str) -> requests.Response:
        return requests.get(url)

    def use_cache(self):
        pass

    def use_proxy(self):
        pass

    def use_user_agents(self):
        pass

    def follow_redirects(self):
        pass

    def retry_on_connection_lost(self):
        pass

    @staticmethod
    def _process_response(response: requests.Response) -> Optional[HTMLPage]:
        html_page = HTMLPage()
        html_page.url = response.url
        html_page.text = None
        if not response.status_code == 200:
            return
        html_page.text = response.text
        return html_page

    def download(self, url: str) -> Optional[HTMLPage]:
        logger.info(f'Thread : {threading.current_thread()} downloading url {url}')
        response = self._get_response("http://" + url)
        logger.info(response.url + " " + str(response.status_code))
        html_page = self._process_response(response)
        if not html_page.text:
            return
        return html_page
