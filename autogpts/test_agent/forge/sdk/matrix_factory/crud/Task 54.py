# Import the necessary modules
from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)


# Define the route for the user profile page
@app.route("/profile/<username>")
def profile(username):
    # Create a dictionary with user information
    user = {
        "username": username,
        "first_name": "John",
        "last_name": "Doe",
        "age": 25,
        "location": "New York City",
    }
    # Render the template with the user information
    return render_template("profile.html", user=user)


# Run the application
if __name__ == "__main__":
    app.run()
