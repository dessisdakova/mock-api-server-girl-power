from tests.db.fixtures import *
from tests_lib.common.yaml_loaders import load_test_data


@pytest.mark.parametrize("test_data", load_test_data("db_test_data")["queries"])
def test_provided_queries(db_executor, test_data, logger):
    # arrange
    query = test_data["query"]
    expected = db_executor.convert_list_into_tuple(test_data["expected_results"])
    logger.debug(f"Executing query for: {test_data['description']}")

    # act
    actual = db_executor.execute_query(query)

    # assert
    db_executor.assert_result(expected, actual)
