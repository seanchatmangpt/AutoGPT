# Import the necessary modules
import re

# Define the search function
def search(query, text):
    # Use regular expressions to find the query in the text
    matches = re.findall(query, text)
    # Return the matches
    return matches

# Test the search function
text = "This is a test string to test the search functionality"
query = "test"
matches = search(query, text)
print(matches) # Output: ['test', 'test']