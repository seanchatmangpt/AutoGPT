"""
This is a dictionary with two keys, and each key has a list as value.
"""
simulations = {
    "metrics": ["code complexity", "code coverage", "code quality"],
    "reports": [
        "execution time",
        "memory usage",
        "performance bottlenecks",
        "areas for optimization",
        "lines of code",
        "cyclomatic complexity",
        "code coverage",
    ],
}

"""
This function takes in a dictionary and returns a list of all values.
"""


def get_values(dictionary):
    return [value for values in dictionary.values() for value in values]


"""
This is a dictionary with two keys, and each key has a list as value.
"""
continuous_integration = {
    "testing": ["automated tests", "continuous integration"],
    "reports": ["execution time", "memory usage", "code coverage"],
}

"""
This is a dictionary with three keys, and each key has a list as value.
"""
code_analysis = {
    "suggestions": ["code readability", "code maintainability", "code improvements"],
    "update": ["affected code", "refactored code"],
    "standards": ["industry standards", "common coding mistakes"],
}

"""
This is a dictionary with two keys, and each key has a list as value.
"""
project_management = {
    "tools": ["project management tools"],
    "info": ["task type", "due date", "priority level", "requirements"],
}

"""
This is a dictionary with three keys, and each key has a list as value.
"""
user_authentication = {
    "actions": ["register", "login", "access account"],
    "user": ["register", "login", "access account"],
    "authentication": ["proper authentication"],
}
