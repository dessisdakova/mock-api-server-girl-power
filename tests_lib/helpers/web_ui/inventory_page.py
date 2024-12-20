from tests_lib.helpers.web_ui.base_page import BasePage
from tests_lib.helpers.web_ui.locators import *


class InventoryPage(BasePage):
    """
    Page object for the inventory page. Inherits from BasePage.
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
        Clicks add to cart button for backpack.
        """
        self.driver.find_element(*ADD_BACKPACK_BUTTON).click()

    def add_bike_light_to_cart(self) -> None:
        """
        Clicks add to cart button for bike light.
        """
        self.driver.find_element(*ADD_BIKE_LIGHT_BUTTON).click()

    def go_to_cart(self) -> None:
        """
        Navigates to the cart page by clicking the cart link.
        """
        self.driver.find_element(*SOPPING_CART_LINK).click()