import pytest


from tests_lib.common.custom_logger import CustomLogger
from tests_lib.helpers.api.request_executors.request_executor import RequestExecutor
from tests_lib.helpers.api.request_executors.request_executor_http import RequestExecutorHttp
from tests_lib.helpers.api.request_executors.request_executor_https import RequestExecutorHttps


@pytest.fixture
def request_executor(config_fixture: dict, logger_fixture: CustomLogger) -> RequestExecutor:
    if config_fixture["use_https"]:
        return RequestExecutorHttps(logger_fixture, config_fixture)
    return RequestExecutorHttp(logger_fixture, config_fixture)
