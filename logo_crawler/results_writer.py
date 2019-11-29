import csv
from abc import ABCMeta, abstractmethod
from typing import Any

from logo_crawler import HTMLPage


class WriterContract(metaclass=ABCMeta):

    @abstractmethod
    def write_to_output(self, html_page: HTMLPage, output_path: Any):
        pass

class CsvWriter(WriterContract):

    def write_to_output(self, html_page, output_path: Any):
        with open(output_path, mode='a') as resulting_file:
            writer = csv.writer(resulting_file, delimiter=',')
            writer.writerow((html_page.url, html_page.logo_url))
