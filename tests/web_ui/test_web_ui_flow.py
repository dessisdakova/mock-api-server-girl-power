from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests_lib.helpers.web_ui.cart_page import CartPage
from tests_lib.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests_lib.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from tests_lib.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_login_page_successful_login(driver, input_data, logger):
    """
    Test login using different users.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    logger.debug(f"Page with url '{login_page.base_url}' is loaded.")

    # act
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    # assert
    assert "inventory" in login_page.get_current_url(), f"Expected text not found in URL."


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


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_cart_page_verify_items_in_shopping_cart(driver, logger, input_data):
    """
    Test that added items from Inventory page are present in Cart page.
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
    inventory_page.go_to_cart()

    # act
    cart_page = CartPage(driver)
    cart_page.load(5)
    logger.debug(f"Page with url '{cart_page.base_url}' is loaded.")

    # assert
    assert "cart" in inventory_page.get_current_url(), f"Expected text not found in URL."
    assert cart_page.get_items_count_in_cart() == 1, f"Actual items count does not match expected."
    assert "Sauce Labs Backpack" in cart_page.get_item_names_in_cart(), f"Expected item name not found in cart."


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_cart_page_verify_checkout_button(driver, logger, input_data):
    """
    Test that the Checkout button in Cart page redirects to Checkout step One page.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    cart_page = CartPage(driver)
    cart_page.load(5)
    logger.debug(f"Page with url '{cart_page.base_url}' is loaded.")

    # act
    cart_page.click_checkout_button()

    # assert
    assert "checkout-step-one" in cart_page.get_current_url(), f"User is not redirected to another page."


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_checkout_one_page_verify_continue_button_with_buyer_information(driver, input_data, logger):
    """
    Test that the Continue button in Checkout One page
    redirects to Checkout Two page when buyer information is filled.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    logger.debug(f"Page with url '{checkout_one_page.base_url}' is loaded.")

    # act
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    checkout_one_page.click_continue_button()

    # assert
    assert "checkout-step-two" in checkout_one_page.get_current_url(), f"Expected text not found in URL."


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_checkout_one_page_verify_continue_button_without_buyer_information(driver, input_data, logger):
    """
    Test that the Continue button in Checkout One page
    does not redirect to Checkout Two page when buyer information is not filled.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    logger.debug(f"Page with url '{checkout_one_page.base_url}' is loaded.")

    # act
    checkout_one_page.click_continue_button()

    # assert
    assert "checkout-step-one" in checkout_one_page.get_current_url(), f"User is redirected to another page."


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


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_checkout_complete_page_verify_message(driver, logger, input_data):
    """
    Test that the message for complete order in present.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    # act
    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.load(5)
    logger.debug(f"Page with url '{checkout_complete.base_url}' is loaded.")

    # assert
    assert "checkout-complete" in checkout_complete.get_current_url(), f"Expected text not found in URL."
    assert "Thank you for your order!" in checkout_complete.get_message_text(), f"Order was not completed."


@pytest.mark.parametrize("input_data", load_test_data("web_ui", "entire_flow"))
def test_complete_flow(driver, logger, input_data):
    """
    Test the entire flow with different users.
    """
    login_page = LoginPage(driver)
    login_page.load(10)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("backpack")
    logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.add_item_to_cart("bike-light")
    logger.info("'Sauce Labs Bike Light' is added to cart.")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(5)
    logger.debug(f"Page with url '{cart_page.base_url}' is loaded.")
    cart_page.click_checkout_button()

    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    logger.debug(f"Page with url '{checkout_one_page.base_url}' is loaded.")
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    logger.info("Buyer's information is filled.")
    checkout_one_page.click_continue_button()

    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    logger.debug(f"Page with url '{checkout_two_page.base_url}' is loaded.")

    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.load(5)
    logger.debug(f"Page with url '{checkout_complete.base_url}' is loaded.")

    assert "Thank you for your order!" in checkout_complete.get_message_text(), f"Order was not completed."
