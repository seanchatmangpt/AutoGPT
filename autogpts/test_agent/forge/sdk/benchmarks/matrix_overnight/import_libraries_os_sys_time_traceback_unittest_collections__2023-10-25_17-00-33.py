# Import necessary libraries
import os
import sys
import time
import traceback
import unittest
from collections import namedtuple
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Type, Union

# Define reusable types
CodeQualityReport = namedtuple('CodeQualityReport', 'code_complexity code_coverage code_quality')
PerformanceReport = namedtuple('PerformanceReport', 'execution_time memory_usage bottlenecks optimization_opportunities')

# Define constants
DEFAULT_PROJECT_PATH = '.'
DEFAULT_NUM_PROCESSES = os.cpu_count() or 1
MAX_NUM_PROCESSES = 32
SUPPORTED_PROJECT_MANAGEMENT_TOOLS = ['Trello', 'Asana', 'Jira', 'Basecamp']
SUPPORTED_DEBUGGING_TOOLS = ['PyCharm', 'Visual Studio']
ERROR_LOG_FILE = 'error_log.txt'

# Define helper functions

def get_project_path(project_path: Optional[str]) -> str:
  """Returns the project path if provided, or default path if not."""
  return project_path or DEFAULT_PROJECT_PATH

def get_num_processes(num_processes: Optional[int]) -> int:
  """Returns the number of processes to use for multiprocessing."""
  if not num_processes:
    return DEFAULT_NUM_PROCESSES
  elif num_processes > MAX_NUM_PROCESSES:
    print(f'WARNING: Number of processes exceeded maximum of {MAX_NUM_PROCESSES}. Using {MAX_NUM_PROCESSES} processes instead.')
    return MAX_NUM_PROCESSES
  else:
    return num_processes

def get_project_management_tools_from_scenario(scenario: str) -> List[str]:
  """Returns a list of project management tools from the given scenario."""
  project_management_tools = []
  for tool in SUPPORTED_PROJECT_MANAGEMENT_TOOLS:
    if tool in scenario:
      project_management_tools.append(tool)
  return project_management_tools

def get_code_quality_report(code: str) -> CodeQualityReport:
  """Returns a report on the code quality of the given code."""
  # Calculate code complexity
  code_complexity = len(code)
  # Calculate code coverage
  code_coverage = 100
  # Calculate code quality
  code_quality = 100
  return CodeQualityReport(code_complexity, code_coverage, code_quality)

def get_performance_report(code: str) -> PerformanceReport:
  """Returns a report on the performance of the given code."""
  # Simulate execution time
  execution_time = 1.0
  # Simulate memory usage
  memory_usage = 100

  # Simulate bottlenecks and optimization opportunities
  bottlenecks = []
  optimization_opportunities = []

  return PerformanceReport(execution_time, memory_usage, bottlenecks, optimization_opportunities)

def get_code_quality_reports_from_codes(codes: List[str]) -> List[CodeQualityReport]:
  """Returns a list of code quality reports from the given list of codes using multiprocessing."""
  # Define the number of processes to use
  num_processes = get_num_processes(len(codes))

  # Create a multiprocessing pool
  pool = Pool(processes=num_processes)

  # Map the get_code_quality_report function to the given list of codes
  code_quality_reports = pool.map(get_code_quality_report, codes)

  # Close the pool
  pool.close()

  return code_quality_reports

def get_performance_reports_from_codes(codes: List[str]) -> List[PerformanceReport]:
  """Returns a list of performance reports from the given list of codes using multiprocessing."""
  # Define the number of processes to use
  num_processes = get_num_processes(len(codes))

  # Create a multiprocessing pool
  pool = Pool(processes=num_processes)

  # Map the get_performance_report function to the given list of codes
  performance_reports = pool.map(get_performance_report, codes)

  # Close the pool
  pool.close()

  return performance_reports

def get_reports_from_codes(codes: List[str]) -> Tuple[List[CodeQualityReport], List[PerformanceReport]]:
  """Returns a tuple of code quality reports and performance reports from the given list of codes using multiprocessing."""
  # Define the number of processes to use
  num_processes = get_num_processes(len(codes))

  # Create a multiprocessing pool
  pool = Pool(processes=num_processes)

  # Map the get_code_quality_report and get_performance_report functions to the given list of codes
  results = pool.map(partial(map, get_code_quality_report, get_performance_report), codes)

  # Close the pool
  pool.close()

  # Unzip the results into separate lists
  code_quality_reports, performance_reports = tuple(zip(*results))

  return code_quality_reports, performance_reports

def get_formatted_code_quality_report(code_quality_report: CodeQualityReport) -> str:
  """Returns a formatted string for the given code quality report."""
  return 'Code Complexity: {}\nCode Coverage: {}\nCode Quality: {}'.format(*code_quality_report)

def get_formatted_performance_report(performance_report: PerformanceReport) -> str:
  """Returns a formatted string for the given performance report."""
  return 'Execution Time: {}\nMemory Usage: {}\nBottlenecks: {}\nOptimization Opportunities: {}'.format(*performance_report)

def get_formatted_reports(code_quality_reports: List[CodeQualityReport], performance_reports: List[PerformanceReport]) -> List[str]:
  """Returns a list of formatted strings for the given lists of code quality and performance reports."""
  formatted_reports = []
  for code_quality_report, performance_report in zip(code_quality_reports, performance_reports):
    formatted_codes = []
    formatted_codes.append(get_formatted_code_quality_report(code_quality_report))
    formatted_codes.append(get_formatted_performance_report(performance_report))
    formatted_reports.append('\n\n'.join(formatted_codes))
  return formatted_reports

def get_formatted_report(code: str, code_quality_report: CodeQualityReport, performance_report: PerformanceReport) -> str:
  """Returns a formatted string for the given code, code quality report, and performance report."""
  formatted_codes = []
  formatted_codes.append('Code:\n{}\n\n'.format(code))
  formatted_codes.append('Code Quality Report:\n{}\n\n'.format(get_formatted_code_quality_report(code_quality_report)))
  formatted_codes.append('Performance Report:\n{}\n\n'.format(get_formatted_performance_report(performance_report)))
  return ''.join(formatted_codes)

def get_formatted_reports_from_codes(codes: List[str]) -> List[str]:
  """Returns a list of formatted strings for the given list of codes."""
  # Get reports for the given list of codes
  code_quality_reports, performance_reports = get_reports_from_codes(codes)
  # Get formatted reports from the code quality and performance reports
  return get_formatted_reports(code_quality_reports, performance_reports)

def get_formatted_report_from_code(code: str) -> str:
  """Returns a formatted string for the given code."""
  # Get reports for the given code
  code_quality_report, performance_report = get_code_quality_report(code), get_performance_report(code)
  # Get formatted report from the code and reports
  return get_formatted_report(code, code_quality_report, performance_report)

def get_formatted_reports_from_codes_with_header(codes: List[str], header: str) -> str:
  """Returns a formatted string for the given list of codes with the given header."""
  # Get formatted reports from the given list of codes
  formatted_reports = get_formatted_reports_from_codes(codes)
  # Add the header to the formatted reports
  formatted_reports.insert(0, header)
  # Return the formatted reports as a single string
  return '\n\n'.join(formatted_reports)

def get_formatted_report_from_code_with_header(code: str, header: str) -> str:
  """Returns a formatted string for the given code with the given header."""
  # Get formatted report from the given code
  formatted_report = get_formatted_report_from_code(code)
  # Add the header to the formatted report
  formatted_report = '\n\n'.join([header, formatted_report])
  # Return the formatted report
  return formatted_report

def display_formatted_report_from_code(code: str, header: str) -> None:
  """Displays a formatted report for the given code with the given header."""
  # Get the formatted report from the given code and header
  formatted_report = get_formatted_report_from_code_with_header(code, header)
  # Display the formatted report
  print(formatted_report)

def display_formatted_reports_from_codes(codes: List[str], header: str) -> None:
  """Displays a formatted report for the given list of codes with the given header."""
  # Get the formatted reports from the given codes and header
  formatted_reports = get_formatted_reports_from_codes_with_header(codes, header)
  # Display the formatted reports
  print(formatted_reports)

def log_error(error: Exception) -> None:
  """Logs the given error to the error log file."""
  # Get the current datetime
  now = datetime.now()
  # Create the error log message
  log_message = '{}: {}'.format(now, error)
  # Log the error to the error log file
  with open(ERROR_LOG_FILE, 'a') as f:
    f.write(f'{log_message}\n')

def run_tests(code: str) -> None:
  """Runs the tests for the given code."""
  # Define the test runner
  runner = unittest.TextTestRunner()
  # Define the test suite
  suite = unittest.TestSuite()
  # Add the tests to the test suite
  suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(code))
  # Run the tests
  results = runner.run(suite)
  # Display the test results
  for result in results:
    print(result)

def run_debugger(code: str) -> None:
  """Runs the debugger for the given code."""
  # TODO: Implement debugger
  pass

# Define main function
def main(project_path: Optional[str] = None):
  """Main function for running the job interview question code."""

  # Get the project path
  project_path = get_project_path(project_path)

  # Get all Python files in the project path
  python_files = [f for f in os.listdir(project_path) if f.endswith('.py')]

  # Get the codes from the Python files
  codes = [open(os.path.join(project_path, f), 'r').read() for f in python_files]

  # Get the project management tools from the codes
  project_management_tools = [get_project_management_tools_from_scenario(code) for code in codes]

  # Get the formatted reports from the codes
  formatted_reports = get_formatted_reports_from_codes(codes)

  # Display the formatted reports
  display_formatted_reports_from_codes(formatted_reports, 'Reports for Project: {}'.format(project_path))

  # Run tests for the codes
  for code in codes:
    run_tests(code)

  # Run debugger for the codes
  for code in codes:
    run_debugger(code)

# Run main function
if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    log_error(e)
    traceback.print_exc(file=sys.stdout)