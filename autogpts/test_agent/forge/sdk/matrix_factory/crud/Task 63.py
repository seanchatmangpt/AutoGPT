# Import the necessary modules
import logging
import sys

# Configure the logging system
logging.basicConfig(level=logging.ERROR, stream=sys.stderr)


# Define a function to test the error reporting system
def test_error_reporting():
    try:
        # Code that may raise an error
        raise ValueError("This is a test error")
    except:
        # Log the error
        logging.exception("An error occurred")


# Call the function to test the error reporting system
test_error_reporting()
