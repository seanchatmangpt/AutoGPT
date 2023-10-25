# Import the necessary modules
import time
import random


# Define a function to test performance
def test_performance():
    # Start the timer
    start = time.time()

    # Generate a list of random numbers
    numbers = [random.randint(1, 100) for i in range(1000000)]

    # Sort the list
    numbers.sort()

    # End the timer
    end = time.time()

    # Calculate the elapsed time
    elapsed = end - start

    # Print the result
    print("Elapsed time: {} seconds".format(elapsed))


# Call the function
test_performance()
