# List of lists containing feature information
features = [
    [
        "Feature: Integration with testing frameworks.",
        "Scenario",
        "The metrics should include execution time, memory usage, and any potential bottlenecks or areas for optimization.",
    ],
    [
        "Feature: Integration with version control systems",
        "",
        "These metrics should include code complexity, execution time, memory usage, and other performance indicators.",
    ],
    [
        "",
        "Feature: Debugging tools for Python code.",
        "Scenario: The system should provide tools for identifying and fixing bugs in Python code.",
    ],
    [
        "Scenario",
        "Given a database schema, the system should generate Python code to interact with the database.",
    ],
    [
        "Feature: Automatic code formatting.",
        "Scenario",
        "The system should automatically format the generated Python code according to PEP8 coding standards.",
    ],
    [
        "",
        "",
        "It should also provide the option to automatically refactor code upon saving or committing changes.",
    ],
    [
        "Feature: Code completion and suggestion.",
        "Scenario",
        "While writing code, the system should automatically detect and suggest changes to improve the code.",
    ],
    [
        "Feature: Real-time collaboration on code editing.",
        "Scenario",
        "Multiple users should be able to simultaneously edit code and see each other's changes.",
    ],
    [
        "Feature: User authentication.",
        "Scenario",
        "As a user, I want to be able to log into the system using my credentials.",
    ],
]


# Function to print features with formatted information
def print_features(features):
    for feature in features:
        # Check if feature has a title
        if feature[0]:
            print(feature[0])
        # Check if feature has a scenario
        if feature[1]:
            print(feature[1])
        # Check if feature has description
        if feature[2]:
            print(feature[2])
        # Add new line for formatting
        print()


# Print features
print_features(features)
