import os
from random import shuffle
from typing import Iterable, List
import anyio
import yaml
import json

from forge.sdk.utils.complete import achat
from forge.sdk.utils.create_prompts import create_python
from forge.sdk.utils.file_tools import write, read

# Include your existing 'write' and 'prompt_matrix' functions here.

from typing import List, Iterable
import anyio

from forge.sdk.utils.prompt_tools import prompt_map


async def prompt_matrix(
    x_prompts_iterable: Iterable[str],
    y_prompts_iterable: Iterable[str],
    max_tokens: int = 50,
    model_list: List[str] = None,
    temperature: float = 0.7,
) -> List[List[str]]:
    # Initialize a 2D list to store the responses.
    responses_2d = []

    async def handle_single_x_prompt(x_prompt):
        y_responses = await prompt_map(
            y_prompts_iterable,
            base_prompt=x_prompt,  # Set base_prompt to current x_prompt
            max_tokens=max_tokens,
            model_list=model_list,
            temperature=temperature,
        )
        responses_2d.append(y_responses)

    async with anyio.create_task_group() as tg:
        for x_prompt in x_prompts_iterable:
            tg.start_soon(handle_single_x_prompt, x_prompt)

    return responses_2d


async def save_prompt_matrix_to_file(
    x_prompts: Iterable[str],
    y_prompts: Iterable[str],
    max_tokens: int = 25,
    model_list: List[str] = None,
    filename: str = None,
    mode: str = "w+",
):
    # Generate the prompt matrix.
    result_matrix = await prompt_matrix(x_prompts, y_prompts, max_tokens, model_list)

    result_str = yaml.dump(result_matrix)

    # # Save the matrix to a file.
    saved_filename = await write(
        contents=result_str,
        mode=mode,
        extension="",
        time_stamp=True,
    )
    return saved_filename


# Example usage
async def main():
    x_prompts = [
        "Feature: Parse natural language task descriptions. Scenario: Given a task description, the Task Parsing Engine should convert it to actionable items.",
        "Feature: Generate initial Python code. Scenario: The Code Generation Engine should create Python source files based on the actionable items.",
        "Feature: Create Gherkin features and scenarios. Scenario: The Gherkin Feature Engine should convert actionable items into Gherkin features and scenarios.",
        "Feature: Automatically refactor code. Scenario: The Refactoring Engine should refactor the code for efficiency and coding best practices.",
        "Feature: Run automated tests and debug. Scenario: The Debugging and Test Engine should execute tests on the Python source code and debug it.",
        "Feature: Generate performance metrics and reports. Scenario: The Metrics and Reporting Engine should analyze the Python source code and generate metrics and reports.",
    ]

    y_prompts = [
        "Feature: Support multi-threading in Python code. Scenario: The system should refactor the Python code to implement multi-threading where applicable.",
        "Feature: Code versioning and Git integration. Scenario: The system should maintain code versions and optionally push changes to a Git repository.",
        "Feature: Cloud deployment automation. Scenario: The system should offer an option to automatically deploy the Python application to a specified cloud provider.",
        "Feature: Real-time code performance monitoring. Scenario: The system should monitor the performance of the Python code in real-time and offer optimizations.",
        "Feature: Code annotation and documentation. Scenario: The system should automatically add comments and documentation to the Python source code.",
        "Feature: Security vulnerability scanning. Scenario: The system should scan the Python source code for known security vulnerabilities and suggest fixes.",
        "Feature: Database schema mapping. Scenario: Given a database schema, the system should generate Python code to interact with the database.",
        "Feature: Dependency conflict resolution. Scenario: The system should resolve any dependency conflicts in the Python project.",
        "Feature: Integration with external APIs. Scenario: The system should generate code to interact with specified external APIs.",
        "Feature: Interactive debugging console. Scenario: The system should offer an interactive console for real-time debugging of Python code.",
    ]

    while True:
        saved_filename = await save_prompt_matrix_to_file(x_prompts, y_prompts)
        # print(f"Saved matrix to {saved_filename}")
        text = await read(filename=saved_filename)

        plan = await create_python(
            text
            + "\n\n# AGI Simulations of David Thomas, Andrew Hunt,Luciano Ramahlo. Do not use the keyword pass\n\n",
        )

        saved_plan = await write(plan, time_stamp=True, extension="py")

        print(f"Saved plan to {saved_plan}")

        await anyio.sleep(30)


async def implement_code_in_file(file_path):
    with open(file_path, "r") as f:
        lines = f.read()

    # remove the word "pass" from the lines
    lines = lines.replace("pass", "")

    # split by def keyword
    lines = lines.split("def")

    code_implementation = ""
    # for line in lines:
    #     code_implementation +=
    code_lines = [await create_python(line, max_tokens=200) for line in lines]

    with open(file_path, "w") as f:
        f.write(code_implementation)


async def main2():
    """ """
    # Loop over every .py file in the current directory
    for filename in os.listdir("."):
        if filename.endswith(".py"):
            await implement_code_in_file(filename)


# Run the main coroutine
anyio.run(main)
# anyio.run(main2)
