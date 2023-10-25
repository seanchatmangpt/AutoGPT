from functools import wraps
from functools import wraps


def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = f(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = f(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = f(*args, **kwargs)
        print("After function call")
        return result

    return wrapper
