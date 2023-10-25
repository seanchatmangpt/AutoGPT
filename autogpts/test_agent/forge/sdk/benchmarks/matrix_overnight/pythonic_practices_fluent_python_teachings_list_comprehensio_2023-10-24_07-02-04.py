# Pythonic practices based on Fluent Python teachings:

# Use list comprehension to extract strings from given input
tasks = [task for task in input if isinstance(task, str)]
metrics = [metric for metric in input if isinstance(metric, str)]
suggestions = [suggestion for suggestion in input if isinstance(suggestion, str)]


# Define a function to assign tasks to team members and track their progress
def assign_tasks(tasks, team_members, progress):
    """Assigns tasks to team members and tracks their progress."""
    assignments = dict(zip(team_members, tasks))
    for key, value in assignments.items():
        progress[key] = value


# Use a lambda function to report errors or failures in the code
report_errors = lambda code: print("Error in code:", code)

# Use a dict comprehension to create a dict of performance indicators and their values
performance_indicators = {
    indicator: value
    for indicator, value in zip(metrics, input)
    if isinstance(value, int)
}


# Define a function to provide suggestions for code
def provide_suggestions(suggestions, code):
    """Provides suggestions for code based on given suggestions and code."""
    print("Suggestions for code:", code)
    for suggestion in suggestions:
        print(suggestion)


# Use a set to store team members
team_members = {"David Thomas", "Andrew Hunt", "Luciano Ramalho"}

# Use the built-in function `isinstance()` to check if item is a string
reports = [report for report in input if isinstance(report, str)]

# Use `str.format()` to format the given input
print(
    "Feature: Task assignment and tracking. Scenario: The system should allow managers to assign tasks to team members and track their progress.\n"
)
print("Feature: Provide suggestions for code. \n")
print(
    "Feature: Code review and collaboration. Scenario: The system should report any errors or failures in the code, and provide suggestions for fixing them.\n"
)

# Use `str.format()` and `join()` to format and print the given metrics
print("Metrics: {}".format(", ".join(metrics)))

# Use `str.format()` to format and print the given team members
print("Team members: {}".format(", ".join(team_members)))

# Use `str.format()` to format and print the given reports
print("Reports: {}".format(", ".join(reports)))
