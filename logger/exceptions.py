class LoggerException(Exception):
    """Base exception for logger errors."""


class InvalidLogLevelError(LoggerException):
    pass


class InvalidOutputTypeError(LoggerException):
    pass