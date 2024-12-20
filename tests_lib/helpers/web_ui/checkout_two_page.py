from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CheckoutTwoPage(BasePage):
    """
    Page object for the checkout step two page. Inherits from BasePage.
    """
    @property
    def base_url(self) -> str:
        """
        The URL of the checkout step two page.

        :return: A string representing the page URL.
        """
        return super().base_url + "checkout-step-two.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the checkout step two page has loaded.

        :return: Locator as tuple.
        """
        return SUMMARY_INFO_DIV

    def click_finish_button(self):
        self.driver.find_element(*FINISH_BUTTON).click()

    def get_items_count_in_order(self) -> int:
        """
        Retrieves all items in the order.

        :return: The number of items added to the cart.
        """
        return len(self.driver.find_elements(*ITEMS_IN_CART))

    def assert_items_count_in_order(self, count: int) -> None:
        """
        Asserts the count of items in order.

        :param count: Number of items in order - int
        :return: None
        """
        assert self.get_items_count_in_order() == count, "Item was not added to cart."
