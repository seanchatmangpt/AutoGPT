# Import the necessary modules
import requests
import json

# Define the base URL for the API
base_url = "https://api.example.com/"

# Define a function to make a GET request to the API
def get_data(endpoint, params=None):
    """
    Makes a GET request to the API and returns the response as a JSON object.
    
    Args:
        endpoint (str): The endpoint to make the request to.
        params (dict, optional): Any parameters to include in the request.
        
    Returns:
        dict: The response from the API as a JSON object.
    """
    # Make the request and store the response
    response = requests.get(base_url + endpoint, params=params)
    
    # Convert the response to a JSON object and return it
    return response.json()

# Define a function to make a POST request to the API
def post_data(endpoint, data):
    """
    Makes a POST request to the API with the given data and returns the response as a JSON object.
    
    Args:
        endpoint (str): The endpoint to make the request to.
        data (dict): The data to include in the request.
        
    Returns:
        dict: The response from the API as a JSON object.
    """
    # Make the request and store the response
    response = requests.post(base_url + endpoint, json=data)
    
    # Convert the response to a JSON object and return it
    return response.json()

# Define a function to make a PUT request to the API
def put_data(endpoint, data):
    """
    Makes a PUT request to the API with the given data and returns the response as a JSON object.
    
    Args:
        endpoint (str): The endpoint to make the request to.
        data (dict): The data to include in the request.
        
    Returns:
        dict: The response from the API as a JSON object.
    """
    # Make the request and store the response
    response = requests.put(base_url + endpoint, json=data)
    
    # Convert the response to a JSON object and return it
    return response.json()

# Define a function to make a DELETE request to the API
def delete_data(endpoint):
    """
    Makes a DELETE request to the API and returns the response as a JSON object.
    
    Args:
        endpoint (str): The endpoint to make the request to.
        
    Returns:
        dict: The response from the API as a JSON object.
    """
    # Make the request and store the response
    response = requests.delete(base_url + endpoint)
    
    # Convert the response to a JSON object and return it
    return response.json()

# Example usage of the functions
# Get data from the "users" endpoint
users = get_data("users")

# Create a new user by making a POST request to the "users" endpoint
new_user = {"name": "John", "age": 30}
response = post_data("users", new_user)

# Update the user's age by making a PUT request to the "users" endpoint with the updated data
updated_user = {"name": "John", "age": 31}
response = put_data("users", updated_user)

# Delete the user by making a DELETE request to the "users" endpoint
response = delete_data("users/1")