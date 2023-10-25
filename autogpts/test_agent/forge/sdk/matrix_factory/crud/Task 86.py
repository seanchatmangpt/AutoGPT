# Import the necessary modules
from hashlib import sha256
from uuid import uuid4


# Define the User class
class User:
    # Initialize the user with a unique ID and empty password
    def __init__(self):
        self.id = uuid4()
        self.password = None

    # Method to set the user's password
    def set_password(self, password):
        # Hash the password using SHA256
        self.password = sha256(password.encode("utf-8")).hexdigest()

    # Method to check if the given password matches the user's password
    def check_password(self, password):
        # Hash the given password using SHA256 and compare it to the stored password
        return self.password == sha256(password.encode("utf-8")).hexdigest()


# Create a dictionary to store user information
users = {}


# Function to register a new user
def register_user(username, password):
    # Check if the username is already taken
    if username in users:
        print("Username already taken.")
    else:
        # Create a new user object
        user = User()
        # Set the user's password
        user.set_password(password)
        # Add the user to the dictionary
        users[username] = user
        print("User successfully registered.")


# Function to authenticate a user
def authenticate_user(username, password):
    # Check if the username exists in the dictionary
    if username in users:
        # Get the user object
        user = users[username]
        # Check if the given password matches the user's password
        if user.check_password(password):
            print("User successfully authenticated.")
        else:
            print("Incorrect password.")
    else:
        print("User does not exist.")


# Example usage
register_user("john", "password123")
authenticate_user("john", "password123")
authenticate_user("john", "wrongpassword")
