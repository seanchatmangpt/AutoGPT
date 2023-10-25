# Import the necessary modules
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

# Create the Flask app
app = Flask(__name__)

# Create the HTTPBasicAuth object
auth = HTTPBasicAuth()

# Define the users and their passwords
users = {"john": "password123", "jane": "secret"}


# Define the authentication function
@auth.verify_password
def verify_password(username, password):
    # Check if the user exists
    if username in users:
        # Check if the password is correct
        if password == users[username]:
            return True
    return False


# Define the route for testing authentication
@app.route("/auth")
@auth.login_required
def test_auth():
    return jsonify({"message": "Authentication successful!"})


# Define the route for testing authorization
@app.route("/auth/authorized")
@auth.login_required(role="admin")
def test_auth_authorized():
    return jsonify({"message": "Authorization successful!"})


# Run the app
if __name__ == "__main__":
    app.run()
