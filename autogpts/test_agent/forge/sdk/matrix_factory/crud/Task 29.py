# Import the necessary modules
import requests
import json

# Define the base URL for the API
base_url = "https://api.example.com/"

# Define the endpoint for the specific resource
endpoint = "users/"

# Define the parameters for the request
params = {"id": 1234, "name": "John Doe"}

# Make the request and store the response
response = requests.get(base_url + endpoint, params=params)

# Convert the response to JSON format
data = response.json()

# Print the data
print(data)