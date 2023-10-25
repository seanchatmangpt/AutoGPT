# Import necessary libraries
from collections import namedtuple
from typing import NamedTuple

# Define custom NamedTuple types for reports and features
Report = NamedTuple(
    "Report",
    [("code_complexity", float), ("test_coverage", float), ("code_quality", float)],
)
Feature = NamedTuple("Feature", [("name", str), ("scenario", str)])

# Define list of features
features = [
    Feature(
        name="Real-time collaboration",
        scenario="Multiple users should be able to work on the same Python project simultaneously and see each",
    ),
    Feature(
        name="Code validation",
        scenario="The system should validate the generated code to ensure it meets the requirements and is free of errors",
    ),
    Feature(
        name="Code review and collaboration",
        scenario="Multiple users should be able to review and collaborate on code changes simultaneously",
    ),
    Feature(
        name="Collaborative code editing",
        scenario="Multiple users should be able to edit the same code file simultaneously, with changes",
    ),
    Feature(
        name="User authentication",
        scenario="The system should allow users to create accounts and log in with secure authentication",
    ),
]

# Define list of reports
reports = [
    Report(code_complexity=0.75, test_coverage=0.95, code_quality=0.90),
    Report(code_complexity=0.80, test_coverage=0.90, code_quality=0.85),
    Report(code_complexity=0.85, test_coverage=0.80, code_quality=0.80),
    Report(code_complexity=0.90, test_coverage=0.75, code_quality=0.75),
    Report(code_complexity=0.95, test_coverage=0.70, code_quality=0.70),
]


# Define function to print features and scenarios
def print_features(features):
    for f in features:
        print(f"Feature: {f.name}")
        print(f"Scenario: {f.scenario}\n")


# Define function to print reports
def print_reports(reports):
    for i, r in enumerate(reports):
        print(f"Report {i+1}:")
        print(f"Code complexity: {r.code_complexity}")
        print(f"Test coverage: {r.test_coverage}")
        print(f"Code quality: {r.code_quality}\n")


# Print features and scenarios
print_features(features)

# Print reports
print_reports(reports)
