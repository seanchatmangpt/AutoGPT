# AGI Simulations of David Thomas, Andrew Hunt, Luciano Ramalho

# Import necessary modules
from functools import partial
import re
from collections import namedtuple
from typing import List

# Define a namedtuple to store the code metrics
CodeMetrics = namedtuple("CodeMetrics", ["complexity", "coverage", "performance"])


# Define a function to calculate code complexity
def calculate_complexity(code: str) -> int:
    """Calculates the complexity of the given code."""
    # Use regex to find all function definitions in the code
    functions = re.findall(r"def [a-zA-Z0-9_]+", code)
    # Return the number of functions as the code complexity
    return len(functions)


# Define a function to calculate code coverage
def calculate_coverage(code: str, tests: List[str]) -> float:
    """Calculates the code coverage based on the given tests."""
    # Use regex to find all function calls in the tests
    function_calls = [re.findall(r"[a-zA-Z0-9_]+\(", test) for test in tests]
    # Flatten the list of function calls
    function_calls = [call for sublist in function_calls for call in sublist]
    # Use regex to find all function definitions in the code
    functions = re.findall(r"def [a-zA-Z0-9_]+", code)
    # Calculate the code coverage as the percentage of functions called in tests
    coverage = (
        len(set(function_calls).intersection(set(functions))) / len(functions)
    ) * 100
    return coverage


# Define a function to calculate code performance
def calculate_performance(code: str) -> float:
    """Calculates the performance of the given code."""
    # Use regex to find all function calls in the code
    function_calls = re.findall(r"[a-zA-Z0-9_]+\(", code)
    # Return the number of function calls as the code performance
    return len(function_calls)


# Define a function to generate a report of code metrics
def generate_report(
    code: str, tests: List[str], metrics: List[str], format: str
) -> str:
    """Generates a report of code metrics based on the given format and type of metrics."""
    # Create a dictionary to map metric names to their corresponding functions
    metric_functions = {
        "complexity": calculate_complexity,
        "coverage": partial(calculate_coverage, tests=tests),
        "performance": calculate_performance,
    }
    # Calculate the desired metrics using the corresponding functions
    calculated_metrics = {metric: metric_functions[metric](code) for metric in metrics}
    # Format the report based on the given format
    if format == "text":
        report = f"Code complexity: {calculated_metrics['complexity']}\n"
        report += f"Code coverage: {calculated_metrics['coverage']:.2f}%\n"
        report += f"Code performance: {calculated_metrics['performance']}"
    elif format == "json":
        report = f'{{"complexity": {calculated_metrics["complexity"]}, '
        report += f'"coverage": {calculated_metrics["coverage"]:.2f}, '
        report += f'"performance": {calculated_metrics["performance"]}}}'
    else:
        report = "Invalid format provided."
    return report


# Define a function to automatically apply suggestions for code improvements
def apply_suggestions(code: str, suggestions: List[str]) -> str:
    """Applies the given suggestions to the given code."""
    # Loop through the suggestions and apply them one by one
    for suggestion in suggestions:
        code = code.replace(suggestion[0], suggestion[1])
    return code


# Define a function to customize the type of metrics and the format of the report
def customize_report(metrics: List[str], format: str) -> None:
    """Customizes the type of metrics and the format of the report."""
    # Change the global variables to the desired values
    global METRICS, FORMAT
    METRICS = metrics
    FORMAT = format


# Define the METRICS and FORMAT variables
METRICS = ["complexity", "coverage", "performance"]
FORMAT = "text"
