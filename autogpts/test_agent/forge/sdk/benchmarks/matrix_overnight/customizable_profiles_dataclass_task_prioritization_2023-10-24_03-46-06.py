# Allow for customizable user profiles
# Use dataclass to create a data structure with fields, methods, and comparison functions
from dataclasses import dataclass


@dataclass
class Profile:
    name: str
    age: int
    job: str
    hobbies: list
    friends: list


# Automatic task prioritization
# Use dictionary for key-value pairs of tasks and their urgency/importance levels
tasks = {"task1": (5, 7), "task2": (2, 9), "task3": (8, 3)}

# Use sorted() function with key parameter to sort tasks by priority
sorted_tasks = sorted(tasks.items(), key=lambda x: x[1], reverse=True)

# Performance metrics and reports
# Use timeit module to measure execution time
import timeit

# Use sys module to measure memory usage
import sys


# Use function to measure line-by-line performance
def performance():
    for i in range(1000000):
        i * 2


# Use cProfile to generate performance reports
import cProfile

# Code review and collaboration
# Use list comprehension to filter code complexity, code coverage, and cyclomatic complexity
reports = [
    report
    for report in reports
    if report in ("code complexity", "code coverage", "cyclomatic complexity")
]
