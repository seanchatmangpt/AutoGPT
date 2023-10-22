from fgn.completion.complete import acreate
from matrix_factory.chat_helpers import ok_models, instruct_models
import time
import openai
import anyio
from typing import Iterable, List
import itertools


# 1. Model Selection
def model_generator(models: List[str]):
    """
    A generator that yields models in a round-robin fashion using itertools.cycle.
    """
    return itertools.cycle(models)

# 2. Prompt Generation (could be expanded if there are more prompt types)
def construct_openai_prompt(base_prompt: str, item: str) -> str:
    return f"{base_prompt}: {item}"

# 3. OpenAI Call
async def call_openai(prompt: str, model_name: str, max_tokens: int = 50) -> str:
    return await acreate(prompt=prompt, model=model_name, max_tokens=max_tokens)


# 4. Timing and Logging
async def timed_openai_call(prompt: str, item: str, model_name: str, max_tokens: int = 50) -> str:
    start_time = time.time()
    response = await call_openai(prompt, model_name, max_tokens)
    end_time = time.time()
    elapsed_time = end_time - start_time
    # print(f"Generated response for \"{item[:30]}...\" using {model_name} in {elapsed_time:.2f} seconds.")
    return response

# 5. Concurrent Execution
async def prompt_map(base_prompt: str, iterable: Iterable[str], max_tokens: int = 50, model_list: List[str] = None) -> List[str]:
    model_gen = model_generator(model_list or instruct_models)
    responses = []

    async def generate_response(index: int, item: str) -> None:
        model_name = next(model_gen)
        prompt = construct_openai_prompt(base_prompt, item)
        response = await timed_openai_call(prompt, item, model_name, max_tokens)
        responses.append((index, response))

    async with anyio.create_task_group() as tg:
        for index, item in enumerate(iterable):
            tg.start_soon(generate_response, index, item)

    # Sort the responses by index
    sorted_responses = [resp for _, resp in sorted(responses)]

    return sorted_responses



# [Rest of your functions and example usage]

# Example models and usage:

# example_prompt = "Translate the following text into French"
# text_list = ["Hello, how are you?", "I love programming", "Thank you very much", "I am doing well", "I am doing poorly"]
# start_time = time.time()
# responses_best_models = await prompt_map(example_prompt, text_list, 50)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Responses: in {elapsed_time:.2f} seconds.", responses_best_models)


async def prompt_filter(base_prompt: str, iterable: Iterable[str], model_list: List[str] = None, max_tokens: int = 50) -> List[str]:
    """
    This function takes a base prompt and filters an iterable based on responses from OpenAI.

    Args:
        base_prompt (str): The base prompt for generating boolean responses.
        iterable (iterable): An iterable (e.g., list, tuple) of strings to be filtered.
        model_list (List[str]): List of models to be used in round-robin fashion. If None, defaults to instruct_models.
        max_tokens (int): The maximum number of tokens in each response.

    Returns:
        list: A list of items from the iterable that pass the condition specified by the prompt.
    """

    filterable = [str(item) + "\n\nProvide a boolean response ('true' or 'false'):\n\nThe statement is: " for item in iterable]

    responses = await prompt_map(base_prompt, filterable, max_tokens, model_list)
    results = [item for item, resp in zip(iterable, responses) if 'true' in resp.lower()]

    return results


filter_prompt = "Is the statement in quotes positive?"


statements = [
    "'The sun is not shining today.'",
    "'I failed the test.'",
    "'The flowers are blooming.'",
    "'The weather is gloomy.'",
    "'I aced the exam!'",
]

# filtered_statements = anyio.run(prompt_filter, filter_prompt, statements)
# print("Positive statements:", filtered_statements)

from typing import List, Iterable, Callable
import anyio


async def prompt_reduce(
        base_prompt: str,
        iterable: Iterable[str],
        reducer: Callable[[List[str]], List[str]],
        model_list: List[str] = None,
        max_tokens: int = 50
) -> List[str]:
    """
    Uses the prompt_map function to collect responses and then reduces the responses based on a given reducer function.

    Args:
        base_prompt (str): The base prompt for generating responses.
        iterable (Iterable[str]): An iterable of strings to generate responses for.
        reducer (Callable[[List[str]], List[str]]): A function to reduce the list of generated responses.
        model_list (List[str]): Optional; list of models to use. If None, uses a default.
        max_tokens (int): Optional; max tokens for each response.

    Returns:
        A reduced list of responses based on the reducer function.
    """

    # First, we generate the responses based on the iterable and the base prompt
    responses = await prompt_map(base_prompt, iterable, max_tokens, model_list)

    # Then, we reduce the list of responses using the reducer function
    return reducer(responses)


async def create_python_class_from_function_names(class_name: str, function_names: List[str]) -> str:
    """
    Creates a Python class string from a list of function names using OpenAI for method content.
    """
    function_strs = []
    for fname in function_names:
        prompt = f"Generate Python code for a class method named {fname}."
        implementation_details = await call_openai(prompt, "text-davinci-002", max_tokens=50)  # You can use your preferred model
        function_strs.append(f"    def {fname}(self, *args, **kwargs):\n        {implementation_details.strip()}")

    functions_str = '\n'.join(function_strs)
    return f"class {class_name}:\n{functions_str}"


async def main():
    ...
    # Example usage
    # domain_statements = [
    #     "The user should be able to deposit money into their account.",
    #     "The user must be able to withdraw funds.",
    #     "The account should display the current balance.",
    #     "The account should allow setting a preferred currency.",
    #     "The account should allow setting a preferred language.",
    #     "Loans should be approved within 24 hours.",
    # ]
    #
    # function_names_base_prompt = "Based on the following statement by a domain expert, " \
    #                              "suggest a suitable pythonic function name. Avoid the words get or set:"
    #
    # # Here you'll call the prompt_reduce function with the necessary parameters. For demonstration, we simulate it.
    # function_names = anyio.run(prompt_reduce, function_names_base_prompt, domain_statements, extract_function_names)
    #
    # print("Extracted function names:", function_names)

