from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CheckoutTwoPage(BasePage):
    """
    Page object for the checkout step two page.
    Inherits from BasePage.
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

    def click_finish_button(self) -> None:
        """
        Click the finish button to complete the order process.
        """
        self.driver.find_element(*FINISH_BUTTON).click()

    def get_items_count_in_order(self) -> int:
        """
        Retrieve all items in the order.

        :return: The number of items added to the cart.
        """
        return len(self.driver.find_elements(*ITEMS_IN_CART))

    def assert_items_count_in_order(self, expected_count: int) -> None:
        """
        Assert that the number of items in the order matches the expected count.

        :param expected_count: The expected number of items in the order.
        :raises AssertionError: If the actual count does not match the expected count.
        """
        actual_count = self.get_items_count_in_order()
        assert actual_count == expected_count, f"Expected {expected_count} items in order, but found {actual_count}."
