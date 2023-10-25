import ast
import os
import time
from asyncio import sleep
from dataclasses import dataclass

import openai

from fgn.completion.chat import achat
import fgn.completion.complete as complete

# Here is your PerfectProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION of your requirements.

import tiktoken

from typetemp.template.typed_template import TypedTemplate

prompt = """
Objective:
Generate a Python dictionary to populate the given Jinja template, based on the information from the provided paragraph.


Dear {{ name }},

I hope this message finds you well in {{ location }}. 
I wanted to remind you about our appointment on {{ date }} 
regarding {{ topic }}. Please let me know if you need to reschedule.

Best regards,
{{ sender_name }}

Paragraph:
Sarah lives in New York and recently mentioned she would like to discuss the new project proposal. Our meeting is set for June 12th, and if she's unavailable, she should contact Mike.

Chain of Thought:
Extract the name of the person the letter is addressed to.
Identify the location where the person lives.
Find the date of the meeting/appointment.
Determine the topic of the discussion/meeting.
Identify who the sender or the point of contact is.
Additional Information:
The name is the person being addressed in the paragraph.
location is the place where the named person resides.
The date represents the scheduled day for the event or meeting.
topic signifies what the meeting or event is about.
sender_name is the individual to be contacted in case of any changes.
Please produce the perfect Python dictionary based on the given data.
"""


chat_models = [
    "gpt_3_5_turbo",
    "gpt_3_5_turbo_0301",
    "gpt_3_5_turbo_0613",
    "gpt_3_5_turbo_16k",
    "gpt_3_5_turbo_16k_0613",
    "gpt_4",
    "gpt_4_0314",
    "gpt_4_0613",
]

models_returning_dict = [
    "gpt_3_5_turbo_instruct",
    "gpt_3_5_turbo_instruct_0914",
    "ada",
    "ada_similarity",
    "babbage",
    "babbage_002",
    "curie",
    "curie_instruct_beta",
    "curie_search_document",
    "curie_search_query",
    "curie_similarity",
    "davinci",
    "davinci_002",
    "davinci_instruct_beta",
    "text_ada_001",
    "text_babbage_001",
    "text_curie_001",
    "text_davinci_001",
    "text_davinci_002",
    "text_davinci_003",
    "text_search_curie_doc_001",
    "text_search_curie_query_001",
    "text_similarity_ada_001",
    "text_similarity_curie_001",
]

best_models = [
    "gpt_3_5_turbo_instruct",
    "gpt_3_5_turbo_instruct_0914",
    "davinci_instruct_beta",
    "text_davinci_002",
    "text_davinci_003",
]

ok_models = [
    "curie_instruct_beta",
    "curie_similarity",
    "davinci_002",
    "text_curie_001",
    "text_similarity_curie_001",
]

all_models = [
    # "gpt_3_5_turbo",
    # "gpt_3_5_turbo_0301",
    # "gpt_3_5_turbo_0613",
    # "gpt_3_5_turbo_16k",
    # "gpt_3_5_turbo_16k_0613",
    "gpt_3_5_turbo_instruct",
    "gpt_3_5_turbo_instruct_0914",
    # "gpt_4",
    # "gpt_4_0314",
    # "gpt_4_0613",
    "ada",
    "ada_code_search_code",
    "ada_code_search_text",
    "ada_search_document",
    "ada_search_query",
    "ada_similarity",
    "babbage",
    "babbage_002",
    "babbage_code_search_code",
    "babbage_code_search_text",
    "babbage_search_document",
    "babbage_search_query",
    "babbage_similarity",
    "code_search_ada_code_001",
    "code_search_ada_text_001",
    "code_search_babbage_code_001",
    "code_search_babbage_text_001",
    "curie",
    "curie_instruct_beta",
    "curie_search_document",
    "curie_search_query",
    "curie_similarity",
    "davinci",
    "davinci_002",
    "davinci_instruct_beta",
    "davinci_search_document",
    "davinci_search_query",
    "davinci_similarity",
    "text_ada_001",
    "text_babbage_001",
    "text_curie_001",
    "text_davinci_001",
    "text_davinci_002",
    "text_davinci_003",
    "text_embedding_ada_002",
    "text_search_ada_doc_001",
    "text_search_ada_query_001",
    "text_search_babbage_doc_001",
    "text_search_babbage_query_001",
    "text_search_curie_doc_001",
    "text_search_curie_query_001",
    "text_search_davinci_doc_001",
    "text_search_davinci_query_001",
    "text_similarity_ada_001",
    "text_similarity_babbage_001",
    "text_similarity_curie_001",
    "text_similarity_davinci_001",
]


@dataclass
class SarahMikeEmailTemplate(TypedTemplate):
    name: str = None
    location: str = None
    date: str = None
    topic: str = None
    sender_name: str = None
    source = """
Dear {{ name }},

I hope this message finds you well in {{ location }}. 
I wanted to remind you about our appointment on {{ date }} 
regarding {{ topic }}. Please let me know if you need to reschedule.

Best regards,
{{ sender_name }}
    """


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


import re
from time import strftime, gmtime


async def generate_filename(
    prompt,
    model="gpt-3.5-turbo-instruct",
    prefix="",
    suffix="",
    extension="txt",
    min_chars=30,
    max_chars=60,
    char_limit=300,
    time_stamp=False,
    **completion_kwargs,
) -> str:
    prompt = prompt[:char_limit]

    completion_prompt = (
        f"Generate a concise filename based on the text: '{prompt}'. "
        f"The filename should:\n"
        f"- Be in lowercase letters.\n"
        f"- Have at least {min_chars} characters.\n"
        f"- Have at most {max_chars} characters.\n"
        f"- Use underscores as separators.\n"
        f"- Exclude file extensions.\n"
        "Suggested filename:"
    )

    file_name = await complete.acreate(
        prompt=completion_prompt, max_tokens=max_chars * 2, **completion_kwargs
    )

    # Post-process the filename
    file_name = re.sub(r"[^a-zA-Z0-9_]", "", file_name)
    file_name = file_name[:max_chars]

    if prefix:
        file_name = f"{prefix}_{file_name}"

    if suffix:
        file_name = f"{file_name}_{suffix}"

    if time_stamp:
        file_name = f"{file_name}_{strftime('%Y-%m-%d_%H-%M-%S', gmtime())}"

    if extension:
        file_name = f"{file_name}.{extension}"

    return file_name


async def main():
    async def run_model(model):
        try:
            result = await generate_filename(globals()[model], prompt)
            return model, result
        except Exception as e:
            print(e)
            return None, None

    # models = jinja_models

    # models = chat_models
    models = models_returning_dict
    # models = best_models
    # models = all_models
    start = time.time()

    # Create a list of coroutines for each model
    tasks = [run_model(model) for model in models]

    # Use asyncio.gather to run all tasks concurrently
    results = await asyncio.gather(*tasks)

    # Filter out None results
    valid_results = [(model, result) for model, result in results if model and result]

    # print("models_returning_def = [")

    for model, result in valid_results:
        print(f"'{model}',")
    print("]")

    for model, result in valid_results:
        try:
            print(f"\n####################\n{model}:,")
            print(result)

        except Exception as e:
            print(e)

    end = time.time()
    print(f"Duration: {end - start}")
    print("Total models:", len(valid_results))

    # results = await asyncio.gather(*[globals()[model](prompt="Hello world!") for model in models])
    # tr

    # print(results)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
