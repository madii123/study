from datetime import datetime

from exceptions.task_exception import InvalidTaskException
from models.reminder import Reminder
from services.task_service import TaskService


class ReminderService:
    def __init__(self, task_service: TaskService):
        self._task_service = task_service
        self._next_reminder_id = 1

    def add_reminder(
        self,
        task_id: int,
        remind_at: datetime,
    ) -> Reminder:

        task = self._task_service.get_task(task_id)

        if remind_at >= task.due_date:
            raise InvalidTaskException("Reminder must be before the task due date")

        reminder = Reminder(
            reminder_id=self._next_reminder_id,
            remind_at=remind_at,
        )

        self._next_reminder_id += 1

        task.reminders.append(reminder)

        return reminder
