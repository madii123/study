from enum import Enum


class TaskAction(Enum):
    CREATED = "created"
    UPDATED = "updated"
    ASSIGNED = "assigned"
    COMPLETED = "completed"
    DELETED = "deleted"
