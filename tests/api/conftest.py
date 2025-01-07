"""
conftest.py

The conftest.py file serves as a means of providing fixtures for an entire directory.
Fixtures defined in a conftest.py can be used by any test in that package without needing to import them
(pytest will automatically discover them)
"""

import pytest
from tests_lib.common.custom_logger import CustomLogger
from tests_lib.common.yaml_loaders import load_config


@pytest.fixture(scope="session")
def config_fixture() -> dict:
    """
    This fixture is used for reading the api_config.yaml file
    All parameters in api_config.yaml are read and parsed into dict, which is returned here
    :return: parsed config_fixture file as a dict.
    """
    return load_config("api_config")


@pytest.fixture
def logger_fixture(request, config_fixture: dict) -> CustomLogger:
    """
    Pytest fixture to provide a configured logger_fixture instance for all tests.
    This fixture creates a CustomLogger instance with a unique log file name for the test scope=function(default scope)
    The 'request' fixture is a special fixture providing information of the requesting test function
    :yield: An instance of CustomLogger.
    """
    local_logger = CustomLogger("test_logger", config_fixture[ "log_file_name" ])
    local_logger.debug(f"Starting {request.node.originalname}")
    yield local_logger
    local_logger.debug(f"Test {request.node.originalname} finished")
