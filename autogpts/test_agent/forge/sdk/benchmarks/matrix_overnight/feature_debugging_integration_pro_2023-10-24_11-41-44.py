# Feature: Debugging
# Scenario: The system should provide debugging capabilities for Python code, allowing developers to step through their code and

import pdb


# Example debugging code
def print_hello():
    pdb.set_trace()
    print("Hello World!")


print_hello()

# Feature: Integration with project management tools
# Scenario: The system should allow for seamless integration with popular project management tools such as

import requests


# Example integration code
def get_project_tasks(project_id):
    response = requests.get(
        f"https://projectmanagement.com/projects/{project_id}/tasks"
    )
    return response.json()


# Feature: Task management
# Scenario: The system should allow users to create, assign, and track tasks for a project.


# Example task management code
def create_task(name, assignee):
    return {"name": name, "assignee": assignee, "status": "In Progress"}


def assign_task(task, assignee):
    task["assignee"] = assignee
    return task


def complete_task(task):
    task["status"] = "Completed"
    return task


# Feature: Code review and collaboration
# Scenario: The system should provide tools for code review and collaboration among team members.


# Example code review and collaboration code
def review_code(code):
    # Code review process
    return {"code": code, "comments": [], "approved": False}


def add_comment(code_review, comment):
    code_review["comments"].append(comment)
    return code_review


def approve_code(code_review):
    code_review["approved"] = True
    return code_review


# Feature: Performance monitoring
# Scenario: The system should provide detailed reports of any performance issues encountered during the testing process.

import time


# Example performance monitoring code
def calculate_factorial(n):
    start_time = time.time()
    result = 1
    for i in range(1, n + 1):
        result *= i
    execution_time = time.time() - start_time
    return {"n": n, "result": result, "execution_time": execution_time}
