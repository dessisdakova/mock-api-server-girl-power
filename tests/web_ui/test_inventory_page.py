from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_inventory_page_add_items_to_cart(driver, logger, input_data):
    """
    Test that items can be added from Inventory page into shopping cart.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    logger.debug(f"Page with url '{inventory_page.base_url}' is loaded.")

    # act
    inventory_page.add_item_to_cart("backpack")
    logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.add_item_to_cart("bike-light")
    logger.info("'Sauce Labs Bike Light' is added to cart.")

    # assert
    assert "inventory" in inventory_page.get_current_url(), f"Expected text not found in URL."
    assert inventory_page.get_items_count_in_cart() == 2, f"Actual items count does not match expected."
