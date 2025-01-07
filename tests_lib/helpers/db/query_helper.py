from tests_lib.helpers.db.database_helper import DatabaseHelper
from typing import List


class QueryHelper(DatabaseHelper):
    """
    Helper class for executing database queries and handling query-related operations.
    Inherits from DatabaseHelper.
    """
    @staticmethod
    def convert_list_into_tuple(lst: List):
        """
        Convert a list of lists into a list of tuples.

        :param lst: List of lists to convert.
        :return: List of tuples.
        """
        return [tuple(row) for row in lst]

    @staticmethod
    def assert_result(expected: List[tuple], actual: List[tuple]) -> None:
        """
        Assert that the expected result matches the actual result.

        :param expected: The expected result.
        :param actual: The actual result.
        :raises AssertionError: If the results do not match.
        """
        assert expected == actual, f"Result mismatch:\n Expected: {expected} \n Actual: {actual}\n"

    def execute_query(self, query: str) -> List[tuple]:
        """
        Execute a SQL query and fetch all results.

        :param query: The SQL query to execute.
        :return: List of tuples returned by the query.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
