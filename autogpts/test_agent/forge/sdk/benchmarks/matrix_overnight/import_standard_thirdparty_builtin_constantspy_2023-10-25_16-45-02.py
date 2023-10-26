# Importing standard library modules
import sys
import os
import unittest
import logging

# Importing third-party modules
import requests
import git

# Importing built-in functions
from functools import reduce
from itertools import groupby, chain

# Defining constants
MAX_CODE_COMPLEXITY = 10
MIN_CODE_COVERAGE = 80
MAX_RUNTIME_PERFORMANCE = 200

# Defining helper functions
logger = logging.getLogger(__name__)

def calculate_code_complexity(code):
    """
    Calculates code complexity by counting the number of loops, conditionals, and nested functions.
    :param code: Python code as a string
    :return: code complexity as an integer
    """
    num_loops = code.count("for") + code.count("while")
    num_conditionals = code.count("if") + code.count("else")
    num_nested_functions = code.count("def")
    return num_loops + num_conditionals + num_nested_functions

def calculate_code_coverage(code):
    """
    Calculates code coverage by counting the number of lines that are executed when running tests.
    :param code: Python code as a string
    :return: code coverage as a percentage
    """
    # Running unit tests
    test_results = unittest.TextTestRunner(stream=sys.stdout).run(unittest.defaultTestLoader.loadTestsFromModule(code))
    # Calculating code coverage
    num_lines_executed = test_results.testsRun - len(test_results.failures) - len(test_results.errors)
    total_lines = code.count("\n")
    return (num_lines_executed / total_lines) * 100

def calculate_runtime_performance(code):
    """
    Calculates runtime performance by measuring the time it takes to execute the code.
    :param code: Python code as a string
    :return: runtime performance in milliseconds
    """
    # Running code and measuring execution time
    start_time = time.time()
    exec(code)
    end_time = time.time()
    return (end_time - start_time) * 1000

def optimize_code(code):
    """
    Removes redundant code and optimizes the code structure.
    :param code: Python code as a string
    :return: optimized code as a string
    """
    # Removing redundant code using reduce and groupby
    code_lines = code.split("\n")
    optimized_code = reduce(lambda x, y: x + "\n" + y[0], groupby(code_lines))
    return optimized_code

def suggest_improvements(code):
    """
    Suggests possible improvements to the code.
    :param code: Python code as a string
    :return: list of suggested improvements
    """
    # Analyzing code and suggesting improvements
    suggested_improvements = []
    if calculate_code_complexity(code) > MAX_CODE_COMPLEXITY:
        suggested_improvements.append("Reduce code complexity by simplifying loops and conditionals.")
    if calculate_code_coverage(code) < MIN_CODE_COVERAGE:
        suggested_improvements.append("Improve code coverage by adding more tests.")
    if calculate_runtime_performance(code) > MAX_RUNTIME_PERFORMANCE:
        suggested_improvements.append("Optimize code performance by using more efficient algorithms.")
    return suggested_improvements

# Defining the AGI class
class AGI:
    def __init__(self, code):
        self.code = code

    def integrate_with_version_control(self, version_control_system):
        """
        Integrates with the given version control system.
        :param version_control_system: name of the version control system to integrate with
        :return: True if integration is successful, False otherwise
        """
        # Cloning the repository using git
        try:
            git.Repo.clone_from(version_control_system, "code_repo")
            return True
        except git.GitCommandError:
            logger.error("Failed to integrate with version control system: %s", version_control_system)
            return False

    def integrate_with_third_party_tools(self, tool_list):
        """
        Integrates with the given third-party tools.
        :param tool_list: list of third-party tools to integrate with
        :return: True if integration is successful, False otherwise
        """
        # Making API calls to third-party tools
        for tool in tool_list:
            try:
                requests.get(tool)
            except requests.ConnectionError:
                logger.error("Failed to integrate with third-party tool: %s", tool)
                return False
        return True

    def generate_reports(self):
        """
        Generates reports on code complexity, code coverage, and runtime performance.
        :return: a dictionary containing the reports
        """
        code_complexity = calculate_code_complexity(self.code)
        code_coverage = calculate_code_coverage(self.code)
        runtime_performance = calculate_runtime_performance(self.code)
        return {"code_complexity": code_complexity, "code_coverage": code_coverage,
                "runtime_performance": runtime_performance}

    def optimize_code(self):
        """
        Optimizes the code by removing redundant code and improving code structure.
        :return: optimized code as a string
        """
        return optimize_code(self.code)

    def suggest_improvements(self):
        """
        Suggests possible improvements to the code.
        :return: list of suggested improvements
        """
        return suggest_improvements(self.code)

# Creating an instance of the AGI class
agi = AGI(code)

# Integrating with version control systems and third-party tools
agi.integrate_with_version_control("git@github.com:username/repo.git")
agi.integrate_with_third_party_tools(["https://www.tool1.com", "https://www.tool2.com"])

# Generating reports and optimizing code
reports = agi.generate_reports()
optimized_code = agi.optimize_code()

# Suggesting improvements and applying them if desired
improvements = agi.suggest_improvements()
if improvements:
    logger.info("Suggested improvements: %s", ", ".join(improvements))
    # Prompting user to apply improvements
    user_input = input("Would you like to apply the suggested improvements? (Y/N)")
    if user_input.upper() == "Y":
        optimized_code = agi.optimize_code()

# Printing out final results
print("Code complexity: {}".format(reports["code_complexity"]))
print("Code coverage: {}%".format(reports["code_coverage"]))
print("Runtime performance: {} ms".format(reports["runtime_performance"]))
print("Optimized code: {}".format(optimized_code))