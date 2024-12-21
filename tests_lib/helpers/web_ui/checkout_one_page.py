from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CheckoutOnePage(BasePage):
    """
    Page object for the checkout step one page.
    Inherits from BasePage.
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

    def enter_buyer_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Enters buyer information.

        :param first_name: The buyers first name.
        :param last_name: The buyers last name.
        :param zip_code: The buyers zip code name.
        """
        self.driver.find_element(*FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*ZIP_CODE_FIELD).send_keys(zip_code)

    def assert_buyer_into_is_entered(self, expected_fn: str, expected_ln: str, expected_zc: str) -> None:
        """
        Assert that the buyer's first name, last name, and zip code are correctly entered in the form.

        :param expected_fn: The expected value for the first name field.
        :param expected_ln: The expected value for the last name field.
        :param expected_zc: The expected value for the zip code field.
        :raises AssertionError: If any of the entered values do not match the expected values.
        """
        assert self.driver.find_element(*FIRST_NAME_FIELD).get_attribute("value") == expected_fn
        assert self.driver.find_element(*LAST_NAME_FIELD).get_attribute("value") == expected_ln
        assert self.driver.find_element(*ZIP_CODE_FIELD).get_attribute("value") == str(expected_zc)

    def click_continue_button(self) -> None:
        """
        Click the continue button to proceed to the next step in the order process.
        """
        self.driver.find_element(*CONTINUE_BUTTON).click()
