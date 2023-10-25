# Improved code
from typing import List
import os
import subprocess
import requests
import json


# get_files function returns a list of files in the specified directory
def get_files(dir_path: str) -> List[str]:
    return os.listdir(dir_path)


# create_report function returns a dictionary with code complexity and code coverage metrics
def create_report(filepath: str) -> dict:
    # calculate code complexity
    complexity = subprocess.check_output(["radon", "cc", filepath])
    # calculate code coverage
    coverage = subprocess.check_output(["coverage", "run", filepath])
    return {"complexity": complexity, "coverage": coverage}


# get_performance_metrics function returns a dictionary with performance metrics such as memory and cpu usage
def get_performance_metrics() -> dict:
    # get memory usage
    mem_usage = subprocess.check_output(["psutil", "virtual_memory"])
    # get cpu usage
    cpu_usage = subprocess.check_output(["psutil", "cpu_percent"])
    return {"memory": mem_usage, "cpu": cpu_usage}


# get_task_suggestions function returns a list of suggestions for improving code
def get_task_suggestions(task: str) -> List[str]:
    # break down task into smaller subtasks
    subtasks = task.split(":")
    # identify key terms and requirements
    key_terms = task.split(" ")
    # suggest potential solutions or resources
    suggestions = [
        "Consider breaking down the task into smaller subtasks.",
        "Identify key terms and requirements for the task.",
        "Research potential solutions or resources for the task.",
    ]
    return suggestions


# Feature: Integration with external project management tools.
# Scenario: The system should allow for seamless integration with popular project management tools such
# as Trello, Asana, and JIRA.
# Improved code
def integrate_project_management_tools(tools: List[str]):
    for tool in tools:
        # make request to API for tool integration
        response = requests.post(
            "https://api.example.com/integrate", json={"tool": tool}
        )
        if response.status_code == 200:
            print(f"Successfully integrated with {tool}.")
        else:
            print(f"Failed to integrate with {tool}.")
