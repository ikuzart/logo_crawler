from abc import ABCMeta, abstractmethod

import requests

from queue.message_queue import MessageQueue


class Crawler(ABCMeta):

    @abstractmethod
    def run(cls):
        pass


class LogosCrawler(Crawler):

    domain_queue: MessageQueue
    retry_queue: MessageQueue
    html_queue: MessageQueue

    def run(self):
        for domain in self.domain_queue.receive():
            response = requests.get(domain)
            if response.status_code is not 200:
                self.retry_queue.send(response.url)
            self.html_queue.send(response.text)




