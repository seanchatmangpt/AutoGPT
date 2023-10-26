from typing import Dict
import requests
import json
from dataclasses import dataclass
from functools import reduce
from time import perf_counter
from memory_profiler import profile
from collections import namedtuple
from datetime import datetime

Feature = namedtuple("Feature", ["name", "description"])

# Utilities


def time_this(func):
    """A decorator to calculate execution time of a function"""
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Function {func.__name__} took {end - start:.4f}s to execute")
        return result
    return wrapper


def get_json(url: str) -> Dict:
    """Get JSON data from a given URL"""
    response = requests.get(url)
    return response.json()


# Features


@dataclass
class Integration:
    """Integration with project management tools"""
    name: str = "Integration"
    description: str = "The system should be able to integrate with popular project management tools such as Jira."


@dataclass
class UserAuthentication:
    """User Authentication"""
    name: str = "User Authentication"
    description: str = "The system should allow users to create accounts, login, and logout securely."


@dataclass
class Alert:
    """Alerting and reporting features"""
    name: str = "Alert"
    description: str = "These reports should include information on code complexity, maintainability, and performance."


# Code Metrics


@dataclass
class Metrics:
    """Code metrics and reports"""
    execution_time: float
    memory_usage: float
    function_calls: int


@dataclass
class CodeComplexity(Metrics):
    name: str = "Code Complexity"
    description: str = "Reports on code complexity and maintainability."


@dataclass
class PerformanceMetrics(Metrics):
    name: str = "Performance Metrics"
    description: str = "Reports on code performance."

# Functions


@time_this
@profile
def get_data(url: str) -> Dict:
    """Get data from a given URL"""
    return get_json(url)


def calculate_average(numbers: list) -> float:
    """Calculate average of a list of numbers"""
    return reduce(lambda x, y: x + y, numbers) / len(numbers)


# Main

if __name__ == "__main__":
    # Integration feature
    integration = Feature("Integration", "The system should be able to integrate with popular project management tools such as Jira.")

    # User authentication feature
    user_auth = Feature("User Authentication", "The system should allow users to create accounts, login, and logout securely.")

    # Alerting and reporting feature
    alert = Feature("Alert", "These reports should include information on code complexity, maintainability, and performance.")

    # Code complexity metrics
    code_complexity = CodeComplexity(
        name="Code Complexity",
        description="Reports on code complexity and maintainability."
    )

    # Performance metrics
    performance_metrics = PerformanceMetrics(
        name="Performance Metrics",
        description="Reports on code performance."
    )

    # Get data from a URL
    data_url = "https://jsonplaceholder.typicode.com/todos/1"
    data = get_data(data_url)
    print(f"Data retrieved: {data}")

    # Calculate average of a list of numbers
    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print(f"Average of {numbers}: {average}")