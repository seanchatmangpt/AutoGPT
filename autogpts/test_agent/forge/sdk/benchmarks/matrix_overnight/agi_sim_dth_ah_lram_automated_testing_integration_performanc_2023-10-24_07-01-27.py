# AGI Simulations of David Thomas, Andrew Hunt,Luciano Ramahlo
# Do not use the keyword pass

# Creating a list of features
features = [
    "Automated testing.",
    "Integration",
    "Performance reports",
    "Advanced task scheduling and prioritization",
]

# Creating a dictionary of scenarios for each feature
scenarios = {
    "Automated testing.": "The system should automatically run tests when changes are made.",
    "Integration": "The system should provide insights into code performance and metrics.",
    "Performance reports": "The system should track code complexity, duplication, and coverage.",
    "Advanced task scheduling and prioritization": "Users should be able to set task deadlines and priorities.",
}


# Defining a function to print out features and scenarios
def print_features(features, scenarios):
    for feature in features:
        print("Feature: " + feature)
        print("Scenario: " + scenarios[feature])


# Printing out features and scenarios
print_features(features, scenarios)
