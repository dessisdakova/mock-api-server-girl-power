from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Base class for all page objects. Provides shared functionalities.
    """
    def __init__(self, driver):
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

    def load(self, explicit_wait: int) -> None:
        """
        Navigate to the base URL and wait for the page to load using explicit wait.

        :param explicit_wait: The time in seconds to wait for the page to load.
        """
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, explicit_wait).until(ec.presence_of_element_located(self.explicit_wait_locator))

    def assert_text_in_url(self, text: str) -> None:
        """
        Assert that a specific text is present in the base URL.

        :param text: The text to check for in the URL.
        :raises AssertionError: If the text is not found in the base URL.
        """
        assert text in self.base_url, "Text is not present in URL."

