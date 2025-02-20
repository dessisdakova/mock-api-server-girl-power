import pytest

from tests.api.constants import TEST_DATA_PATH, INVENTORY_DEVICES_URL
from tests_lib.common.custom_logger import CustomLogger
from tests_lib.common.json_loader import load_json
from tests_lib.helpers.api.request_executors.request_executor_fixture import request_executor


@pytest.fixture(autouse=True, scope="function")
def clear_inventory_appliances(request_executor, logger_fixture):
    """
    This fixture is run before each test case.
    It's required in order to clean the internal inventory devices data in the mock server,
    so all tests can run independently and reliably
    """
    yield
    logger_fixture.info('clearing inventories')
    empty_inventory = load_json(TEST_DATA_PATH + 'PUT_inventory_empty_list.json')
    put_response = request_executor.execute_put(INVENTORY_DEVICES_URL, empty_inventory)
    assert put_response.status_code == 200
    logger_fixture.info('inventories cleared')


@pytest.mark.parametrize("status_code", load_json(TEST_DATA_PATH + "http_status_codes.json")["HTTP_STATUS_CODES"])
def test_put_inventory_appliances(status_code: int, logger_fixture: CustomLogger, request_executor):
    """
    Test inventory functionality of mock-api-server.
    Executing the PUT method, updating the whole resource by adding body and status code.
    """
    logger_fixture.info(f"Starting test_put_get_guids with status_code: {status_code}")
    expected_data_json = load_json(TEST_DATA_PATH + "PUT_inventory_positive.json")
    expected_data_json["status_code"] = status_code
    print()
    put_response = request_executor.execute_put(INVENTORY_DEVICES_URL, expected_data_json)
    put_response_json = put_response.json()
    assert put_response.status_code == 200
    assert put_response_json["new_status_code"] == status_code
    assert put_response_json["new_body"] == expected_data_json["body"]
    logger_fixture.info("Test passed successfully")


def test_put_inventory_without_key_body(logger_fixture: CustomLogger, request_executor):
    """
    Negative test for PUT inventory functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have body key.
    """
    expected_data_json = load_json(TEST_DATA_PATH + "PUT_inventory_without_body.json")
    put_response = request_executor.execute_put(INVENTORY_DEVICES_URL, expected_data_json)
    assert put_response.status_code == 500
    logger_fixture.info("Test passed successfully")


def test_put_inventory_without_key_status_code(logger_fixture: CustomLogger, request_executor):
    """
    Negative test for PUT inventory functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have status code.
    """
    expected_data_json = load_json(TEST_DATA_PATH + "PUT_inventory_without_status_code.json")
    put_response = request_executor.execute_put(INVENTORY_DEVICES_URL, expected_data_json)
    assert put_response.status_code == 500
    logger_fixture.info("Test passed successfully")



def test_put_inventory_without_request_body(logger_fixture: CustomLogger, request_executor):
    """
    Negative test for PUT inventory functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have any content.
    """

    put_response = request_executor.execute_put(INVENTORY_DEVICES_URL)
    assert put_response.status_code == 400
    logger_fixture.info("Test passed successfully")

