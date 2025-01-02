import requests
from typing import Optional

from tests.api.request_executors.request_executor import RequestExecutor
from tests_lib.common.custom_logger import CustomLogger


class RequestExecutorHttp(RequestExecutor):
    def __init__(self, logger: CustomLogger, config: dict):
        self.logger = logger
        self.config = config

    def execute_get(self, url: str) -> requests.Response:
        self.logger.info("Executing HTTP GET")
        return requests.get(self.config["base_url_http"] + url)

    def execute_post(self, url: str) -> requests.Response:
        self.logger.info("Executing HTTP POST")
        return requests.post(self.config["base_url_http"] + url)

    def execute_put(self, url: str, body: Optional[dict] = None) -> requests.Response:
        self.logger.info("Executing HTTP PUT")
        return requests.put(self.config["base_url_http"] + url, json=body)


