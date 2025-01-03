import requests
from typing import Optional

from tests.api.request_executors.request_executor import RequestExecutor
from tests_lib.common.custom_logger import CustomLogger


class RequestExecutorHttps(RequestExecutor):
    """
    Class for executing HTTPS requests with certificate verification.

    Inherits from the `RequestExecutor` abstract base class and provides
    implementations for `execute_get`, `execute_post`, and `execute_put`
    using HTTPS with certificate verification.
    """

    def __init__(self, logger: CustomLogger, config: dict):
        self.logger = logger
        self.config = config


    def execute_get(self, url: str) -> requests.Response:
        """
        Executes an HTTPS GET request.
        Logs the request and sends an HTTPS GET request to the specified URL
        with certificate verification.
        """
        self.logger.info("Executing HTTPS GET")
        return requests.get(self.config["base_url_https"] + url, verify=self.config["https_config"]["cert_file"])


    def execute_post(self, url: str) -> requests.Response:
        """
        Executes an HTTPS POST request.
        Logs the request and sends an HTTPS POST request to the specified URL
        with certificate verification.
        """
        self.logger.info("Executing HTTPS POST")
        return requests.post(self.config["base_url_https"] + url, verify=self.config["https_config"]["cert_file"])


    def execute_put(self, url: str, body: Optional[dict] = None) -> requests.Response:
        """
        Executes an HTTPS PUT request.
        Logs the request and sends an HTTPS PUT request to the specified URL
        with certificate verification and the provided JSON body (if any).
        """
        self.logger.info("Executing HTTPS PUT")
        return requests.put(self.config["base_url_https"] + url, json=body, verify=self.config["https_config"]["cert_file"])

