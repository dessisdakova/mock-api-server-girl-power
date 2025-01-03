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

    def add_backpack_to_cart(self) -> None:
        """
        Click the button to add the backpack item to the shopping cart.
        """
        self.driver.find_element(*ADD_BACKPACK_BUTTON).click()

    def add_bike_light_to_cart(self) -> None:
        """
        Click the button to add the bike light item to the shopping cart.
        """
        self.driver.find_element(*ADD_BIKE_LIGHT_BUTTON).click()

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
