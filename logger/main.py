from enums import LogLevel, OutputType
from custom_logger import Logger


def main():
    logger = Logger(
        level=LogLevel.INFO,
        output_type=OutputType.STDOUT,
        pattern="{timestamp} | {level} | {message}",
    )

    logger.info("Application started")
    logger.debug("Debug message")
    logger.error("Something went wrong")


if __name__ == "__main__":
    main()