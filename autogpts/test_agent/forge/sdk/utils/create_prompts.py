import ast
from textwrap import dedent

import anyio
import inflection
import loguru
from icontract import require, ensure

from forge.sdk.typetemp.template.typed_template import TypedTemplate
from .create_primatives import create_list
from .complete import achat, acreate
from .models import get_model
from .file_tools import extract_code, write


async def create_domain_model_from_yaml(
    prompt, max_tokens=2500, model="gpt4", filepath=None
):
    model = get_model(model)

    prompt = dedent(prompt)

    yaml_prompt = dedent(
        f"""
    Objective:
    Craft a robust, Pythonic, non-anemic domain model rooted in YAML formatted input. The model should fuse the Pythonic 
    principles of Luciano Ramalho, the Domain-Driven Design precepts of Vaughn Vernon, and the pragmatic wisdom of 
    Andrew Hunt and David Thomas. Verify that none of the Sample Input is included in your response.

    Key Principles:
    - Fluent Interfaces: Employ fluent interfaces for method chaining and immutability.
    - Design by Contract: Use 'require' and 'ensure' to define contracts for methods.
    - DRY Principle: Avoid repetitive code to improve maintainability.
    - Pythonic: Aim for readability and elegance in the Pythonic sense.

    Sample Input:
    ```yaml
    OnlineContractAdminCapability:
      overview_description: "Welcome to Contract Administration."
      features:
        - "Dashboard with Metrics"
        - "Interactive Query Tool"
    ```

    Template:
    ```python
    from dataclasses import dataclass, field
    from typing import List
    from icontract import require, ensure

    @dataclass
    class Contract:
        contract_id: str
        contract_name: str
        metrics: List[ContractMetric]  # Assume ContractMetric is defined elsewhere
        approval_rates: List[ApprovalRate]  # Assume ApprovalRate is defined elsewhere
        pending_reviews: List[PendingReview]  # Assume PendingReview is defined elsewhere
        health_monitor: HealthMonitor  # Assume HealthMonitor is defined elsewhere
        is_active: bool = field(default=True)
        has_been_approved: bool = field(default=False)

        @ensure(lambda result: result is not None and all(isinstance(x, ContractMetric) for x in result), "Must return a list of ContractMetric objects.")
        def view_metrics(self):
            '''
            Design by Contract Principle: The postcondition ensures that we return metrics that have valid data.
            Pythonic Idiom: Leverage list comprehensions to elegantly filter metrics.

            # Luciano's take on implementation:
            filtered_metrics = [m for m in self.metrics if m.is_relevant()]
            if not filtered_metrics:
                raise ValueError("No relevant metrics found.")
            return filtered_metrics
            '''
            pass

        @require(lambda user_id: isinstance(user_id, str) and user_id.strip() != "", "User ID must be a non-empty string.")
        @ensure(lambda result: isinstance(result, bool), "Must return a boolean value.")
        def user_has_approved(self, user_id: str):
            '''
            Design by Contract Principle: Preconditions validate the user_id.
            Fluent Python: Use any() to express the idea elegantly.

            # Luciano's take on implementation:
            return any(rate.user_id == user_id and rate.is_approved for rate in self.approval_rates)
            '''
            pass

        @ensure(lambda result: not self.is_active, "Must set is_active to False.")
        def close_contract(self):
            '''
            Design by Contract Principle: Postcondition ensures the contract is no longer active.
            Fluent Python: Use simple, yet effective language constructs.

            # Luciano's take on implementation:
            self.is_active = False
            return True
            '''
            pass
    ```
    
    DO NOT REFERENCE OnlineContractAdminCapability in your code. It is only provided as an example.

    User Requirement Input:
    {prompt}
    """
    )
    return await __chat(
        prompt=yaml_prompt,
        md_type="python",
        model=model,
        max_tokens=max_tokens,
        filepath=filepath,
    )


async def create_yaml(prompt, max_tokens=2500, model=None):
    yaml_prompt = dedent(
        f"""
    Objective:
    Transform the given input (whether it's Python code, project documentation, or another form of structured data) into a YAML format.

    GIVEN INPUT:
    {prompt}

    GIVEN OUTPUT:
    """
    )
    return await __create(
        prompt=yaml_prompt, md_type="yaml", model=model, max_tokens=max_tokens
    )


create_python_template = """
Objective:
Transform the given input (whether it's Python code, project documentation, or another form of structured data) 
into PYTHON CODE that aligns with the Pythonic practices Luciano Ramalho would advocate for based on his 
teachings in "Fluent Python". Ensure it's idiomatic, concise, and leverages Python's features effectively.
Use the standard library and built-in functions unless the library is specified in the prompt.
Use functional programming without classes. Do not use the keyword pass.

You are generating answer code for a job interview question. The code should be production-ready and
ready to be deployed to a production environment.

```prompt
{{prompt}}
```

"""


async def create_python(
    prompt, max_tokens=2500, model=None, filepath=None, temperature=0.7
):
    create_prompt = TypedTemplate(source=create_python_template, prompt=prompt)()

    return await __create(
        prompt=create_prompt,
        filepath=filepath,
        md_type="python",
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
    )


__create_template = """
{{prompt}}
```{{md_type}}
# Here is your PerfectPythonProductionCode® AGI response.\n\n
"""


async def __create(
    prompt, md_type="text", max_tokens=2500, model=None, filepath=None, temperature=0.0, stop=None
):
    model = get_model(model)

    create_prompt = TypedTemplate(
        source=__create_template, prompt=prompt, md_type=md_type
    )()

    result = await acreate(
        prompt=create_prompt,
        model=model,
        stop=["```"],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    # loguru.logger.info(f"Prompt: {result}")
    # loguru.logger.info(f"Result: {result}")

    if filepath:
        await write(contents=result, filename=filepath)

    return result


async def __chat(
    prompt,
    md_type="text",
    max_tokens=2500,
    filepath=None,
    temperature=0.0,
    model="gpt4",
    **kwargs,
):
    model = get_model(model)

    prompt = dedent(
        f"""
    {prompt}
    ```{md_type}\n# Here is your PerfectPythonProductionCode® AGI response. Tests have been written to a different file:\n"""
    )
    result = await achat(prompt=prompt, model=model)
    loguru.logger.info(f"Prompt: {result}")
    loguru.logger.info(f"Result: {result}")

    if filepath:
        await write(contents=result, filename=filepath)

    return result


async def create_dict(model, prompt, **kwargs):
    question = (
        f"Generate a Python dictionary from:\n\n'{prompt}'"
        f"\n\nPlease produce the perfect Python dictionary based on the given data:\n\n"
        f"```python\nperfect_dict = {{\n"
    )
    result = await acreate(
        model=model,
        temperature=0.0,
        stop=["```"],
        prompt=question,
        **kwargs,
    )

    try:
        return extract_dictionary("{" + result)
    except ValueError:
        loguru.logger.warning(f"Invalid dictionary generated: {result}")
        fix_instructions = (
            f"Please fix the dictionary {result} ```python\nperfect_dict = {{\n"
        )
        return await acreate(
            model=model,
            temperature=0.0,
            stop=["```"],
            **kwargs,
        )


async def create_boolean(completion_function, prompt, **completion_kwargs):
    completion_prompt = f"Based on the following text, provide a boolean response ('true' or 'false'): '{prompt}'"

    result = await completion_function(prompt=completion_prompt, **completion_kwargs)
    # Convert the result to lowercase and check against "true" and "false"
    boolean_value = result.strip().lower() == "true"
    return boolean_value


def extract_dictionary(input_str: str) -> dict:
    """
    Extracts a dictionary from a given string, ignoring content before the '{' character.

    Parameters:
    - input_str (str): The input string containing the dictionary representation.

    Returns:
    - dict: The extracted dictionary.
    """
    # Find the starting position of the dictionary
    start_pos = input_str.find("{")

    # Check if '{' is not found
    if start_pos == -1:
        raise ValueError("No dictionary found in the input string.")

    # Extract the dictionary substring
    dict_str = input_str[start_pos:]

    # Safely evaluate the dictionary substring
    return ast.literal_eval(dict_str)


async def main():
    prompt = (
        "The system uses phone AI to talk to customers and answer their questions. "
    )
    "If a human is needed to answer the question, the system will transfer the "
    "customer to a human. The system will also record the conversation and "
    "transcribe it into text. The system will also send a summary of the "
    f"conversation to the manager via email."

    # \n\nThis domain model is for the {domain_model} class."

    # List of domain_model class names
    # domain_model_classes = ["CustomerService", "AITalk", "HumanTalk", "ConversationRecord", "Transcription",
    #                         "SummaryEmail"]

    domain_model_classes = await create_list(
        prompt="Generate a list of multi word domain model class names from\n\n"
        + prompt,
        min_len=5,
        max_len=7,
    )

    # Iterate over each domain_model class name
    for domain_model in domain_model_classes:
        # Replace {domain_model} placeholder with the actual class name
        class_name_prompt = f"\n\nThis domain model is for the {domain_model} class."

        create_prompt = prompt + class_name_prompt

        # Create a domain model from the yaml description
        created_model = await create_domain_model_from_yaml(create_prompt, model="gpt4")

        print(created_model)

        # Write the created domain model to a .py file
        await write(
            contents=extract_code(created_model),
            filename=f"phone_system/{inflection.underscore(domain_model)}.py",
        )


if __name__ == "__main__":
    anyio.run(main)
