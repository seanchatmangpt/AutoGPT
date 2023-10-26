import ast
import time

# Here is your PerfectPythonProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION of your requirements.

from dataclasses import dataclass

import pyperclip

from forge.sdk.typetemp.template.typed_template import TypedTemplate
from forge.sdk.utils.complete import acreate
from forge.sdk.utils.models import best_models


# Function to extract a dictionary from a given string
def extract_dictionary(input_str: str) -> dict:
    start_pos = input_str.find("{")
    if start_pos == -1:
        raise ValueError("No dictionary found in the input string.")
    dict_str = input_str[start_pos:]
    return ast.literal_eval(dict_str + "}")


async def generate_template_with_model(model, template_class, prompt):
    """
    Asynchronously generates content for a template using a specific model.

    Parameters:
    - model (str): The model to use for generation.
    - template_class (TypedTemplate): The template class to be filled.
    - prompt (str): The prompt for the model.

    Returns:
    - tuple: A tuple containing the model name, template class, and the rendered template content.
    """
    try:
        # Here, you'd call the model (this is a placeholder; replace it with the actual API call)
        result = await acreate(
            model=model, prompt=prompt, temperature=0.0, max_tokens=1000, stop=["}"]
        )
        # logger.info(
        #     f"Model: {model} | Template: {template_class.__name__} | Result: {result}"
        # )
        kwargs = extract_dictionary(result)
        rendered_template = template_class(**kwargs)()
        return model, template_class, rendered_template
    except Exception as e:
        return model, template_class, None


async def main():
    """
    Asynchronous main function to run the templates with models in a round-robin manner.
    """
    start = time.time()
    tasks = []
    model_count = len(best_models)
    project_prompt = """
    1. Refine my six item list spend a dedicated amount of time really figuring out what the most important things 
    to do are.

2. I need to scale my template generation process. Everything can be done using Jinjat lists which cut down on the 
amount of wasted tokens or tuples. The challenge is sorting the relevant important of all of my theories. I can just work backwards in time to start.

3. The ideas that come to mind are filename generators. Read me, working backwards press Release Agent conversation, 
Typed Templates and Prompts, DDD classes and functions.

4. Take a list of template requests and generate templates using models (I have to frost the GPT> Everything in me 
wants to be strategic and use chat GPT. A workflow may need to take a list and apply the same task or workflow to it. 
I needsome kind of quick creation, review, update, quit, alb, try/attempt, etc patterns of prompt execution. 
These can be represented by workflows/FSM.5. Workflow/FSM generation, First loop: 2 Models gun, 3 compares 
and improves. Do this 3 times. This can then be parameterized. I need to have faith that I can scale my text 
production.6. The most efficient way to do this is to take this text and plan with GPT 4 how to implement. 
I have to get my code through the sean chatman development cycle: Ideation, prototype, CLI, 
Full stack Tracer Bullet, MVP, Version one, Enterprise. I can generate the Jinja templates, tasks, 
workflows, code, deployment, marketing, and sales text required for everything."""  # pyperclip.paste()

    project_prompt = await acreate(
        prompt=f"{project_prompt}\n\nPlease convert this into a "
        f"Enterprise Project PRD:\n\n"
        f"# Project Requirements Document for ",
        max_tokens=500,
    )

    for idx, template_class in enumerate(README_templates):
        model = best_models[idx % model_count]  # Round-robin model assignment
        prompt = construct_prompt_for_model(
            template_class, base_prompt=project_prompt
        )  # Adjust the base_prompt as needed
        tasks.append(generate_template_with_model(model, template_class, prompt))

    results = await asyncio.gather(*tasks)

    # You can process the results, e.g., save them to files or aggregate them into a single README
    for model, template_class, content in results:
        print(content)
        if content:
            with open(f"README_{start}.md", "a+") as f:
                f.write(content)

    end = time.time()
    # logger.info(f"Total time taken: {end - start} seconds")


# Function to construct a detailed prompt for models
def construct_prompt_for_model(template_class, base_prompt):
    docstring = template_class.__doc__

    # Extract class attributes and types
    attributes = [
        (attr, typ.__name__) for attr, typ in template_class.__annotations__.items()
    ]
    attributes_info = "\n".join([f"- {attr}:  {typ}" for attr, typ in attributes])
    # {attributes_info}

    # For
    # example:
    # {{{{'key1': 'value1', 'key2': 'value2', ...}}}}
    detailed_instruction = f"""
Objective:
Generate a Python dictionary to populate the given Jinja template based on the information provided.

Details:
- The response should STRICTLY be a Python dictionary.
- The dictionary should have the following keys and types:
{attributes_info}

Please adhere to the structure and types. Ensure the response is ONLY the dictionary without additional text or explanations.
"""

    return f"{base_prompt}\n\n{detailed_instruction}\n\n{docstring}"


# Project Title Jinja Template
project_title_template = """
# {{ project_title }}

{{ project_description }}
"""

# API Reference Jinja Templates
api_reference_template = """
## API Reference
"""

get_all_items_template = """
#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
"""

get_item_template = """
#### Get item

```http
  GET /api/items/${{ id }}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |
"""

add_function_template = """
#### add(num1, num2)

Takes two numbers and returns the sum.
"""

# Appendix Jinja Template
appendix_template = """
## Appendix

{{ additional_information }}
"""

# Deployment Jinja Template
deployment_template = """
## Deployment

To deploy this project run

```bash
  {{ deployment_command }}
```
"""

# Documentation Jinja Template
documentation_template = """
## Documentation

[Documentation]({{ documentation_link }})
"""

# Environment Variables Jinja Template
environment_variables_template = """
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

{{ environment_variables }}
"""

# FAQ Jinja Template
faq_template = """
## FAQ

{% for question, answer in faq.items() %}
#### {{ question }}

{{ answer }}
{% endfor %}
"""

# Features Jinja Template
features_template = """
## Features

{% for feature in features %}
- {{ feature }}
{% endfor %}
"""

# Installation Jinja Template
installation_template = """
## Installation

Install {{ project_name }} with npm

```bash
  npm install {{ project_name }}
  cd {{ project_name }}
```
"""

# Lessons Learned Jinja Template
lessons_learned_template = """
## Lessons Learned

{{ lessons }}
"""

# Optimizations Jinja Template
optimizations_template = """
## Optimizations

{{ optimizations }}
"""

# Roadmap Jinja Template
roadmap_template = """
## Roadmap

{% for roadmap_item in roadmap %}
- {{ roadmap_item }}
{% endfor %}
"""

# Run Locally Jinja Template
run_locally_template = """
## Run Locally

Clone the project

```bash
  git clone {{ project_link }}
```

Go to the project directory

```bash
  cd {{ project_directory }}
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```
"""

# Support Jinja Template
support_template = """
## Support

For support, email {{ email }} or join our {{ communication_channel }}.
"""

# Tech Stack Jinja Template
tech_stack_template = """
## Tech Stack

**Client:** {{ client_techs }}

**Server:** {{ server_techs }}
"""

# Running Tests Jinja Template
running_tests_template = """
## Running Tests

To run tests, run the following command

```bash
  {{ test_command }}
```
"""

# Usage/Examples Jinja Template
usage_examples_template = """
## Usage/Examples

```javascript
{{ usage_example_code }}
```
"""


@dataclass
class ProjectTitle(TypedTemplate):
    """
    Template for the project title and description.

    Attributes:
    - project_title: The main title of your enterprise project.
    - project_description: A brief overview of the project's purpose and audience.
    """

    project_title: str
    project_description: str
    source = project_title_template


@dataclass
class APIReference(TypedTemplate):
    """
    Template for the API reference section. Generally a placeholder indicating where the detailed API descriptions will be.
    """

    source = api_reference_template


@dataclass
class GetAllItems(TypedTemplate):
    """
    Template for the API endpoint that retrieves all items.

    Attributes:
    - api_key: The required API key for accessing this endpoint.
    """

    api_key: str
    source = get_all_items_template


@dataclass
class GetItem(TypedTemplate):
    """
    Template for the API endpoint to retrieve a specific item by its ID.

    Attributes:
    - id: The unique identifier for the item to be fetched.
    """

    id: str
    source = get_item_template


@dataclass
class AddFunction(TypedTemplate):
    """
    Template to describe the 'add' function which sums two numbers.
    Typically used to showcase an example or utility function in your project.
    """

    source = add_function_template


@dataclass
class Appendix(TypedTemplate):
    """
    Template for the appendix section, detailing any additional, supplementary information regarding the project.

    Attributes:
    - additional_information: Supplementary details or notes for the project.
    """

    additional_information: str
    source = appendix_template


@dataclass
class Deployment(TypedTemplate):
    """
    Template detailing how to deploy the project.

    Attributes:
    - deployment_command: The specific command used for deployment, e.g., using npm or other package managers.
    """

    deployment_command: str
    source = deployment_template


@dataclass
class Documentation(TypedTemplate):
    """
    Template pointing to external documentation for the project.

    Attributes:
    - documentation_link: A direct link to where the detailed project documentation is hosted.
    """

    documentation_link: str
    source = documentation_template


@dataclass
class EnvironmentVariables(TypedTemplate):
    """
    Template indicating necessary environment variables for the project.

    Attributes:
    - environment_variables: The list or string of environment variables essential for the project's operation.
    """

    environment_variables: str
    source = environment_variables_template


@dataclass
class FAQ(TypedTemplate):
    """
    Template for the Frequently Asked Questions (FAQ) section.

    Attributes:
    - faq: A dictionary with questions as keys and their corresponding answers as values.
    """

    faq: dict
    source = faq_template


@dataclass
class Features(TypedTemplate):
    """
    Template listing the features of the project.

    Attributes:
    - features: A list of strings, each detailing a unique feature of the project.
    """

    features: list
    source = features_template


@dataclass
class Installation(TypedTemplate):
    """
    Template detailing how to install the project for local development or use.

    Attributes:
    - project_name: The name of the project or package.
    """

    project_name: str
    source = installation_template


@dataclass
class LessonsLearned(TypedTemplate):
    """
    Template discussing lessons learned during the project's development.

    Attributes:
    - lessons: A description of challenges faced, insights gained, and overall learnings from the project.
    """

    lessons: str
    source = lessons_learned_template


@dataclass
class Optimizations(TypedTemplate):
    """
    Template detailing any optimizations made in the code, including refactors, performance improvements, or increased accessibility.

    Attributes:
    - optimizations: A description of the specific optimizations implemented in the project.
    """

    optimizations: str
    source = optimizations_template


@dataclass
class Roadmap(TypedTemplate):
    """
    Template listing future enhancements or integrations planned for the project.

    Attributes:
    - roadmap: A list of items or features planned for future releases.
    """

    roadmap: list
    source = roadmap_template


@dataclass
class RunLocally(TypedTemplate):
    """
    Template detailing steps to run the project locally, including cloning, installation, and execution.

    Attributes:
    - project_link: The URL to clone the project repository.
    - project_directory: The directory name to navigate into after cloning.
    """

    project_link: str
    project_directory: str
    source = run_locally_template


@dataclass
class Support(TypedTemplate):
    """
    Template indicating where users or developers can seek support for the project.

    Attributes:
    - email: The support email address.
    - communication_channel: Additional channels for support, such as Slack or forums.
    """

    email: str
    communication_channel: str
    source = support_template


@dataclass
class TechStack(TypedTemplate):
    """
    Template detailing the technical stack used in the project, both client-side and server-side.

    Attributes:
    - client_techs: A description or list of technologies used on the client side.
    - server_techs: A description or list of technologies used on the server side.
    """

    client_techs: str
    server_techs: str
    source = tech_stack_template


@dataclass
class RunningTests(TypedTemplate):
    """
    Template describing how to run tests for the project.

    Attributes:
    - test_command: The specific command used to execute the tests, e.g., using npm or other package managers.
    """

    test_command: str
    source = running_tests_template


@dataclass
class UsageExamples(TypedTemplate):
    """
    Template providing examples of how to use the project or its components.

    Attributes:
    - usage_example_code: Sample code showcasing how to use the project or one of its components.
    """

    usage_example_code: str
    source = usage_examples_template


README_templates = [
    ProjectTitle,  # The class name you'll use for the main title of your README
    APIReference,  # The template for your API reference
    GetAllItems,  # The template for the "Get all items" API endpoint
    GetItem,  # The template for the "Get item by ID" API endpoint
    AddFunction,  # The template for your "add" function documentation
    Appendix,  # The appendix section of your README
    Deployment,  # Instructions on how to deploy your project
    Documentation,  # Link to external documentation
    EnvironmentVariables,  # Descriptions of required environment variables
    FAQ,  # A FAQ section for your README
    Features,  # A list of features your project offers
    Installation,  # How to install and set up your project locally
    LessonsLearned,  # What you learned while building this project
    Optimizations,  # Optimizations you've made in your project
    Roadmap,  # A roadmap for future updates or features
    RunLocally,  # How to run the project locally
    Support,  # How users can get support or help
    TechStack,  # The technologies used in your project
    RunningTests,  # Instructions on how to run tests
    UsageExamples,  # Examples of how to use your project or API
]


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
