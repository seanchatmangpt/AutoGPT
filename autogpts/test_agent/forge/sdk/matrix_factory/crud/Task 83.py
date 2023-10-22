# Import the necessary modules
import re
import json

# Define the validation function
def validate(data, schema):
    # Check if the data matches the schema
    if re.match(schema, data):
        # If it does, return True
        return True
    else:
        # If it doesn't, return False
        return False

# Define the schema for the test data
schema = r'^[a-zA-Z0-9]+$'

# Define the test data
data = 'Test123'

# Validate the test data using the defined schema
result = validate(data, schema)

# Print the result
print(result)