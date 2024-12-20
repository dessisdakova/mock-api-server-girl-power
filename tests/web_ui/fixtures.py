from tests_lib.common.yaml_loaders import load_config
from tests_lib.common.custom_logger import CustomLogger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest


@pytest.fixture(scope="session")
def driver() -> webdriver:
    config = load_config("web_ui_config")
    if config["options"] == "chrome":
        options = ChromeOptions()
    elif config["options"] == "firefox":
        options = FirefoxOptions()
    elif config["options"] == "edge":
        options = EdgeOptions()
    else:
        raise TypeError("Browser not supported!")
    options.add_argument("--headless")

    driver = webdriver.Remote(config["executor"], options=options)
    driver.implicitly_wait(config["wait_time"])
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def logger() -> CustomLogger:
    log = CustomLogger("web_ui_logger", "web_ui_tests.log")
    return log
