import pytest

from tests.api.constants import TEST_DATA_PATH, GUID_GET_URL, GUID_ADD_URL
from tests_lib.helpers.api.request_executors.request_executor_fixture import request_executor
from tests_lib.common.custom_logger import CustomLogger
from tests_lib.common.json_loader import load_json


@pytest.fixture(autouse=True, scope="function")
def clear_guids(request_executor, logger_fixture):
    """
    This fixture cleans the internal guids data after the test execution.
    It's required in order to clean the internal guids data in the mock server,
    so all tests can run independently and reliably
    """
    yield
    logger_fixture.info("clearing guids")
    empty_guids = load_json(TEST_DATA_PATH + 'PUT_guids_empty_list.json')
    put_response = request_executor.execute_put(GUID_GET_URL, empty_guids)
    assert put_response.status_code == 200
    logger_fixture.info("guids cleared")


def test_post_guid_add(logger_fixture: CustomLogger, request_executor):
    """
    Verifying positive case: that response return valid body and status for POST request which contain guid in URL.
    """
    new_guid = load_json(TEST_DATA_PATH + "new_guid.json")
    add_url = GUID_ADD_URL.replace("<path:guid>", new_guid)

    post_response = request_executor.execute_post(add_url)
    assert post_response.status_code == 200
    assert new_guid in post_response.json()['guids']
    logger_fixture.info("Test passed successfully")


def test_post_guid_add_without_guid(logger_fixture: CustomLogger, request_executor):
    """
    Verifying negative case: that response return status 404 for POST request which contain no guid in URL.
    """
    post_response = request_executor.execute_post(f"//add")
    assert post_response.status_code == 404
    logger_fixture.info("Test passed successfully")



@pytest.mark.parametrize("status_code", load_json(TEST_DATA_PATH + "http_status_codes.json")["HTTP_STATUS_CODES"])
def test_put_guids(status_code: int | str, logger_fixture: CustomLogger, request_executor):
    """
    Test guids functionality of mock-api-server.
    Executing the put method.
    """
    logger_fixture.info(f"Starting test_put_get_guids with status_code: {status_code}")
    expected_data_json = load_json(TEST_DATA_PATH + "PUT_guids_positive.json")
    expected_data_json["status_code"] = status_code
    put_response = request_executor.execute_put(GUID_GET_URL, expected_data_json)
    put_response_json = put_response.json()
    assert put_response.status_code == 200
    assert put_response_json["new_status_code"] == status_code
    assert put_response_json["new_body"] == expected_data_json["body"]
    logger_fixture.info("Test passed successfully")


@pytest.mark.parametrize("test_file", [
                         "PUT_guids_without_key_body.json",
                         "PUT_guids_without_key_status_code.json"])
def test_put_guids_without_key_body(test_file, logger_fixture: CustomLogger, request_executor):
    """
    Negative test for PUT guids functionality of mock-api-server.
    This test check PUT request
    (1) without key body, but contains the key status_code and
    (2) without key status code, but contain the key body
    """
    test_file_path = TEST_DATA_PATH + test_file
    expected_data_json = load_json(test_file_path)
    put_response = request_executor.execute_put(GUID_GET_URL, expected_data_json)
    assert put_response.status_code == 500
    logger_fixture.info("Test passed successfully")


def test_put_guids_without_request_body(logger_fixture: CustomLogger, request_executor):
    """
    Negative test for PUT guids functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have any content.
    """

    put_response = request_executor.execute_put(GUID_GET_URL)
    assert put_response.status_code == 400
    logger_fixture.info("Test passed successfully")


def test_get_guids(logger_fixture: CustomLogger, request_executor):
    """
    Test guids functionality of mock-api-server using GET request.
    """
    expected_data_json = load_json(TEST_DATA_PATH + "PUT_guids_empty_list.json")
    get_rsp = request_executor.execute_get(GUID_GET_URL)
    assert get_rsp.status_code == expected_data_json["status_code"]
    assert get_rsp.json() == expected_data_json["body"]
    logger_fixture.info("Test passed successfully")


def test_post_several_items(logger_fixture: CustomLogger, request_executor):
    """
    Test POST request by adding several guids(one at a time) to guids list.
    Then verifying guids list using GET request
    """
    new_guid = load_json(TEST_DATA_PATH + "new_guid.json")
    add_url = GUID_ADD_URL.replace("<path:guid>", new_guid)
    for _ in range(5):
        request_executor.execute_post(add_url)

    get_rsp = request_executor.execute_get(GUID_GET_URL)
    assert get_rsp.status_code == 200
    assert get_rsp.json()['guids'] == [new_guid] * 5

