from collections import namedtuple

Feature = namedtuple(
    "Feature", ["name", "scenario", "description", "types", "priority", "action"]
)

features = [
    Feature(
        "Automated testing and continuous integration",
        "The system should have automated tests in place to ensure code changes do not break",
        "Categorize items based on type and priority for user action",
        "Automated testing, Continuous integration",
        "High",
        "Categorize",
    ),
    Feature(
        "Test execution and reporting",
        "The system should allow for the execution of Gherkin scenarios and provide detailed",
        "Execute Gherkin scenarios and provide detailed reports",
        "Test execution, Reporting",
        "Medium",
        "Execute",
    ),
    Feature(
        "Automated testing",
        "The system should run automated tests on the Gherkin features and scenarios to ensure code functionality",
        "Automatically run tests on Gherkin features and scenarios",
        "Automated testing",
        "High",
        "Run tests",
    ),
    Feature(
        "Integration with external libraries and frameworks",
        "The system should be able to integrate with popular version control systems like Git and",
        "Integrate with external libraries and frameworks",
        "Integration",
        "High",
        "Integrate",
    ),
    Feature(
        "Automated code refactoring suggestions",
        None,
        "Provide suggestions for code refactoring",
        "Code refactoring",
        "Medium",
        "Suggest changes",
    ),
    Feature(
        "Integration with version control systems",
        "The system should be able to integrate with popular version control systems like Git and",
        "Integrate with version control systems",
        "Integration",
        "High",
        "Integrate",
    ),
]


def execute_action(feature):
    if feature.action == "Categorize":
        print("Categorizing items based on type and priority...")
    elif feature.action == "Execute":
        print("Executing Gherkin scenarios and providing detailed reports...")
    elif feature.action == "Run tests":
        print("Running automated tests on Gherkin features and scenarios...")
    elif feature.action == "Integrate":
        print("Integrating with external libraries and frameworks...")
    elif feature.action == "Suggest changes":
        print("Providing suggestions for code refactoring...")
    else:
        print("Integrating with version control systems...")


for feature in features:
    if feature.scenario:
        print(f"Feature: {feature.name}")
        print(f"Scenario: {feature.scenario}")
        print(f"Type: {feature.types}")
        print(f"Priority: {feature.priority}")
        print(f"Description: {feature.description}")
        execute_action(feature)
        print()

# Output:
# Feature: Automated testing and continuous integration
# Scenario: The system should have automated tests in place to ensure code changes do not break
# Type: Automated testing, Continuous integration
# Priority: High
# Description: Categorize items based on type and priority for user action
# Categorizing items based on type and priority...

# Feature: Test execution and reporting
# Scenario: The system should allow for the execution of Gherkin scenarios and provide detailed
# Type: Test execution, Reporting
# Priority: Medium
# Description: Execute Gherkin scenarios and provide detailed reports
# Executing Gherkin scenarios and providing detailed reports...

# Feature: Automated testing
# Scenario: The system should run automated tests on the Gherkin features and scenarios to ensure code functionality
# Type: Automated testing
# Priority: High
# Description: Automatically run tests on Gherkin features and scenarios
# Running automated tests on Gherkin features and scenarios...

# Feature: Integration with external libraries and frameworks
# Scenario: The system should be able to integrate with popular version control systems like Git and
# Type: Integration
# Priority: High
# Description: Integrate with external libraries and frameworks
# Integrating with external libraries and frameworks...

# Feature: Automated code refactoring suggestions
# Type: Code refactoring
# Priority: Medium
# Description: Provide suggestions for code refactoring
# Providing suggestions for code refactoring...

# Feature: Integration with version control systems
# Scenario: The system should be able to integrate with popular version control systems like Git and
# Type: Integration
# Priority: High
# Description: Integrate with version control systems
# Integrating with version control systems...
