from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.checkout_one_page import CheckoutOnePage
from tests.web_ui.fixtures import *


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
