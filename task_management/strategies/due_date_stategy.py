from datetime import datetime

from strategies.task_search_strategy import TaskSearchStrategy


class DueDateSearchStrategy(TaskSearchStrategy):
    def __init__(self, from_date: datetime, to_date: datetime):
        self.from_date = from_date
        self.to_date = to_date

    def matches(self, task):
        if self.from_date is not None and task.due_date < self.from_date:
            return False

        return not (self.to_date is not None and task.due_date > self.to_date)
