from abc import ABC, abstractmethod


class Output(ABC):

    @abstractmethod
    def write(self, message: str) -> None:
        pass