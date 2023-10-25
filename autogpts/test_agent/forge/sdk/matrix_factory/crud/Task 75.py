# Import the necessary modules
from collections import defaultdict
from datetime import datetime


# Define a function to track user activity
def track_activity(user, activity):
    # Get the current date and time
    now = datetime.now()
    # Create a defaultdict to store the user's activities
    user_activities = defaultdict(list)
    # Add the current activity to the user's list of activities
    user_activities[user].append(activity)
    # Print a message confirming the activity was tracked
    print(f"Activity '{activity}' tracked for user '{user}' at {now}")
    # Return the updated user_activities dictionary
    return user_activities


# Test the function
user_activities = track_activity("John", "logged in")
user_activities = track_activity("John", "viewed profile")
user_activities = track_activity("Jane", "logged in")
user_activities = track_activity("Jane", "posted a comment")

# Print the user_activities dictionary
print(user_activities)
