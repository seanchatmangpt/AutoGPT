```python
# Module: state_machine.py

class StateMachine:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def execute(self):
        while True:
            self.state.run()
            self.state = self.state.next_state()

# Module: task_submission_system.py

class TaskSubmissionSystem:
    def __init__(self):
        self.task_generator = TaskGenerator()
        self.state_machine = StateMachine()
        self.state_machine.set_state(self.task_generator)

    def run(self):
        self.state_machine.execute()

# Module: task_generator.py

class TaskGenerator:
    def run(self):
        # Generate tasks
    
    def next_state(self):
        return self

# Module: code_execution_feature.py

class CodeExecutionFeature:
    def run(self):
        # Execute code
    
    def next_state(self):
        return self

# Module: metrics_feature.py

class MetricsFeature:
    def run(self):
        # Collect and report metrics
    
    def next_state(self):
        return self

# Module: interactive_coding_challenges.py

class InteractiveCodingChallenges:
    def run(self):
        # Implement interactive coding challenges
    
    def next_state(self):
        return self

# Module: task_submission_system.py

if __name__ == "__main__":
    task_submission_system = TaskSubmissionSystem()
    task_submission_system.run()
```

# Tests have been written to a different file: