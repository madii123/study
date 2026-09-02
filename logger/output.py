from abc import ABC, abstractmethod

from enums import OutputType
from exceptions import OutputTypeException


class Output(ABC):
    @abstractmethod
    def flush(self, message: str):
        pass


class PrintOutput(Output):
    def flush(self, message: str):
        print("print: " + message)


class FileOutput(Output):
    def flush(self, message: str):
        print("file: " + message)


class OutputFaactory:
    @staticmethod
    def get_output(type: OutputType) -> Output:
        if type == OutputType.STDOUT:
            return PrintOutput()
        if type == OutputType.FILE:
            return FileOutput()
        raise OutputTypeException()
