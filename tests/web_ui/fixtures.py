from tests_lib.common.yaml_loaders import load_config
from tests_lib.common.custom_logger import CustomLogger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest
from typing import Generator


@pytest.fixture(scope="session")
def logger() -> CustomLogger:
    """
    Fixture to provide a logger for web UI tests.

    :return: A CustomLogger instance for logging test-related information.
    """
    log = CustomLogger("web_ui_logger", "web_ui_tests.log")
    return log


@pytest.fixture(scope="function")
def driver(logger, request) -> Generator[webdriver.Remote, None, None]:
    """
    Fixture to initialize a web driver for UI tests based on the configuration.

    This fixture sets up the selected browser (Chrome, Firefox, or Edge) in headless mode
    and creates a remote WebDriver instance. It also sets an implicit wait time for elements.

    :param logger: Logger fixture to log browser type.
    :param request: Request object providing test information.
    :return: A web driver instance to be used for the duration of each test.
    :raises TypeError: If the specified browser is not supported.
    """
    config = load_config("web_ui_config")

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

    logger.debug(f"WebDriver is closed.")
    logger.add_divider()


