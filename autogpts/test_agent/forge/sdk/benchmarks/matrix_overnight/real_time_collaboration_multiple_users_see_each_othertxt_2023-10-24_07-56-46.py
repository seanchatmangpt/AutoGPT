# Feature: Real-time collaboration. Scenario: Multiple users should be able to
# work on the same task simultaneously and see each other''s

from collections import defaultdict

# use defaultdict to create a dictionary that can handle multiple values for the same key
users = defaultdict(list)


# function to add a user to the task
def add_user(task, user):
    users[task].append(user)


# function to remove a user from the task
def remove_user(task, user):
    users[task].remove(user)


# function to display users working on a task
def display_users(task):
    print("Users working on task '{}':".format(task))
    for user in users[task]:
        print(user)


# example usage
add_user("create website", "John")
add_user("create website", "Jane")
display_users("create website")
remove_user("create website", "Jane")
display_users("create website")
