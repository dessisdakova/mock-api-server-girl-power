from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests_lib.helpers.web_ui.cart_page import CartPage
from tests_lib.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests_lib.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from tests_lib.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from tests.web_ui.fixtures import *


def test_login_page_load_page(driver):
    # arrange
    login_page = LoginPage(driver)

    # act
    login_page.load(5)

    # assert
    login_page.assert_text_in_url("saucedemo")


@pytest.mark.parametrize("input_data", load_test_data("web_ui_login_test_data"))
def test_login_page_log_with_credentials(driver, input_data, logger):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)

    # act
    logger.debug(f"Page with url '{login_page.base_url}' is loaded.")
    logger.debug(f"Login with username: {input_data['username']}.")
    login_page.login(input_data["username"], input_data["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)

    # assert
    inventory_page.assert_text_in_url("inventory")


@pytest.mark.parametrize("input_data", load_test_data("web_ui_buyer_info_test_data"))
def test_inventory_page_add_item_to_cart(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    inventory_page = InventoryPage(driver)
    inventory_page.load(5)

    # act
    logger.debug(f"Page with url '{inventory_page.base_url}' is loaded.")
    inventory_page.add_backpack_to_cart()
    logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.go_to_cart()
    logger.info("Shopping cart link is clicked, loading cart page...")

    cart_page = CartPage(driver)
    cart_page.load(5)
    logger.debug(f"Page with url '{cart_page.base_url}' is loaded.")

    # assert
    cart_page.assert_text_in_url("cart")
    logger.debug(f"Number of items in cart: {cart_page.get_items_count_in_cart()}")
    cart_page.assert_item_count_in_cart(1)


@pytest.mark.parametrize("input_data", load_test_data("web_ui_buyer_info_test_data"))
def test_checkout_one_page_enter_buyer_credentials(driver, input_data, logger):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(5)
    cart_page.click_checkout()
    logger.info("Checkout button is clicked, loading checkout step one page...")

    # act
    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    checkout_one_page.assert_text_in_url("checkout-step-one")
    logger.info(f"Page with url '{checkout_one_page.base_url}' is loaded.")
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])

    # assert
    checkout_one_page.assert_buyer_into_is_entered(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])


@pytest.mark.parametrize("input_data", load_test_data("web_ui_buyer_info_test_data"))
def test_checkout_two_page_item_in_order(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.load(5)
    cart_page.click_checkout()

    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    checkout_one_page.click_continue_button()

    # act
    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    logger.info(f"Page with url '{checkout_two_page.base_url}' is loaded.")
    checkout_two_page.assert_text_in_url("checkout-step-two")
    logger.debug(f"Number of items in order: {checkout_two_page.get_items_count_in_order()}")

    # assert
    checkout_two_page.assert_items_count_in_order(1)


@pytest.mark.parametrize("input_data", load_test_data("web_ui_buyer_info_test_data"))
def test_checkout_complete_page_order_completed(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_backpack_to_cart()
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

    # act
    logger.info("Finish button is clicked, loading checkout complete page...")
    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.load(5)
    logger.info(f"Page with url '{checkout_complete.base_url}' is loaded.")

    # assert
    checkout_complete.assert_text_in_url("checkout-complete")
    checkout_complete.assert_message_text("Thank you for your order!")
