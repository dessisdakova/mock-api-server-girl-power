import pytest


from tests_lib.common.custom_logger import CustomLogger
from tests_lib.helpers.api.request_executors.request_executor import RequestExecutor
from tests_lib.helpers.api.request_executors.request_executor_http import RequestExecutorHttp
from tests_lib.helpers.api.request_executors.request_executor_https import RequestExecutorHttps


@pytest.fixture
def request_executor(config_fixture: dict, logger_fixture: CustomLogger) -> RequestExecutor:
    if config_fixture["protocol"] == "https":
        return RequestExecutorHttps(logger_fixture, config_fixture)
    elif config_fixture["protocol"] == "http":
        return RequestExecutorHttp(logger_fixture, config_fixture)
    else:
        logger_fixture.error(f"Unsupported protocol {config_fixture["protocol"]}")
