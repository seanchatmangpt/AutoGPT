# Feature: Implement logging in Python code.
# Scenario: The system should add logging statements to the Python code to track program execution

import logging

# configure logger
logging.basicConfig(level=logging.INFO)


# example function using logging
def divide(x, y):
    logging.info(f"Dividing {x} by {y}")
    return x / y
