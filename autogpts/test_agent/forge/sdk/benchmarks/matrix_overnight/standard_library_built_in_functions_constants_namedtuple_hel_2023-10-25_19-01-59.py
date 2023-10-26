# Standard library
from typing import Set

# Built-in functions
from collections import namedtuple

# Constants
FEATURE_NAME_KEY = 'Feature'
SCENARIO_NAME_KEY = 'Scenario'

# Namedtuple declaration
Report = namedtuple('Report', 'name metrics')

# Helper functions
def parse_features(raw_data: list) -> Set:
    """
    Parses the features from the raw data and returns a set of feature names.
    :param raw_data: List containing the raw data.
    :return: Set of feature names.
    """
    return {feature[FEATURE_NAME_KEY] for feature in raw_data}

def generate_reports(reports: list, feature: str) -> dict:
    """
    Generates a dictionary of reports for a given feature.
    :param reports: List containing the reports data.
    :param feature: Feature name to generate reports for.
    :return: Dictionary containing the reports for the given feature.
    """
    return {report.name: report.metrics for report in reports if report.name == feature}

def get_feature_names(reports: list) -> Set:
    """
    Retrieves the unique feature names from the given reports.
    :param reports: List containing the reports data.
    :return: Set of unique feature names.
    """
    return {report.name for report in reports}


if __name__ == '__main__':
    # Raw data
    raw_data = [
        {FEATURE_NAME_KEY: 'Code Quality'},
        {FEATURE_NAME_KEY: 'Performance'},
        {FEATURE_NAME_KEY: 'Integration'},
        {FEATURE_NAME_KEY: 'Code Collaboration and Version Control'},
        {FEATURE_NAME_KEY: 'Code Refactoring'},
    ]

    # Generate reports
    reports = [
        Report(name='Code Quality', metrics=['code complexity', 'code coverage', 'code quality']),
        Report(name='Performance', metrics=['CPU usage', 'memory usage', 'execution time']),
        Report(name='Integration', metrics=['code complexity', 'execution time', 'memory usage']),
        Report(name='Code Collaboration and Version Control', metrics=['detailed error messages', 'error suggestions']),
        Report(name='Code Refactoring', metrics=['detailed reports', 'error suggestions'])
    ]

    # Feature: Integration
    feature_names = get_feature_names(reports)
    integration_reports = generate_reports(reports, 'Integration')

    # Feature: Code Collaboration and Version Control
    collab_reports = generate_reports(reports, 'Code Collaboration and Version Control')

    # Feature: Code Refactoring
    refactor_reports = generate_reports(reports, 'Code Refactoring')

    # Feature: Integration with version control systems
    version_control_reports = generate_reports(reports, 'Integration with version control systems')

    # Feature: Code collaboration and version control
    collab_version_reports = generate_reports(reports, 'Code collaboration and version control')

    # Feature: Code refactoring
    refactor_reports = generate_reports(reports, 'Code refactoring')