from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CheckoutOnePage(BasePage):
    """
    Page object for the checkout step one page. Inherits from BasePage.
    """
    @property
    def base_url(self) -> str:
        """
        The URL of the checkout step one page.
        :return: A string representing the page URL.
        """
        return super().base_url + "checkout-step-one.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the checkout step one page has loaded.
        :return: Locator as tuple.
        """
        return CHECKOUT_INFO_CONTAINER

    def enter_buyer_info_and_proceed_to_next_page(self, first_name, last_name, zip_code) -> None:
        """
        Enters buyer information and clicks continue button.

        :param first_name: The buyers first name.
        :param last_name: The buyers last name.
        :param zip_code: The buyers zip code name.
        :return: None.
        """
        self.driver.find_element(*FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*ZIP_CODE_FIELD).send_keys(zip_code)
        self.driver.find_element(*CONTINUE_BUTTON).click()
