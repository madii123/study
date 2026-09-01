from datetime import datetime

from enums.task_priority import TaskPriority
from enums.task_status import TaskStatus
from models.reminder import Reminder


class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        due_date: datetime,
        priority: TaskPriority = TaskPriority.MEDIUM,
        status: TaskStatus = TaskStatus.PENDING,
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.assigned_to = None
        self.reminders: list[Reminder] = []
