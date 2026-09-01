from datetime import datetime

from enums.task_action import TaskAction


class TaskHistory:
    def __init__(
        self,
        task_id: int,
        action: TaskAction,
        timestamp: datetime,
        user_id: int,
    ):
        self.task_id = task_id
        self.action = action
        self.timestamp = timestamp
        self.user_id = user_id
