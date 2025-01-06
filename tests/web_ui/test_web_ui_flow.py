from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests_lib.helpers.web_ui.cart_page import CartPage
from tests_lib.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests_lib.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from tests_lib.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from tests_lib.helpers.web_ui.assertions import Assertions
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_test_data("web_ui_login_credentials_test_data"))
def test_login_page_successful_login(driver, input_data, logger):
    """
    Test login into the website using different users.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)

    # act
    logger.debug(f"Page with url '{login_page.base_url}' is loaded.")
    logger.debug(f"Login with username: {input_data['username']}.")
    login_page.login(input_data["username"], input_data["password"])

    # assert
    try:
        Assertions.assert_text_in_current_url(driver, "inventory")
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED. \n AssertionError: \n {e}")
        raise


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_inventory_page_add_items_to_cart(driver, logger, input_data):
    """
    Test that items can be added from Inventory page into shopping cart.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    logger.info("Login button is clicked, loading inventory page...")
    inventory_page = InventoryPage(driver)
    inventory_page.load(5)

    # act
    inventory_page.add_item_to_cart("backpack")
    logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.add_item_to_cart("bike-light")
    logger.info("'Sauce Labs Bike Light' is added to cart.")

    # assert
    try:
        Assertions.assert_text_in_current_url(driver, "inventory")
        logger.debug(f"Number of items in cart: {inventory_page.get_items_count_in_cart()}")
        Assertions.assert_items_count_in_inventory_page(inventory_page.get_items_count_in_cart(), 2)
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED. \n AssertionError: \n {e}")
        raise


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_cart_page_view_shopping_cart(driver, logger, input_data):
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
    inventory_page.add_item_to_cart("bike-light")
    inventory_page.go_to_cart()
    logger.info("Shopping cart link is clicked, loading cart page...")

    # act
    cart_page = CartPage(driver)
    cart_page.load(5)

    # assert
    try:
        Assertions.assert_text_in_current_url(driver, "cart")
        Assertions.assert_items_count_in_cart_page(cart_page.get_items_count_in_cart(), 2)
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED. \n AssertionError: \n {e}")
        raise


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_checkout_one_page_fill_buyer_information(driver, input_data, logger):
    """
    Test that the form for buyer information in Checkout step One page can be filled.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("backpack")
    inventory_page.add_item_to_cart("bike-light")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(5)
    cart_page.click_checkout()
    logger.info("Checkout button is clicked, loading checkout step one page...")

    # act
    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    logger.info(f"Page with url '{checkout_one_page.base_url}' is loaded.")
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])

    # assert
    try:
        Assertions.assert_text_in_current_url(driver, "checkout-step-one")
        Assertions.assert_buyer_info_is_entered(checkout_one_page.get_buyer_info(), input_data["first_name"],
                                                input_data["last_name"], input_data["postal_code"])
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED. \n AssertionError: \n {e}")
        raise


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_checkout_two_page_verify_items_in_order(driver, logger, input_data):
    """
    Test that the checkout overview in Checkout step Two page represents the order correctly.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("backpack")
    inventory_page.add_item_to_cart("bike-light")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(5)
    cart_page.click_checkout()

    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    checkout_one_page.click_continue_button()
    logger.info("Continue button is clicked, loading checkout step two page...")

    # act
    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    logger.debug(f"Number of items in order: {checkout_two_page.get_items_count_in_order()}")

    # assert
    try:
        Assertions.assert_text_in_current_url(driver, "checkout-step-two")
        Assertions.assert_items_count_in_order(checkout_two_page.get_items_count_in_order(), 2)
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED. \n AssertionError: \n {e}")
        raise


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_checkout_complete_page_verify_order_is_completed(driver, logger, input_data):
    """
    Test that the order is completed.
    """
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_item_to_cart("backpack")
    inventory_page.add_item_to_cart("bike-light")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(5)
    cart_page.click_checkout()

    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    checkout_one_page.click_continue_button()

    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    checkout_two_page.click_finish_button()
    logger.info("Finish button is clicked, loading checkout complete page...")

    # act
    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.load(5)
    logger.info(f"Page with url '{checkout_complete.base_url}' is loaded.")

    # assert
    try:
        Assertions.assert_text_in_current_url(driver, "checkout-complete")
        Assertions.assert_message_for_complete_order(checkout_complete.get_message_text(), "Thank you for your order!")
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED. \n AssertionError: \n {e}")
        raise
