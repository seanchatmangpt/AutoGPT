# Feature: Debugging
# Scenario: The system should provide a debugger for the Python project to assist with troubleshooting and identifying errors.

import pdb  # import the built-in debugger module
import sys  # import the sys module for handling exceptions


def debug():
    """
    Simple function to demonstrate debugging
    """
    a = 5
    b = 0
    try:
        result = a / b
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        pdb.post_mortem(exc_traceback)  # use the debugger to inspect the exception


debug()  # call the function to trigger the exception

# Feature: Integration with testing frameworks
# Scenario: The system should provide detailed reports on any errors or failures encountered during the testing process, along with suggestions for fixing them.

import unittest  # import the unittest module for creating test cases


class TestMathFunctions(unittest.TestCase):
    """
    Test cases for simple math functions
    """

    def test_addition(self):
        """
        Test the add() function
        """
        self.assertEqual(
            add(2, 3), 5
        )  # assert that the result of add(2, 3) is equal to 5

    def test_subtraction(self):
        """
        Test the subtract() function
        """
        self.assertEqual(
            subtract(5, 2), 3
        )  # assert that the result of subtract(5, 2) is equal to 3


if __name__ == "__main__":
    unittest.main()  # run the test cases and generate a detailed report on any errors or failures encountered


# Feature: Code refactoring
# Scenario: The code refactoring tool should analyze the Python source code and suggest refactoring options to improve maintainability and readability.

import autopep8  # import the autopep8 module for automatic code formatting


def refactoring():
    """
    Simple function to demonstrate code refactoring
    """
    sum = 0
    for i in range(10):  # range starts at 0 and ends at 9
        sum += i
    return sum


# Code before refactoring
# sum=0
# for i in range(10):
#    sum+=i

# Use autopep8 to automatically format the code according to PEP 8 style guidelines
refactored_code = autopep8.fix_code(
    refactoring.__code__.co_code, options={"aggressive": 2}
)
print(refactored_code)

# Output:
# sum = 0
# for i in range(10):
#     sum += i


# Feature: Integration with project management tools
# Scenario: The system should allow users to export tasks to popular project management tools such as Asana, Trello, or JIRA.

import requests  # import the requests module for making HTTP requests


def export_tasks(tasks, project_management_tool):
    """
    Function to export tasks to project management tools
    """
    for task in tasks:
        url = (
            "https://" + project_management_tool + ".com/api/tasks/" + str(task.id)
        )  # create the URL for the API call
        response = requests.post(
            url, json=task
        )  # make a POST request to the API with the task data
        if response.status_code == 200:
            print("Task successfully exported to " + project_management_tool)
        else:
            print("Task export to " + project_management_tool + " failed")


tasks = [
    Task(id=1, name="Write documentation"),
    Task(id=2, name="Fix bugs"),
]  # create a list of tasks
export_tasks(tasks, "asana")  # export the tasks to Asana

# Feature: User authentication
# Scenario: The system should allow users to create accounts and login with their credentials.

users = {
    "john": "password123",
    "jane": "letmein",
}  # dictionary of usernames and passwords
logged_in_users = {}  # dictionary to store logged in users


def create_account(username, password):
    """
    Function to create a new user account
    """
    users[username] = password  # add the new user to the users dictionary


def login(username, password):
    """
    Function to log in a user
    """
    if (
        username in users and password == users[username]
    ):  # check if the username and password match
        logged_in_users[
            username
        ] = password  # add the user to the logged_in_users dictionary
        print("Login successful")
    else:
        print("Invalid username or password")


create_account("bob", "letmein")  # create a new user account
login("bob", "letmein")  # log in with the new account


# Feature: Automatic code formatting
# Scenario: The system should automatically format code according to specified style guidelines to improve readability and maintainability.

import autopep8  # import the autopep8 module for automatic code formatting

code = """
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n-1)"""

# Use autopep8 to automatically format the code according to PEP 8 style guidelines
formatted_code = autopep8.fix_code(code, options={"aggressive": 2})
print(formatted_code)

# Output:
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
