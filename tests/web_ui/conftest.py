import pytest
from tests.web_ui.fixtures import logger
from tests_lib.common.custom_logger import CustomLogger
from pathlib import Path
"""
# Set up the API logger
logger = CustomLogger("selenium_logger", "selenium_tests.log")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_protocol(item):
    if Path(item.fspath).parent.name == "web_ui":
        logger.info(f"Starting test... {item.name}")
    yield


def pytest_runtest_logreport(report):
    if "web_ui" in str(report.fspath):  # Check if the test belongs to the 'api' directory
        if report.when == "call":
            if report.passed:
                logger.info(f"{report.nodeid} PASSED")
            elif report.failed:
                logger.error(f"{report.nodeid} FAILED")
                if report.longrepr:
                    logger.error(f"Error: {report.longreprtext}")
            elif report.skipped:
                logger.warning(f"{report.nodeid} SKIPPED")
            logger.add_divider()
    """
