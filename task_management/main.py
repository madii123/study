from datetime import datetime, timedelta

from enums.task_priority import TaskPriority
from enums.task_status import TaskStatus
from models.user import User
from repositories.task_history_repository import TaskHistoryRepository
from repositories.task_repository import TaskRepository
from services.reminder_service import ReminderService
from services.task_history_service import TaskHistoryService
from services.task_service import TaskService
from strategies.priority_search_strategy import PrioritySearchStrategy


def main():
    # Users
    madhu = User(1, "Madhu")
    pankaj = User(2, "Pankaj")

    # Repositories
    task_repository = TaskRepository()
    history_repository = TaskHistoryRepository()

    # Services
    history_service = TaskHistoryService(
        history_repository
    )

    task_service = TaskService(
        task_repository=task_repository,
        history_service=history_service,
    )

    reminder_service = ReminderService(
        task_service=task_service
    )

    # Create task
    task = task_service.create_task(
        title="Prepare LLD",
        description="Prepare task management system",
        due_date=datetime.now() + timedelta(days=2),
        user=madhu,
        priority=TaskPriority.HIGH,
    )

    print(f"Created task: {task.task_id}")

    # Assign task
    task_service.assign_task(
        task_id=task.task_id,
        assigned_user=pankaj,
        user=madhu,
    )

    # Add reminder
    reminder_service.add_reminder(
        task_id=task.task_id,
        remind_at=datetime.now() + timedelta(days=1),
    )

    # Update task
    task_service.update_task(
        task_id=task.task_id,
        user=pankaj,
        description="Prepare and practice LLD",
    )

    # Search high-priority tasks
    strategy = PrioritySearchStrategy(
        TaskPriority.HIGH
    )

    high_priority_tasks = task_service.search_tasks(
        strategy
    )

    print("\nHigh priority tasks:")
    for task in high_priority_tasks:
        print(task.task_id, task.title)

    # Complete task
    task_service.complete_task(
        task_id=task.task_id,
        user=pankaj,
    )

    # History
    history = task_service.get_task_history(
        task.task_id
    )

    print("\nTask history:")
    for entry in history:
        print(
            entry.action.value,
            entry.user_id,
            entry.timestamp,
        )


if __name__ == "__main__":
    main()