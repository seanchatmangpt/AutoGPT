# All of your data should be stored in dictionaries, lists, or tuples
# rather than classes or objects.

# This will make your code more concise and make it easier to manipulate
# and pass around data.

# You should also use built-in functions and the standard library
# whenever possible, rather than creating your own custom functions.

# For example, instead of creating your own function to format code according to
# the PEP 8 style guide, you can use the built-in function "black.format_file()"
# from the "black" library.

# Additionally, you should use functional programming rather than classes.
# This means using pure functions that do not modify any global state or
# have any side effects.

# Here is an example of a pure function that takes in a list of numbers
# and returns the sum of all the even numbers in the list:

# Import necessary libraries
from functools import reduce

# Define the function
def sum_even_numbers(numbers):
    return reduce(lambda x, y: x + y if y % 2 == 0 else x, numbers, 0)

# Initialize list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print sum of even numbers
print(sum_even_numbers(numbers))

# Output: 30 (2 + 4 + 6 + 8 + 10 = 30)

# Define function to connect to external APIs
def connect_external_api(api_url):
    # Code to connect to the external API and retrieve data
    # Return the retrieved data
    pass

# Define function to integrate with project management tools
def integrate_project_management_tools(tool_name):
    # Code to integrate with the project management tool specified
    pass

# Define function to format code according to PEP 8 style guide
def format_code(code):
    # Code to format code using the "black" library
    pass

# Define function to generate code reports
def generate_code_reports():
    # Code to generate code complexity, code coverage, and memory usage reports
    pass

# Define function to review and collaborate on code
def code_review_and_collaborate():
    # Code to review and collaborate on code using reports and other tools
    pass

# Define function to automatically format code
def auto_format_code(code):
    # Code to automatically format code according to project's coding standards
    pass

# Define function to optimize code
def optimize_code():
    # Code to optimize code for performance, remove unused variables and functions,
    # and organize code into separate functions and modules
    pass

# Define function to generate reports for developers
def generate_developer_reports():
    # Code to generate reports for developers including code complexity, code duplication,
    # and code coverage
    pass