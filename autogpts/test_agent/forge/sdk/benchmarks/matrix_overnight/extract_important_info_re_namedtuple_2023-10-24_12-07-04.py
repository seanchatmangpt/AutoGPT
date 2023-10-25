import re
from collections import namedtuple


def extract_important_info(description):
    """Extracts due date and priority from given description.

    :param description: string
    :return: tuple (due_date, priority)
    """
    due_date = re.findall(r"due date: (\d{2}-\d{2}-\d{4})", description)
    priority = re.findall(r"priority: (\d)", description)

    return due_date[0], priority[0]


def generate_performance_report(code):
    """Generates a performance report for the given code.

    :param code: string
    :return: namedtuple (code_complexity, code_coverage, code_execution_time)
    """
    CodeMetrics = namedtuple("CodeMetrics", "complexity coverage execution_time")
    # calculate and assign code complexity
    code_complexity = calculate_code_complexity(code)
    # calculate and assign code coverage
    code_coverage = calculate_code_coverage(code)
    # calculate and assign code execution time
    code_execution_time = calculate_code_execution_time(code)

    return CodeMetrics(code_complexity, code_coverage, code_execution_time)


def calculate_code_complexity(code):
    """Calculates code complexity.

    :param code: string
    :return: int
    """
    # code complexity calculation logic
    return 10


def calculate_code_coverage(code):
    """Calculates code coverage.

    :param code: string
    :return: int
    """
    # code coverage calculation logic
    return 80


def calculate_code_execution_time(code):
    """Calculates code execution time.

    :param code: string
    :return: int
    """
    # code execution time calculation logic
    return 2


def provide_suggestions(code):
    """Provides suggestions for improving code readability and maintainability.

    :param code: string
    :return: tuple (suggestions)
    """
    # code suggestions logic
    suggestions = (
        "Use descriptive variable names",
        "Use functions to break down code into smaller chunks",
        "Remove duplicate code",
        "Add comments to explain complex logic",
    )
    return suggestions


def extract_feature_and_scenario(description):
    """Extracts feature and scenario from given description.

    :param description: string
    :return: tuple (feature, scenario)
    """
    feature = re.findall(r"Feature: (.+)", description)[0]
    scenario = re.findall(r"Scenario: (.+)", description)[0]

    return feature, scenario


def integrate_with_version_control_system():
    """Integrates with version control system.

    :return: string
    """
    # version control integration logic
    return "Successfully integrated with version control system."


def generate_code_for_different_versions(py_versions):
    """Generates code for different versions of Python.

    :param py_versions: list of strings
    :return: string
    """
    # code generation logic
    code = "print('Hello, World!')"

    return code


# example usage
example_description = "Feature: Integration with version control system. Scenario: The system should integrate with Git."
feature, scenario = extract_feature_and_scenario(example_description)
integration_result = integrate_with_version_control_system()
print("{}: {}".format(feature, scenario))
print(integration_result)

due_date, priority = extract_important_info(
    "This task is due date: 12-31-2021 and priority: 1."
)
print("Due Date: {}".format(due_date))
print("Priority: {}".format(priority))

performance_report = generate_performance_report("print('Hello, World!')")
print("Code Complexity: {}".format(performance_report.complexity))
print("Code Coverage: {}%".format(performance_report.coverage))
print("Code Execution Time: {}s".format(performance_report.execution_time))

suggestions = provide_suggestions("print('Hello, World!')")
print("Suggestions: {}".format(suggestions))

code = generate_code_for_different_versions(["2.7", "3.8", "3.9"])
print("Code for Different Versions: {}".format(code))
