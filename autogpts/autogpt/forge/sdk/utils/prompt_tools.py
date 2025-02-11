import itertools
import time

# import anyio
from typing import Iterable, List

from icontract import ensure, require

from .complete import acreate
from .models import instruct_models, ok_models


# 1. Model Selection
def model_generator(models: List[str]):
    """
    A generator that yields models in a round-robin fashion using itertools.cycle.
    """
    return itertools.cycle(models)


# 2. Prompt Generation (could be expanded if there are more prompt types)
def construct_openai_prompt(base_prompt: str, item: str) -> str:
    return f"{item}{base_prompt}"


# 3. OpenAI Call
async def call_openai(
    prompt: str, model_name: str, max_tokens: int = 50, temperature: float = 0.7
) -> str:
    return await acreate(
        prompt=prompt, model=model_name, max_tokens=max_tokens, temperature=temperature
    )


# 4. Timing and Logging
async def timed_openai_call(
    prompt: str, item: str, model_name: str, max_tokens: int = 50, temperature: float = 0.7
) -> str:
    start_time = time.time()
    response = await call_openai(prompt, model_name, max_tokens, temperature)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(
        f'Generated response for "{item[:30]}..." using {model_name} in {elapsed_time:.2f} seconds.'
    )
    return response


# 5. Concurrent Execution
async def prompt_map(
    prompts_iterable: Iterable[str],
    base_prompt: str = "",
    max_tokens: int = 50,
    model_list: List[str] = None,
    temperature: float = 0.7,
) -> List[str]:
    model_gen = model_generator(model_list or instruct_models)
    responses = []

    async def generate_response(index: int, item: str) -> None:
        model_name = next(model_gen)
        prompt = construct_openai_prompt(base_prompt, item)
        response = await timed_openai_call(prompt, item, model_name, max_tokens)
        responses.append((index, response))

    async with anyio.create_task_group() as tg:
        for index, item in enumerate(prompts_iterable):
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


async def prompt_filter(
    base_prompt: str,
    prompts_iterable: Iterable[str],
    model_list: List[str] = None,
    max_tokens: int = 50,
) -> List[str]:
    """
    This function takes a base prompt and filters an iterable based on responses from OpenAI.

    Args:
        base_prompt (str): The base prompt for generating boolean responses.
        prompts_iterable (iterable): An iterable (e.g., list, tuple) of strings to be filtered.
        model_list (List[str]): List of models to be used in round-robin fashion. If None, defaults to instruct_models.
        max_tokens (int): The maximum number of tokens in each response.

    Returns:
        list: A list of items from the iterable that pass the condition specified by the prompt.
    """

    filterable = [
        f"Create a Python bool based on the prompt: '{prompt}'."
        f"\nPlease complete the following code block:\n"
        f"```python\n"
        f"from typing import bool\n"
        f"# {prompt} \n"
        f"perfect_bool: bool = "
        for prompt in prompts_iterable
    ]

    responses = await prompt_map(base_prompt, filterable, max_tokens, model_list)
    results = [item for item, resp in zip(prompts_iterable, responses) if "true" in resp.lower()]

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

from typing import Callable, Iterable, List

import anyio


async def prompt_reduce(
    base_prompt: str,
    prompts_iterable: Iterable[str],
    reducer: Callable[[List[str]], List[str]],
    model_list: List[str] = None,
    max_tokens: int = 50,
) -> List[str]:
    """
    Uses the prompt_map function to collect responses and then reduces the responses based on a given reducer function.

    Args:
        base_prompt (str): The base prompt for generating responses.
        prompts_iterable (Iterable[str]): An iterable of strings to generate responses for.
        reducer (Callable[[List[str]], List[str]]): A function to reduce the list of generated responses.
        model_list (List[str]): Optional; list of models to use. If None, uses a default.
        max_tokens (int): Optional; max tokens for each response.

    Returns:
        A reduced list of responses based on the reducer function.
    """

    # First, we generate the responses based on the iterable and the base prompt
    responses = await prompt_map(base_prompt, prompts_iterable, max_tokens, model_list)

    # Then, we reduce the list of responses using the reducer function
    return reducer(responses)


async def create_python_class_from_function_names(
    class_name: str, function_names: List[str]
) -> str:
    """
    Creates a Python class string from a list of function names using OpenAI for method content.
    """
    function_strs = []
    for fname in function_names:
        prompt = f"Generate Python code for a class method named {fname}."
        implementation_details = await call_openai(
            prompt, "text-davinci-002", max_tokens=50
        )  # You can use your preferred model
        function_strs.append(
            f"    def {fname}(self, *args, **kwargs):\n        {implementation_details.strip()}"
        )

    functions_str = "\n".join(function_strs)
    return f"class {class_name}:\n{functions_str}"


@require(lambda x_prompts_iterable: all(isinstance(x, str) for x in x_prompts_iterable))
@require(lambda y_prompts_iterable: all(isinstance(y, str) for y in y_prompts_iterable))
@require(lambda max_tokens: isinstance(max_tokens, int) and max_tokens > 0)
@ensure(lambda result: isinstance(result, list))
@ensure(lambda result: all(isinstance(sublist, list) for sublist in result))
@ensure(
    lambda x_prompts_iterable, y_prompts_iterable, result: len(result) == len(x_prompts_iterable)
)
@ensure(
    lambda x_prompts_iterable, y_prompts_iterable, result: all(
        len(sublist) == len(y_prompts_iterable) for sublist in result
    )
)
async def prompt_matrix(
    x_prompts_iterable: Iterable[str],
    y_prompts_iterable: Iterable[str],
    max_tokens: int = 50,
    model_list: List[str] = None,
) -> List[List[str]]:
    # Initialize a 2D list to store the results.
    responses_2d = []

    # Loop through each x_prompt.
    for x_prompt in x_prompts_iterable:
        # Initialize a list to hold the responses for this x_prompt.
        y_responses = []

        # Loop through each y_prompt.
        for y_prompt in y_prompts_iterable:
            # Combine the x_prompt and y_prompt to create the new base prompt.
            combined_prompt = f"{x_prompt} {y_prompt}"

            # Call the existing prompt_map function with the complete set of y_prompts.
            single_response = await prompt_map(combined_prompt, [y_prompt], max_tokens, model_list)

            # Append the response for the current y_prompt to y_responses.
            y_responses.append(single_response[0])

        # Append the list of y_responses to the 2D list of responses.
        responses_2d.append(y_responses)

    return responses_2d


# Example usage
# async def main():
#     x_prompts = ["Create a python function for", "Create a python class for"]
#     y_prompts = ["sorting an array", "finding the maximum element"]
#     result = await prompt_map2d(x_prompts, y_prompts, max_tokens=50)
#     print(result)


from typing import Callable, List, Type

from icontract import ensure, require

# I have IMPLEMENTED your PerfectPythonProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION code of your requirements.


class Verifiers:
    """
    A class designed to judge the validity of thoughts and answers produced by language models. This verifier can assess if a thought is a valid form of reasoning for deriving an answer from a question and if the answer is correct.
    """

    def __init__(self):
        pass

    async def generate_solutions(self, problem: str) -> List[str]:
        """
        Generates solutions for a given problem leveraging OpenAI prompts, inspired by the idea of adding explicit "thought" variables to improve model performance.
        """
        base_prompt = f"Given the concept of 'Self-Taught Reasoner' and 'rationale generation with rationalization', propose solutions for: {problem}"
        solutions = await prompt_map(
            base_prompt, [problem for _ in range(5)], model_list=ok_models, max_tokens=300
        )  # Simulating 5 potential solutions
        print("Generated solutions:", solutions)
        return solutions

    async def verify_solutions(self, solutions: List[str]) -> List[str]:
        """
        Validates the provided solutions based on the concept of "verification" labels, which determine if a solution is derived through valid reasoning.
        """
        base_prompt = "Is this useful to an expert?"
        verified_solutions = await prompt_filter(base_prompt, solutions)
        return verified_solutions

    async def pick_best_solution(self, verified_solutions: List[str]) -> str:
        """
        Chooses the best solution among the verified ones, leveraging the notion of ranking solutions by their validity.
        """
        base_prompt = f"Using the idea of 'N-step reasoning' and 'verification model', identify the best solution among the following verified solutions:"
        combined_solutions = "\n".join(verified_solutions)
        best_solution = await prompt_map(base_prompt, [combined_solutions])
        return best_solution[0]  # Return the first item as it should contain the best solution


async def main():
    verifier = Verifiers()
    solutions = await verifier.generate_solutions(
        "How to improve code readability in a DDD abstraction framework? Expert level Opinions only with Python examples. Out of the box ideas\n```python\n# Code examples\n```"
    )
    verified_solutions = await verifier.verify_solutions(solutions)
    best_solution = await verifier.pick_best_solution(verified_solutions)
    print("Best Solution:", best_solution)


if __name__ == "__main__":
    anyio.run(main)
    # Example usage
    domain_statements = [
        "The user should be able to deposit money into their account.",
        "The user must be able to withdraw funds.",
        "The account should display the current balance.",
        "The account should allow setting a preferred currency.",
        "The account should allow setting a preferred language.",
        "Loans should be approved within 24 hours.",
    ]

    function_names_base_prompt = (
        "Based on the following statement by a domain expert, "
        "suggest a suitable pythonic function name. Avoid the words get or set:"
    )

    # Here you'll call the prompt_reduce function with the necessary parameters. For demonstration, we simulate it.
    # function_names = anyio.run(prompt_reduce, function_names_base_prompt, domain_statements, extract_function_names)
    #
    # print("Extracted function names:", function_names)
