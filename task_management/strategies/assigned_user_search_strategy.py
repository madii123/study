from task_search_strategy import TaskSearchStrategy

from models.user import User


class AssignedUserSearchStrategy(TaskSearchStrategy):
    def __init__(self, user: User):
        self.user = user

    def matches(self, task):
        return task.user == self.user
