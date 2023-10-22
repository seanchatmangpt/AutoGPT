import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def test_logging():
    logger.info("This is a test log message")
    
if __name__ == "__main__":
    test_logging()