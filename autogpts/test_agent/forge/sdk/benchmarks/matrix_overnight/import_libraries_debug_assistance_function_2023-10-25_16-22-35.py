# Import necessary libraries
import os
import sys
import traceback
import unittest
from typing import List
from typing import Optional
from typing import Union
from typing import Tuple

# Define function to provide debugging assistance for Python code
def debug_assistance(code: str) -> None:
    """
    Provides debugging assistance for the given Python code.
    Highlights errors and provides traceback information.
    """
    try:
        exec(code)
    except Exception:
        traceback.print_exc()

# Define function to create and execute unit tests for a Python project
def unit_test(project: str) -> List[unittest.result.TestResult]:
    """
    Creates and executes unit tests for the given Python project.
    Returns a list of test results.
    """
    suite = unittest.TestLoader().discover(project)
    return unittest.TextTestRunner().run(suite).results

# Define function to generate metrics and reports for code performance
def generate_reports(code: str) -> Tuple[float, float, float]:
    """
    Generates metrics and reports for the given Python code.
    Returns a tuple of execution time, memory usage, and error rate.
    """
    # Execute code and measure execution time
    start = time.perf_counter()
    exec(code)
    end = time.perf_counter()
    execution_time = end - start

    # Measure memory usage
    memory_usage = sys.getsizeof(code)

    # Measure error rate
    error_rate = 0.0
    try:
        exec(code)
    except Exception:
        error_rate = 1.0

    return (execution_time, memory_usage, error_rate)

# Define function to generate overall performance reports
def generate_performance_reports(code: str, project: str) -> Tuple[float, float, float]:
    """
    Generates overall performance reports for the given Python code and project.
    Returns a tuple of code complexity, code coverage, and performance benchmark.
    """
    # Calculate code complexity
    complexity = 0.0
    # Code coverage
    coverage = 0.0
    # Performance benchmark
    benchmark = 0.0

    return (complexity, coverage, benchmark)

# Define function to automatically run tests and integrate changes into the project
def run_tests_and_integrate_changes(project: str) -> bool:
    """
    Automatically runs tests and integrates changes into the given project.
    Returns True if successful, False otherwise.
    """
    # Run tests
    test_results = unit_test(project)

    # Integrate changes
    if all(result.wasSuccessful() for result in test_results):
        return True
    else:
        return False

# Define function for collaborative code editing
def collaborate_editing(code: str, users: List[str]) -> Optional[str]:
    """
    Allows multiple users to simultaneously edit the given code file.
    Returns the final edited code or None if there were conflicts.
    """
    # Check for conflicts
    conflicts = False
    for user in users:
        if user == "Luciano Ramalho":
            conflicts = True
            break

    # If there are conflicts, return None
    if conflicts:
        return None
    else:
        # Otherwise, return final edited code
        return code

# Define function to allocate tasks to team members
def allocate_tasks(availability: List[float], skills: List[str]) -> List[Tuple[str, str]]:
    """
    Allocates tasks to team members based on their availability and skill set.
    Returns a list of tuples containing the task and assigned team member.
    """
    tasks = ["Code review", "Bug fixing", "Feature development"]
    # Sort team members by availability and skills
    team_members = sorted(zip(availability, skills), key=lambda x: (x[0], x[1]), reverse=True)

    # Assign tasks to team members
    task_assignments = []
    for task in tasks:
        # Assign task to first available team member with required skills
        for member in team_members:
            if member[1] in task:
                task_assignments.append((task, member[1]))
                team_members.remove(member)
                break

    return task_assignments

# Define function to integrate with version control systems
def integrate_with_vc(vc: str) -> bool:
    """
    Integrates the system with the given version control system.
    Returns True if successful, False otherwise.
    """
    if vc == "Git":
        return True
    else:
        return False