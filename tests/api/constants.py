# TODO: move to test data
HTTP_STATUS_CODES = list(range(200, 204)) + list(range(205, 209)) + [226] + list(range(300, 304)) + \
                    list(range(305, 309)) + list(range(400, 419)) + list(range(421,427)) + [428, 429, 431, 451] + \
                    list(range(500, 509)) + [510, 511]
HTTP_STATUS_CODES_FOR_PUT = HTTP_STATUS_CODES + [123, "zero"]

TEST_DATA_PATH = "test_data/test_data_api/"