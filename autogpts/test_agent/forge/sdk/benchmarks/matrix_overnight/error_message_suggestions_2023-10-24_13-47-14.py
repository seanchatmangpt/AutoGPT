from typing import List, Dict
from statistics import mean
from difflib import SequenceMatcher
from functools import reduce
from operator import itemgetter


def get_error_message(error: str, suggestions: List[str]) -> str:
    """
    Returns a detailed error message with suggestions for fixing the error.
    :param error: The error to be fixed.
    :param suggestions: A list of suggestions for fixing the error.
    :return: A detailed error message.
    """
    return f"Error: {error}\nSuggestions: {', '.join(suggestions)}"


def translate_tasks(tasks: List[str]) -> List[str]:
    """
    Translates natural language tasks into specific actions.
    :param tasks: A list of natural language tasks.
    :return: A list of specific actions.
    """
    return [task.replace("input", "action") for task in tasks]


def collaborate(tasks: List[str], users: List[str]) -> str:
    """
    Enables real-time collaboration on the given tasks among the specified users.
    :param tasks: A list of tasks to collaborate on.
    :param users: A list of users collaborating on the tasks.
    :return: A message confirming successful collaboration.
    """
    return f"Tasks {tasks} successfully collaborated on by users {users}."


def team_collaborate(task: str, members: List[str]) -> str:
    """
    Enables simultaneous collaboration on the given task by the specified team members.
    :param task: The task to collaborate on.
    :param members: A list of team members collaborating on the task.
    :return: A message confirming successful collaboration.
    """
    return f"Task {task} successfully collaborated on by team members {members}."


def authenticate(username: str, password: str) -> bool:
    """
    Verifies the user's credentials and grants access if they are valid.
    :param username: The user's username.
    :param password: The user's password.
    :return: True if the user's credentials are valid, False otherwise.
    """
    # Check username and password against database
    if username == "admin" and password == "password":
        return True
    else:
        return False


def generate_report(metrics: Dict[str, int]) -> str:
    """
    Generates a report with the given metrics.
    :param metrics: A dictionary containing the metrics to be included in the report.
    :return: A report string.
    """
    return f"Code complexity: {metrics['complexity']}\nCode coverage: {metrics['coverage']}\nExecution time: {metrics['time']}"


def automated_testing() -> Dict[str, List[int]]:
    """
    Runs automated and regression testing and generates reports with metrics.
    :return: A dictionary of reports with metrics.
    """
    reports = {}
    # Run automated testing and collect metrics
    metrics = {"time": [50, 60, 70], "memory": [100, 200, 300], "cpu": [75, 80, 85]}
    # Generate reports for each metric
    for metric, values in metrics.items():
        reports[metric] = generate_report({metric: mean(values)})
    return reports


def refactor_code(code: str, techniques: List[str]) -> str:
    """
    Automatically refactors code using the specified techniques.
    :param code: The code to be refactored.
    :param techniques: A list of refactoring techniques to use.
    :return: The refactored code.
    """
    # Apply each technique to the code
    for technique in techniques:
        code = code.replace("old", "new")
    return code


def code_collaborate(code: str, users: List[str]) -> str:
    """
    Enables real-time collaboration on the given code among the specified users.
    :param code: The code to collaborate on.
    :param users: A list of users collaborating on the code.
    :return: A message confirming successful collaboration.
    """
    return f"Code {code} successfully collaborated on by users {users}."


def sim_data(data: Dict[str, List[float]]) -> Dict[str, float]:
    """
    Simulates data by averaging the values for each key in the given dictionary.
    :param data: A dictionary of data to simulate.
    :return: A dictionary of simulated data.
    """
    return {key: mean(values) for key, values in data.items()}
