import logging
from pathlib import Path


class CustomLogger(logging.Logger):
    """
    A custom logger class for managing test logs with extended functionality.

    This class extends the base logging.Logger to provide preconfigured logging settings,
    including a log file handler, a custom log format, and a utility method to add dividers
    between log sessions for better readability.
    """
    def __init__(self, logger_name: str, log_file_name: str):
        """
        Overrides the base class constructor to configure a custom logger.

        Sets up a log file handler with a specified file name, applies a custom format, and
        stores logs in the "logs/" folder. The logger level is set to DEBUG by default.

        :param logger_name: Name of the logger instance.
        :param log_file_name: Name of the log file where logs will be saved.
        """
        # calling parent initializer to create a custom logger and sets its name and level
        super().__init__(logger_name, logging.DEBUG)

        # set logs/ folder to be used as default folder for all log files
        self.log_file_path = Path(__file__).resolve().parent.parent.parent / "logs" / log_file_name

        # create a file handler
        handler = logging.FileHandler(self.log_file_path)

        # create a formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        # add formatter to handler
        handler.setFormatter(formatter)

        # add handler the created custom logger
        self.addHandler(handler)

    def add_divider(self) -> None:
        """
        Appends a divider line to the log file separating log sessions for better readability.

        :return: None
        """
        with open(self.log_file_path, "a") as log_file:
            log_file.write("-------------------------------------------------------------------\n")
