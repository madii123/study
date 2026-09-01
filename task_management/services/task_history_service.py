from datetime import datetime, timezone

from enums.task_action import TaskAction
from models.task_history import TaskHistory
from repositories.task_history_repository import TaskHistoryRepository


class TaskHistoryService:
    def __init__(
        self,
        history_repository: TaskHistoryRepository,
    ):
        self._history_repository = history_repository

    def record(
        self,
        task_id: int,
        action: TaskAction,
        user_id: int,
    ) -> None:

        history = TaskHistory(
            task_id=task_id,
            action=action,
            timestamp=datetime.now(tz=timezone.utc),
            user_id=user_id,
        )

        self._history_repository.save(history)

    def get_history(self, task_id: int) -> list[TaskHistory]:
        return self._history_repository.get_by_task_id(task_id)
