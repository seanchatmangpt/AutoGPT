# Import the logging module
import logging

# Configure the logging module
logging.basicConfig(level=logging.ERROR)


# Define the error reporting function
def report_error(error):
    # Log the error with the logging module
    logging.error(error)


# Example usage
report_error("An error occurred")
