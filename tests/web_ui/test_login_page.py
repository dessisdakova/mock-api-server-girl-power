from tests_lib.common.yaml_loaders import load_test_data
from tests_lib.helpers.web_ui.login_page import LoginPage
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