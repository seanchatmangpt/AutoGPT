# Feature: Provide code suggestions for better performance.
# Scenario: The code analysis tool should provide suggestions for improving performance, such as using
# built-in functions and standard library.

# Import necessary libraries
import sys
import timeit
import time
from collections import Counter
from functools import partial
from itertools import islice


# Function to analyze code and provide performance suggestions
def analyze_code(code):
    """
    Analyzes given code and provides suggestions to improve performance
    """

    # Use timeit module to measure execution time
    t = timeit.Timer(code)
    execution_time = t.timeit()

    # Use sys.getsizeof() to measure object size in bytes
    object_size = sys.getsizeof(code)

    # Use Counter to count occurrences of elements in code
    code_elements = Counter(code)

    # Use partial to pre-fill arguments for functions
    add = partial(sum, [1, 2, 3])

    # Use islice to iterate over a sequence in chunks
    chunks = islice([1, 2, 3, 4, 5, 6], 2)

    # Print suggestions to improve performance
    print("To improve performance, consider using built-in functions and libraries:")
    print("Execution time:", execution_time)
    print("Object size:", object_size)
    print("Frequent elements in code:", code_elements.most_common(3))
    print("Partial function:", add())
    print("Code in chunks:", list(chunks))


# Call analyze_code function with sample code
analyze_code("a = 1 + 2 + 3; b = sum([1, 2, 3]); c = [i for i in range(10)]")

# Feature: Integration with project management tools.
# Scenario: The system should be able to automatically create and assign tasks in specified project management
# tool.

# Import necessary libraries
import requests
import json


# Function to create and assign tasks in project management tool
def create_task(project, title, description):
    """
    Creates a task in specified project and assigns it to logged-in user
    """

    # Make API call to project management tool
    response = requests.post(
        "https://projectmanagement.com/api/tasks/create",
        data=json.dumps(
            {"project": project, "title": title, "description": description}
        ),
    )

    # Check for successful response
    if response.status_code == 200:
        print("Task created and assigned successfully!")
    else:
        print("Error creating and assigning task.")


# Call create_task function with sample data
create_task(
    "Project A", "Implement feature X", "Task to implement feature X in project A"
)

# Feature: Code profiling and optimization.
# Scenario: The system should be able to analyze and identify areas of code that could be
# optimized for better performance.

# Import necessary libraries
import cProfile
import pstats


# Function to profile and optimize code
def optimize_code(code):
    """
    Profiles given code and provides insights for optimization
    """

    # Use cProfile to profile code
    cProfile.run(code, "profile_results")

    # Use pstats to print profiling results
    stats = pstats.Stats("profile_results")
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats(".*")


# Call optimize_code function with sample code
optimize_code("a = 1 + 2 + 3; b = [i for i in range(100)]; c = sum(b)")

# Feature: Code formatting.
# Scenario: The system should apply standard formatting rules to the generated Python code,
# ensuring consistency and readability.

# Import necessary libraries
import black


# Function to format code using Black
def format_code(code):
    """
    Applies standard formatting rules to given code
    """

    # Use Black to format code
    formatted_code = black.format_str(code)

    # Print formatted code
    print(formatted_code)


# Call format_code function with sample code
format_code("a = 1+2+3;b = [i for i in range(100)];   c = sum(b)")

# Feature: User Login
# Scenario: As a user, I want to be able to log in to the system with my credentials.

# Import necessary libraries
import getpass


# Function to handle user login
def user_login():
    """
    Allows user to log in with credentials
    """

    # Get username and password from user
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Check credentials and log user in
    if username == "demo" and password == "demo123":
        print("Successfully logged in!")
    else:
        print("Invalid credentials. Please try again.")


# Call user_login function
user_login()
