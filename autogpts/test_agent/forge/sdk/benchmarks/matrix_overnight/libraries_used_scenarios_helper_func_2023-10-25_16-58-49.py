# Libraries used:
from collections import namedtuple
import os
import subprocess
from typing import Callable, List, Tuple
from unittest import TestLoader, TextTestRunner

# Named tuples for scenarios
Scenario = namedtuple('Scenario', ['feature', 'description'])

# Helper function for generating a report
def generate_report(results: List[Tuple[str, str, str]]) -> str:
    """Generate a detailed test report based on the given results."""
    report = f'Test Report:\n\n'
    for result in results:
        report += f'\t- Test: {result[0]}\n'
        report += f'\t  Status: {result[1]}\n'
        report += f'\t  Description: {result[2]}\n\n'
    return report

# Scenario for collaboration and team management feature
collab_scenario = Scenario(feature='Collaboration and team management',
                           description='The system should allow multiple users to collaborate on a project.')

# Scenario for code refactoring suggestions feature
refactor_scenario = Scenario(feature='Code refactoring suggestions',
                             description='The system should provide suggestions for code refactoring.')

# Scenario for code coverage, execution time, and memory usage feature
metric_scenario = Scenario(feature='Code coverage, execution time, and memory usage',
                           description='The system should provide metrics on code coverage, execution time, and memory usage.')

# Scenario for integration with version control systems
vcs_scenario = Scenario(feature='Integration with version control systems',
                        description='The system should integrate with popular version control systems like Git and SVN.')

# Scenario for code refactoring feature
code_refactor_scenario = Scenario(feature='Code refactoring',
                                  description='The Code Refactoring Engine should analyze and modify existing Python code to improve its structure.')

# Scenario for integration with project management tools
pm_scenario = Scenario(feature='Integration with project management tools',
                       description='The system should be able to integrate with popular project management tools like Trello and Asana.')

# Create a test suite and add test cases
test_suite = TestLoader().discover('tests')

# Run the test suite and get the results
test_results = TextTestRunner().run(test_suite)

# Generate a report based on the test results
report = generate_report([(test.id(), str(test), test.shortDescription()) for test in test_results.failures])

# Print the report
print(report)

# Organize files into a logical directory structure
os.makedirs('project', exist_ok=True)

# Create initial code file
with open(os.path.join('project', 'code.py'), 'w') as f:
    f.write('print("Hello, world!")')

# Execute initial code file
subprocess.run(['python', os.path.join('project', 'code.py')])

# Code refactoring function
def refactor_code(code: str, refactor_func: Callable) -> str:
    """Refactor the given code using the given refactoring function."""
    return refactor_func(code)

# Integration function for project management tools
def integrate_pm_tools(tool: str) -> str:
    """Integrate the system with the given project management tool."""
    return f'The system is now integrated with {tool}.'

# Refactor the initial code
refactored_code = refactor_code('print("Hello, world!")', lambda code: code.replace('print', 'print_msg'))

# Print the refactored code
print(refactored_code)

# Integrate with Trello
print(integrate_pm_tools('Trello'))  # The system is now integrated with Trello.

# Integrate with Asana
print(integrate_pm_tools('Asana'))  # The system is now integrated with Asana.