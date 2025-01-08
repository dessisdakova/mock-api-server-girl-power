from selenium import webdriver


class Assertions:
    @staticmethod
    def assert_text_in_current_url(current_url: str, text: str) -> None:
        """
        Assert that a specific text is present in the current URL of the web driver.

        :param current_url: The current URL of the driver.
        :param text: The text expected to be present in the current URL.
        :raises AssertionError: If the specified text is not found in the current URL.
        """
        assert text in current_url, f"Expected text '{text}' not found in URL '{current_url}'."

    @staticmethod
    def assert_items_count_in_inventory_page(actual_count: int, expected_count: int) -> None:
        """
        Assert that the number of items in the cart matches the expected count on the Inventory page.

        :param actual_count: The actual number of items in the cart.
        :param expected_count: The expected number of items in the cart.
        :raises AssertionError: If the actual count does not match the expected count.
        """
        actual_count = actual_count
        assert actual_count == expected_count, f"Expected {expected_count} items in cart, but found {actual_count}."

    @staticmethod
    def assert_items_count_in_cart_page(actual_count: int, expected_count: int) -> None:
        """
        Assert that the number of items in the cart matches the expected count on the Cart page.

        :param actual_count: The actual number of items in the cart.
        :param expected_count: The expected number of items in the cart.
        :raises AssertionError: If the actual count does not match the expected count.
        """
        actual_count = actual_count
        assert actual_count == expected_count, f"Expected {expected_count} items in cart, but found {actual_count}."

    @staticmethod
    def assert_items_count_in_order(actual_count: int, expected_count: int) -> None:
        """
        Assert that the number of items in the order matches the expected count.

        :param actual_count: The actual number of items in the order, retrieved from the website.
        :param expected_count: The expected number of items in the order.
        :raises AssertionError: If the actual count does not match the expected count.
        """
        assert actual_count == expected_count, f"Expected {expected_count} items in order, but found {actual_count}."

    @staticmethod
    def assert_message_for_complete_order(actual_text: str, expected_text: str) -> None:
        """
        Assert that the message text for a completed order matches the expected text.

        :param actual_text: The actual message text displayed in the website.
        :param expected_text: The expected text to compare with the message header.
        :raises AssertionError: If the actual message text does not match the expected text.
        """
        assert actual_text == expected_text, f"Order was not completed. " \
                                             f"Expected message '{expected_text}', but got '{actual_text}'."
