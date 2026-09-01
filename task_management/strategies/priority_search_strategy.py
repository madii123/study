from enums.task_priority import TaskPriority
from strategies.task_search_strategy import TaskSearchStrategy


class PrioritySearchStrategy(TaskSearchStrategy):
    def __init__(self, priority: TaskPriority):
        self.priority = priority

    def matches(self, task):
        return task.priority == self.priority
