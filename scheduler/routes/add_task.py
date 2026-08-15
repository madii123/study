import itertools

from fastapi import APIRouter

from models import Task, TaskInput
from queues import intake_queue

enque_task_router = APIRouter(prefix="/task")
counter = itertools.count()


@enque_task_router.post("/")
async def enque(task_input: TaskInput):
    task = Task(
        id=task_input.id,
        name=task_input.name,
        priority=task_input.priority,
    )
    await intake_queue.put((task.priority, next(counter), task))
    return {
        "message": f"Task {task.name} added to intake queue with priority {task.priority}"
    }
