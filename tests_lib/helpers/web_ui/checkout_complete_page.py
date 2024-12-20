from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CheckoutCompletePage(BasePage):
    """
    Page object for the checkout complete page. Inherits from BasePage.
    """

    @property
    def base_url(self):
        """
        The URL of the checkout complete page.

        :return: A string representing the page URL.
        """
        return super().base_url + "checkout-complete.html"

    @property
    def explicit_wait_locator(self):
        """
        Locator for the element used to verify the checkout complete page has loaded.

        :return: Locator as tuple.
        """
        return CHECKOUT_COMPLETE_CONTAINER

    def get_message_text(self) -> str:
        """
        Retrieves the element containing the final message for completed order.

        :return: String representation of the complete order message.
        """
        return self.driver.find_element(*MESSAGE_HEADER).text

    def assert_message_text(self, text: str) -> None:
        """
        Asserts if a given text equals complete order message on website.

        :param text: Assertion text - string
        :return: None
        """
        assert self.get_message_text() == text, "Order was not completed."
