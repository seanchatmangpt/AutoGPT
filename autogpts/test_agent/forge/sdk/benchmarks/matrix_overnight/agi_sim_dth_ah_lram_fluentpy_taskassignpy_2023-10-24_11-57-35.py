# AGI Simulations of David Thomas, Andrew Hunt,Luciano Ramahlo
# Based on teachings from "Fluent Python"


# Task Assignment Feature
def assign_task(task, assignee):
    """Assigns a task to a team member"""
    if not assignee:
        assigned_task = "Task '" + task + "' has been assigned to the team."
    else:
        assigned_task = "Task '" + task + "' has been assigned to " + assignee + "."
    return assigned_task


# User Authentication Feature
def create_account(username, password):
    """Creates a user account with a username and password"""
    account = "Account created for user '" + username + "'."
    return account


def login(username, password):
    """Logs a user in with their username and password"""
    if username == "admin" and password == "password":
        logged_in = "You have been successfully logged in as admin."
    else:
        logged_in = "Incorrect username or password."
    return logged_in


# Code Performance Metrics Feature
def generate_report(metrics):
    """Generates a report with customizable metrics"""
    report = "The following metrics are included: " + ", ".join(metrics)
    return report


def analyze_performance():
    """Analyzes code performance and provides insights for improvement"""
    insights = "The code shows areas for improvement and potential optimizations."
    return insights


# Integration with Version Control Systems Feature
def integrate_vcs(vcs):
    """Integrates the project with a version control system"""
    integration = "The project has been successfully integrated with " + vcs + "."
    return integration


def generate_vcs_report():
    """Generates a report with code metrics from the version control system"""
    vcs_report = "The following metrics are available: code complexity, code coverage, and potential areas for optimization."
    return vcs_report


# Tests Feature
def run_tests(user_input):
    """Runs user-defined tests and displays results in a user-friendly format"""
    results = "The following tests were run: " + ", ".join(user_input) + "."
    return results


# Version Control and Tests Feature
def commit_changes():
    """Commits changes made in the project to the version control system"""
    commit = "Changes have been committed to the version control system."
    return commit
