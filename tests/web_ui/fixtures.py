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
    Fixture to load and provide the driver configuration.

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
def driver(config) -> Generator[webdriver.Remote, None, None]:
    """
    Fixture to initialize a web driver for tests based on the configuration.

    This fixture sets up the selected browser (Chrome, Firefox, or Edge) in headless mode
    and creates a remote WebDriver instance. It also sets an implicit wait time for elements.

    :param config: Config fixture.
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

    driver = webdriver.Remote(command_executor=config["executor"], options=options)
    driver.implicitly_wait(config["implicit_wait_time"])
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_capabilities(driver) -> dict:
    """
    Fixture to provide the capabilities of the WebDriver instance.

    :param driver: Fixture for web driver.
    :return: A dictionary containing information about the WebDriver's capabilities (e.g., browser name, version).
    """
    return driver.capabilities


@pytest.fixture(scope="function", autouse=True)
def log_test_start_and_result(logger, request, driver_capabilities) -> None:
    """
    Fixture to log the start and result of each test.

    :param logger: Fixture for logging.
    :param request: The pytest request object providing information about the current test.
    :param driver_capabilities: Fixture providing the WebDriver's capabilities.
    """
    logger.debug(f"Initialized WebDriver for {driver_capabilities['browserName']} "
                 f"version {driver_capabilities['browserVersion']}.")
    logger.info(f"Running test '{request.node.name}'...")
    yield
    if get_results(request)["status"] == "passed":
        logger.info("Test PASSED.")
    elif get_results(request)["status"] == "failed":
        logger.error(f"Test FAILED. \n Error: \n {get_results(request)['message']}")
    else:
        logger.info(f"Test {get_results(request)['status']}.")
    logger.debug(f"WebDriver is closed.")
    logger.add_divider()
