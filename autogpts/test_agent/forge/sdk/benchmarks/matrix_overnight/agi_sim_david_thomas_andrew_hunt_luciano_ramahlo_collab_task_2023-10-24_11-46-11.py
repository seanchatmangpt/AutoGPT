# AGI Simulations of David Thomas, Andrew Hunt,Luciano Ramahlo

# Feature: Collaboration and version control
# -
# Feature: Task Management
# Scenario: The system should allow users to create, assign, and track tasks within the project
# -
# Feature: Automatic task assignment based on user skills
# Scenario: When a new task is created, the system should automatically assign it


# This function creates a report for the given input
def create_report(report_info):
    # Initialize empty list for storing report information
    report = []

    # Loop through the input list and add each item to the report
    for item in report_info:
        report.append(item)

    # Return the report as a string
    return "\n".join(report)


# This function generates detailed reports on any errors or failures encountered during the testing process
def generate_test_reports(test_results):
    # Initialize empty list for storing report information
    reports = []

    # Loop through the test results and generate a report for each item
    for result in test_results:
        # Check if the test was successful
        if result[1] == "Passed":
            # If successful, add a report stating that the test passed
            reports.append("Test {} passed".format(result[0]))
        else:
            # If unsuccessful, add a report stating the test failed and the reason for failure
            reports.append("Test {} failed: {}".format(result[0], result[2]))

    # Return the generated reports as a string
    return "\n".join(reports)


# This function generates reports on code complexity, test coverage, and runtime performance
def generate_performance_reports(code_complexity, test_coverage, runtime_performance):
    # Initialize empty list for storing report information
    reports = []

    # Add code complexity report
    reports.append("Code complexity: {}".format(code_complexity))

    # Add test coverage report
    reports.append("Test coverage: {}".format(test_coverage))

    # Add runtime performance report
    reports.append("Runtime performance: {}".format(runtime_performance))

    # Return the generated reports as a string
    return "\n".join(reports)


# This function generates reports on code execution time, memory usage, and other relevant performance metrics
def generate_resource_reports(execution_time, memory_usage, performance_metrics):
    # Initialize empty list for storing report information
    reports = []

    # Add execution time report
    reports.append("Execution time: {}".format(execution_time))

    # Add memory usage report
    reports.append("Memory usage: {}".format(memory_usage))

    # Add performance metrics report
    reports.append("Performance metrics: {}".format(performance_metrics))

    # Return the generated reports as a string
    return "\n".join(reports)


# This function generates reports on code complexity, code coverage, and potential performance issues
def generate_quality_reports(code_complexity, code_coverage, performance_issues):
    # Initialize empty list for storing report information
    reports = []

    # Add code complexity report
    reports.append("Code complexity: {}".format(code_complexity))

    # Add code coverage report
    reports.append("Code coverage: {}".format(code_coverage))

    # Add performance issues report
    reports.append("Performance issues: {}".format(performance_issues))

    # Return the generated reports as a string
    return "\n".join(reports)
