import csv
from abc import ABCMeta, abstractmethod
from typing import Iterable


class SeedContract(metaclass=ABCMeta):

    @abstractmethod
    def get_next_url(self) -> str:
        pass


class SeedFromCsv(SeedContract):

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def get_next_url(self) -> Iterable:
        with open(self.csv_path, 'r') as csv_file:
            for row in csv.reader(csv_file):
                yield row[0]


class SeedFromMessageQueue(SeedContract):

    def get_next_url(self) -> str:
        pass
