from collections import namedtuple

# Define a named tuple to store task information
Task = namedtuple("Task", ["name", "assigned_to", "completed"])

# Initialize an empty list to store tasks
tasks = []


# Function to assign a task to a specific team member
def assign_task(task_name, assigned_to):
    tasks.append(Task(task_name, assigned_to, False))


# Function to mark a task as completed
def mark_completed(task_name):
    for task in tasks:
        if task.name == task_name:
            task.completed = True


# Function to generate performance reports
def generate_performance_report(features, integration):
    print("Performance report for feature:", features)
    print("Integration with", integration)
    print(
        "Code complexity, code coverage, and other performance measures should be included."
    )
    print(
        "Reports should also include execution time, memory usage, and potential bottlenecks."
    )
    print(
        "Task assignment and tracking should be integrated with these reports to identify areas for improvement."
    )


# Assign tasks
assign_task("Task 1", "John")
assign_task("Task 2", "Jane")
assign_task("Task 3", "Bob")

# Mark tasks as completed
mark_completed("Task 2")

# Generate performance reports
generate_performance_report("Task assignment and tracking", "Performance measures")
generate_performance_report("Integration", "Performance indicators")
