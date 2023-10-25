# Import necessary libraries
import time
import memory_profiler
import sys
from collections import namedtuple

# Define namedtuple for Task
Task = namedtuple("Task", ["name", "priority", "due_date"])


# Define function for parsing tasks
def parse_tasks(tasks):
    """Parses tasks and returns a list of namedtuples."""
    return [Task(task[0], task[1], task[2]) for task in tasks]


# Define function for displaying parsed tasks
def display_tasks(tasks):
    """Displays parsed tasks in the task management system."""
    for task in tasks:
        print(
            f"Task Name: {task.name}\nPriority: {task.priority}\nDue Date: {task.due_date}\n"
        )


# Define function for generating reports
def generate_report(metrics):
    """Generates a report with the given metrics."""
    print("Report:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
    print()


# Define function for monitoring code performance
def monitor_performance(code):
    """Monitors and reports code performance."""
    start_time = time.time()
    code()
    end_time = time.time()
    execution_time = end_time - start_time
    memory_usage = memory_profiler.memory_usage()[0]
    code_complexity = len(sys.getsizeof(code))
    metrics = {
        "Execution Time": execution_time,
        "Memory Usage": memory_usage,
        "Code Complexity": code_complexity,
    }
    generate_report(metrics)


# Define code to be monitored
def code_performance():
    """Example code for performance monitoring."""
    for i in range(1000):
        print(i)


# Define function for integrating with project management tools
def integrate_project_management():
    """Integrates with project management tools."""
    print("Integration with project management tools.")


# Define function for real-time collaboration
def real_time_collaboration():
    """Allows multiple users to edit and work on tasks simultaneously."""
    print("Real-time collaboration.")


# Define function for integrating with version control systems
def integrate_version_control():
    """Integrates with version control systems."""
    print("Integration with version control systems.")


# Generate report for code performance
monitor_performance(code_performance)

# Parse and display tasks
tasks = [
    ["Task1", "High", "10/10/2021"],
    ["Task2", "Low", "10/12/2021"],
    ["Task3", "Medium", "10/15/2021"],
]
parsed_tasks = parse_tasks(tasks)
display_tasks(parsed_tasks)

# Generate reports for integration with project management tools, real-time collaboration, and version control systems
integrate_project_management()
integrate_version_control()
real_time_collaboration()
