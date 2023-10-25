# Feature: Error handling
# Scenario: The system should handle errors and exceptions when interacting with external APIs and provide appropriate feedback to the user


def handle_errors(api_response):
    """
    Handles errors and exceptions when interacting with external APIs.
    Input: api_response (dict)
    Output: error_message (str)
    """
    if "error" in api_response:
        error_message = api_response["error"]
    else:
        error_message = "Unknown error occurred."

    return error_message
