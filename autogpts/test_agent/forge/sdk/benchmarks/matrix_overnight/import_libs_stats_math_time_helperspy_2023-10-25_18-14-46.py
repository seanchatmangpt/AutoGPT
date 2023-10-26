# Importing necessary libraries
import statistics
import math
import time
from typing import Callable, Any, List, Dict, Tuple

# Defining helper functions
def display_results(results: List[Any]) -> None:
    """Prints the results to the user for further analysis and troubleshooting."""
    print("The results are:")
    for result in results:
        print(result)

def custom_report_generator(report_type: str, metrics: List[str]) -> Callable:
    """Returns a function that generates customizable reports based on the input metrics."""
    def generate_report(results: List[Tuple[str, List[int]]]) -> Dict[Any, Any]:
        """Generates a report based on the given results and metrics."""
        report: Dict[Any, Any] = {}
        for metric in metrics:
            metric_values = []
            for result in results:
                if metric in result[1]:
                    metric_values.append(result[1][metric])
            report[metric] = report_type(metric_values)
        return report
    return generate_report

# Defining the system class
class System:
    """Represents a system that allows for collaboration and peer review among team members."""
    def __init__(self, code: str) -> None:
        self.code = code
        self.metrics: Dict[str, Any] = {}
        self.reports: Dict[str, Callable] = {}

    def add_metric(self, metric: str, func: Callable) -> None:
        """Adds a metric to the system with the given function."""
        self.metrics[metric] = func

    def add_report(self, report_name: str, report_func: Callable) -> None:
        """Adds a report to the system with the given name and function."""
        self.reports[report_name] = report_func

    def run_metrics(self) -> None:
        """Runs the metrics on the system and stores the results."""
        for metric_name, metric_func in self.metrics.items():
            self.metrics[metric_name] = metric_func(self.code)

    def generate_reports(self) -> Dict[str, Any]:
        """Generates the reports based on the stored metrics."""
        results: List[Tuple[str, List[int]]] = list(self.metrics.items())
        reports: Dict[str, Any] = {}
        for report_name, report_func in self.reports.items():
            reports[report_name] = report_func(results)
        return reports

# Initializing the system
system = System("Feature: Collaboration and peer review. Scenario: The system should allow for collaboration between team members by enabling them to review. It should also provide suggestions for improvement to the developer.")

# Adding metrics
system.add_metric("code complexity", lambda code: len(code))
system.add_metric("number of lines of code", lambda code: code.count("\n"))
system.add_metric("execution time", lambda code: time.perf_counter())

# Adding reports
system.add_report("customizable report", custom_report_generator(statistics.mean, ["code complexity", "number of lines of code", "execution time"]))
system.add_report("performance report", custom_report_generator(statistics.median, ["execution time"]))

# Running metrics and generating reports
system.run_metrics()
reports = system.generate_reports()

# Displaying the results
display_results(reports["customizable report"].items())
display_results(reports["performance report"].items())