import logging

from collections import defaultdict
from functools import reduce
from time import perf_counter

# Helper functions
def timeit(func):
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logging.info(f"Execution time of {func.__name__}: {end - start} seconds")
        return result
    return wrapper

def log_errors(func):
    """Decorator to log any errors or failures that occur during testing."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error while executing {func.__name__}: {e}")
    return wrapper

def generate_report(data):
    """Function to generate a detailed report from performance monitoring data."""
    report = defaultdict(list)
    for d in data:
        report[d["metric"]].append(d["value"])
    for k, v in report.items():
        logging.info(f"{k}: {reduce(lambda x, y: x + y, v) / len(v)}")
    return report

def organize_files(files):
    """Function to organize files by type and format them properly."""
    for f in files:
        file_type = f.split(".")[-1]
        if file_type in ["py", "ipynb"]:
            logging.info(f"Properly formatting {f}...")
            # Code to format the file goes here
        else:
            logging.warning(f"Unknown file type: {f}. Skipping...")
    logging.info("All files organized and formatted successfully.")


@timeit
@log_errors
def code_performance_monitoring(data):
    """Function to monitor the performance of code and provide suggestions for refactoring."""
    # Code to monitor code performance goes here
    return data


@timeit
@log_errors
def code_documentation_generator(files):
    """Function to generate documentation from code files."""
    organize_files(files)
    # Code to generate documentation goes here


# Test code
data = [
    {"metric": "execution time", "value": 10},
    {"metric": "execution time", "value": 15},
    {"metric": "memory usage", "value": 500},
    {"metric": "memory usage", "value": 600},
    {"metric": "cpu utilization", "value": 70},
    {"metric": "cpu utilization", "value": 80}
]

logging.basicConfig(level=logging.INFO)
logging.info("Starting code performance monitoring...")
report = code_performance_monitoring(data)
logging.info("Code performance monitoring complete.")
generate_report(report)

files = ["file1.py", "file2.ipynb", "file3.txt"]
logging.info("Starting code documentation generation...")
code_documentation_generator(files)
logging.info("Code documentation generation complete.")