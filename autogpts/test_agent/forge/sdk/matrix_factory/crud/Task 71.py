# Define a function to check user permissions
def check_permissions(user):
    # Check if user is an admin
    if user.is_admin:
        # If user is an admin, print a message
        print("User has admin permissions.")
    else:
        # If user is not an admin, print a message
        print("User does not have admin permissions.")


# Create a user object with admin permissions
user1 = User(is_admin=True)

# Call the check_permissions function with the user object
check_permissions(user1)

# Output: User has admin permissions.
