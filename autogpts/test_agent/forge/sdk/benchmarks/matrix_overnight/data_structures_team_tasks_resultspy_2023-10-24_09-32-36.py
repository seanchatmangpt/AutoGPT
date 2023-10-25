# Data structures for storing team members and tasks
team_members = {
    "David Thomas": ["Code completion", "Code refactoring"],
    "Andrew Hunt": ["Team collaboration", "User authentication"],
    "Luciano Ramalho": ["Code completion", "Code refactoring"],
}


# Function for displaying results of tests and debugging
def display_results(results):
    """Displays results of tests and debugging to the user."""
    print("Results:")
    for result in results:
        print(f"- {result}")
    print()


# Function for providing a detailed report of errors or failures
def report_errors(errors):
    """Provides a detailed report of any errors or failures encountered during the testing process."""
    print("Error Report:")
    for error in errors:
        print(f"- {error}")
    print()


# Function for team collaboration and task assignment
def assign_task(assigner, assignee, task):
    """Assigns a task from a team member to another team member."""
    print(f'{assigner} assigned the task "{task}" to {assignee}.')
    print()


# Function for user authentication
def verify_credentials(username, password):
    """Verifies a user's credentials and grants access if they are correct."""
    if username == "user" and password == "password":
        print("Access granted.")
    else:
        print("Incorrect username or password.")
    print()


# Function for generating metrics and reports
def generate_reports(metrics):
    """Generates reports including code complexity, code coverage, and performance metrics."""
    print("Reports:")
    for metric in metrics:
        print(f"- {metric}")
    print()


# Data structures for storing performance metrics
performance_metrics = {
    "Execution time": "1.2 seconds",
    "Memory usage": "512 MB",
    "CPU utilization": "75%",
}

# Displaying results
display_results(["Test 1 passed", "Test 2 failed", "Debugging complete"])

# Reporting errors
report_errors(["Error: Unable to connect to database", "Error: Invalid input"])

# Assigning tasks
assign_task("David Thomas", "Andrew Hunt", "Code refactoring")

# Verifying credentials
verify_credentials("user", "password")

# Generating reports
generate_reports(
    ["Code complexity: high", "Code coverage: 80%", "Memory usage: 512 MB"]
)
