# Import the Flask library
import flask

# Create a new Flask application
app = flask.Flask(__name__)


# Define a route for the home page
@app.route("/")
def home():
    return "Hello, world!"


# Run the application
if __name__ == "__main__":
    app.run()
