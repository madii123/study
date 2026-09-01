from datetime import datetime

from enums.task_action import TaskAction
from enums.task_priority import TaskPriority
from enums.task_status import TaskStatus
from exceptions.task_exception import InvalidTaskException, TaskNotFoundException
from models.task import Task
from models.user import User
from repositories.task_repository import TaskRepository
from services.task_history_service import TaskHistoryService
from strategies.task_search_strategy import TaskSearchStrategy
from models.task_history import TaskHistory


class TaskService:
    def __init__(
        self, task_repository: TaskRepository, history_service: TaskHistoryService
    ) -> Task:
        self.task_repository = task_repository
        self.history_service = history_service
        self.next_task_id = 1

    def create_task(
        self,
        title: str,
        description: str,
        due_date: datetime,
        user: User,
        priority: TaskPriority = TaskPriority.MEDIUM,   
    ):
        task = Task(
            self.next_task_id,
            title,
            description,
            due_date,
            priority,
            TaskStatus.PENDING,
        )
        self.next_task_id += 1
        self.task_repository.save(task)

        self.history_service.record(
            task_id=task.task_id, action=TaskAction.CREATED, user_id=user.user_id
        )
        return task

    def get_task(self, task_id: int) -> Task:
        task = self.task_repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundException()
        return task

    def update_task(
        self,
        task_id: int,
        user: User,
        title: str | None = None,
        description: str | None = None,
        due_date: datetime | None = None,
        priority: TaskPriority | None = None,
    ):
        task = self.task_repository.get_by_id(task_id)
        if task is None:
            raise InvalidTaskException()

        if task.title:
            task.title = title
        if task.description:
            task.description = description
        if task.due_date:
            task.due_date = due_date
        if task.priority:
            task.priority = priority
        self.task_repository.save(task)

        self.history_service.record(
            task_id=task.task_id, action=TaskAction.UPDATED, user_id=user.user_id
        )
        return task

    def delete_task(self, task_id: int, user: User):
        del self.task_repository[task_id]

        self.history_service.record(
            task_id=task_id, action=TaskAction.DELETED, user_id=user.user_id
        )

    def assign_task(self, task_id: int, assigned_user: User, user: User):
        task = self.get_task(task_id)
        task.assigned_to = assigned_user
        self.task_repository.save(task)

        self.history_service.record(
            task_id=task.task_id, action=TaskAction.ASSIGNED, user_id=user.user_id
        )
        return task

    def complete_task(self, task_id: int, user: User):
        task = self.get_task(task_id)
        task.status = TaskStatus.COMPLETED
        self.task_repository.save(task)
        self.history_service.record(
            task_id=task.task_id, action=TaskAction.COMPLETED, user_id=user.user_id
        )
        return task

    def search_tasks(self, strategy: TaskSearchStrategy) -> list[Task]:
        tasks = self.task_repository.get_all()
        return [task for task in tasks if strategy.matches(task)]

    def get_task_history(self, task_id: int) -> list[TaskHistory]:
        return self.history_service.get_history(task_id)
