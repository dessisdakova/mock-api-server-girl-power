from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Base class for all page objects. Provides shared functionalities.
    """
    def __init__(self, driver: webdriver.Remote):
        """
        Initialize with a WebDriver instance.

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

    def get_current_url(self):
        """
        Return the current driver url.
        """
        return self.driver.current_url

    def load(self, explicit_wait: int) -> None:
        """
        Navigate to the base URL and wait for the page to load using explicit wait.
        Each derived class must define the "explicit_wait_locator" property,
        which is used to verify the page has loaded before proceeding.

        :param explicit_wait: The time in seconds to wait for the page to load.
        :raises AttributeError: If no locator is defined in the derived class.
        """
        self.driver.get(self.base_url)
        if not hasattr(self, "explicit_wait_locator"):
            raise AttributeError(f"No explicit wait locator provided in {self.__class__.__name__} class.")
        WebDriverWait(self.driver, explicit_wait).until(ec.presence_of_element_located(self.explicit_wait_locator))
