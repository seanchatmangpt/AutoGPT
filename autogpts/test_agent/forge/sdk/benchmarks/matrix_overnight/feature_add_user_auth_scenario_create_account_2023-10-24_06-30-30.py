# Feature: Add user authentication and authorization.
# Scenario: The system should allow users to create accounts and login with secure credentials.

# Import necessary libraries
import hashlib
import secrets


# Function to create a user account
def create_account(username, password):
    salt = secrets.token_hex(16)  # Generate a random salt
    hashed_password = hashlib.sha256(
        password.encode() + salt.encode()
    ).hexdigest()  # Hash the password with the salt
    return {
        "username": username,
        "password": hashed_password,
        "salt": salt,
    }  # Return the user account details


# Function to verify login credentials
def login(username, password, user_accounts):
    if username in user_accounts:  # Check if the username exists in the user accounts
        salt = user_accounts[username]["salt"]
        hashed_password = hashlib.sha256(
            password.encode() + salt.encode()
        ).hexdigest()  # Hash the password with the stored salt
        if (
            hashed_password == user_accounts[username]["password"]
        ):  # Compare the hashed passwords
            return True  # Return True if the passwords match
    return False  # Return False if the credentials are invalid


# Feature: Automated testing.
# Scenario: The system should automatically run unit tests and integration tests to ensure code functionality and catch any errors.

# Import necessary libraries
import unittest


# Create a test class
class TestAuthentication(unittest.TestCase):
    # Function to set up the test environment
    def setUp(self):
        self.user_accounts = {
            "John": {"username": "John", "password": "password", "salt": "1234567890"},
            "Jane": {"username": "Jane", "password": "qwerty", "salt": "0987654321"},
        }

    # Test function to check if a user can create an account
    def test_create_account(self):
        new_user = create_account("Jack", "12345")
        self.assertEqual(new_user["username"], "Jack")
        self.assertNotEqual(
            new_user["password"], "12345"
        )  # Check if the password is hashed
        self.assertEqual(
            len(new_user["salt"]), 32
        )  # Check if the salt is 32 characters long

    # Test function to check if a user can login with valid credentials
    def test_login_valid(self):
        self.assertTrue(login("John", "password", self.user_accounts))
        self.assertTrue(login("Jane", "qwerty", self.user_accounts))

    # Test function to check if a user cannot login with invalid credentials
    def test_login_invalid(self):
        self.assertFalse(login("Jack", "12345", self.user_accounts))
        self.assertFalse(login("John", "qwerty", self.user_accounts))


# Run the tests
if __name__ == "__main__":
    unittest.main()

# Feature: Code compilation.
# Scenario: The system should be able to compile the generated Python code into executable files.

# Import necessary libraries
import py_compile

# Compile the python file
py_compile.compile("my_code.py")

# Feature: Code execution.
# Scenario: The system should be able to execute the generated Python code.

# Import necessary libraries
import subprocess


# Function to execute the python file
def execute_file(file):
    process = subprocess.Popen(
        ["python", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()  # Return the output and error messages


# Run the python file
output, errors = execute_file("my_code.py")
print(output)  # Print the output
print(errors)  # Print the error messages
