# Import the necessary modules
import random
import string


# Define the function to generate a random string
def generate_random_string(length):
    # Use the string module to generate a random string of lowercase letters
    letters = string.ascii_lowercase
    # Use the random module to select a random character from the letters string
    random_string = "".join(random.choice(letters) for i in range(length))
    # Return the random string
    return random_string


# Define the function to shard the database
def shard_database(num_shards):
    # Create an empty dictionary to store the shards
    shards = {}
    # Use a for loop to generate the specified number of shards
    for i in range(num_shards):
        # Generate a random string to use as the shard name
        shard_name = generate_random_string(10)
        # Add the shard name as a key in the dictionary and assign an empty list as the value
        shards[shard_name] = []
    # Return the dictionary of shards
    return shards


# Call the function to shard the database with 5 shards
shards = shard_database(5)

# Print the dictionary of shards
print(shards)
