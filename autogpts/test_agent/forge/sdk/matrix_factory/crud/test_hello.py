# Import the pytest library
import pytest

# Define the function with the correct name
def say_hello():
     # Add the print statement
     print("Hello, world!")

# Create a pytest function
def test_say_hello():
     # Call the function and save the output as a variable
     result = say_hello()
     # Use assert to check if the output is correct
     assert result == "Hello, world!"