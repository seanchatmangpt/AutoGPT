# Import the `lru_cache` decorator from the `functools` module
from functools import lru_cache


# Define a function that uses the `lru_cache` decorator to cache its results
@lru_cache()
def test_caching():
    # Perform some expensive computation here
    result = 1 + 2 + 3 + 4 + 5
    return result


# Call the function and print the result
print(test_caching())
