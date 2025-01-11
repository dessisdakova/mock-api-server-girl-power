from tests.api.constants import ROOT_CA_URL, INTERMEDIATE_CA_URL, FILE_ADD_URL
from tests_lib.helpers.api.request_executors.request_executor_fixture import request_executor
from tests_lib.common.custom_logger import CustomLogger


def test_get_ca_cert(logger_fixture: CustomLogger, request_executor):
    get_rsp = request_executor.execute_get(ROOT_CA_URL)
    byte_stream = get_rsp.content
    assert get_rsp.status_code == 200
    content = byte_stream.decode().strip()  # decode method is required to transform bytes to str
    assert content.startswith("-----BEGIN CERTIFICATE-----")
    assert content.endswith("-----END CERTIFICATE-----")


def test_get_intermediate_ca_cert(logger_fixture: CustomLogger, request_executor):
    get_rsp = request_executor.execute_get(INTERMEDIATE_CA_URL)
    byte_stream = get_rsp.content
    assert get_rsp.status_code == 200
    content = byte_stream.decode().strip()  # decode method is required to transform bytes to str
    assert content.startswith("-----BEGIN CERTIFICATE-----")
    assert content.endswith("-----END CERTIFICATE-----")


def test_post_image_add(logger_fixture: CustomLogger, request_executor):
    post_rsp = request_executor.execute_post(FILE_ADD_URL, files={'file': open('test_data/api/txt_data.txt', 'rb')})
    assert post_rsp.status_code == 200
    content = post_rsp.content.decode().strip()  # decode method is required to transform bytes to str
    assert "File uploaded successfully" in content


def test_post_image_add_empty_str_filename(logger_fixture: CustomLogger, request_executor):
    post_rsp = request_executor.execute_post(FILE_ADD_URL, files={'file': ('', open('test_data/api/txt_data.txt', 'rb'), 'text/x-spam')})
    assert post_rsp.status_code == 400
    content = post_rsp.content.decode().strip()  # decode method is required to transform bytes to str
    assert "No selected file" in content


def test_post_image_add_negative(logger_fixture: CustomLogger, request_executor):
    post_rsp = request_executor.execute_post(FILE_ADD_URL)  # files are not provided
    assert post_rsp.status_code == 400
    content = post_rsp.content.decode().strip()  # decode method is required to transform bytes to str
    assert "No file part in the request" == content
