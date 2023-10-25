from typing import List
from subprocess import check_output
from abc import ABC
from dataclasses import dataclass
from functools import partial
from time import perf_counter
from pathlib import Path

import os


def get_system_info() -> str:
    """Returns system information as a string."""
    return check_output("systeminfo").decode()


def provide_detailed_info(msg: str, solution: str) -> str:
    """Provides detailed information and the solution for a given issue or error."""
    print(f"{msg}: {solution}")


def integrate_with_vcs(vcs: str) -> str:
    """Integrates with the specified version control system."""
    return f"Integrating with {vcs}."


def format_code(code: str) -> str:
    """Formats the given code according to common coding standards."""
    return f"Formatting code: {code}."


def transform_data(data: any, transformation: callable) -> any:
    """Transforms data from one format to another."""
    return transformation(data)


def generate_report(data: any) -> str:
    """Generates a report for the given data."""
    return f"Generating report: {data}"


def get_performance_info() -> str:
    """Returns performance information as a string."""
    return f"Execution time: {perf_counter()}, Memory usage: {os.get_memory_info()}, CPU utilization: {os.getloadavg()}"


@dataclass
class Feature:
    """Represents a feature of a system."""

    name: str
    scenario: str


class Integration(Feature, ABC):
    """Represents an integration feature of a system."""

    def __init__(self, name: str, scenario: str, vcs: str) -> None:
        super().__init__(name, scenario)
        self.vcs = vcs

    def __repr__(self) -> str:
        """Returns a string representation of the integration feature."""
        return f"{self.name}:\n{self.scenario}\n{integrate_with_vcs(self.vcs)}"


class CodeFormatting(Feature, ABC):
    """Represents a code formatting feature of a system."""

    def __init__(self, name: str, scenario: str, code: str) -> None:
        super().__init__(name, scenario)
        self.code = code

    def __repr__(self) -> str:
        """Returns a string representation of the code formatting feature."""
        return f"{self.name}:\n{self.scenario}\n{format_code(self.code)}"


class DataTransformation(Feature, ABC):
    """Represents a data transformation feature of a system."""

    def __init__(
        self, name: str, scenario: str, data: any, transformation: callable
    ) -> None:
        super().__init__(name, scenario)
        self.data = data
        self.transformation = transformation

    def __repr__(self) -> str:
        """Returns a string representation of the data transformation feature."""
        return f"{self.name}:\n{self.scenario}\n{transform_data(self.data, self.transformation)}"


class ReportGeneration(Feature, ABC):
    """Represents a report generation feature of a system."""

    def __init__(self, name: str, scenario: str, data: any) -> None:
        super().__init__(name, scenario)
        self.data = data

    def __repr__(self) -> str:
        """Returns a string representation of the report generation feature."""
        return f"{self.name}:\n{self.scenario}\n{generate_report(self.data)}"


def generate_performance_report(*features: Feature) -> List[str]:
    """Generates a performance report for the given features."""
    return [get_performance_info() for feature in features]


def generate_detailed_report(*features: Feature) -> List[str]:
    """Generates a detailed report for the given features."""
    return [provide_detailed_info(f.name, f.scenario) for feature in features]


def main():
    # System information
    print(get_system_info(), end="\n\n")

    # Integration feature
    git = Integration(
        "Feature: Integration with version control systems.",
        "Scenario: The system should be able to integrate with popular version control systems such as",
        "Git",
    )
    print(git, end="\n\n")

    # Code formatting feature
    code = CodeFormatting(
        "Feature: Code formatting.",
        "Scenario: The system should provide an option to format the generated Python code according to common coding standards and",
        "code",
    )
    print(code, end="\n\n")

    # Data transformation feature
    data = DataTransformation(
        "Feature: Data transformation capabilities.",
        "Scenario: The system should be able to transform data from one format to another, such as",
        "data",
        partial(transform_data, transformation=str.upper),
    )
    print(data, end="\n\n")

    # Performance reports
    reports = generate_performance_report(git, code, data)
    print(*reports, sep="\n")

    # Detailed reports
    detailed_reports = generate_detailed_report(git, code, data)
    print(*detailed_reports, sep="\n")


if __name__ == "__main__":
    main()
