from datetime import datetime
import resource
import threading
import os
import subprocess
import itertools


def get_execution_time(func):
    """Decorator to get execution time of a function"""

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Execution time: {end - start}")
        return result

    return wrapper


@get_execution_time
def get_memory_usage():
    """Function to get current memory usage in MB"""
    mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    print(f"Memory usage: {mem_usage} MB")


def get_thread_utilization():
    """Function to get current thread utilization"""
    thread_util = threading.active_count()
    print(f"Thread utilization: {thread_util}")


@get_execution_time
def get_code_metrics(file):
    """Function to get lines of code, cyclomatic complexity, and code coverage"""
    lines_of_code = 0
    cyclomatic_complexity = 0
    code_coverage = 0

    with open(file, "r") as f:
        for line in f:
            lines_of_code += 1
            if line.strip().startswith("if"):
                cyclomatic_complexity += 1
            elif line.strip().startswith("for"):
                cyclomatic_complexity += 1
            elif line.strip().startswith("while"):
                cyclomatic_complexity += 1

    # Calculate code coverage as percentage of lines of code with branches
    code_coverage = cyclomatic_complexity / lines_of_code * 100

    print(f"Lines of code: {lines_of_code}")
    print(f"Cyclomatic complexity: {cyclomatic_complexity}")
    print(f"Code coverage: {code_coverage}%")


def real_time_collaboration():
    """Function to enable real-time collaboration for multiple users"""
    # Use a dictionary to store tasks and assign them to users
    tasks = {}

    # Use a dictionary to store user IDs and their assigned tasks
    users = {}

    def assign_task(user_id, task):
        """Function to assign a task to a specific user"""
        tasks[task] = user_id
        users[user_id].append(task)

    def complete_task(user_id, task):
        """Function to complete a task and remove it from the user's assigned tasks"""
        tasks.pop(task)
        users[user_id].remove(task)

    # Simulate multiple users working on the same task
    user_ids = ["User1", "User2", "User3"]
    for user_id in itertools.cycle(user_ids):
        task = input(f"User {user_id}, please enter a task: ")
        assign_task(user_id, task)
        print(f"Task {task} assigned to User {user_id}")
        # Check if all tasks are completed
        if not tasks:
            print("All tasks completed!")
            break


def integration_with_version_control():
    """Function to integrate with popular version control systems"""
    # Use subprocess module to execute Git or SVN commands
    subprocess.run(["git", "status"])
    subprocess.run(["svn", "status"])


def get_error_report():
    """Function to generate a detailed report of errors and failures encountered during testing"""
    # Use os module to search for error files
    error_files = [file for file in os.listdir() if file.endswith(".error")]

    # Print contents of each error file
    for file in error_files:
        with open(file, "r") as f:
            print(f.read())


# Example usage
get_memory_usage()
get_thread_utilization()
get_code_metrics("main.py")
real_time_collaboration()
integration_with_version_control()
get_error_report()
