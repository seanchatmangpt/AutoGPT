import time
from functools import wraps

def performance_monitoring(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start} seconds to execute.")
        return result
    return wrapper

@performance_monitoring
def my_function():
    # code to be monitored
    pass

my_function() # prints "Function my_function took x seconds to execute."