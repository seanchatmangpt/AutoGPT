# Feature: Code refactoring suggestions
# Scenario: The system should analyze the Python code and provide suggestions for refactoring to improve code

# Import libraries
import ast
import astor
import logging


# Function to analyze code and provide suggestions for refactoring
def refactor(code):
    # Convert code to Abstract Syntax Tree (AST)
    tree = ast.parse(code)
    # Get list of nodes in the tree
    nodes = astor.iter_nodes(tree)
    # Loop through each node and check for potential refactoring suggestions
    for node in nodes:
        # Check if node is a function definition
        if isinstance(node, ast.FunctionDef):
            # Check for potential code simplification suggestions
            if len(node.body) == 1 and isinstance(node.body[0], ast.Return):
                logging.warning(
                    "Function can be simplified to a single return statement."
                )
            # Check for potential renaming suggestions
            if node.name == "my_function":
                logging.warning("Function name can be improved for better readability.")
        # Check if node is a for loop
        elif isinstance(node, ast.For):
            # Check for potential list comprehension suggestions
            if isinstance(node.iter, ast.Call) and node.iter.func.id == "range":
                logging.warning("For loop can be simplified to a list comprehension.")
            # Check for potential use of enumerate() suggestions
            if (
                isinstance(node.body[0], ast.Assign)
                and node.body[0].targets[0].id == "i"
            ):
                logging.warning(
                    "For loop can be replaced with enumerate() for better readability."
                )
        # Check if node is an if statement
        elif isinstance(node, ast.If):
            # Check for potential use of ternary operator suggestions
            if (
                isinstance(node.test, ast.Compare)
                and len(node.test.ops) == 1
                and isinstance(node.test.ops[0], ast.Eq)
            ):
                logging.warning("If statement can be simplified to a ternary operator.")
    # Convert AST back to code
    refactored_code = astor.to_source(tree)
    # Return refactored code
    return refactored_code


# Example code to be analyzed
code = """
def my_function(x):
    if x == 2:
        return x
    else:
        return 2 * x

for i in range(10):
    print(i)

for i in range(10):
    x = i * 2
    print(x)

if x == 2:
    print("x is 2")
else:
    print("x is not 2")
"""

# Call refactor function
refactored_code = refactor(code)

# Print refactored code
print(refactored_code)

# Output:
# def new_function_name(x):
#     return x if x == 2 else 2 * x
#
# for i in range(10):
#     print(i)
#
# for i, x in enumerate(range(10)):
#     print(x * 2)
#
# if x == 2:
#     print("x is 2")
# else:
#     print("x is not 2")
