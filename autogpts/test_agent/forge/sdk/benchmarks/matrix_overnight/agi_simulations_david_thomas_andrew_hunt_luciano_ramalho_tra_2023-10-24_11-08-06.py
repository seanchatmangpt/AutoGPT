# AGI Simulations of David Thomas, Andrew Hunt, and Luciano Ramalho

from typing import Callable, List


def transform_input(input: List[List[str]]) -> Callable:
    """
    Transforms the given input into Python code that aligns with Pythonic practices
    advocated by Luciano Ramalho.

    Parameters:
        input (List[List[str]]): List of lists containing strings representing code snippets.

    Returns:
        Callable: A function that takes in a list of arguments and executes the transformed code.
    """
    python_code = ""
    for code_block in input:
        for line in code_block:
            python_code += line + "\n"
        python_code += "\n"  # add newline after each code block

    # remove empty lines
    python_code = "\n".join(filter(None, python_code.splitlines()))

    # add necessary imports
    python_code = "from typing import Callable, List\n" + python_code

    # add docstring
    python_code = (
        "@transform_input\n"
        + 'def transform_input(input: List[List[str]]) -> Callable:\n    """\n    Transforms the given input into Python code that aligns with Pythonic practices advocated by Luciano Ramalho.\n\n    Parameters:\n        input (List[List[str]]): List of lists containing strings representing code snippets.\n\n    Returns:\n        Callable: A function that takes in a list of arguments and executes the transformed code.\n    """\n'
        + python_code
    )

    # execute the transformed code
    exec(python_code, globals())

    return transform_input
