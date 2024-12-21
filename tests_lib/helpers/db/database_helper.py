from tests_lib.common.yaml_loaders import load_config
import psycopg2


class DatabaseHelper:
    """
    Helper class for managing database configuration and setup.
    """
    def __init__(self):
        """
        Initialize an object with database configuration parameters.
        """
        self.db_params = load_config("db_config")
        self.connection = None

    def connect(self) -> None:
        """
        Establish a connection to the database using the configuration parameters.
        """
        if not self.connection:
            self.connection = psycopg2.connect(**self.db_params)

    def close(self) -> None:
        """
        Close the database connection if it is open.
        """
        if self.connection:
            self.connection.close()
            self.connection = None
