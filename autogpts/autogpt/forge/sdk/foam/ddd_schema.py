import inspect
from textwrap import dedent
from typing import Dict, List, Type, TypeVar, Union

import anyio
import yaml
from pydantic import BaseModel, Field

from create_primatives import create_dict, create_list, extract_list
from foam.ddd_models import *
from utils.file_tools import extract_code

# Serialize and deserialize to YAML
ddd_instance = DDD(
    aggregates=[
        Aggregate(
            root_entity="Project",
            entities=[
                Entity(
                    name="Project",
                    definition="A Project entity",
                    business_functions=[
                        BusinessFunction(
                            name="AssignDeveloper",
                            parameters=[{"parameter": "developer", "type": "Developer"}],
                            definition="Assigns a developer to the project.",
                            contract={
                                "require": [
                                    Require(condition="lambda developer: developer is not None")
                                ],
                                "ensure": [Ensure(condition="lambda result: result is not None")],
                            },
                        )
                    ],
                    factories=[
                        Factory(
                            name="CreateProject",
                            parameters=[{"parameter": "name", "type": "string"}],
                        )
                    ],
                    repositories=[
                        Repository(
                            name="ProjectRepository",
                            methods=[
                                {
                                    "name": "find_by_name",
                                    "parameters": [{"parameter": "name", "type": "string"}],
                                }
                            ],
                        )
                    ],
                )
            ],
            value_objects=[
                ValueObject(
                    name="Task",
                    definition="A Task value object",
                    properties=[
                        {"name": "title", "type": "string"},
                        {"name": "description", "type": "string"},
                    ],
                )
            ],
            aggregate_business_functions=[
                BusinessFunction(
                    name="MoveTaskToProject",
                    parameters=[
                        {"parameter": "task", "type": "Task"},
                        {"parameter": "project", "type": "Project"},
                    ],
                    definition="Moves a task to a different project.",
                    contract={
                        "require": [
                            Require(
                                condition="lambda task, project: task is not None and project is not None"
                            )
                        ],
                        "ensure": [Ensure(condition="lambda result: result is True")],
                    },
                )
            ],
        )
    ]
)
# Serialize to YAML
# print(ddd_instance.to_yaml("ddd.yaml"))


# # Add a pre-condition to check the type of the 'prompt' variable
# @require(lambda prompt: isinstance(prompt, str))
# # Add a post-condition to check the type of the result and ensure that the dictionary meets constraints
# @ensure(
#     lambda result, min_len, max_len: isinstance(result, dict)
#     and all(isinstance(key, str) for key in result.keys())
#     and all(isinstance(value, str) for value in result.values())
#     and min_len <= len(result) <= max_len,
#     "Dictionary size must be within min_len and max_len, and all keys and values must be strings.",
# )
# async def create_vo(prompt, min_len=1, max_len=20, **kwargs) -> dict:
#     # Explicit instructions without line breaks within the dictionary
#     instructions = dedent(
#         f"""Create a Python dictionary where both keys and values are strings.
#                               The dictionary should be based on the prompt: '{prompt}'.
#                               The dictionary should have a minimum size of {min_len} and a maximum size of {max_len}.
#                               It should be formatted according to PEP8 guidelines with no line breaks within the dictionary.
#                               Please complete the following code block:
#                               ```python
#                               from typing import Dict
#                               perfect_str_dict: Dict[str, str] = {{"""
#     )
#
#     result = await acreate(
#         prompt=instructions,
#         stop=["```", "\n\n"],
#         max_tokens=2000,
#         **kwargs,
#     )
#
#     try:
#         # Extract the dictionary and validate its keys and values are strings
#         extracted_dict = extract_dict("{" + result.replace("\n", ""))
#         return extracted_dict
#     except (ValueError, SyntaxError) as e:
#         loguru.logger.warning(f"Invalid dictionary generated: {e} {result}")
#
#         # Prompt to fix the invalid dictionary with explicit constraints
#         fix_instructions = dedent(
#             f"""The dictionary generated earlier did not meet the specified requirements due to the following error: {e}.
#                                       Please correct the dictionary format, ensuring all keys and values are strings and adhere to PEP8 guidelines.
#                                       The dictionary should also meet the size constraints: a minimum of {min_len} and a maximum of {max_len} key-value pairs.
#                                       Complete the following code block:
#                                       ```python
#                                       perfect_str_dict: Dict[str, str] = {{"""
#         )
#
#         fixed_dict = await acreate(
#             prompt=fix_instructions,
#             stop=["```", "\n\n"],
#             max_tokens=2000,
#             **kwargs,
#         )
#         return extract_dict("{" + fixed_dict.replace("\n", ""))


import ast
from textwrap import dedent
from typing import Callable, Type, TypeVar

import anyio
import loguru
from icontract import ensure, require

from llm.complete import acreate, chat

project_description = """
Project Title: CoALA-Based Language Agent Development

Project Description:

We are seeking a talented software development team with expertise in cognitive architectures and natural language processing to build a language agent system based on the CoALA framework.

Project Objectives:

System Implementation: Develop a language agent that adheres to the CoALA framework, including the core components such as memory modules, actions (grounding, reasoning, retrieval, and learning), and decision-making.

Memory Organization: Implement multiple memory modules, including short-term working memory and long-term memories (episodic, semantic, procedural), as described in the CoALA framework.

Action Spaces: Define and structure the agent's action spaces, distinguishing between internal memory accesses and external interactions with the world, as outlined in the CoALA framework.

Grounding Actions: Create procedures for grounding actions, allowing the agent to interact with external environments (physical, dialogue with humans, digital environments) as described in CoALA.

Retrieval Actions: Implement retrieval procedures to read information from long-term memories into working memory, and explore various retrieval methods as per the CoALA framework.

Reasoning Actions: Develop reasoning procedures that enable the agent to process working memory contents, generate new knowledge, and support decision-making.

Learning Actions: Enable the agent to learn by updating long-term memory, including episodic, semantic, and procedural memory, as described in the CoALA framework.

Decision-Making: Design a robust decision-making process that allows the agent to choose actions based on evaluations, proposals, and simulations, following the CoALA decision cycle.    """


# I have IMPLEMENTED your PerfectPythonProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION code of your requirements.


def generate_prompt(project_description: str, demo_yaml: str) -> str:
    """
    Generate a chat prompt string for CoALA framework based on the project description and demo YAML schema.

    Parameters:
    - project_description (str): The description of the project.
    - demo_yaml (str): The demonstration YAML schema to be shown as an example.

    Returns:
    - str: The complete chat prompt string.
    """
    prompt_intro = (
        "You are tasked with creating a DDD YAML Schema framework based on the project description."
    )
    schema_example_intro = "To assist you, here is a sample YAML Schema for reference:"
    detailed_instruction = (
        "Please carefully adhere to the schema constraints demonstrated above, "
        "while introducing a plethora of Value Objects, Entities, etc., to craft "
        "the most robust YAML Schema possible. Make sure the YAML will pass pydantic validation for DDD Class."
    )

    prompt = (
        f"{prompt_intro}\n\n"
        f"{project_description}\n\n"
        f"{schema_example_intro}\n\n"
        f"DO NOT COPY, THIS IS ONLY FOR REFERENCE\n```yaml\n{demo_yaml}```\n\n"
        f"Pydantic models for reference:\n{open('ddd_models.py').read()}\n"
        f"Project description to turn into YAML:\n```text\n{project_description}```\n\n"
        f"{detailed_instruction}\n"
    )

    return prompt


# Example usage:
# project_description = "Your project is aimed at creating a domain-driven design (DDD) for a software development process."
# demo_yaml_content = "Your sample YAML here..."
#
# chat_prompt = generate_prompt(project_description, demo_yaml_content)
# coala_yaml = chat(prompt=chat_prompt, model="4")
#
# print(coala_yaml)
# open("coala.yaml", "w").write(coala_yaml)


async def main():
    """Build 100 value objects."""
    # vos = await create_vos()

    # print(vos)

    # for vo_name in vo_names:
    #     print(vo_name)
    #     vo = await create_value_object_names(vo_name)
    #     print(vo)
    #     vo.to_yaml(f"vo_{vo_name}.yaml")

    demo_yaml = DDD.from_yaml("ddd.yaml")
    #
    # print(demo_yaml)
    #

    coala_prompt = generate_prompt(project_description, demo_yaml.to_yaml())
    #
    # print(coala_prompt)
    # coala_yaml = chat(coala_prompt)

    #
    # print(coala_yaml)

    # open("coala.yaml", "w").write(extract_code(coala_yaml))
    # print("Wrote coala.yaml")
    # print(coala_yaml)

    coala_ddd = DDD.from_yaml("coala.yaml")
    print(coala_ddd)

    # coala_yaml =


vo_description = """
    
"""


async def create_vos():
    vo_names = await create_list(
        "You are a Value Object Class Name Creation AGI assistant. Let's think about what that means\n"
        + project_description
        + "\nYou are a Value Object Class Name Creation AGI assistant that creates excellent Value Object Class Names. "
        "Let's think about what that means in terms of PEP8 compliant class names.\n"
        + "valid PEP8 Class Names. Validate your list meets all requirements before responding:\n",
        min_len=15,
        max_len=40,
    )
    print(vo_names)
    vos = []
    for vo_name in vo_names[:3]:
        source_code = inspect.getsource(ValueObject)

        vo_yaml = ValueObject(
            name="Task",
            definition="A Task value object",
            properties=[
                {"name": "title", "type": "string"},
                {"name": "description", "type": "string"},
            ],
        ).to_yaml()

        vo_dict = await create_dict(
            f"Example:\n{vo_yaml}\nDO NOT REPEAT EXAMPLE, come up with new names\nValue Object {vo_name}\n\n{source_code}\n",
            min_len=3,
            max_len=6,
        )
        vos.append(ValueObject(**vo_dict))
    return vos


# vos = [ValueObject(name='CoALA_LanguageAgent', definition='A Value Object for the CoALA Language Agent', properties=[{'name': 'language', 'type': 'string'}, {'name': 'agent_type', 'type': 'string'}, {'name': 'version', 'type': 'string'}]), ValueObject(name='MemoryModule', definition='A Value Object MemoryModule', properties=[{'name': 'title', 'type': 'string'}, {'name': 'description', 'type': 'string'}]), ValueObject(name='ShortTermMemory', definition='A Value Object that stores short term memories', properties=[{'name': 'memory', 'type': 'string'}, {'name': 'emotion', 'type': 'string'}, {'name': 'time', 'type': 'string'}])]

if __name__ == "__main__":
    anyio.run(main)
