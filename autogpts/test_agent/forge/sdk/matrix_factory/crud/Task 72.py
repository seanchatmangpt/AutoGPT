# Import the necessary modules
import os
import sys
import hashlib

# Define a function to check the user's password
def check_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Compare the hashed password to the stored password
    if hashed_password == stored_password:
        print("Access granted")
    else:
        print("Access denied")

# Get the stored password from a secure location
stored_password = os.environ.get("PASSWORD")

# Get the user's input for the password
password = input("Enter your password: ")

# Check the password
check_password(password)