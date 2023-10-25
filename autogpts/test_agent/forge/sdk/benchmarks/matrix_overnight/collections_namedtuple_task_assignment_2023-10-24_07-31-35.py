from collections import namedtuple

# Define namedtuples for features and scenarios
Feature = namedtuple("Feature", ["name", "scenarios"])
Scenario = namedtuple("Scenario", ["name", "description"])

# Define features
task_assignment = Feature(
    name="Task assignment and tracking",
    scenarios=[
        Scenario(
            name="System allows team members to be assigned specific tasks and track their progress"
        )
    ],
)

file_management = Feature(
    name="File management",
    scenarios=[
        Scenario(
            name="System can create, edit and delete files within project directory"
        )
    ],
)

code_profiling = Feature(
    name="Code profiling",
    scenarios=[
        Scenario(
            name="System provides a code profiling tool that can identify and optimize the most time-consuming aspects of code"
        )
    ],
)

integration_version = Feature(
    name="Integration with version",
    scenarios=[
        Scenario(
            name="System generates reports on code complexity, performance bottlenecks and potential areas for optimization"
        )
    ],
)

automated_code_review = Feature(
    name="Automated code review",
    scenarios=[
        Scenario(
            name="System displays test results and provides recommendations for fixes and optimizations"
        )
    ],
)

code_formatting = Feature(
    name="Code formatting",
    scenarios=[
        Scenario(
            name="System improves code structure by removing duplicate code, simplifying complex code, and enforcing formatting standards"
        )
    ],
)

debugging_tools = Feature(
    name="Debugging tools for Python code",
    scenarios=[
        Scenario(name="System provides tools for users to debug their Python code")
    ],
)

# Define list of features
features = [
    task_assignment,
    file_management,
    code_profiling,
    integration_version,
    automated_code_review,
    code_formatting,
    debugging_tools,
]

# Print all features and scenarios
for feature in features:
    print(f"Feature: {feature.name}")
    for scenario in feature.scenarios:
        print(f"Scenario: {scenario.name}")
