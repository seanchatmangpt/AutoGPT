# Feature: User Login

# Scenario: Given a registered user on the website

# When the user enters their username and password

registered_user = True
username = "John"
password = "abc123"

if registered_user and username == "John" and password == "abc123":
    print("User successfully logged in.")
else:
    print("Invalid login credentials.")

# Feature: Collaboration and team management.
# Scenario: The system should allow multiple developers to collaborate on a project, assign tasks, and

# generate reports on team performance.

team_members = ["John", "Mary", "Bob"]
project_tasks = ["Design UI", "Implement backend", "Write documentation"]

# Feature: Code formatting.
# Scenario: The system should automatically format the generated Python code according to industry standards.
# Feature: Code debugging.

# Feature: Generate code for data manipulation.
# Scenario: The Code Generation Engine should create code for manipulating data, such as parsing and

# sorting.

# Example code for sorting a list of dictionaries by a specific key:

users = [
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 30},
    {"name": "Bob", "age": 20},
]

sorted_users = sorted(users, key=lambda x: x["age"])

print(
    sorted_users
)  # [{'name': 'Bob', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Mary', 'age': 30}]

# Feature: Generate reports on code performance.
# Scenario: The system should automatically generate reports on code performance, including execution time, memory usage, and function calls.

# Example code for generating a report on code performance:

import cProfile


def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


cProfile.run("calculate_sum(1000000)")  # 8 function calls in 0.061 seconds

# Feature: Integration with task management software.
# Scenario: The system should be able to integrate with popular task management software such as Trello, Asana, etc.

# Feature: Task assignment.
# Scenario: Users should be able to assign tasks to team members and set deadlines.

# Example code for creating a task assignment system:

tasks = {
    "Design UI": {"assignee": "John", "deadline": "09/30/2021"},
    "Implement backend": {"assignee": "Mary", "deadline": "10/31/2021"},
    "Write documentation": {"assignee": "Bob", "deadline": "11/30/2021"},
}

print(tasks["Design UI"]["assignee"])  # John
print(tasks["Write documentation"]["deadline"])  # 11/30/2021
