from tests.db.fixtures import *
from tests_lib.common.yaml_loaders import load_test_data


@pytest.mark.parametrize("test_data", load_test_data("db_test_data")["queries"])
def test_provided_queries(db_connection, test_data, logger):
    # arrange
    query = test_data["query"]
    logger.debug(f"Query for execution: {query}.")
    expected = db_connection.convert_list_into_tuple(test_data["expected_results"])
    logger.debug(f"Executed query for '{test_data['description']}'.")

    # act
    actual = db_connection.execute_query(query)

    # assert
    try:
        db_connection.assert_result(expected, actual)
        logger.info("Test PASSED.")
    except AssertionError as e:
        logger.error(f"Test FAILED with error:\n {e}")
        raise
