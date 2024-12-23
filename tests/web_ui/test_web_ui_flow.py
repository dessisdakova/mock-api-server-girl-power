from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.inventory_page import InventoryPage
from tests_lib.helpers.web_ui.cart_page import CartPage
from tests_lib.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests_lib.helpers.web_ui.checkout_two_page import CheckoutTwoPage
from tests_lib.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from tests.web_ui.fixtures import *


@pytest.mark.parametrize("input_data", load_test_data("web_ui_login_credentials_test_data"))
def test_login_page_successful_login(driver, input_data, logger):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)

    # act
    logger.debug(f"Page with url '{login_page.base_url}' is loaded.")
    logger.debug(f"Login with username: {input_data['username']}.")
    login_page.login(input_data["username"], input_data["password"])

    # assert
    login_page.assert_text_in_url("inventory")


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_inventory_page_add_items_to_cart(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    inventory_page = InventoryPage(driver)
    inventory_page.load(5)

    # act
    logger.debug(f"Page with url '{inventory_page.base_url}' is loaded.")
    inventory_page.add_backpack_to_cart()
    logger.info("'Sauce Labs Backpack' is added to cart.")
    inventory_page.add_bike_light_to_cart()
    logger.info("'Sauce Labs Bike Light' is added to cart.")

    # assert
    inventory_page.assert_text_in_url("inventory")
    logger.debug(f"Number of items in cart: {inventory_page.get_items_in_cart()}")
    inventory_page.assert_items_in_cart_using_cart_badge(2)


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_cart_page_view_shopping_cart(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")
    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.go_to_cart()
    logger.info("Shopping cart link is clicked, loading cart page...")

    # act
    cart_page = CartPage(driver)
    cart_page.load(5)

    # assert
    cart_page.assert_text_in_url("cart")
    cart_page.assert_item_count_in_cart(2)


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_checkout_one_page_fill_buyer_information(driver, input_data, logger):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

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
    logger.info(f"Page with url '{checkout_one_page.base_url}' is loaded.")
    checkout_one_page.enter_buyer_info(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])

    # assert
    checkout_one_page.assert_text_in_url("checkout-step-one")
    checkout_one_page.assert_buyer_into_is_entered(
        input_data["first_name"], input_data["last_name"], input_data["postal_code"])


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_checkout_two_page_verify_items_in_order(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
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
    checkout_two_page.assert_text_in_url("checkout-step-two")
    checkout_two_page.assert_items_count_in_order(2)


@pytest.mark.parametrize("input_data", load_test_data("web_ui_common_test_data"))
def test_checkout_complete_page_order_completed(driver, logger, input_data):
    # arrange
    login_page = LoginPage(driver)
    login_page.load(5)
    login_page.login(input_data["username"], input_data["password"])
    logger.debug(f"Login with username: {input_data['username']}.")

    inventory_page = InventoryPage(driver)
    inventory_page.load(5)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
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
    checkout_complete.assert_text_in_url("checkout-complete")
    checkout_complete.assert_message_for_complete_order("Thank you for your order!")