# Import the necessary modules
import os
import sys


# Define a function to print a message
def print_message(message):
    print(message)


# Define a class for a person
class Person:
    # Initialize the class with a name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a method to print the person's information
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Create an instance of the Person class
person = Person("John", 30)

# Print a message
print_message("Hello, world!")

# Print the person's information
person.print_info()
