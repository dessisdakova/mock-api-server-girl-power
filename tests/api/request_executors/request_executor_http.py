import requests
from typing import Optional

from tests.api.request_executors.request_executor import RequestExecutor
from tests_lib.common.custom_logger import CustomLogger


class RequestExecutorHttp(RequestExecutor):
    """
    Class for executing HTTP requests without certificate verification.

    Inherits from the `RequestExecutor` abstract base class and provides
    implementations for `execute_get`, `execute_post`, and `execute_put`
    using HTTP (without certificate verification).
    """
    def __init__(self, logger: CustomLogger, config: dict):
        self.logger = logger
        self.config = config

    def execute_get(self, url: str) -> requests.Response:
        """
        Executes an HTTP GET request.
        Logs the request and sends an HTTP GET request to the specified URL.
        """
        self.logger.info("Executing HTTP GET")
        return requests.get(self.config["base_url_http"] + url)

    def execute_post(self, url: str) -> requests.Response:
        """
        Executes an HTTP POST request.
        Logs the request and sends an HTTP POST request to the specified URL.
        """
        self.logger.info("Executing HTTP POST")
        return requests.post(self.config["base_url_http"] + url)

    def execute_put(self, url: str, body: Optional[dict] = None) -> requests.Response:
        """
        Executes an HTTP PUT request.
        Logs the request and sends an HTTP PUT request to the specified URL
        and the provided JSON body (if any).
        """
        self.logger.info("Executing HTTP PUT")
        return requests.put(self.config["base_url_http"] + url, json=body)


