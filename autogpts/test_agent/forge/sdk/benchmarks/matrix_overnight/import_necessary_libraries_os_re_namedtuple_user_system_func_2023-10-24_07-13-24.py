# Import necessary libraries
import os
import re
from collections import namedtuple
from typing import Callable

# Define named tuples for User and System
User = namedtuple("User", ["email", "password"])
System = namedtuple("System", ["metrics", "reports", "project_management_tools"])


# Define functions to analyze code performance and suggest changes
def analyze_code_execution(code: str) -> System:
    """
    Analyzes the execution of Python code to provide insights into its performance and potential.
    :param code: A string containing Python code
    :return: A System named tuple with metrics, reports, and project management tools
    """
    # Use regular expressions to extract metrics from code
    code_complexity = re.findall(r"(?<=def\s)[a-zA-Z0-9_]+", code)
    code_coverage = re.findall(r"(?<=if\s)[a-zA-Z0-9_]+", code)
    code_quality = re.findall(r"(?<=for\s)[a-zA-Z0-9_]+", code)

    # Use lambda functions to suggest code changes for optimization
    change_code_complexity = lambda x: x.replace("def", "class")
    change_code_coverage = lambda x: x.replace("if", "elif")
    change_code_quality = lambda x: x.replace("for", "while")

    # Create reports with suggested code changes
    report_complexity = f"Change 'def' to 'class' in {', '.join(code_complexity)}."
    report_coverage = f"Change 'if' to 'elif' in {', '.join(code_coverage)}."
    report_quality = f"Change 'for' to 'while' in {', '.join(code_quality)}."

    # Create a list of reports
    reports = [report_complexity, report_coverage, report_quality]

    # Specify project management tools
    project_management_tools = ["Asana", "Trello", "JIRA"]

    # Return a System named tuple with metrics, reports, and project management tools
    return System(
        metrics=(code_complexity, code_coverage, code_quality),
        reports=reports,
        project_management_tools=project_management_tools,
    )


# Define a function for user authentication
def user_authentication(user: User) -> bool:
    """
    Authenticates user with valid credentials.
    :param user: A User named tuple with email and password
    :return: True if user is authenticated, False otherwise
    """
    # Define a dictionary of valid credentials
    valid_credentials = {
        "john.doe@example.com": "password123",
        "jane.doe@example.com": "qwerty123",
    }

    # Check if user's email and password match the valid credentials
    if (
        user.email in valid_credentials
        and user.password == valid_credentials[user.email]
    ):
        return True
    else:
        return False


# Define a function for collaboration and team communication
def collaboration_and_communication(metrics: str, format: Callable) -> str:
    """
    Generates reports with information on code complexity, code coverage, and other performance metrics.
    :param metrics: A string specifying the type of metrics to include in the report
    :param format: A callable function to format the report
    :return: A string with the formatted report
    """
    # Define a dictionary of available metrics and their corresponding information
    available_metrics = {
        "code complexity": "The number of functions and classes in the code.",
        "code coverage": "The number of if statements in the code.",
        "code quality": "The number of for loops in the code.",
    }

    # Format the report based on the specified metrics
    report = f"Report for {metrics}:\n{format(available_metrics[metrics])}"

    # Return the formatted report
    return report


# Example usage
if __name__ == "__main__":
    # Define sample Python code
    python_code = """
def add(x, y):
    return x + y

if x > 0:
    result = add(x, y)

for i in range(10):
    print(i)
"""

    # Analyze the code execution and generate reports
    system = analyze_code_execution(python_code)

    # Authenticate user with valid credentials
    user = User("john.doe@example.com", "password123")
    authenticated = user_authentication(user)

    # Generate report on code complexity in markdown format
    report = collaboration_and_communication(
        "code complexity", lambda x: f"* **Metric:** {x}"
    )
    print(report)

    # Integrate with project management tools
    print(f"Integrating with {', '.join(system.project_management_tools)}...")
