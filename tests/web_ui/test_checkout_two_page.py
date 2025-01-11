from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests_lib.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_checkout_two_page_verify_items_in_order(driver, logger, input_data):
    """
    Test that items in order in Checkout Two page match the items added in Inventory page.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("backpack")
    logger.info("'Sauce Labs Backpack' is added to cart.")

    # act
    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    logger.debug(f"Page with url '{checkout_two_page.base_url}' is loaded.")

    # assert
    assert "checkout-step-two" in checkout_two_page.get_current_url(), f"Expected text not found in URL."
    assert checkout_two_page.get_items_count_in_order() == 1, f"Actual items count does not match expected."
    assert "Sauce Labs Backpack" in checkout_two_page.get_item_names_in_cart(), f"Expected item name not found in cart."


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_checkout_two_page_verify_finish_button(driver, logger, input_data):
    """
    Test that the Finish button redirects to Checkout Complete page.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    logger.debug(f"Page with url '{checkout_two_page.base_url}' is loaded.")

    # act
    checkout_two_page.click_finish_button()

    # assert
    assert "checkout-complete" in checkout_two_page.get_current_url(), f"User is not redirected to another page."
