from pathlib import Path
from typing import Any

import yaml


def load_yaml(file_path: Path) -> Any:
    """
    An expandable method for loading a YAML file from a folder and returning its contents as a Python object.

    :param file_path: path to the YAML file - path.
    :return: contents of the YAML file, which can be a Python dictionary, list, or other supported.
    :raises FileNotFoundError: if the file does not exist.
    :raises RuntimeError: if the YAML file cannot be parsed.
    """
    found_path = Path(file_path)
    if not found_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(found_path, "r") as file:
        return yaml.safe_load(file)



def load_config(config_name: str):
    """
    Load a configuration YAML file from the 'config' folder.

    :param config_name: name of the configuration file (without the .yaml extension) - string
    :return: contents of the YAML file, which can be a Python dictionary, list, or other supported.
    :raises FileNotFoundError: if the file does not exist.
    :raises RuntimeError: if the YAML file cannot be parsed.
    """
    base_path = Path(__file__).resolve().parent.parent.parent / 'config'
    file_path = base_path / f"{config_name}.yaml"
    return load_yaml(file_path)


def load_test_data(data_name: str) -> Any:
    """
    Load a test data YAML file from the 'test_data' folder.

    :param data_name: name of the test data file (without the .yaml extension) - string.
    :return: contents of the YAML file, which can be a Python dictionary, list, or other supported.
    :raises FileNotFoundError: if the file does not exist.
    :raises RuntimeError: if the YAML file cannot be parsed
    """
    base_path = Path(__file__).resolve().parent.parent.parent / 'test_data'
    file_path = base_path / f"{data_name}.yaml"
    return load_yaml(file_path)
