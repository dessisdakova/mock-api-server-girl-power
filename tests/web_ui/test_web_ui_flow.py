import pytest
from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests_lib.helpers.web_ui.cart_page import CartPage
from tests_lib.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests_lib.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from tests_lib.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_test_data("web_ui_login_test_data"))
def test_login_page(driver, input_data, logger):
    login_page = LoginPage(driver)
    login_page.load(5)
    logger.info(f"Page with url '{login_page.base_url}' is loaded.")
    login_page.assert_text_in_url("saucedemo")
    login_page.login(input_data["username"], input_data["password"])
    logger.info(f"Successful login with username: {input_data['username']}.")


def test_inventory_page(driver, logger):
    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    logger.info(f"Page with url '{inventory_page.base_url}' is loaded.")
    inventory_page.assert_text_in_url("inventory")
    inventory_page.add_backpack_to_cart()
    logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.go_to_cart()
    logger.info("Shopping cart link is clicked, loading cart page...")


def test_cart_page(driver, logger):
    cart_page = CartPage(driver)
    cart_page.load(5)
    logger.info(f"Page with url '{cart_page.base_url}' is loaded.")
    cart_page.assert_text_in_url("cart")
    cart_page.assert_item_count_in_cart(1)
    cart_page.click_checkout()
    logger.info("Checkout button is clicked, loading checkout step one page...")


@pytest.mark.parametrize("input_data", load_test_data("web_ui_buyer_info_test_data"))
def test_checkout_one_page(driver, input_data, logger):
    checkout_one_page = CheckoutOnePage(driver)
    checkout_one_page.load(5)
    logger.info(f"Page with url '{checkout_one_page.base_url}' is loaded.")
    checkout_one_page.assert_text_in_url("checkout-step-one")
    checkout_one_page.enter_buyer_info_and_proceed_to_next_page(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])
    logger.info("Buyer's information is entered, continue button is clicked, loading checkout step two page...")


def test_checkout_two_page(driver, logger):
    checkout_two_page = CheckoutTwoPage(driver)
    checkout_two_page.load(5)
    logger.info(f"Page with url '{checkout_two_page.base_url}' is loaded.")
    checkout_two_page.assert_text_in_url("checkout-step-two")
    checkout_two_page.assert_items_count_in_order(1)
    checkout_two_page.click_finish_button()
    logger.info("Finish button is clicked, loading checkout complete page...")


def test_checkout_complete_page(driver, logger):
    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.load(5)
    logger.info(f"Page with url '{checkout_complete.base_url}' is loaded.")
    checkout_complete.assert_text_in_url("checkout-complete")
    checkout_complete.assert_message_text("Thank you for your order!")



