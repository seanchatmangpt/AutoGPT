# Feature: User authentication.
# Scenario: The system should allow users to create accounts and log in with their credentials.
import hashlib
import secrets


# Create a function to generate a unique identifier for each user
def generate_id():
    return secrets.token_urlsafe(32)


# Create a dictionary to store user credentials
users = {}


# Create a function to create a new user account
def create_account(username, password):
    # Check if username is already taken
    if username in users:
        print("Username already taken. Please choose a different username.")
    else:
        # Create a unique ID for the user
        user_id = generate_id()
        # Hash the password for security
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        # Store the user's information in the dictionary
        users[username] = {"id": user_id, "password": hashed_password}
        print("Account successfully created.")


# Create a function to log in a user
def login(username, password):
    # Check if username exists in the dictionary
    if username in users:
        # Hash the password for comparison
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        # Check if the hashed password matches the one stored in the dictionary
        if users[username]["password"] == hashed_password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please create an account.")


# Test the functions
create_account("user1", "password123")
create_account("user2", "abc123")
login("user1", "password123")
login("user2", "password123")
login("user2", "abc123")
