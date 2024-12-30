import json
import pytest

from tests.api.constants import HTTP_STATUS_CODES_FOR_PUT, TEST_DATA_PATH
from tests.api.request_utilities import execute_put, execute_get, execute_post

NEW_GUID = "12345678-abcd-ef01-2345-6789abcde-aka"


@pytest.fixture(autouse=True)
def clear_guids():
    """
    This fixture is run before each test case.
    It's required in order to clean the internal guids data in the mock server,
    so all tests can run independently and reliably
    """
    with open(TEST_DATA_PATH + "PUT_guids_empty_list.json", 'r') as data_file:
        empty_guids = json.load(data_file)
    put_response = execute_put("/guids", empty_guids)
    assert put_response.status_code == 200


def test_post_guid_add(logger):
    """
    Verifying positive case: that response return valid body and status for POST request which contain guid in URL.
    """
    try:
        post_response = execute_post(f"/{NEW_GUID}/add")
        assert post_response.status_code == 200
        assert NEW_GUID in post_response.json()['guids']
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")


def test_post_guid_add_without_guid(logger):
    """
    Verifying negative case: that response return status 404 for POST request which contain no guid in URL.
    """
    try:
        post_response = execute_post(f"//add")
        assert post_response.status_code == 404
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")


@pytest.mark.parametrize("status_code", HTTP_STATUS_CODES_FOR_PUT)
def test_put_get_guids(status_code: int | str, logger):
    """
    Test guids functionality of mock-api-server.
    After executing the put method, we check that the get method for the corresponding guid value will return
    the updated value.
    """
    logger.info(f"Starting test_put_get_guids with status_code: {status_code}")
    try:
        with open(TEST_DATA_PATH + "PUT_guids_positive.json", 'r') as expected_data_file:
            expected_data_json = json.load(expected_data_file)

        expected_data_json["status_code"] = status_code


        put_response = execute_put(f"/guids", expected_data_json)
        put_response_json = put_response.json()
        assert put_response.status_code == 200
        assert put_response_json["new_status_code"] == status_code
        assert put_response_json["new_body"] == expected_data_json["body"]
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")


@pytest.mark.parametrize("test_file", [
                         "PUT_guids_without_key_body.json",
                         "PUT_guids_without_key_status_code.json"])
def test_put_guids_without_key_body(test_file, logger):
    """
    Negative test for PUT guids functionality of mock-api-server.
    This test check PUT request
    (1) without key body, but contains the key status_code and
    (2) without key status code, but contain the key body
    """
    try:
        with open(TEST_DATA_PATH + test_file, 'r') as expected_data_file:
            expected_data_json = json.load(expected_data_file)

        put_response = execute_put("/guids", expected_data_json)
        assert put_response.status_code == 500
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")


def test_put_guids_without_request_body(logger):
    """
    Negative test for PUT guids functionality of mock-api-server.
    PUT request body should contain both body and status_code.
    In this case PUT request doesn't have any content.
    """
    try:
        put_response = execute_put("/guids")
        assert put_response.status_code == 400
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")



def test_get_guids(logger):
    """
    Test guids functionality of mock-api-server using GET request.
    """
    try:
        with open(TEST_DATA_PATH + "PUT_guids_empty_list.json", 'r') as expected_data_file:
            expected_data_json = json.load(expected_data_file)
        get_rsp = execute_get(f"/guids")
        assert get_rsp.status_code == expected_data_json["status_code"]
        assert get_rsp.json() == expected_data_json["body"]
        logger.info("Test passed successfully")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
        raise


def test_post_several_items(logger):
    """
    Test POST request by adding several guids(one at a time) to guids list.
    Then verifying guids list using GET request
    """
    try:
        for _ in range(5):
            execute_post(f"/{NEW_GUID}/add")

        get_rsp = execute_get(f"/guids")
        assert get_rsp.status_code == 200
        assert get_rsp.json()['guids'] == [NEW_GUID] * 5
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
