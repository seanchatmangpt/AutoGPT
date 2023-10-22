# Import the necessary modules
import re

# Define the data validation system
def validate(data, pattern):
    # Use the re module to match the pattern to the data
    match = re.match(pattern, data)
    # If there is a match, return True
    if match:
        return True
    # If there is no match, return False
    else:
        return False

# Define the pattern to be used for validation
pattern = r'^[a-zA-Z]+$'

# Test the validation system with different inputs
print(validate("Hello", pattern)) # Output: True
print(validate("123", pattern)) # Output: False
print(validate("Hello123", pattern)) # Output: False