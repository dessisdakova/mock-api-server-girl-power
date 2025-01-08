import shutil

from tests_lib.common.yaml_loaders import load_config
import logging
from pathlib import Path


class CustomLogger(logging.Logger):
    """
    A custom logger class for managing test logs with extended functionality.
    """
    def __init__(self, logger_name: str, log_file_name: str):
        """
        Initializes a custom logger with a file handler and custom formatter.

        :param logger_name: Name of the logger instance.
        :param log_file_name: Name of the log file.
        """
        # Create a logger
        super().__init__(logger_name, self._get_log_level())

        # Set up log file path
        self.log_file_path = self._get_log_file_path(log_file_name)

        # Set up the file handler and add it to the logger
        file_handler = self._create_file_handler()
        self.addHandler(file_handler)

    def _get_log_level(self) -> str:
        """
        Gets the log level from a config file.

        :return: String representation of the level.
        """
        config = load_config("logger_config")
        return config["log_level"]

    def _get_log_file_path(self, log_file_name: str) -> Path:
        """
        Constructs the path to the log file.

        :param log_file_name: Name of the log file.
        :return: Full path to the log file.
        """
        logs_folder = Path(__file__).resolve().parent.parent.parent / "logs"
        return logs_folder / log_file_name

    def _create_file_handler(self) -> logging.FileHandler:
        """
        Creates a file handler for logging to the log file.

        :return: Configured file handler.
        """
        handler = logging.FileHandler(self.log_file_path)
        handler.setFormatter(self._create_formatter())
        return handler

    def _create_formatter(self) -> logging.Formatter:
        """
        Creates a custom formatter for log messages.

        :return: Configured formatter.
        """
        return logging.Formatter(
            "%(asctime)s | %(levelname)-5s | %(name)-s | %(filename)s | %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S"
        )

    def add_divider(self) -> None:
        """
        Append a divider line to the log file separating log sessions for better readability.
        """
        with open(self.log_file_path, "a") as log_file:
            log_file.write("----------------------------------------------------------------------------------------\n")
