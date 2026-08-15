from typing import Optional

from pydantic import BaseModel


class Step(BaseModel):
    name: str
    description: str
    next: Optional["Step"] = None


class TaskInput(BaseModel):
    id: int
    name: str
    priority: int


class Task(TaskInput):
    current_step: Step | None = None


QueueItem = tuple[int, int, Task]
