from textwrap import dedent

import openai

from forge.sdk.abilities.code.radon_workbench import get_code_metrics, fix_code

test_code = """# Feature: Adaptive Task Generation
# Scenario: Evaluate System Performance

# Given a system that generates tasks based on a loop
def generate_tasks():
    while True:
        # Task generation logic goes here
        task = generate_task()
        execute_task(task)

# Generating Task 1
def generate_task():
    task = {
        "Difficulty": "Easy",
        "Type": "String Manipulation"
    }
    return task

# Executing Task
def execute_task(task):
    # Code to execute the task goes here

# Feature: Adaptive System Update
# Scenario: Evaluate System Performance

# 1. Implement a Task Queue
class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

# Architecture

# User Interface for Task Execution
# Welcome Screen
# The first screen will display a welcome message and a brief description
def display_welcome_screen():
    print("Welcome to the Task Execution Interface!")
    print("Please select an option:")
    # Options go here

# Interactive Code Simulations
# Allow users to input their own code and see the results in real-time simulations.
def simulate_code_execution():
    code = input("Enter your Python code: ")
    # Code execution logic goes here

# Algorithm for evaluating Python code against a given task's requirements
# Start the program
# Take input from the user
# Evaluate the input against the task's requirements
# Display the evaluation result (pass or fail)
def evaluate_code(code, task_requirements):
    # Evaluation logic goes here
    if code_meets_requirements(code, task_requirements):
        print("Pass")
    else:
        print("Fail")

# Input Interface
# The first component of the system is the user input interface
def get_user_input():
    code = input("Enter your Python code: ")
    task_description = input("Enter the task description: ")
    return code, task_description

# Task Execution Interface
# Welcome message, with a brief description
# Task List
# Create New Task
# View Existing Tasks
# Run Task

# Algorithm: Evaluating Python code against given task requirements
# Input: Python code, task requirements
# Output: Evaluation result (pass or fail)
def evaluate_code(code, task_requirements):
    # Evaluation logic goes here
    if code_meets_requirements(code, task_requirements):
        return "Pass"
    else:
        return "Fail"

# User Interface for Task Execution
# Task List
# Create New Task
# View Existing Tasks
# Run Task

# Input Interface
# The first component of the system is the user input interface.
def get_user_input():
    code = input("Enter your Python code: ")
    task_description = input("Enter the task description: ")
    return code, task_description

# Feature: Adaptive System Update
# Scenario: Evaluate and Update based on user feedback
# Given the system receives user feedback

# 1. Use a state machine
# Implement a state machine that has a "task generation" state and a "task execution" state
class StateMachine:
    def __init__(self):
        self.state = "task_generation"

    def run(self):
        while True:
            if self.state == "task_generation":
                task = generate_task()
                execute_task(task)
                self.state = "task_execution"
            elif self.state == "task_execution":
                code = input("Enter your Python code: ")
                task_requirements = input("Enter the task requirements: ")
                evaluation_result = evaluate_code(code, task_requirements)
                # Update system based on evaluation result goes here
                self.state = "task_generation"


# Architecture
# The architecture of a closed-loop system for Python coding tasks would consist of multiple components
# User Interface
# Task List
# Find a Bug
# Optimize Code
# Write Unit Tests
# Display Metrics
# Implement a feedback loop
def main():
    while True:
        display_task_list()
        option = input("Select an option: ")
        if option == "1":
            find_a_bug()
        elif option == "2":
            optimize_code()
        elif option == "3":
            write_unit_tests()
        elif option == "4":
            display_metrics()
        else:
            break

if __name__ == "__main__":
    main()
    """


def main():
    glossary = dedent(
        """### Glossary

    #### SPR-Related Terms

    1. **Sparse Priming Representation (SPR)**: A token-efficient form of information designed to activate specific areas of an LLM's latent space for desired behaviors or responses.

    2. **Latent Space**: The internal multi-dimensional space in neural networks, including LLMs, that can be activated by priming for specific behaviors.

    3. **Priming**: The use of concise, meaningful inputs to guide the model's behavior in a desired direction.

    4. **Token-Efficiency**: The measure of how many tokens are used to convey a complex concept, with fewer tokens being more efficient.

    5. **Metadata**: Information stored alongside primary data, like an SPR in a KG node, that offers contextual or descriptive clarification.

    #### LLM-Related Terms

    1. **Large Language Models (LLMs)**: Deep neural networks capable of various text-based tasks, whose behavior can be modified by SPRs.

    2. **In-Context Learning**: The process of guiding an LLM's behavior or teaching it new concepts through the immediate conversational context.

    3. **Associative Learning**: The model's ability to relate different pieces of information in its responses, activated effectively by SPRs.

    #### Techniques

    1. **Decompression/Enhancement**: The act of expanding an SPR into a more detailed and nuanced form for human understanding.

    2. **Conceptual Compression**: The technique of reducing complex ideas into simpler, token-efficient forms without losing their essential meaning.
    """
    )

    # Generate SPR
    def generate_spr(text):
        fixed_code = fix_code(text)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct-0914",
            prompt=dedent(
                f"""
            MISSION: Generate an SPR (Sparse Priming Representation) for the following Python code, 
            including important import statements. SPR is a compressed, token-efficient representation of the code that 
            captures its essence and functionality. It's used to efficiently convey complex code structures to language 
            models, enabling them to understand the code without seeing it entirely.
            THEORY: Use the latent abilities of LLMs to store a vast amount of information in a compressed format. The 
            SPR should be designed so that another model can decompress it back into the original code, including necessary imports.
            IMPORTS: Make sure to include essential import statements in the SPR and ensure they are utilized in the decompressed code.
            METHODOLOGY: Capture the core logic, variables, and flow of the Python code in as few words as possible. Maintain fidelity to the original code, including essential import statements.
            
            {glossary}

            Input Python Code:
            ```python
            {fixed_code}
            ```
            
            Output SPR:
            ```text\n"""
            ),
            max_tokens=500,
        )
        return response.choices[0].text.strip()

    # Decompress SPR
    def decompress_spr(spr):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct-0914",
            prompt=dedent(
                f"""
                MISSION: Decompress the SPR back into Python code and match its complexity as indicated by the provided metrics. SPR (Sparse Priming Representation) is a compressed version of the code, and your task is to reconstruct it faithfully.
                THEORY: Utilize latent abilities to interpret the SPR and generate code that closely aligns with the original in terms of complexity and functionality.
                
                Input SPR:
                {spr}
                
                {glossary}
                
                Do not use pass or print. All functions were implemented in the original code. 
                Make sure to reimplement them in the decompressed code.
                ```python\n"""
            ),
            max_tokens=500,
        )
        return response.choices[0].text.strip()

    # Test with example Python code for calculating factorial
    example_code = test_code

    # print(f"Original Python Code:\n{example_code}")

    spr = generate_spr(example_code)
    print(f"\nGenerated SPR:\n{spr}")

    decompressed_code = decompress_spr(spr)
    print(f"\nDecompressed Python Code:\n{decompressed_code}")

    open("test.py", "w").write(fix_code(decompressed_code))


if __name__ == "__main__":
    main()
