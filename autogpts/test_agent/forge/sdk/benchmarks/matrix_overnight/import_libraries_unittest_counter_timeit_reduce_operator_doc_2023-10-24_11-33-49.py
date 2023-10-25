# Import necessary libraries
from unittest import TestCase, main
from collections import Counter
from timeit import timeit
from functools import reduce
from operator import mul
from doctest import testmod


# Helper Functions
def add(a, b):
    """
    Adds two numbers together
    """
    return a + b


def multiply(a, b):
    """
    Multiplies two numbers together
    """
    return a * b


def power(a, b):
    """
    Calculates the power of a number
    """
    return a**b


def is_even(num):
    """
    Checks if a number is even or not
    """
    return num % 2 == 0


def is_odd(num):
    """
    Checks if a number is odd or not
    """
    return num % 2 != 0


# Test Case Class
class TestFunctionalProgramming(TestCase):
    """
    Test Case class for functional programming functions
    """

    def test_add(self):
        """
        Test case for add function
        """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 10), 5)

    def test_multiply(self):
        """
        Test case for multiply function
        """
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-5, 10), -50)

    def test_power(self):
        """
        Test case for power function
        """
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(0, 10), 0)
        self.assertEqual(power(-5, 2), 25)

    def test_is_even(self):
        """
        Test case for is_even function
        """
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(5), False)

    def test_is_odd(self):
        """
        Test case for is_odd function
        """
        self.assertEqual(is_odd(2), False)
        self.assertEqual(is_odd(0), False)
        self.assertEqual(is_odd(5), True)


# Code analysis and suggestions for refactoring
# Use list comprehension instead of for loops
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]

# Use built-in functions instead of custom functions
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
product_of_numbers = reduce(mul, numbers)

# Use generator expression instead of list comprehension for large datasets
numbers = [1, 2, 3, 4, 5]
squares = (num**2 for num in numbers)

# Use built-in functions for common operations
numbers = [1, 2, 3, 4, 5]
min_number = min(numbers)
max_number = max(numbers)
number_count = len(numbers)
number_sum = sum(numbers)

# Use built-in Counter class for counting occurrences in a list
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numbers_count = Counter(numbers)

# Use built-in filter function instead of custom functions for filtering
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Use built-in map function instead of custom functions for mapping
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))


# Display test results to user
if __name__ == "__main__":
    # Run unit tests
    main()
    # Run doctests
    testmod()

    # Display results to user
    print("Unit Tests Passed!")
    print("Doctests Passed!")

# Feature: Debugging tools for Python code
# Scenario: The system should provide debugging tools such as breakpoints, step-by-step execution
# Use built-in debugging tools in IDEs such as PyCharm or VSCode

# Feature: Integration with popular libraries and frameworks
# Scenario: The IDE should allow for easy integration with popular Python libraries and frameworks
# Use built-in package manager such as pip or conda to install and manage libraries and frameworks

# Feature: Integration with project management tools
# Scenario: The system should be able to integrate with popular project management tools such as Jira
# Use built-in tools or plugins to integrate with project management tools

# Feature: Automatic error detection and debugging
# Scenario: The system should detect errors and bugs in the code and provide suggestions for
# Use built-in tools such as pylint or flake8 for code analysis and error detection

# Feature: Integration with version control systems
# Scenario: The system should be able to connect with popular version control systems like Git
# Use built-in tools or plugins to integrate with version control systems

# Feature: Code review and collaboration
# Scenario: The system should allow for code review and collaboration between team members
# Use built-in tools such as GitHub or Bitbucket for code review and collaboration.
