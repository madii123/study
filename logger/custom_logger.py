import threading

from enums import LogLevel, OutputType
from factories.output_factory import OutputFactory
from factories.strategy_factory import StrategyFactory
from formatter import Formatter


class Logger:

    DEFAULT_FORMAT = "[{timestamp}] [{level}] {message}"

    def __init__(
        self,
        level: LogLevel,
        output_type: OutputType,
        file_path: str | None = None,
        pattern: str = DEFAULT_FORMAT,
    ):
        self._level_strategy = StrategyFactory.get_strategy(level)

        self._output = OutputFactory.get_output(
            output_type=output_type,
            file_path=file_path,
        )

        self._formatter = Formatter(pattern)

        self._lock = threading.Lock()

    def debug(self, message: str) -> None:
        self._log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        self._log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        self._log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        self._log(LogLevel.ERROR, message)

    def _log(
        self,
        level: LogLevel,
        message: str,
    ) -> None:

        if not self._level_strategy.should_log(level):
            return

        formatted_message = self._formatter.format(
            level=level.value,
            message=message,
        )

        with self._lock:
            self._output.write(formatted_message)