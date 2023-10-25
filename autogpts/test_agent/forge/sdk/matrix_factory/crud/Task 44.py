# Import the functools module
import functools


# Define a decorator function to cache the results of a function
def cache(func):
    # Create a dictionary to store the cached results
    cache = {}

    # Define a wrapper function that checks if the result is already cached
    # If not, it calls the original function and stores the result in the cache
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key for the cache using the function name and arguments
        key = (func.__name__, args, frozenset(kwargs.items()))

        # Check if the result is already cached
        if key not in cache:
            # Call the original function and store the result in the cache
            cache[key] = func(*args, **kwargs)

        # Return the cached result
        return cache[key]

    # Return the wrapper function
    return wrapper


# Define a function to be cached
@cache
def expensive_function(x, y):
    # Perform some expensive calculations
    result = x**y

    # Return the result
    return result


# Call the expensive function with the same arguments multiple times
expensive_function(2, 3)
expensive_function(2, 3)
expensive_function(2, 3)

# The result will be retrieved from the cache instead of recalculating it
# This improves performance and avoids unnecessary calculations
