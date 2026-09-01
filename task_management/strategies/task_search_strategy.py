from abc import ABC, abstractmethod

from models.task import Task


class TaskSearchStrategy(ABC):
    @abstractmethod
    def matches(self, task: Task) -> bool:
        pass
