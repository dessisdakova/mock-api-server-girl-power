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
        Navigates to the base URL and wait for the page to load using explicit wait.

        :param explicit_wait: Time the driver should wait for in seconds - int
        :return:
        """
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, explicit_wait).until(ec.presence_of_element_located(self.explicit_wait_locator))

    def assert_text_in_url(self, text: str) -> None:
        """
        Asserts if a given text is present in page's URL.

        :param text: Assertion text - string
        :return: None
        """
        assert text in self.base_url, "Text is not present in URL."

