# AGI Simulations of David Thomas, Andrew Hunt, Luciano Ramalho
# Do not use the keyword pass

from collections import namedtuple

Feature = namedtuple("Feature", ["title", "description", "scenario", "reports"])

features = [
    Feature(
        title="Improve Code Quality",
        description="Implement coding standards and guidelines to improve the quality of the code.",
        scenario="The system should suggest improvements and allow the user to make changes directly in the code editor.",
        reports=["Lines of code", "Cyclomatic complexity", "Code coverage"],
    ),
    Feature(
        title="Error Handling and Logging",
        description="Implement error handling and logging to aid in debugging and troubleshooting.",
        scenario="The system should report errors and allow the user to fix them.",
        reports=[],
    ),
    Feature(
        title="Collaboration and Team Management",
        description="Implement features for collaboration and team management within the system.",
        scenario="The system should facilitate collaboration and project management for teams.",
        reports=[],
    ),
    Feature(
        title="Performance Monitoring",
        description="Include reports on code performance to help identify areas for improvement.",
        scenario="The system should provide performance data for each function and module in the code.",
        reports=["Execution time", "Memory usage", "CPU utilization"],
    ),
]


def generate_reports(features):
    for feature in features:
        print(f"{feature.title} Reports:")
        if feature.reports:
            print(*feature.reports, sep="\n")
        else:
            print("No reports available.")
        print()


if __name__ == "__main__":
    generate_reports(features)
