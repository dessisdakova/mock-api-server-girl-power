import logging
import os
from tests_lib.common.yaml_loaders import load_config


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
        stores logs in the "/opt/project/logs" folder. The logger level is set to in config/common_config.yaml

        :param logger_name: Name of the logger instance.
        :param log_file_name: Name of the log file where logs will be saved.
        """
        config = load_config("common_config")
        super().__init__(logger_name, config["log_level"])

        log_dir = config["log_file_dir"]
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file_path = os.path.join(log_dir, log_file_name)

        # create a file handler
        handler = logging.FileHandler(self.log_file_path)

        # create a formatter
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(filename)s | %(message)s", datefmt="%Y/%m/%d %H:%M:%S")
        handler.setFormatter(formatter)

        # add handler the created custom logger
        self.addHandler(handler)

    def add_divider(self) -> None:
        """
        Append a divider line to the log file separating log sessions for better readability.

        """
        with open(self.log_file_path, "a") as log_file:
            log_file.write("-------------------------------------------------------------------\n")
