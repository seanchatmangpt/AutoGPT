import ast
import astor


def replace_function_in_file(source, replace_name, new_function_code):
    original_ast = ast.parse(source)

    # Step 2: Define a function to modify the AST for functions
    def modify_function_ast(node):
        if isinstance(node, ast.FunctionDef) and node.name == replace_name:
            # Replace the function with the provided new function code
            new_function_ast = ast.parse(new_function_code)
            return new_function_ast
        return node

    # Step 3: Define a function to modify the AST for classes
    def modify_class_ast(node):
        if isinstance(node, ast.ClassDef) and node.name == replace_name:
            # Replace the class with the provided new class code
            new_class_ast = ast.parse(new_class_code)
            return new_class_ast
        return node

    # Step 4: Recursively modify the AST for both functions and classes
    def recursive_modify(node):
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                new_value = []
                for item in value:
                    if isinstance(item, ast.AST):
                        new_item = recursive_modify(item)
                        new_value.append(new_item)
                    else:
                        new_value.append(item)
                setattr(node, field, new_value)
            elif isinstance(value, ast.AST):
                new_node = recursive_modify(value)
                setattr(node, field, new_node)
        if isinstance(node, ast.FunctionDef):
            return modify_function_ast(node)
        elif isinstance(node, ast.ClassDef):
            return modify_class_ast(node)
        return node

    modified_ast = recursive_modify(original_ast)

    # Step 5: Generate Python source code from the modified AST
    modified_code = astor.to_source(modified_ast)

    return modified_code


# Example usage for replacing a class:
class_name_to_replace = "MyClass"
new_class_code = """
class NewClass:
    # New class implementation here
    def __init__(self):
        pass
"""

# Example usage for replacing a function:
function_name_to_replace = "enable_realtime_collaboration"
new_function_code = """
def function_to_replace(x, y):
    # New function implementation here
    result = x + y
    return result
"""

input_file = "/Users/candacechatman/dev/test_agent/forge/sdk/benchmarks/matrix_overnight/refactor_simplify_code_use_stdlib_builtinspy_2023-10-24_13-28-24.py"

# Step 1: Parse the Python source code into an AST
with open(input_file, "r") as file:
    source = file.read()

# Replace a class in the Python file
modified_code_class = replace_function_in_file(
    source, class_name_to_replace, new_class_code
)

# Replace a function in the Python file
modified_code_function = replace_function_in_file(
    modified_code_class, function_name_to_replace, new_function_code
)

with open("modified_code.py", "w") as file:
    file.write(modified_code_function)
