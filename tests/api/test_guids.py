import json
import pytest

from tests.api.constants import HTTP_STATUS_CODES_FOR_PUT, TEST_DATA_PATH
from tests.api.request_executors.request_executor_fixture import request_executor
from tests_lib.common.custom_logger import CustomLogger
from tests_lib.common.json_loader import load_json

#  TODO: move to test_data_api
NEW_GUID = '12345678-abcd-ef01-2345-6789abcde-aka'


@pytest.fixture(autouse=True, scope="function")
def clear_guids(request_executor, logger_fixture):
    """
    This fixture is run before each test case.
    It's required in order to clean the internal guids data in the mock server,
    so all tests can run independently and reliably
    """
    logger_fixture.info("clear_guids")
    empty_guids = load_json(TEST_DATA_PATH + 'PUT_guids_empty_list.json', logger_fixture)
    put_response = request_executor.execute_put("/guids", empty_guids)
    assert put_response.status_code == 200


def test_post_guid_add(logger_fixture: CustomLogger, request_executor):
    """
    Verifying positive case: that response return valid body and status for POST request which contain guid in URL.
    """
    try:
        post_response = request_executor.execute_post(f"/{NEW_GUID}/add")
        assert post_response.status_code == 200
        assert NEW_GUID in post_response.json()['guids']
        logger_fixture.info("Test passed successfully")
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")


def test_post_guid_add_without_guid(logger_fixture: CustomLogger, request_executor):
    """
    Verifying negative case: that response return status 404 for POST request which contain no guid in URL.
    """
    try:
        post_response = request_executor.execute_post(f"//add")
        assert post_response.status_code == 404
        logger_fixture.info("Test passed successfully")
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")


@pytest.mark.parametrize("status_code", HTTP_STATUS_CODES_FOR_PUT)
def test_put_guids(status_code: int | str, logger_fixture: CustomLogger, request_executor):
    """
    Test guids functionality of mock-api-server.
    After executing the put method, we check that the get method for the corresponding guid value will return
    the updated value.
    """
    logger_fixture.info(f"Starting test_put_get_guids with status_code: {status_code}")
    try:
        # with open(TEST_DATA_PATH + "PUT_guids_positive.json", 'r') as expected_data_file:
        #     expected_data_json = json.load(expected_data_file)

        expected_data_json = load_json(TEST_DATA_PATH + "PUT_guids_positive.json", logger_fixture)
        expected_data_json["status_code"] = status_code


        put_response = request_executor.execute_put(f"/guids", expected_data_json)
        put_response_json = put_response.json()
        assert put_response.status_code == 200
        assert put_response_json["new_status_code"] == status_code
        assert put_response_json["new_body"] == expected_data_json["body"]
        logger_fixture.info("Test passed successfully")
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")


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
    try:
        expected_data_json = load_json(test_file_path, logger_fixture)
        put_response = request_executor.execute_put("/guids", expected_data_json)
        assert put_response.status_code == 500
        logger_fixture.info("Test passed successfully")
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")
        raise


def test_put_guids_without_request_body(logger_fixture: CustomLogger, request_executor):
    """
    Negative test for PUT guids functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have any content.
    """
    try:
        put_response = request_executor.execute_put("/guids")
        assert put_response.status_code == 400
        logger_fixture.info("Test passed successfully")
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")



def test_get_guids(logger_fixture: CustomLogger, request_executor):
    """
    Test guids functionality of mock-api-server using GET request.
    """
    try:
        # with open(TEST_DATA_PATH + "PUT_guids_empty_list.json", 'r') as expected_data_file:
        #     expected_data_json = json.load(expected_data_file)
        expected_data_json = load_json(TEST_DATA_PATH + "PUT_guids_empty_list.json", logger_fixture)
        get_rsp = request_executor.execute_get(f"/guids")
        assert get_rsp.status_code == expected_data_json["status_code"]
        assert get_rsp.json() == expected_data_json["body"]
        logger_fixture.info("Test passed successfully")
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")
        raise


def test_post_several_items(logger_fixture: CustomLogger, request_executor):
    """
    Test POST request by adding several guids(one at a time) to guids list.
    Then verifying guids list using GET request
    """
    try:
        for _ in range(5):
            request_executor.execute_post(f"/{NEW_GUID}/add")

        get_rsp = request_executor.execute_get(f"/guids")
        assert get_rsp.status_code == 200
        assert get_rsp.json()['guids'] == [NEW_GUID] * 5
    except Exception as e:
        logger_fixture.error(f"Test failed with error: {e}")
