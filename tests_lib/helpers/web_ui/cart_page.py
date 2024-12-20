from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class CartPage(BasePage):
    """
    Page object for the cart page. Inherits from BasePage.
    """
    @property
    def base_url(self) -> str:
        """
        The URL of the cart page.

        :return: A string representing the page URL.
        """
        return super().base_url + "cart.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the cart page has loaded.

        :return: Locator as tuple.
        """
        return CART_CONTENTS_CONTAINER

    def get_items_count_in_cart(self) -> int:
        """
        Retrieves all items in the cart.

        :return: The number of items added to the cart.
        """
        return len(self.driver.find_elements(*ITEMS_IN_CART))

    def click_checkout(self) -> None:
        """
        Navigates to the checkout step one page by clicking the checkout button.
        """
        self.driver.find_element(*CHECKOUT_BUTTON).click()

    def assert_item_count_in_cart(self, count: int) -> None:
        """
        Asserts the count of items in cart.

        :param count: Number of items added in the cart - int
        :return: None
        """
        assert self.get_items_count_in_cart() == count, "Item was not added to cart."
