# Import the necessary modules
import logging
import sys

# Set up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Create a handler to output to the console
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.ERROR)

# Add the handler to the logger
logger.addHandler(handler)

# Define a function to test error monitoring
def test_error_monitoring():
    try:
        # Code to be tested
        result = 1 / 0
    except Exception as e:
        # Log the error
        logger.error("An error occurred: %s", e)

# Call the function to test error monitoring
test_error_monitoring()