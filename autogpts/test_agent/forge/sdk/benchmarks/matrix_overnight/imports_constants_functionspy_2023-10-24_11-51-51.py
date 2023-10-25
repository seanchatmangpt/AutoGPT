# Imports
import sys
import os
import time
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Union

# Constants
REPORTS_DIR = "reports"
PYTHON_FILE_EXT = ".py"
TESTS_DIR = "tests"
CODE_COMPLETION_MSG = "Code generation completed successfully."


# Functions
def generate_python_code(
    input: Dict[str, Union[str, List[str]]],
    params: Dict[str, Union[str, int, List[int]]],
) -> None:
    """Generate a Python source file using the given input and parameters."""
    # Validate input
    if not input or not isinstance(input, dict):
        raise ValueError("Input must be a non-empty dictionary.")
    if not params or not isinstance(params, dict):
        raise ValueError("Parameters must be a non-empty dictionary.")

    # Create the code file
    code_file_name = f"{params['module']}{PYTHON_FILE_EXT}"
    code_file_path = Path(params["output_dir"], code_file_name)
    with open(code_file_path, "w") as code_file:
        # Add imports
        for module in input["imports"]:
            code_file.write(f"import {module}\n")
        code_file.write("\n")

        # Add constants
        for constant in input["constants"]:
            code_file.write(f"{constant}\n")
        code_file.write("\n")

        # Add functions
        for function in input["functions"]:
            code_file.write(f"{function}\n")
        code_file.write("\n")


# Feature: Automated testing and quality assurance.
# Scenario: The system should have a suite of automated tests to ensure code quality and
#           These reports should be accessible to the user through a dashboard or interface.
def run_tests(code_file_path: str) -> None:
    """Run automated tests on the generated Python code."""
    # Get the code file name
    code_file_name = Path(code_file_path).name
    # Get the code file directory
    code_file_dir = Path(code_file_path).parent
    # Create the reports directory if it doesn't exist
    reports_dir_path = Path(code_file_dir, REPORTS_DIR)
    if not reports_dir_path.exists():
        reports_dir_path.mkdir()

    # Generate the pytest report
    report_name = f"pytest_report_{code_file_name}.html"
    report_path = Path(reports_dir_path, report_name)
    subprocess.run(["pytest", "-v", "--html", str(report_path), code_file_path])

    # Generate the coverage report
    coverage_report_name = f"coverage_report_{code_file_name}.html"
    coverage_report_path = Path(reports_dir_path, coverage_report_name)
    subprocess.run(
        ["coverage", "run", "--source", code_file_path, "-m", "pytest", code_file_path]
    )
    subprocess.run(["coverage", "html", "-d", str(reports_dir_path)])

    # Display success message
    print(CODE_COMPLETION_MSG)


# Feature: Error handling.
# Scenario: If the system encounters an error during code generation, it should display a descriptive error message to
#           the user and exit.
def handle_error(error_msg: str) -> None:
    """Display an error message and exit the program."""
    print(f"ERROR: {error_msg}")
    sys.exit()


# Feature: Automated testing.
# Scenario: The system should automatically run tests on the Python code to ensure functionality and catch any bugs.
def main() -> None:
    # Given that the Code Generation Engine has received the necessary input and parameters for creating a Python source file,
    # When the Code
    # Validate input
    if len(sys.argv) < 3:
        handle_error("Missing input and/or parameters.")
    # Get input and params
    input = sys.argv[1]
    params = sys.argv[2]
    # Generate the Python code
    generate_python_code(input, params)
    # Run automated tests
    run_tests(params["output_dir"])
    # Display success message
    print(CODE_COMPLETION_MSG)


# Execute the program
if __name__ == "__main__":
    main()
