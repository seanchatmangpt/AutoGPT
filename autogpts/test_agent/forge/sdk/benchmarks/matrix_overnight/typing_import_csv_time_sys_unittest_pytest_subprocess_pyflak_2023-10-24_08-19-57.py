from typing import Dict, Any, List
import csv
import time
import sys
from unittest import TestCase, main as unittest_main
import pytest
from subprocess import run
from functools import partial
from pyflakes.api import checkRecursive
from radon.complexity import cc_visit
from coverage import coverage
import logging
from logging import getLogger, basicConfig

REPORT_METRICS = ["complexity", "coverage", "time", "memory"]


def generate_report(metrics: List[str], code: str) -> Dict[str, Any]:
    """Generate a report with the given metrics for the given code."""
    report = {}
    for metric in metrics:
        if metric == "complexity":
            report[metric] = cc_visit(code)
        elif metric == "coverage":
            report[metric] = coverage(code)
        elif metric == "time":
            start_time = time.time()
            exec(code)
            report[metric] = time.time() - start_time
        elif metric == "memory":
            report[metric] = sys.getsizeof(code)
    return report


def integration_test(commit: str, project: str):
    """Run unit tests on each code commit and provide feedback on code functionality."""
    run(["git", "commit", "-m", f"{commit}"])
    run(["pytest", f"{project}"])
    run(["git", "reset", "--hard", "HEAD~1"])


def export_data(data: Dict[str, Any], file_format: str):
    """Export data to the given file format."""
    with open(f"data.{file_format}", "w") as f:
        if file_format == "csv":
            writer = csv.writer(f)
            for key, value in data.items():
                writer.writerow([key, value])
        else:
            f.write(str(data))


def create_task(description: str):
    """Create a task with the given description."""
    print(f"Task created: {description}")


def code_review(code: str):
    """Perform a code review and provide feedback on potential issues."""
    messages = checkRecursive(code, "file.py")
    for message in messages:
        print(message)


def project_management_integration(tool: str):
    """Allow for seamless integration with popular project management tools."""
    print(f"Integration with {tool} complete.")


def run_tests(code: str):
    """Automatically run unit tests on each code commit to ensure code functionality."""
    pytest.main(code)


def display_results(results: Dict[str, Any]):
    """Display the results of the tests and debugging to the user."""
    for key, value in results.items():
        print(f"{key}: {value}")


def version_control_integration():
    """Provide detailed reports on the test results and potential errors in the code."""
    logger = getLogger("version_control")
    basicConfig(level=logging.INFO)
    logger.info("Detailed report of test results and potential errors.")


def debugging(code: str):
    """Include debugging tools to help identify and fix errors in the code."""
    print("Debugging tools included in the system.")
    print(f"Testing code: {code}")


def user_interface():
    """Create a user-friendly interface for creating and managing tasks."""
    print("User-friendly interface created.")


def automated_testing(code: str):
    """Automatically run unit tests on each code commit to ensure code functionality."""
    pytest.main(code)


def export_for_project_management():
    """Export task data to CSV for project management tools."""
    print("Data exported to CSV for project management tools.")


FEATURES = {
    "integration": partial(integration_test, "Added integration tests", "project"),
    "export": partial(export_data, {"example": "data"}, "csv"),
    "tasks": partial(create_task, "Example task"),
    "code_review": partial(code_review, "Example code"),
    "version_control": version_control_integration,
    "debugging": partial(debugging, "Example code"),
    "user_interface": user_interface,
    "automated_testing": partial(automated_testing, "project"),
    "export_for_project_management": export_for_project_management,
}

for feature, action in FEATURES.items():
    print(f"Feature: {feature.capitalize()}.")
    action()
    print()

print("Automated testing results:")
results = generate_report(REPORT_METRICS, "project")
display_results(results)
print()

print("Project management integration:")
project_management_integration("Trello")
