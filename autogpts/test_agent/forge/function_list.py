import autopep8
import os

import ast

from forge.replace import replace_and_check_in_ast
from forge.sdk.abilities.code.radon_workbench import fix_code
from forge.sdk.utils.complete import create, acreate
from forge.sdk.utils.create_prompts import create_python, create_yaml


def extract_functions_with_source(source_code):
    """
    Extracts the source code of all functions (including decorators and docstrings)
    defined in a Python source file.

    Args:
    file_path (str): The path to the Python source file.

    Returns:
    dict: A dictionary where keys are function names and values are the source code of the functions.
    """
    # Initialize an empty dictionary to store function names and their source code
    functions_with_source = {}

    try:
        # source_code = fix_code(source_code)

        # Parse the source code into an Abstract Syntax Tree (AST)
        parsed_ast = ast.parse(source_code)

        # Iterate through the AST nodes to find function definitions
        for node in ast.walk(parsed_ast):
            if isinstance(node, ast.FunctionDef):
                # Extract function name, source code, and docstring
                function_name = node.name
                source_lines = source_code.split("\n")[
                    node.lineno - 1 : node.end_lineno
                ]
                function_source = "\n".join(source_lines)

                # Store the function name and its source code in the dictionary
                functions_with_source[function_name] = function_source

    except Exception as e:
        print(f"An error occurred while extracting functions: {e}")

    return functions_with_source


# Example usage:
# file_path = "/Users/candacechatman/dev/test_agent/forge/sdk/benchmarks/matrix_overnight/user_task_data_structurespy_2023-10-24_08-21-12.py"
# functions_with_source = extract_functions_with_source(file_path)

# Print the extracted function names and their source code
# for name, source in functions_with_source.items():
#     print(source)

from itertools import cycle, islice


import anyio

prompt = '''
class User(NamedTuple):
    """Represents a user with a username and password."""

    username: str
    password: str


class Task(NamedTuple):
    """Represents a task with a name, assignee, and status."""

    name: str
    assignee: str
    status: str


# Define functions for features


def authenticate(user: User) -> bool:
    """Checks if the user is authenticated based on their username and password."""
    # Implementation not shown
    return True
    
def assign_task(task: Task, assignee: str) -> Task:
    """Assigns a task to a team member."""
    return task._replace(assignee=assignee)


def track_task(task: Task, status: str) -> Task:
    """Updates the status of a task."""
    return task._replace(status=status)


def create_task(name: str) -> Task:
    """Creates a new task with the given name."""
    return Task(name, "", "pending")
'''

# async def main():
#     func_cycle = cycle(functions_with_source.values())
#     with open(file_path, "r") as source_file:
#         source_code = source_file.read()
#
#     # while True:
#         # Use islice to get the next three function sources
#         # batch = list(islice(func_cycle, 3))
#
#     task = await acreate(prompt + "\nConvert this into a code implementation prompt for a expert "
#                                            "Python programmer job interview. Make sure to describe the all the requirements "
#                                            "and require professional implementation that uses a SQL Alchemy. Require expert imports.\n\n")
#
#     deps = await acreate(task + "\nCreate a list of external python libraries that could be used to show proficiency in a "
#                                 "wide variety of python skills.\n\n")
#
#     # prompt = f"MISSION: Decompress the SPR back into Python code and optimize it. SPR (Sparse Priming Representation) is a compressed version of the code, and your task is to not only reconstruct it but improve upon it.\nTHEORY: Utilize latent abilities to interpret the SPR and generate more efficient, Pythonic, and robust code.\nMETHODOLOGY: Translate the compressed SPR into Python code, introducing optimizations, such as error-handling, simplifications, and performance improvements.\n\nInput SPR:\n{str(batch)}",
#
#     code = await create_python(task+"use these libraries to create the python program\n"+deps+"\n\n")
#
#
#     print(code)

def fix_source_in_dir(directory_path):
    print('start')
    for filename in os.listdir(directory_path):
        print(filename)
        if filename == '__init__.py':
            continue

        if filename.endswith(".py"):  # You can specify the file extension you want to process
            file_path = os.path.join(directory_path, filename)
            #
            with open(file_path, "r") as source_file:
                source_code = source_file.read()

            source_code = fix_code(source_code)

            with open(file_path, "w") as modified_file:
                modified_file.write(source_code)

            print(f"Fixed {filename}")


if __name__ == "__main__":
    # anyio.run(main)

    # fix_source_in_dir('/Users/candacechatman/dev/test_agent/forge/interview/entities')
    interviewer_path = '/Users/candacechatman/dev/test_agent/forge/interview/entities/interviewer_bad.py'
    interviewer_update = '/Users/candacechatman/dev/test_agent/forge/interview/entities/interviewer.py'

    # Open and read the Python source file
    with open(interviewer_path, "r") as source_file:
        source_code = source_file.read()

    funcs = extract_functions_with_source(source_code)

    fixed_funcs = {}

    corrected_class = source_code

    for k, func in funcs.items():
        if k == '__init__':
            continue

        if 'icontract' in func:
            feedback = create(func + "\nProvide feedback to the candidate based on the why the "
                                                "function is incorrect. how is icontract supposed to be used?\n\n```feedback\n")

            correct = create(
                f"{func}\n\n{feedback}\n\nAdd the correct decorators to the function only and remove the icontract calls.\n\n```python\n",
                stop=['```'])

            print(correct)

            # Replace any import strings
            correct = correct.replace("import icontract", "\n")
            correct = correct.replace("icontract.", "")
            fixed_funcs[k] = correct
            corrected_class = replace_and_check_in_ast(source_code, k, correct)
        # else:
        #     feedback = create(func + "\nProvide feedback to the candidate based on the why the "
        #                              "function is incorrect. how is icontract supposed to be used?\n\n```feedback\n")
        #
        #     correct = create(
        #         f"{func}\n\nCorrect the implementation of the function with 4 icontract decorators maximum only.\n\n```python\nfrom icontract import require, ensure\n\n",
        #         stop=['```'])
        #
        #     print(correct)
        #
        #     # Replace any import strings
        #     correct = correct.replace("import icontract", "\n")
        #     correct = correct.replace("icontract.", "")
        #     fixed_funcs[k] = correct
        #
        #     corrected_class = replace_and_check_in_ast(source_code, k, correct)

    print(corrected_class)

    corrected_class = autopep8.fix_code(corrected_class, options={"aggressive": 1})

    with open(interviewer_update, "w") as modified_file:
        modified_file.write(corrected_class)

    print(f"Fixed {interviewer_update}")