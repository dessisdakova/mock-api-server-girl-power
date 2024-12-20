from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class LoginPage(BasePage):
    """
    Page object for the login page. Inherits from BasePage.
    """

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the page has loaded.

        :return: Locator as tuple.
        """
        return LOGO_DIV

    def login(self, username: str, password: str) -> None:
        """
        Performs a login action by entering the username and password and clicking the login button.
        Logs the action.

        :param username: The username to enter.
        :param password: The password to enter.
        :return: None
        """
        self.driver.find_element(*USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LOGIN_BUTTON).click()
