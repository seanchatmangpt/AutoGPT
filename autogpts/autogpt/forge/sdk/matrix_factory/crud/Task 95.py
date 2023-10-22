# Import the necessary modules
from flask import Flask, session, redirect, url_for, escape, request

# Create the Flask app
app = Flask(__name__)

# Set the secret key for the session
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Define a route for the home page
@app.route('/')
def index():
    # Check if the user is logged in
    if 'username' in session:
        # Display a personalized greeting
        return 'Logged in as %s' % escape(session['username'])
    # If not logged in, redirect to the login page
    return redirect(url_for('login'))

# Define a route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the username from the form
        username = request.form['username']
        # Set the username in the session
        session['username'] = username
        # Redirect to the home page
        return redirect(url_for('index'))
    # If request method is GET, display the login form
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

# Define a route for the logout page
@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)
    # Redirect to the home page
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run()