from abc import ABC, abstractmethod
import requests
from typing import Optional


class RequestExecutor(ABC):
    """
    Abstract Base Class for executing HTTP(S) requests.

    This class defines a common interface for executing GET, POST, and PUT requests
    using the `requests` library. Subclasses must implement specific behaviors for
    handling HTTP and HTTPS requests.
    """
    @abstractmethod
    def execute_get(self, url: str) -> requests.Response:
        """
        This get method as abstract, must be implemented by any subclass of the RequestExecutor(ABC)
        """
        pass


    @abstractmethod
    def execute_post(self, url: str, files: Optional[dict] = None) -> requests.Response:
        """
        This post method as abstract, must be implemented by any subclass of the RequestExecutor(ABC)
        """
        pass


    @abstractmethod
    def execute_put(self, url: str, body: Optional[dict] = None) -> requests.Response:
        """
        This put method as abstract, must be implemented by any subclass of the RequestExecutor(ABC)
        """
        pass


