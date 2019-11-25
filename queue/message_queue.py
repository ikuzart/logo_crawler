from abc import ABCMeta, abstractmethod
from typing import List

class MessageQueue(metaclass=ABCMeta):

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, messages_number: int) -> List[str]:
        pass
