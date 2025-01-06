from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class InventoryPage(BasePage):
    """
    Page object for the inventory page.
    Inherits from BasePage.
    """
    @property
    def base_url(self) -> str:
        """
        The URL of the inventory page.

        :return: A string representing the inventory page URL.
        """
        return super().base_url + "inventory.html"

    @property
    def explicit_wait_locator(self) -> tuple:
        """
        Locator for the element used to verify the inventory page has loaded.

        :return: Locator tuple for the inventory container.
        """
        return INVENTORY_CONTAINER

    def add_item_to_cart(self, item: str) -> None:
        """
        Add item to cart based on the following values:
         - "backpack" - adds Sauce Labs Backpack
         - "bike-light" - adds Sauce Labs Bike Light

        :param item: Must be one of the provided values.
        :return: None
        :raises ValueError: If the value of item does not match the provided ones.
        """
        if item == "backpack":
            self.driver.find_element(*ADD_BACKPACK_BUTTON).click()
        elif item == "bike-light":
            self.driver.find_element(*ADD_BIKE_LIGHT_BUTTON).click()
        else:
            raise ValueError(f"Unknown item '{item}'!")

    def get_items_count_in_cart(self) -> int:
        """
        Retrieve items count in cart from shopping cart badge.
        """
        items = self.driver.find_element(*SHOPPING_CART_BADGE).text
        return int(items)

    def go_to_cart(self) -> None:
        """
        Navigate to the shopping cart page by clicking the cart link.
        """
        self.driver.find_element(*SHOPPING_CART_LINK).click()
