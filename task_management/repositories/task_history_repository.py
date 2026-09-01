from models.task_history import TaskHistory


class TaskHistoryRepository:
    def __init__(self):
        self._history: dict[int, list[TaskHistory]] = {}

    def save(self, history: TaskHistory) -> None:
        if history.task_id not in self._history:
            self._history[history.task_id] = []

        self._history[history.task_id].append(history)

    def get_by_task_id(self, task_id: int) -> list[TaskHistory]:
        return self._history.get(task_id, [])
