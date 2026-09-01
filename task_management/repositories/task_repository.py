from models.task import Task


class TaskRepository:
    def __init__(self):
        self.tasks: dict[int, Task] = {}

    def save(self, task: Task) -> None:
        self.tasks[task.task_id] = task

    def get_by_id(self, task_id: int) -> Task | None:
        return self.tasks.get(task_id)

    def get_all(self) -> list[Task]:
        return self.tasks.values()

    def delete(self, task_id: int) -> None:
        del self.tasks[task_id]
