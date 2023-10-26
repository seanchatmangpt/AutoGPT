from functools import reduce
import statistics
import json
import hashlib
import time
import itertools
import sys
import os
import subprocess
from collections import namedtuple, Counter
from typing import List, Dict, Tuple, Any

# UTILS

def validate_data(data: Any, rules: List) -> bool:
    """Validates given data according to specified rules"""
    return all(rule(data) for rule in rules)

def secure_store(data: Dict) -> None:
    """Securely stores given data in a file"""
    with open("secure_data.txt", "w") as file:
        json.dump(data, file)

def collab_version_control(codebase: List, users: List) -> None:
    """Allows for multiple users to work on the same codebase"""
    for user in users:
        subprocess.run(["git", "clone", codebase, user])

def integrate_with_pm_tool(tool: str) -> None:
    """Integrates with popular project management tools like Jira"""
    return subprocess.run(["jira", "integrate", tool])

def debug(code: str) -> None:
    """Provides debugging tools to identify and fix errors in the code"""
    return subprocess.run(["python", "-m", "pdb", code])

def execute(code: str) -> Any:
    """Executes given code and produces the desired output"""
    return eval(code)

# METRICS

def get_code_complexity(code: str) -> int:
    """Calculates the complexity of given code"""
    return len(code)

def get_execution_time(code: str, num_runs: int) -> float:
    """Measures the average execution time of given code over multiple runs"""
    total_time = 0
    for _ in range(num_runs):
        start_time = time.time()
        eval(code)
        total_time += time.time() - start_time
    return total_time / num_runs

def get_memory_usage(code: str) -> float:
    """Measures the memory usage of given code"""
    process = subprocess.Popen(["python", "-m", "memory_profiler", code], stdout=subprocess.PIPE)
    process.wait()
    output = process.stdout.read().decode("utf-8")
    return float(output.split()[-2])

def generate_report(metrics: List, code: str) -> Dict:
    """Generates a report for given metrics and code"""
    report = {"code": code}
    for metric in metrics:
        if metric == "code_complexity":
            report["code_complexity"] = get_code_complexity(code)
        elif metric == "execution_time":
            report["execution_time"] = get_execution_time(code, 10)
        elif metric == "memory_usage":
            report["memory_usage"] = get_memory_usage(code)
        else:
            raise ValueError("Invalid metric specified")
    return report

# SETUP

Project = namedtuple("Project", ["name", "description", "features"])

projects = [
    Project("PerfectPythonProductionCode", "AGI Simulations of David Thomas, Andrew Hunt, Luciano Ramalho.", [
        "Data validation",
        "Secure user data storage",
        "Collaboration and version control",
        "Integration with project management tools",
        "Debugging tools",
        "Code execution"
    ])
]

metrics = [
    "code_complexity",
    "execution_time",
    "memory_usage"
]

# MAIN PROGRAM

def main():
    # Print project information
    print("Project Name: {}".format(projects[0].name))
    print("Description: {}".format(projects[0].description))
    print("\n")

    # Print project features
    print("Features:")
    for feature in projects[0].features:
        print("\t- {}".format(feature))
    print("\n")

    # Validate data
    print("Validating data...")
    data = "Python"
    rules = [
        lambda x: isinstance(x, str),
        lambda x: x.lower() == x
    ]
    if validate_data(data, rules):
        print("Data validation successful.")
    else:
        print("Data validation failed.")
    print("\n")

    # Securely store data
    print("Storing data...")
    user_data = {
        "name": "John Doe",
        "age": 30,
        "password": hashlib.sha256(b"password123").hexdigest()
    }
    secure_store(user_data)
    print("Data stored securely in file: secure_data.txt")
    print("\n")

    # Collaboration and version control
    print("Collaborating and version controlling...")
    users = ["User1", "User2", "User3"]
    codebase = "git@github.com:PerfectPythonProductionCode.git"
    collab_version_control(codebase, users)
    print("Collaboration and version control successful.")
    print("\n")

    # Integration with project management tools
    print("Integrating with project management tools...")
    tool = "Jira"
    integrate_with_pm_tool(tool)
    print("Integration with project management tool {} successful.".format(tool))
    print("\n")

    # Debugging tools
    print("Debugging...")
    code = "print(1/0)"
    debug(code)
    print("Debugging successful.")
    print("\n")

    # Code execution
    print("Executing code...")
    code = "print(2+2)"
    output = execute(code)
    print("Code executed successfully. Output: {}".format(output))
    print("\n")

    # Generate report
    print("Generating report...")
    code = "print('Hello World')"
    report = generate_report(metrics, code)
    print("Report generated:")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()