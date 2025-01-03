from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from abc import ABC, abstractmethod


class BasePage(ABC):
    """
    Base class for all page objects. Provides shared functionalities.
    """
    def __init__(self, driver: webdriver.Remote):
        """
        Initialize the BasePage with a WebDriver instance.

        :param driver: WebDriver instance to interact with the browser.
        """
        self.driver = driver

    @property
    def base_url(self) -> str:
        """
        The base URL of the website.

        :return: A string representing the base URL.
        """
        return "https://www.saucedemo.com/"

    @property
    @abstractmethod
    def explicit_wait_locator(self) -> tuple:
        """
        Each derived class must define the "explicit_wait_locator" property,
        which is used to verify the page has loaded before proceeding.

        :return: A tuple representing the locator (By, value).
        """
        pass

    def load(self, explicit_wait: int) -> None:
        """
        Navigate to the base URL and wait for the page to load using explicit wait.

        :param explicit_wait: The time in seconds to wait for the page to load.
        """
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, explicit_wait).until(ec.presence_of_element_located(self.explicit_wait_locator))
