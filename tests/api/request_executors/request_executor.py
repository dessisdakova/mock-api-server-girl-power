from abc import ABC, abstractmethod
import requests
from typing import Optional


class RequestExecutor(ABC):
    @abstractmethod
    def execute_get(self, url: str) -> requests.Response:
        pass


    @abstractmethod
    def execute_post(self, url: str) -> requests.Response:
        pass


    @abstractmethod
    def execute_put(self, url: str, body: Optional[dict] = None) -> requests.Response:
        pass


