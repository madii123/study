from enums import LogLevel
from strategies.level_strategy import (
    DebugLevelStrategy,
    ErrorLevelStrategy,
    InfoLevelStrategy,
    LevelStrategy,
    WarningLevelStrategy,
)


class StrategyFactory:

    @staticmethod
    def get_strategy(level: LogLevel) -> LevelStrategy:
        strategies = {
            LogLevel.DEBUG: DebugLevelStrategy,
            LogLevel.INFO: InfoLevelStrategy,
            LogLevel.WARNING: WarningLevelStrategy,
            LogLevel.ERROR: ErrorLevelStrategy,
        }

        strategy_class = strategies.get(level)

        if strategy_class is None:
            raise ValueError(
                f"Unsupported log level: {level}"
            )

        return strategy_class()