from tests_lib.helpers.db.query_helper import QueryHelper
from tests_lib.common.custom_logger import CustomLogger
import pytest


@pytest.fixture(scope="session")
def db_connection(logger):
    """
    Fixture to provide a database connection using the QueryHelper.
    Establishes a connection at the start of the test session and closes it afterward.

    :param logger: Logger fixture for logging database connection events.
    :yield: An instance of QueryHelper with an active database connection.
    """
    db = QueryHelper()
    db.connect()
    logger.info("Connection to the database is established.")
    yield db
    db.close()
    logger.info("Connection to the database is closed.")


@pytest.fixture(scope="session")
def logger() -> CustomLogger:
    """
    Fixture to provide a logger for database tests.

    :return: A CustomLogger instance for logging test-related information.
    """
    log = CustomLogger("db_logger", "db_tests.log")
    return log


# request fixture is a special fixture providing information of the requesting test function
@pytest.fixture(scope="function", autouse=True)
def log_test_start(logger, request):
    """
    Automatically logs the start of each test function and adds a decides for better readability.

    :param logger: Logger fixture for logging test details.
    :param request: Request object providing test context information.
    """
    logger.info(f"Running test '{request.node.name}'...")
    yield
    logger.add_divider()
