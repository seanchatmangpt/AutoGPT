# Best practices: use meaningful, descriptive names for variables and functions
# and avoid using the pass keyword

# Use the built-in library itertools to iterate over the list
# and filter out empty strings
list_of_strings = ["- -", "", "", "", "", "", "", "", "", ""]

import itertools

# Use list comprehension to filter out empty strings
cleaned_list = [
    string for string in itertools.filterfalse(lambda x: x == "", list_of_strings)
]

# Use a generator expression to iterate over the list and yield the cleaned strings
cleaned_strings = (
    string for string in itertools.filterfalse(lambda x: x == "", list_of_strings)
)

# Use a list comprehension to generate a list of the cleaned strings
cleaned_list = [string for string in cleaned_strings]

# Use a for loop to print each string in the cleaned list
for string in cleaned_list:
    print(string)

# Use the built-in library subprocess to execute system commands
import subprocess

# Use a list comprehension to generate a list of the system commands
system_commands = [f"git add {file}" for file in cleaned_list]

# Use the subprocess module to execute each system command
for command in system_commands:
    subprocess.run(command, shell=True)

# Use the built-in library statistics to calculate the mean, median, and standard deviation of a list of numbers
list_of_numbers = [1, 2, 3, 4, 5]

import statistics

# Use the mean function to calculate the average of the list
average = statistics.mean(list_of_numbers)

# Use the median function to calculate the middle value of the list
median = statistics.median(list_of_numbers)

# Use the stdev function to calculate the standard deviation of the list
standard_deviation = statistics.stdev(list_of_numbers)

# Use the built-in library unittest to write and run tests for the code
import unittest


# Define a class for the tests
class TestCode(unittest.TestCase):
    # Write a test function using the assertEqual method to check if two values are equal
    def test_average(self):
        self.assertEqual(average, 3)

    # Write a test function using the assertIn method to check if a value is in a list
    def test_median(self):
        self.assertIn(median, list_of_numbers)

    # Write a test function using the assertGreater method to check if one value is greater than another
    def test_standard_deviation(self):
        self.assertGreater(standard_deviation, 0)


# Run the tests
unittest.main()

# Use the built-in library timeit to measure the execution time of a function
import timeit


# Define a function to measure the execution time of
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Use the timeit function to measure the execution time of the factorial function
execution_time = timeit.timeit("factorial(5)", globals=globals(), number=100000)

print(f"Execution time for factorial function: {execution_time} seconds")

# Use the built-in library memory_profiler to measure the memory usage of a function
import memory_profiler


# Define a function to measure the memory usage of
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Use the memory_profiler function to measure the memory usage of the fibonacci function
memory_usage = memory_profiler.memory_usage(proc=fibonacci, max_usage=True)

print(f"Maximum memory usage for fibonacci function: {memory_usage[0]} MB")
