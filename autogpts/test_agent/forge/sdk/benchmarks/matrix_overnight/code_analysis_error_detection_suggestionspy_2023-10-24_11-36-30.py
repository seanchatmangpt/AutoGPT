# Feature: Code analysis and error detection.
# Scenario: The system should provide suggestions for code improvements and automatically implement them if selected by the user.

# import libraries
from collections import defaultdict
import ast
import astor


# define function to analyze code and suggest improvements
def analyze_code(code):
    # parse code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)

    # create a dictionary to store suggestions
    suggestions = defaultdict(list)

    # iterate through all nodes in the AST
    for node in ast.walk(tree):
        # check for specific types of nodes
        if isinstance(node, ast.Assign):
            # suggest renaming variables using snake_case
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if not target.id.islower():
                        suggestions["rename_variables"].append(target.id)

        elif isinstance(node, ast.FunctionDef):
            # suggest extracting functions
            if len(node.body) > 5:
                suggestions["extract_functions"].append(node.name)

        # add more checks for other code improvements

    # print suggestions
    for suggestion, items in suggestions.items():
        print("Suggestion: {}".format(suggestion))
        print("Items: {}".format(items))

    # prompt user to select suggestions to implement
    selected_suggestions = input(
        "Select suggestions to implement (separated by commas): "
    ).split(",")

    # implement selected suggestions
    for suggestion in selected_suggestions:
        if suggestion in suggestions:
            # implement suggestion
            if suggestion == "rename_variables":
                # rename variables using snake_case
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        target.id = target.id.lower()

            elif suggestion == "extract_functions":
                # extract function
                func_name = suggestions[suggestion][0]
                func = [
                    node
                    for node in ast.walk(tree)
                    if isinstance(node, ast.FunctionDef) and node.name == func_name
                ][0]

                # create a new function using the extracted code
                new_func = ast.FunctionDef(
                    name="new_" + func_name,
                    args=func.args,
                    body=func.body,
                    decorator_list=[],
                )

                # replace the extracted code with a function call
                func.body = [
                    ast.Call(func=ast.Name(id="new_" + func_name), args=[], keywords=[])
                ]

    # return updated code
    return astor.to_source(tree)
