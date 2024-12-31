import requests
from typing import Optional


def execute_get(url: str, config: dict) -> requests.Response:
    if config["use_https"]:
        return requests.get(config["base_url_https"] + url, verify=config["https_config"]["cert_file"])
    return requests.get(config["base_url_http"] + url)


def execute_post(url: str, config: dict) -> requests.Response:
    if config["use_https"]:
        return requests.post(config["base_url_https"] + url, verify=config["https_config"]["cert_file"])
    return requests.post(config["base_url_http"] + url)


def execute_put(url: str, config: dict, body: Optional[dict] = None) -> requests.Response:
    if config["use_https"]:
        return requests.put(config["base_url_https"] + url, json=body, verify=config["https_config"]["cert_file"])
    return requests.put(config["base_url_http"] + url, json=body)

