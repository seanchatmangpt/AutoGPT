# Import the necessary modules
import time
import random


# Define the load testing function
def load_test(url, num_requests):
    # Start the timer
    start = time.time()

    # Send the specified number of requests to the given URL
    for _ in range(num_requests):
        response = requests.get(url)

    # Calculate the total time taken
    end = time.time()
    total_time = end - start

    # Print the results
    print(f"Total time taken: {total_time} seconds")
    print(f"Average time per request: {total_time/num_requests} seconds")


# Set the URL and number of requests
url = "https://www.example.com"
num_requests = 100

# Call the load testing function
load_test(url, num_requests)
