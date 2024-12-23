from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CheckoutCompletePage(BasePage):
    """
    Page object for the checkout complete page.
    Inherits from BasePage.
    """

    @property
    def base_url(self):
        """
        The URL of the checkout complete page.

        :return: A string representing the page URL.
        """
        return super().base_url + "checkout-complete.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the checkout complete page has loaded.

        :return: Locator as tuple.
        """
        return CHECKOUT_COMPLETE_CONTAINER

    def get_message_text(self) -> str:
        """
        Retrieve the text from the message header element.

        :return: The text content of the message header.
        """
        return self.driver.find_element(*MESSAGE_HEADER).text

    def assert_message_for_complete_order(self, expected_text: str) -> None:
        """
        Assert that the message text matches the expected text.

        :param expected_text: The expected text to compare with the message header.
        :raises AssertionError: If the actual message text does not match the expected text.
        """
        actual_text = self.get_message_text()
        assert actual_text == expected_text, f"Order was not completed. " \
                                             f"Expected message '{expected_text}', but got '{actual_text}'."
