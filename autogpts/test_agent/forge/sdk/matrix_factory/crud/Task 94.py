# Import the necessary modules
import uuid
import datetime

# Define the UserSession class
class UserSession:
    # Initialize the class with a unique session ID and current timestamp
    def __init__(self):
        self.session_id = uuid.uuid4()
        self.timestamp = datetime.datetime.now()

    # Method to update the session timestamp
    def update_timestamp(self):
        self.timestamp = datetime.datetime.now()

# Create a dictionary to store user sessions
user_sessions = {}

# Function to create a new user session and add it to the dictionary
def create_session():
    # Create a new instance of the UserSession class
    session = UserSession()
    # Add the session to the dictionary with the session ID as the key
    user_sessions[session.session_id] = session
    # Return the session ID for reference
    return session.session_id

# Function to check if a session is still active
def is_session_active(session_id):
    # Check if the session ID exists in the dictionary
    if session_id in user_sessions:
        # Update the session timestamp
        user_sessions[session_id].update_timestamp()
        # Return True to indicate the session is still active
        return True
    else:
        # Return False if the session ID does not exist
        return False

# Function to end a user session
def end_session(session_id):
    # Check if the session ID exists in the dictionary
    if session_id in user_sessions:
        # Delete the session from the dictionary
        del user_sessions[session_id]
        # Return True to indicate the session was successfully ended
        return True
    else:
        # Return False if the session ID does not exist
        return False

# Example usage:
# Create a new session
session_id = create_session()
# Check if the session is still active
print(is_session_active(session_id))
# End the session
end_session(session_id)
# Check if the session is still active
print(is_session_active(session_id))