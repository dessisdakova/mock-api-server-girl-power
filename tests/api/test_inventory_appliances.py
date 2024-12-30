from tests.api.request_utilities import execute_put, execute_get
from tests.api.constants import HTTP_STATUS_CODES, TEST_DATA_PATH
import json, pytest


@pytest.mark.parametrize("status_code", HTTP_STATUS_CODES)
def test_put_get_inventory_appliances(status_code: int, logger):
    """
    Test inventory functionality of mock-api-server.
    After executing the put method, we check that the get method for the corresponding inventory_appliances value
    will return the updated value.
    """
    logger.info(f"Starting test_put_get_guids with status_code: {status_code}")
    try:
        with open(TEST_DATA_PATH + "PUT_inventory_positive.json", 'r') as expected_data_file:
            expected_data_json = json.load(expected_data_file)

        expected_data_json["status_code"] = status_code

        put_response = execute_put("/inventory/devices", expected_data_json)
        put_response_json = put_response.json()
        assert put_response.status_code == 200
        assert put_response_json["new_status_code"] == status_code
        assert put_response_json["new_body"] == expected_data_json["body"]

        get_rsp = execute_get("/inventory/devices")

        assert get_rsp.status_code == expected_data_json["status_code"]
        assert get_rsp.json() == expected_data_json["body"]
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
        raise


def test_put_inventory_without_key_body(logger):
    """
    Negative test for PUT inventory functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    """
    try:
        with open(TEST_DATA_PATH + "PUT_inventory_without_body.json", 'r') as expected_data_file:
            expected_data_json = json.load(expected_data_file)

        put_response = execute_put("/inventory/devices", expected_data_json)
        assert put_response.status_code == 500
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")


def test_put_inventory_without_key_status_code(logger):
    """
    Negative test for PUT inventory functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    """
    try:
        with open(TEST_DATA_PATH + "PUT_inventory_without_status_code.json", 'r') as expected_data_file:
            expected_data_json = json.load(expected_data_file)

        put_response = execute_put("/inventory/devices", expected_data_json)
        assert put_response.status_code == 500
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")


def test_put_inventory_without_request_body(logger):
    """
    Negative test for PUT inventory functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have any content.
    """
    try:
        put_response = execute_put("/inventory/devices")
        assert put_response.status_code == 400
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
