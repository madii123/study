from enums.task_status import TaskStatus
from strategies.task_search_strategy import TaskSearchStrategy


class StatusSearchStrategy(TaskSearchStrategy):
    def __init__(self, status: TaskStatus):
        self.status = status

    def matches(self, task):
        return task.status == self.status
