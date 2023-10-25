from collections import namedtuple

Task = namedtuple("Task", ["code_complexity", "code_coverage", "code_quality"])

# reports are stored in a list
reports = [
    Task(code_complexity=50, code_coverage=80, code_quality=90),
    Task(code_complexity=60, code_coverage=70, code_quality=80),
    Task(code_complexity=70, code_coverage=60, code_quality=70),
    Task(code_complexity=80, code_coverage=50, code_quality=60),
    Task(code_complexity=90, code_coverage=40, code_quality=50),
]


# function to calculate the average of a given attribute in a list of namedtuples
def calculate_average(tasks, attribute):
    return sum(getattr(task, attribute) for task in tasks) / len(tasks)


# calculate the average of each attribute in the reports
average_code_complexity = calculate_average(reports, "code_complexity")
average_code_coverage = calculate_average(reports, "code_coverage")
average_code_quality = calculate_average(reports, "code_quality")

# print the average values
print(f"Code complexity average: {average_code_complexity}")
print(f"Code coverage average: {average_code_coverage}")
print(f"Code quality average: {average_code_quality}")

# feature report
print("Feature: Code completion.")
print(
    "Scenario: The code editor should provide suggestions and auto-completion for Python syntax as the user is typing."
)
