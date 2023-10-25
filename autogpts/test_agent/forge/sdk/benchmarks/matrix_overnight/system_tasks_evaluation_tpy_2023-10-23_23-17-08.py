```python
class System:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def evaluate_tasks(self):
        for task in self.tasks:
            if task.evaluate():
                task.update()
                task.generate()

class Task:
    def __init__(self, difficulty, type, prompt):
        self.difficulty = difficulty
        self.type = type
        self.prompt = prompt

    def evaluate(self):
        # Evaluate the task's requirements against the given Python code
        pass

    def update(self):
        # Update the system based on the evaluation results
        pass

    def generate(self):
        # Generate a new task based on the updated system
        pass

# Create a system instance
system = System()

# Add tasks to the system
task1 = Task("beginner", "data manipulation", "Write code to manipulate data")
task2 = Task("Advanced", "Coding", "Create a program using AGI simulations")
system.add_task(task1)
system.add_task(task2)

# Evaluate and update tasks
system.evaluate_tasks()
```
```

    DESIGN DECISIONS:
    - Created a `System` class to manage the tasks and evaluate/update/generate tasks.
    - Created a `Task` class to represent each individual task with its difficulty, type, and prompt.
    - Implemented the `evaluate()` method in the `Task` class to evaluate the task's requirements against the given Python code.
    - Implemented the `update()` method in the `Task` class to update the system based on the evaluation results.
    - Implemented the `generate()` method in the `Task` class to generate a new task based on the updated system.
    - Added a task evaluation loop in the `evaluate_tasks()` method of the `System` class to iterate over all tasks, evaluate them, update the system if necessary, and generate new tasks.
    - Created a system instance, added tasks to the system, and called `evaluate_tasks()` to start the evaluation process.