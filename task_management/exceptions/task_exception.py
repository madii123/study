class TaskManagementException(Exception):
    pass


class TaskNotFoundException(TaskManagementException):
    pass


class InvalidTaskException(TaskManagementException):
    pass
