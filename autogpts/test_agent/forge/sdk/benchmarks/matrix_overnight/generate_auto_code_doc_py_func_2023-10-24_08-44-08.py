# Feature: Generate automatic code documentation
# Scenario: The system should be able to automatically generate documentation for Python code, including function

import inspect
from typing import Dict


def generate_code_documentation(code: str) -> Dict[str, str]:
    """
    Generates documentation for the given Python code.

    :param code: Python code to generate documentation for
    :return: Dictionary mapping function names to their documentation
    """
    functions = inspect.getmembers(code, inspect.isfunction)
    documentation = {}
    for func_name, func in functions:
        documentation[func_name] = inspect.getdoc(func)
    return documentation
