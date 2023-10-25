```python
import random

def evaluate_code(code, requirements):
    # Evaluate the code against the requirements
    if code == requirements:
        return True
    else:
        return False

def generate_task():
    # Generate a new task
    tasks = [
        {
            "prompt": "Write a function that takes in two numbers and returns their sum.",
            "difficulty": "Beginner"
        },
        {
            "prompt": "Calculate the average of a list of numbers",
            "difficulty": "Basic"
        },
        {
            "prompt": "Implementing the Fibonacci sequence",
            "difficulty": "Intermediate"
        }
    ]
    return random.choice(tasks)
```

The above code includes two functions. The `evaluate_code` function takes in a piece of code and the task requirements, and returns `True` if the code meets the requirements, and `False` otherwise. The `generate_task` function randomly selects a task from a list of tasks and returns it. These functions can be used to manage the state of the system and ensure continuous looping back to task generation after each cycle.

Please note that this code has been generated based on the given input and may require additional modifications to meet your specific needs.
```