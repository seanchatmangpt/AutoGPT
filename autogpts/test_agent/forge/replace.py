import ast
import astor
import autopep8

from forge.sdk.abilities.code.radon_workbench import refactor_code


def replace_and_check_in_ast(source, replace_name, new_code):
    # Perform initial check
    # source = refactor_code(source)
    # new_code = refactor_code(new_code)

    # Parse the source code into an AST
    original_ast = ast.parse(source)

    # Replace the function or class in the AST
    modified_ast = replace_in_ast(original_ast, replace_name, new_code)

    # Generate the modified source code from the modified AST
    modified_code = astor.to_source(modified_ast)

    autopep8.fix_code(modified_code, options={"aggressive": 1})

    return modified_code


def replace_in_ast(original_ast, replace_name, new_code):
    def modify_ast(node):
        if (
            isinstance(node, (ast.FunctionDef, ast.ClassDef))
            and node.name == replace_name
        ):
            new_ast = ast.parse(new_code).body[0]
            return new_ast
        return node

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

        return modify_ast(node)

    modified_ast = recursive_modify(original_ast)
    return modified_ast


# Example usage
replace_name = "my_function"
new_code = """
    def my_function(x, y):
    return x * y
"""

replace_name = "__init__"
new_code = """
    def __init__(x, y):
    self.x = x
    self.y = y
"""

# Source code to replace function in
source_code = """
class MyClass:
    def __init__(self):
        pass
    def my_function(x, y):
    return x + y
    
        def my_other_function(x, y):
    return x - y
    
def main():
    modified_code = replace_and_check_in_ast(source_code, replace_name, new_code)
    print("Modified code:")
    print(modified_code)


if __name__ == '__main__':
    main()
"""


def main():
    modified_code = replace_and_check_in_ast(source_code, replace_name, new_code)
    print("Modified code:")
    print(modified_code)


if __name__ == "__main__":
    main()
