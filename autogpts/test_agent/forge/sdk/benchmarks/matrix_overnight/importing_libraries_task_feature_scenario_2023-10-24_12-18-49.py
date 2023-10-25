# importing required libraries
from collections import namedtuple

# defining the Task class
Task = namedtuple("Task", "feature scenario")

# defining the Feature class
Feature = namedtuple("Feature", "name description")

# defining the Scenario class
Scenario = namedtuple("Scenario", "name description")

# creating a list of features
features = [
    Feature(
        "Collaboration",
        "This will allow users to input tasks in a more natural language format instead of having to use specific syntax or keywords.",
    ),
    Feature(
        "Reporting and analytics",
        "The system should provide detailed reports and analytics on project progress, team productivity, and task metrics.",
    ),
    Feature(
        "Integration with popular",
        "These metrics and reports should include but are not limited to code complexity, code coverage, and code quality.",
    ),
    Feature(
        "User authentication",
        "Given a user has entered their login credentials, the system should verify their identity and grant access.",
    ),
    Feature(
        "Code execution",
        "The system should be able to execute the Gherkin features and scenarios and provide feedback on performance metrics such as execution time and memory usage.",
    ),
]

# creating a list of scenarios
scenarios = [
    Scenario(
        "The system should provide detailed reports and analytics.",
        "These reports should include information on code complexity, code coverage, and performance metrics such as execution time and memory usage.",
    ),
    Scenario(
        "The system should verify user identity and grant access.",
        "Given a user has entered their login credentials.",
    ),
    Scenario(
        "The system should be able to execute the Gherkin features and scenarios and provide feedback.",
        "Performance metrics such as execution time and memory usage.",
    ),
]


# defining a function to print features and scenarios
def print_features_and_scenarios(features, scenarios):
    # printing features
    for feature in features:
        print("Feature:", feature.name)
        print(feature.description)
        # printing scenarios
        for scenario in scenarios:
            if feature.name in scenario.description:
                print("Scenario:", scenario.name)
                print(scenario.description)
        print("")


# calling the function to print features and scenarios
print_features_and_scenarios(features, scenarios)
