from tests_lib.common.custom_logger import CustomLogger


l = CustomLogger("My logger", "test_from_class.log")
l.debug("hi debug test")
l.info("hi info test")
l.warning("hi warning test")
l.error("hi error test")
l.critical("hi critical test")

l.info("BEFORE")
l.add_divider()
l.info("AFTER")
