# Import the necessary modules
from flask import Flask
from flask import render_template

# Create the Flask app
app = Flask(__name__)


# Define the route for the homepage
@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")


# Define the route for the React app
@app.route("/react")
def react():
    # Render the react.html template
    return render_template("react.html")


# Run the app
if __name__ == "__main__":
    app.run()
