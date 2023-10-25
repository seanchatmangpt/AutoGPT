import os
import sys
import logging
import dataclasses
import time
import datetime
import math
import statistics
import itertools
import functools
import operator
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)
from collections import defaultdict, deque, Counter
from contextlib import contextmanager


# Utility Functions
def get_files(path: str) -> List[str]:
    """Return a list of files in a given path."""
    return [
        file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))
    ]


def get_subdirectories(path: str) -> List[str]:
    """Return a list of subdirectories in a given path."""
    return [
        directory
        for directory in os.listdir(path)
        if os.path.isdir(os.path.join(path, directory))
    ]


def get_file_extension(file: str) -> str:
    """Return the extension of a given file."""
    return os.path.splitext(file)[1]


def get_report_name(file: str) -> str:
    """Return a formatted report name for a given file."""
    return f"{os.path.basename(file).split('.')[0]}_report.txt"


# Logging Configuration
logging.basicConfig(level=logging.INFO)


# Functions to create and write reports
def create_report_header(report_name: str) -> str:
    """Create a header for a given report name."""
    return f"********** {report_name} **********\n"


def create_report_summary(data: Dict[str, Any]) -> str:
    """Create a summary report for a given data dictionary."""
    summary = ""
    for key, value in data.items():
        summary += f"{key}: {value}\n"
    return summary + "\n"


def create_report_details(data: Dict[str, Any]) -> str:
    """Create a detailed report for a given data dictionary."""
    details = ""
    for key, value in data.items():
        details += f"{key}: {value}\n"
    return details + "\n"


def create_report(
    file: str, report_name: str, report_type: str, data: Dict[str, Any]
) -> None:
    """Create a report for a given file, report name, type, and data dictionary."""
    report = create_report_header(report_name)
    if report_type == "summary":
        report += create_report_summary(data)
    elif report_type == "details":
        report += create_report_details(data)
    else:
        logging.warning("Invalid report type. Please use 'summary' or 'details'.")
        return
    with open(file, "w") as f:
        f.write(report)


# Functions to calculate code complexity
def calculate_cyclomatic_complexity(func: Callable) -> int:
    """Calculate the cyclomatic complexity for a given function."""
    cc = 1
    bytecode = dis.Bytecode(func)
    for instruction in bytecode:
        op_name = instruction.opname
        if op_name.startswith("JUMP"):
            cc += 1
    return cc


def calculate_average_complexity(file: str) -> float:
    """Calculate the average cyclomatic complexity for a given file."""
    complexity_list = []
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                cc = calculate_cyclomatic_complexity(func)
                complexity_list.append(cc)
    return statistics.mean(complexity_list)


def calculate_total_complexity(file: str) -> int:
    """Calculate the total cyclomatic complexity for a given file."""
    total_cc = 0
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                cc = calculate_cyclomatic_complexity(func)
                total_cc += cc
    return total_cc


# Functions to calculate code coverage
def calculate_code_coverage(num_lines: int, num_lines_covered: int) -> float:
    """Calculate the code coverage given the number of lines and number of lines covered."""
    return (num_lines_covered / num_lines) * 100


def calculate_average_coverage(file: str) -> float:
    """Calculate the average code coverage for a given file."""
    coverage_list = []
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                num_lines = func.__code__.co_lnotab
                num_lines_covered = len(func.__code__.co_code)
                coverage = calculate_code_coverage(num_lines, num_lines_covered)
                coverage_list.append(coverage)
    return statistics.mean(coverage_list)


def calculate_total_coverage(file: str) -> float:
    """Calculate the total code coverage for a given file."""
    total_coverage = 0
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                num_lines = func.__code__.co_lnotab
                num_lines_covered = len(func.__code__.co_code)
                coverage = calculate_code_coverage(num_lines, num_lines_covered)
                total_coverage += coverage
    return total_coverage


# Functions to calculate performance benchmarks
def calculate_execution_time(func: Callable) -> float:
    """Calculate the execution time for a given function."""
    start = time.time()
    func()
    end = time.time()
    return end - start


def calculate_average_runtime(file: str) -> float:
    """Calculate the average execution time for a given file."""
    runtime_list = []
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                runtime = calculate_execution_time(func)
                runtime_list.append(runtime)
    return statistics.mean(runtime_list)


def calculate_total_runtime(file: str) -> float:
    """Calculate the total execution time for a given file."""
    total_runtime = 0
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                runtime = calculate_execution_time(func)
                total_runtime += runtime
    return total_runtime


def calculate_memory_usage(func: Callable) -> float:
    """Calculate the memory usage for a given function."""
    mem_start = memory_profiler.memory_usage()[0]
    func()
    mem_end = memory_profiler.memory_usage()[0]
    return mem_end - mem_start


def calculate_average_memory_usage(file: str) -> float:
    """Calculate the average memory usage for a given file."""
    memory_list = []
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                memory = calculate_memory_usage(func)
                memory_list.append(memory)
    return statistics.mean(memory_list)


def calculate_total_memory_usage(file: str) -> float:
    """Calculate the total memory usage for a given file."""
    total_memory = 0
    with open(file, "r") as f:
        for line in f:
            if "def" in line:
                func_name = line.split(" ")[1].split("(")[0]
                func = getattr(sys.modules[__name__], func_name)
                memory = calculate_memory_usage(func)
                total_memory += memory
    return total_memory


# Functions to generate reports and analyze data
def generate_report(file: str, report_type: str) -> None:
    """Generate a summary or detailed report for a given file."""
    report_name = get_report_name(file)
    if report_type == "summary":
        report_summary = {
            "Average Cyclomatic Complexity": calculate_average_complexity(file),
            "Total Cyclomatic Complexity": calculate_total_complexity(file),
            "Average Code Coverage": calculate_average_coverage(file),
            "Total Code Coverage": calculate_total_coverage(file),
            "Average Runtime": calculate_average_runtime(file),
            "Total Runtime": calculate_total_runtime(file),
            "Average Memory Usage": calculate_average_memory_usage(file),
            "Total Memory Usage": calculate_total_memory_usage(file),
        }
        create_report(file, report_name, "summary", report_summary)
    elif report_type == "details":
        report_details = {}
        with open(file, "r") as f:
            for line in f:
                if "def" in line:
                    func_name = line.split(" ")[1].split("(")[0]
                    func = getattr(sys.modules[__name__], func_name)
                    cc = calculate_cyclomatic_complexity(func)
                    num_lines = func.__code__.co_lnotab
                    num_lines_covered = len(func.__code__.co_code)
                    coverage = calculate_code_coverage(num_lines, num_lines_covered)
                    runtime = calculate_execution_time(func)
                    memory = calculate_memory_usage(func)
                    report_details[func_name] = {
                        "Cyclomatic Complexity": cc,
                        "Code Coverage": coverage,
                        "Execution Time": runtime,
                        "Memory Usage": memory,
                    }
        create_report(file, report_name, "details", report_details)
    else:
        logging.warning("Invalid report type. Please use 'summary' or 'details'.")


def generate_reports(path: str, report_type: str) -> None:
    """Generate reports for all files in a given path."""
    files = get_files(path)
    for file in files:
        if get_file_extension(file) == ".py":
            file_path = os.path.join(path, file)
            generate_report(file_path, report_type)


def analyze_report(file: str, report_type: str) -> None:
    """Analyze a given report file."""
    with open(file, "r") as f:
        for line in f:
            if "**********" in line:
                report_name = line.strip("*").strip().strip("Report")
                print(f"********** {report_name} **********")
            else:
                print(line.strip())


def analyze_reports(path: str, report_type: str) -> None:
    """Analyze all report files in a given path."""
    files = get_files(path)
    for file in files:
        if get_file_extension(file) == ".txt":
            file_path = os.path.join(path, file)
            analyze_report(file_path, report_type)


# Generate and analyze reports
if __name__ == "__main__":
    generate_reports("path/to/your/project", "summary")
    analyze_reports("path/to/your/project", "summary")
    generate_reports("path/to/your/project", "details")
    analyze_reports("path/to/your/project", "details")
