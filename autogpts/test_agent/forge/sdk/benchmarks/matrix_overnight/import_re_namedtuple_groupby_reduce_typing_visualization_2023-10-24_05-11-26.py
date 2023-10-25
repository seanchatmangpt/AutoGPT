import re
from collections import namedtuple
from itertools import groupby
from functools import reduce
from typing import List

# Feature: Implement data visualization.
# Scenario: The system should generate visual representations of data using charts, graphs, and other visual elements
# This will help improve the performance and maintainability of the code.


def generate_visualizations(data):
    """
    Generates visual representations of data using charts, graphs, and other visual elements.
    :param data: input data to be visualized
    :return: visual representation of data
    """
    # TODO: implement visualization generation logic
    pass


# Feature: Automated testing.
# Scenario: The system should be able to run automated tests on the codebase to ensure proper functionality
def run_tests(codebase):
    """
    Runs automated tests on the codebase to ensure proper functionality.
    :param codebase: input codebase to be tested
    :return: test results
    """
    # TODO: implement automated testing logic
    pass


# Feature: Collaboration and team management.
# Scenario: The system should allow multiple users to collaborate on the same codebase and manage
def manage_collaboration(users, codebase):
    """
    Allows multiple users to collaborate on the same codebase and manage.
    :param users: list of users collaborating on the codebase
    :param codebase: codebase to be collaborated on
    :return: collaboration management results
    """
    # TODO: implement collaboration management logic
    pass


# Feature: Integration with version control systems.
# Scenario: The system should integrate with popular version control systems, such as Git
def integrate_with_version_control(codebase):
    """
    Integrates with popular version control systems, such as Git.
    :param codebase: codebase to be integrated with version control
    :return: integration results
    """
    # TODO: implement version control integration logic
    pass


# Feature: Support for virtual environments.
# Scenario: The system should allow the user to create and manage virtual environments for their Python project
def create_virtual_environment(name):
    """
    Creates a virtual environment for the given name.
    :param name: name of the virtual environment
    :return: virtual environment
    """
    # TODO: implement virtual environment creation logic
    pass


# AGI Simulations of David Thomas, Andrew Hunt, Luciano Ramalho.

# Transform input into a list of names
names_str = "David Thomas, Andrew Hunt, Luciano Ramalho"
names = [name.strip() for name in names_str.split(",")]

# Create a namedtuple for storing information on each individual
Individual = namedtuple("Individual", ["first_name", "last_name"])

# Use functional programming to create a list of Individual objects
individuals = list(
    map(
        lambda name: Individual(first_name=name.split()[0], last_name=name.split()[1]),
        names,
    )
)


# Function to get the average of a list of numbers
def get_average(numbers: List[float]) -> float:
    """
    Calculates the average of a list of numbers.
    :param numbers: input list of numbers
    :return: average of the numbers
    """
    return reduce(lambda x, y: x + y, numbers) / len(numbers)


# Function to get the maximum value in a list of numbers
def get_max(numbers: List[float]) -> float:
    """
    Finds the maximum value in a list of numbers.
    :param numbers: input list of numbers
    :return: maximum value in the list
    """
    return reduce(lambda x, y: x if x > y else y, numbers)


# Function to get the minimum value in a list of numbers
def get_min(numbers: List[float]) -> float:
    """
    Finds the minimum value in a list of numbers.
    :param numbers: input list of numbers
    :return: minimum value in the list
    """
    return reduce(lambda x, y: x if x < y else y, numbers)


# Function to get the median value in a list of numbers
def get_median(numbers: List[float]) -> float:
    """
    Calculates the median value in a list of numbers.
    :param numbers: input list of numbers
    :return: median value in the list
    """
    sorted_numbers = sorted(numbers)
    middle = len(numbers) // 2
    return (
        sorted_numbers[middle]
        if len(numbers) % 2
        else (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    )


# Function to calculate the variance of a list of numbers
def get_variance(numbers: List[float]) -> float:
    """
    Calculates the variance of a list of numbers.
    :param numbers: input list of numbers
    :return: variance of the numbers
    """
    mean = get_average(numbers)
    return reduce(lambda x, y: x + (y - mean) ** 2, numbers) / len(numbers)


# Function to calculate the standard deviation of a list of numbers
def get_standard_deviation(numbers: List[float]) -> float:
    """
    Calculates the standard deviation of a list of numbers.
    :param numbers: input list of numbers
    :return: standard deviation of the numbers
    """
    return get_variance(numbers) ** 0.5


# Function to group individuals by last name
def group_by_last_name(individuals: List[Individual]) -> dict:
    """
    Groups individuals by their last name.
    :param individuals: input list of individuals
    :return: dictionary with last names as keys and a list of individuals with that last name as values
    """
    group_by_last = groupby(
        sorted(individuals, key=lambda i: i.last_name), lambda i: i.last_name
    )
    return {key: list(value) for key, value in group_by_last}


# Function to get the full name of an individual
def get_full_name(individual: Individual) -> str:
    """
    Returns the full name of an individual.
    :param individual: input individual
    :return: full name of the individual
    """
    return f"{individual.first_name} {individual.last_name}"


# Function to get the initials of an individual
def get_initials(individual: Individual) -> str:
    """
    Returns the initials of an individual.
    :param individual: input individual
    :return: initials of the individual
    """
    return f"{individual.first_name[0]}.{individual.last_name[0]}."


# Function to clean up a string
def clean_string(string: str) -> str:
    """
    Cleans up a string by removing any non-alphanumeric characters and converting it to lowercase.
    :param string: input string
    :return: cleaned up string
    """
    return re.sub(r"\W+", "", string).lower()


# Function to find the most common word in a string
def get_most_common_word(string: str) -> str:
    """
    Finds the most common word in a string.
    :param string: input string
    :return: most common word in the string
    """
    words = clean_string(string).split()
    return max(set(words), key=words.count)


# Function to find the least common word in a string
def get_least_common_word(string: str) -> str:
    """
    Finds the least common word in a string.
    :param string: input string
    :return: least common word in the string
    """
    words = clean_string(string).split()
    return min(set(words), key=words.count)
