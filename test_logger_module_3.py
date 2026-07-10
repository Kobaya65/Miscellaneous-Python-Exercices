"""Test module #3 for test_logger()"""
from logging import getLogger

logger = getLogger("TestLoggerIn_test_core")

def fonction_3() -> None:
    """Function 3."""
    print("Function 3")
    logger.info("Function 3() called")
