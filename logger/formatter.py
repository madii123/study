from datetime import datetime


class Formatter:

    def __init__(self, pattern: str):
        self.pattern = pattern

    def format(self, level: str, message: str) -> str:
        return self.pattern.format(
            timestamp=datetime.now(),
            level=level,
            message=message,
        )