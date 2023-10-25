# Import the necessary modules
from hashlib import sha256


# Define the User class
class User:
    # Initialize the class with a username and password
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Define a method to hash the password using SHA256
    def hash_password(self):
        self.password = sha256(self.password.encode()).hexdigest()

    # Define a method to authenticate the user
    def authenticate(self, password):
        # Hash the given password
        hashed_password = sha256(password.encode()).hexdigest()
        # Check if the hashed password matches the stored password
        if hashed_password == self.password:
            print("Authentication successful!")
        else:
            print("Authentication failed.")


# Create a new user
user = User("JohnDoe", "password123")

# Hash the password
user.hash_password()

# Authenticate the user
user.authenticate("password123")
