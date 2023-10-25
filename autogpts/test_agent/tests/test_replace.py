from textwrap import dedent

import pytest
from forge.replace import replace_and_check_in_ast


# Test for valid replacement
def test_replace_and_check_in_ast_valid():
    source = dedent(
        """
    def my_function(x, y):
        return x + y
    """
    )

    replace_name = "my_function"
    new_code = dedent(
        """
    def my_function(x, y):
        return x * y
    """
    )

    expected_output = dedent(
        """
    def my_function(x, y):
        return x * y
    """
    )

    modified_code = replace_and_check_in_ast(source, replace_name, new_code)
    assert modified_code.strip() == expected_output.strip()


# Test for invalid initial code
def test_replace_and_check_class():
    source = dedent(
        """
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
    )

    replace_name = "__init__"
    new_code = dedent(
        """
        def __init__(x, y):
        self.x = x
        self.y = y
    """
    )

    expected_output = dedent(
        '''
    class MyClass:

    def __init__(self, x, y):
        """
    Initializes the class with given x and y values.
    :param x: x value
    :param y: y value
    """
        self.x = x
        self.y = y

    def my_function(x, y):
        """This function adds two numbers together and returns the result"""
        return x + y

    def my_other_function(x, y):
        """This function subtracts two numbers and returns the result"""
        return x - y


def main():
    """This function calls the replace_and_check_in_ast function and prints the modified code"""
    modified_code = replace_and_check_in_ast(source_code, replace_name,
        new_code)
    print('Modified code:')
    print(modified_code)


if __name__ == '__main__':
    main()
    '''
    )

    modified_code = replace_and_check_in_ast(source, replace_name, new_code)
    assert modified_code.strip() == expected_output.strip()
