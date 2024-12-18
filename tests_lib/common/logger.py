import logging
import os
from pathlib import Path
from tests_lib.common.yaml_loaders import load_config

def create_logger(logger_name: str, log_file_name: str):
    """
    Creates a logger with INFO level(set up in config/common_config.yaml), a file handler.

    :param logger_name: name of the logger - string.
    :param log_file_name: the name of log file - string.
    :return: logger instance.
    """
    config = load_config("common_config")
    log_dir = config["log_file_dir"]
    log_level_str = config["log_level"]

    logger = logging.getLogger(logger_name)  # create custom logger
    logger.setLevel(logging.getLevelNamesMapping()[log_level_str])
    log_file_path = os.path.join(log_dir, log_file_name)
    # create a file handler to save logs in a file
    handler = logging.FileHandler(log_file_path)

    # set the format for logs saved in the file
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -  %(filename)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)  # set the desired format for logs in the file

    # add file handler to logger
    if not logger.handlers:  # prevent duplicate handlers if logger is reused
        logger.addHandler(handler)

    return logger
