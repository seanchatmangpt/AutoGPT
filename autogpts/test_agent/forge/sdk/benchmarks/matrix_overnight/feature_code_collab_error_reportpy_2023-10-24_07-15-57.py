# Feature: Code collaboration and version control.
# Scenario: The system should provide detailed reports on any errors or failures encountered.

# Import necessary libraries
import sys
import traceback


# Define function to provide detailed error reports
def error_report():
    try:
        # Run code to generate errors
        x = 1 / 0
    except:
        # Get error information
        error_type, error_value, error_traceback = sys.exc_info()
        # Print error message
        print("An error occurred: " + str(error_type.__name__))
        # Get error traceback
        error_traceback = traceback.extract_tb(error_traceback)
        # Print error traceback
        for error in error_traceback:
            print("File: " + error[0] + ", line " + str(error[1]) + ", in " + error[2])
            print(error[3])
    finally:
        # Print confirmation message
        print("Error report generated.")


# Call function to generate error report
error_report()
