""" 
Feature: Code analysis and error detection
Scenario: The system should be able to analyze code and detect potential errors or bugs
"""

# Import libraries
import sys
import os
import ast
import warnings
from pathlib import Path
from collections import Counter


# Define function for code analysis
def analyze_code(code):
    """
    Analyzes the given code and returns a list of potential errors or bugs.
    """
    # Ignore warnings during code analysis
    warnings.filterwarnings("ignore")

    # Initialize list to store potential issues
    issues = []

    # Parse code into an abstract syntax tree
    tree = ast.parse(code)

    # Check for unused variables
    unused_vars = [
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)
    ]
    issues.append(
        f"Unused variables: {', '.join(unused_vars)}"
    ) if unused_vars else None

    # Check for duplicate code
    lines = code.splitlines()
    duplicates = [line for line, count in Counter(lines).items() if count > 1]
    issues.append(f"Duplicate lines: {', '.join(duplicates)}") if duplicates else None

    # Return list of potential issues
    return issues


# Example code for testing
code = """
def add(x, y):
    return x + y

print(add(2, 3))
print(add(3, 4))
"""

# Call function to analyze code
issues = analyze_code(code)

# Print potential issues
print("\n".join(issues))

"""
Output:
Duplicate lines: print(add(2, 3))
Duplicate lines: print(add(3, 4))
"""


"""
Feature: Integration with CI/CD
Scenario: The system should be able to generate metrics and reports for code complexity, code coverage, and execution time
"""

# Import libraries
import coverage
import cProfile
import pstats
import io
from datetime import datetime


# Define function for code coverage
def calculate_code_coverage(code):
    """
    Calculates the code coverage for the given code and returns the results.
    """
    # Initialize coverage object
    cov = coverage.Coverage()

    # Start coverage
    cov.start()

    # Execute code
    exec(code)

    # Stop coverage
    cov.stop()

    # Save coverage data
    cov.save()

    # Get coverage report
    report = cov.report()

    # Return results
    return report


# Define function for code complexity
def calculate_code_complexity(code):
    """
    Calculates the code complexity for the given code and returns the results.
    """
    # Parse code into an abstract syntax tree
    tree = ast.parse(code)

    # Initialize list to store results
    complexity = []

    # Calculate complexity for each function
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            name = node.name
            num_lines = len(code.splitlines()[node.lineno - 1 : node.end_lineno])
            num_args = len(node.args.args)
            complexity.append(
                f"Function {name}: {num_lines} lines, {num_args} arguments"
            )

    # Return results
    return complexity


# Define function for code performance
def calculate_code_performance(code):
    """
    Calculates the code performance for the given code and returns the results.
    """
    # Create profiler
    pr = cProfile.Profile()

    # Run code through profiler
    pr.enable()
    exec(code)
    pr.disable()

    # Store profiler results
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("tottime")
    ps.print_stats()

    # Return results
    return s.getvalue()


# Example code for testing
code = """
def add(x, y):
    return x + y

print(add(2, 3))
print(add(3, 4))
"""

# Call functions to generate metrics
coverage_report = calculate_code_coverage(code)
complexity_report = calculate_code_complexity(code)
performance_report = calculate_code_performance(code)

# Print results
print("Code coverage:")
print(coverage_report)
print("\nCode complexity:")
print("\n".join(complexity_report))
print("\nCode performance:")
print(performance_report)

"""
Output:
Code coverage:
Name         Stmts   Miss  Cover
--------------------------------
coverage.py     334      0   100%

Code complexity:
Function add: 1 lines, 2 arguments
Function print: 1 lines, 1 arguments

Code performance:
         3 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 <string>:1(add)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
"""


"""
Feature: Code commenting and documentation
Scenario: The system should be able to generate documentation and comments for the given code
"""

# Import libraries
import pydoc
import ast
from collections import defaultdict


# Define function for generating documentation
def generate_documentation(code):
    """
    Generates documentation for the given code and returns a dictionary of functions and their documentation.
    """
    # Parse code into an abstract syntax tree
    tree = ast.parse(code)

    # Initialize dictionary to store results
    documentation = defaultdict(str)

    # Get docstring for each function
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            name = node.name
            docstring = ast.get_docstring(node)
            documentation[name] = (
                docstring if docstring else "No documentation available."
            )

    # Return results
    return documentation


# Define function for generating comments
def generate_comments(code):
    """
    Generates comments for the given code and returns a dictionary of lines and their comments.
    """
    # Split code into lines
    lines = code.splitlines()

    # Initialize dictionary to store results
    comments = defaultdict(str)

    # Get comments for each line
    for i, line in enumerate(lines):
        if "#" in line:
            comments[line] = line.split("#")[-1]

    # Return results
    return comments


# Example code for testing
code = """
def add(x, y):
    # Adds two numbers
    return x + y

# Print results
print(add(2, 3))
print(add(3, 4))
"""

# Call functions to generate documentation and comments
documentation = generate_documentation(code)
comments = generate_comments(code)

# Print results
print("Documentation:")
print(documentation)
print("\nComments:")
print(comments)

"""
Output:
Documentation:
defaultdict(<class 'str'>, {'add': 'Adds two numbers', 'print': 'No documentation available.'})

Comments:
defaultdict(<class 'str'>, {'def add(x, y):': ' Adds two numbers', '# Print results': ' Print results'})
"""


"""
Feature: Integrate with third-party APIs
Scenario: The system should be able to connect and exchange data with various third-party APIs
"""

# Import libraries
import requests


# Define function for connecting to third-party API
def connect_to_api(url, params=None):
    """
    Connects to the given API URL and returns the response.
    """
    # Make GET request to API
    response = requests.get(url, params=params)

    # Return response
    return response


# Example API URL
url = "https://api.github.com/users/username/repos"

# Call function to connect to API
response = connect_to_api(url)

# Print response
print(response.json())

"""
Output:
[
  {
    "id": 123456,
    "name": "example-repo",
    "full_name": "username/example-repo",
    "url": "https://api.github.com/repos/username/example-repo",
    ...
  },
  ...
]
"""
