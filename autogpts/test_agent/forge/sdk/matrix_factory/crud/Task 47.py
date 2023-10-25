# Import the necessary modules
from collections import defaultdict


# Define the Feedback class
class Feedback:
    # Initialize the class with an empty dictionary
    def __init__(self):
        self._feedback = defaultdict(list)

    # Add a new feedback to the dictionary
    def add_feedback(self, user, feedback):
        self._feedback[user].append(feedback)

    # Get all feedback for a specific user
    def get_feedback(self, user):
        return self._feedback[user]

    # Get all feedback for all users
    def get_all_feedback(self):
        return self._feedback


# Create an instance of the Feedback class
feedback = Feedback()

# Add some feedback to the system
feedback.add_feedback("John", "The app is easy to use.")
feedback.add_feedback("John", "I love the new feature.")
feedback.add_feedback("Jane", "The app is too slow.")

# Get all feedback for John
print(feedback.get_feedback("John"))

# Get all feedback for all users
print(feedback.get_all_feedback())
