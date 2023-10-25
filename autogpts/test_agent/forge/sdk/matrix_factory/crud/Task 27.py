# Test User Documentation

# This is a test user documentation for a Python project.

# The project is a simple calculator that can perform basic arithmetic operations.

# To use the calculator, simply import the calculator module and create an instance of the Calculator class.

from calculator import Calculator

# Create an instance of the Calculator class
calc = Calculator()

# To perform an operation, use the appropriate method and pass in the two numbers as arguments.

# Addition
result = calc.add(5, 10)
print(result)  # Output: 15

# Subtraction
result = calc.subtract(10, 5)
print(result)  # Output: 5

# Multiplication
result = calc.multiply(5, 10)
print(result)  # Output: 50

# Division
result = calc.divide(10, 5)
print(result)  # Output: 2

# The calculator also has a memory feature that allows you to store a number and use it in subsequent calculations.

# To store a number in memory, use the "store" method and pass in the number as an argument.
calc.store(10)

# To use the number in memory, simply omit one of the arguments in the calculation method.
result = calc.add(5)
print(result)  # Output: 15 (10 + 5)

# You can also clear the memory by using the "clear" method.
calc.clear()

# Thank you for using the calculator!
