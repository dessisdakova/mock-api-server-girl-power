"""
conftest.py

The conftest.py file serves as a means of providing fixtures for an entire directory.
Fixtures defined in a conftest.py can be used by any test in that package without needing to import them
(pytest will automatically discover them)
"""

import pytest
from tests_lib.common.custom_logger import CustomLogger


@pytest.fixture()
def logger(request):
    """
    Pytest fixture to provide a configured logger instance for all tests.
    This fixture creates a CustomLogger instance with a unique log file name for the test scope=function(default scope)
    :return: An instance of CustomLogger.
    """
    log_file_name = f"test_api.log"
    local_logger = CustomLogger("test_logger", log_file_name)
    local_logger.debug(f"Starting {request.node.originalname}")
    yield local_logger
    local_logger.debug(f"Test {request.node.originalname} finished")
