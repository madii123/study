from abc import ABC, abstractmethod

from enums import LogLevel


class LevelStrategy(ABC):

    @abstractmethod
    def should_log(
        self,
        level: LogLevel,
    ) -> bool:
        pass


class DebugLevelStrategy(LevelStrategy):

    def should_log(
        self,
        level: LogLevel,
    ) -> bool:
        return True


class InfoLevelStrategy(LevelStrategy):

    def should_log(
        self,
        level: LogLevel,
    ) -> bool:
        return level in (
            LogLevel.INFO,
            LogLevel.WARNING,
            LogLevel.ERROR,
        )


class WarningLevelStrategy(LevelStrategy):

    def should_log(
        self,
        level: LogLevel,
    ) -> bool:
        return level in (
            LogLevel.WARNING,
            LogLevel.ERROR,
        )


class ErrorLevelStrategy(LevelStrategy):

    def should_log(
        self,
        level: LogLevel,
    ) -> bool:
        return level == LogLevel.ERROR