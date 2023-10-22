# Import the necessary modules
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

# Create the Flask app
app = Flask(__name__)

# Create an instance of HTTPBasicAuth
auth = HTTPBasicAuth()

# Define a dictionary of users and their passwords
users = {
    'john': 'secret',
    'susan': 'password'
}

# Create a function to verify the user's credentials
@auth.verify_password
def verify_password(username, password):
    # Check if the username exists in the dictionary
    if username in users:
        # Check if the password matches the one in the dictionary
        if password == users[username]:
            return True
    return False

# Create a route for the login page
@app.route('/login')
@auth.login_required
def login():
    # Return a message indicating successful login
    return jsonify({'message': 'You are now logged in'})

# Run the app
if __name__ == '__main__':
    app.run()