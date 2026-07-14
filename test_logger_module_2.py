"""Test module #2 for test_logger()"""
from logging import getLogger

logger = getLogger("TestLoggerIn_test_core")

def fonction_2() -> None:
    """Function 2."""
    print("=> Function 2")
    logger.info("Function 2() called")
