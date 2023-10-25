import subprocess
import statistics
import time
import warnings


def execute_python_code(code, *args):
    """
    Executes given Python code and returns resulting output.
    Args:
        code: string with valid Python code
        *args: any number of arguments to pass to the code
    Returns:
        output: result of code execution
    Raises:
        SyntaxError: if code is not valid Python syntax
        TypeError: if code is not a string
    """
    if not isinstance(code, str):
        raise TypeError("code must be a string")

    try:
        output = subprocess.check_output(
            ["python", "-c", code], universal_newlines=True, *args
        )
    except subprocess.CalledProcessError as e:
        raise SyntaxError("code is not valid Python syntax") from e

    return output


def create_task(name, description, priority):
    """
    Creates a new task with the given name, description, and priority.
    Args:
        name: name of task
        description: description of task
        priority: priority of task
    Returns:
        task: dictionary representing the task
    """
    task = {
        "name": name,
        "description": description,
        "priority": priority,
        "status": "To Do",
    }

    return task


def assign_task(task, assignee):
    """
    Assigns a task to the given assignee.
    Args:
        task: dictionary representing the task
        assignee: name of the assigned user
    Returns:
        task: updated task with assignee information
    """
    task["assignee"] = assignee

    return task


def track_task(task, status):
    """
    Updates the status of a task.
    Args:
        task: dictionary representing the task
        status: updated status of the task
    Returns:
        task: updated task with new status
    """
    task["status"] = status

    return task


def generate_task_report(tasks):
    """
    Generates a report of task information.
    Args:
        tasks: list of dictionaries representing tasks
    Returns:
        report: string containing task information
    """
    report = ""

    for task in tasks:
        report += "Task: {}\n".format(task["name"])
        report += "Description: {}\n".format(task["description"])
        report += "Priority: {}\n".format(task["priority"])
        report += "Status: {}\n\n".format(task["status"])

    return report


def generate_code_report(code, *args):
    """
    Generates a report of code information.
    Args:
        code: string with valid Python code
        *args: any number of arguments to pass to the code
    Returns:
        report: string containing code information
    """
    report = ""

    # execute code and report any errors or warnings
    try:
        warnings.filterwarnings("error")
        start_time = time.perf_counter()
        result = execute_python_code(code, *args)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        report += "Code executed successfully in {} seconds.\n".format(elapsed_time)
        report += "Result: {}\n\n".format(result)
    except Exception as e:
        report += "Code execution failed with the following error:\n{}\n\n".format(e)

    # get code complexity, test coverage, and performance benchmarks
    try:
        subprocess.run(["radon", "cc", "-s", code])
        subprocess.run(["coverage", "run", "--branch", "-a", "-m", "pytest", "-v"])

        code_complexity = subprocess.check_output(
            ["radon", "cc", "-s", code], universal_newlines=True
        )
        test_coverage = subprocess.check_output(
            ["coverage", "report"], universal_newlines=True
        )

        report += "Code complexity:\n{}\n\n".format(code_complexity)
        report += "Test coverage:\n{}\n\n".format(test_coverage)
    except Exception as e:
        report += "Code complexity and test coverage analysis failed with the following error:\n{}\n\n".format(
            e
        )

    # get runtime performance information
    try:
        subprocess.check_call(["pytest", "--benchmark-skip"])
    except Exception as e:
        try:
            subprocess.check_call(
                ["pytest", "--benchmark-min-rounds=10", "--benchmark-disable", "-v"]
            )
        except Exception as e:
            report += "Runtime performance analysis failed with the following error:\n{}\n\n".format(
                e
            )

    try:
        benchmark_data = subprocess.check_output(
            [
                "pytest",
                "--benchmark-sort=name",
                "--benchmark-group-by=fullname",
                "--benchmark-columns=fullname,median,mean,stddev,min,max",
                "--benchmark-group-by=fullname",
                "--benchmark-histogram=fullname",
            ],
            universal_newlines=True,
        )

        report += "Runtime performance:\n{}\n\n".format(benchmark_data)
    except Exception as e:
        report += "Runtime performance analysis failed with the following error:\n{}\n\n".format(
            e
        )

    return report
