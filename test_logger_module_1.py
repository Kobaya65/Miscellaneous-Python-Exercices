"""Test module #1 for test_logger()"""
from logging import getLogger

logger = getLogger("TestLoggerIn_test_core")

def fonction_1() -> None:
    """Function 1."""
    print("=> Function 1")
    logger.info("Function 1() called")
