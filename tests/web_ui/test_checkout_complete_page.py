from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
from tests_lib.helpers.web_ui.checkout_complete_page import CheckoutCompletePage
from tests.web_ui.fixtures import *


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
