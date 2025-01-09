from tests_lib.common.yaml_loaders import load_config
from tests_lib.common.custom_logger import CustomLogger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest
from typing import Generator
from pytest_custom_outputs import get_results


@pytest.fixture(scope="session")
def config() -> dict:
    """
    Fixture to load and provide the web UI configuration for the test session.

    :return: A dictionary containing the loaded configuration.
    """
    return load_config("web_ui_config")


@pytest.fixture(scope="session")
def logger(config) -> CustomLogger:
    """
    Fixture to provide a logger for web UI tests.

    :param config: Config fixture.
    :return: A CustomLogger instance for logging test-related information.
    """
    log_file_name = config["log_file_name"]
    log = CustomLogger("web_ui_logger", log_file_name)
    return log


@pytest.fixture(scope="function")
def driver(config, logger, request) -> Generator[webdriver.Remote, None, None]:
    """
    Fixture to initialize a web driver for UI tests based on the configuration.

    This fixture sets up the selected browser (Chrome, Firefox, or Edge) in headless mode
    and creates a remote WebDriver instance. It also sets an implicit wait time for elements.

    :param config: Config fixture.
    :param logger: Logger fixture.
    :param request: Request object providing test context information.
    :return: A web driver instance to be used for the duration of the test session.
    :raises TypeError: If the specified browser is not supported.
    """

    if config["browser"] == "chrome":
        options = ChromeOptions()
    elif config["browser"] == "firefox":
        options = FirefoxOptions()
    elif config["browser"] == "MicrosoftEdge":
        options = EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: '{config['browser']}'")
    options.add_argument("--headless")

    try:
        driver = webdriver.Remote(command_executor=config["executor"], options=options)
    except Exception as e:
        logger.error(f"Failed to initialize WebDriver: {e}")
        raise

    driver.implicitly_wait(config["implicit_wait_time"])

    capabilities = driver.capabilities
    logger.debug(f"Initialized WebDriver for {capabilities['browserName']} version {capabilities['browserVersion']}.")
    logger.info(f"Running test '{request.node.name}'...")

    yield driver
    driver.quit()

    logger.info(f"{get_results(request)}")
    logger.info("Test completed.")
    logger.debug(f"WebDriver is closed.")
    logger.add_divider()
