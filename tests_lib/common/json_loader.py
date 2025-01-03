import json
from pathlib import Path
from typing import Any
import pytest

from tests_lib.common.custom_logger import CustomLogger


def load_json(file_path: Path, logger_fixture: CustomLogger) -> Any:
    """
    Loads a JSON file from the given path.
    args: file_path (Path): Path to the JSON file.
    returns: Any: The loaded JSON data.
    ....
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        error_message = f"Test data file {file_path} is not found"
        logger_fixture.error(error_message)
        pytest.fail(error_message)
    except json.JSONDecodeError as e:
        error_message = f"Invalid JSON data in {file_path}"
        logger_fixture.error(error_message)
        pytest.fail(error_message)
        raise ValueError(f"Invalid JSON data in {file_path}: {e}")
