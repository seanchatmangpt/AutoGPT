import ast
import os
import time
from asyncio import sleep
from dataclasses import dataclass
from litellm import acompletion


import openai

from fgn.completion.chat import achat
import fgn.completion.complete as complete


# Here is your PerfectProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION of your requirements.

import tiktoken

from typetemp.template.typed_template import TypedTemplate

email_prompt = """
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


async def acreate(model, prompt, **kwargs):
    return await acompletion(
        model=model,
        temperature=0.0,
        max_tokens=100,
        stop=["}"],
        messages=[{"role": "user", "content": prompt }],
        **kwargs,
    )


async def chat(model, **kwargs):
    return await achat(model=model, **kwargs)
    

async def gpt_3_5_turbo(**kwargs):
    return await chat(model="gpt-3.5-turbo", **kwargs)


async def gpt_3_5_turbo_0301(**kwargs):
    return await chat(model="gpt-3.5-turbo-0301", **kwargs)


async def gpt_3_5_turbo_0613(**kwargs):
    return await chat(model="gpt-3.5-turbo-0613", **kwargs)


async def gpt_3_5_turbo_16k(**kwargs):
    return await chat(model="gpt-3.5-turbo-16k", **kwargs)


async def gpt_3_5_turbo_16k_0613(**kwargs):
    return await chat(model="gpt-3.5-turbo-16k-0613", **kwargs)


async def gpt_4(**kwargs):
    return await chat(model="gpt-4", **kwargs)


async def gpt_4_0314(**kwargs):
    return await chat(model="gpt-4-0314", **kwargs)


async def gpt_4_0613(**kwargs):
    return await chat(model="gpt-4-0613", **kwargs)

async def gpt_3_5_turbo_instruct(**kwargs):
    return await acreate(model="gpt-3.5-turbo-instruct", **kwargs)


async def gpt_3_5_turbo_instruct_0914(**kwargs):
    return await acreate(model="gpt-3.5-turbo-instruct-0914", **kwargs)


async def ada(**kwargs):
    return await acreate(model="ada", **kwargs)


async def ada_code_search_code(**kwargs):
    return await acreate(model="ada-code-search-code", **kwargs)


async def ada_code_search_text(**kwargs):
    return await acreate(model="ada-code-search-text", **kwargs)


async def ada_search_document(**kwargs):
    return await acreate(model="ada-search-document", **kwargs)


async def ada_search_query(**kwargs):
    return await acreate(model="ada-search-query", **kwargs)


async def ada_similarity(**kwargs):
    return await acreate(model="ada-similarity", **kwargs)


async def babbage(**kwargs):
    return await acreate(model="babbage", **kwargs)


async def babbage_002(**kwargs):
    return await acreate(model="babbage-002", **kwargs)


async def babbage_code_search_code(**kwargs):
    return await acreate(model="babbage-code-search-code", **kwargs)


async def babbage_code_search_text(**kwargs):
    return await acreate(model="babbage-code-search-text", **kwargs)


async def babbage_search_document(**kwargs):
    return await acreate(model="babbage-search-document", **kwargs)


async def babbage_search_query(**kwargs):
    return await acreate(model="babbage-search-query", **kwargs)


async def babbage_similarity(**kwargs):
    return await acreate(model="babbage-similarity", **kwargs)


async def code_davinci_edit_001(**kwargs):
    return await acreate(model="code-davinci-edit-001", **kwargs)


async def code_search_ada_code_001(**kwargs):
    return await acreate(model="code-search-ada-code-001", **kwargs)


async def code_search_ada_text_001(**kwargs):
    return await acreate(model="code-search-ada-text-001", **kwargs)


async def code_search_babbage_code_001(**kwargs):
    return await acreate(model="code-search-babbage-code-001", **kwargs)


async def code_search_babbage_text_001(**kwargs):
    return await acreate(model="code-search-babbage-text-001", **kwargs)


async def curie(**kwargs):
    return await acreate(model="curie", **kwargs)


async def curie_instruct_beta(**kwargs):
    return await acreate(model="curie-instruct-beta", **kwargs)


async def curie_search_document(**kwargs):
    return await acreate(model="curie-search-document", **kwargs)


async def curie_search_query(**kwargs):
    return await acreate(model="curie-search-query", **kwargs)


async def curie_similarity(**kwargs):
    return await acreate(model="curie-similarity", **kwargs)


async def davinci(**kwargs):
    return await acreate(model="davinci", **kwargs)


async def davinci_002(**kwargs):
    return await acreate(model="davinci-002", **kwargs)


async def davinci_instruct_beta(**kwargs):
    return await acreate(model="davinci-instruct-beta", **kwargs)


async def davinci_search_document(**kwargs):
    return await acreate(model="davinci-search-document", **kwargs)


async def davinci_search_query(**kwargs):
    return await acreate(model="davinci-search-query", **kwargs)


async def davinci_similarity(**kwargs):
    return await acreate(model="davinci-similarity", **kwargs)


async def text_ada_001(**kwargs):
    return await acreate(model="text-ada-001", **kwargs)


async def text_babbage_001(**kwargs):
    return await acreate(model="text-babbage-001", **kwargs)


async def text_curie_001(**kwargs):
    return await acreate(model="text-curie-001", **kwargs)


async def text_davinci_001(**kwargs):
    return await acreate(model="text-davinci-001", **kwargs)


async def text_davinci_002(**kwargs):
    return await acreate(model="text-davinci-002", **kwargs)


async def text_davinci_003(**kwargs):
    return await acreate(model="text-davinci-003", **kwargs)


async def text_davinci_edit_001(**kwargs):
    return await acreate(model="text-davinci-edit-001", **kwargs)


async def text_embedding_ada_002(**kwargs):
    return await acreate(model="text-embedding-ada-002", **kwargs)


async def text_search_ada_doc_001(**kwargs):
    return await acreate(model="text-search-ada-doc-001", **kwargs)


async def text_search_ada_query_001(**kwargs):
    return await acreate(model="text-search-ada-query-001", **kwargs)


async def text_search_babbage_doc_001(**kwargs):
    return await acreate(model="text-search-babbage-doc-001", **kwargs)


async def text_search_babbage_query_001(**kwargs):
    return await acreate(model="text-search-babbage-query-001", **kwargs)


async def text_search_curie_doc_001(**kwargs):
    return await acreate(model="text-search-curie-doc-001", **kwargs)


async def text_search_curie_query_001(**kwargs):
    return await acreate(model="text-search-curie-query-001", **kwargs)


async def text_search_davinci_doc_001(**kwargs):
    return await acreate(model="text-search-davinci-doc-001", **kwargs)


async def text_search_davinci_query_001(**kwargs):
    return await acreate(model="text-search-davinci-query-001", **kwargs)


async def text_similarity_ada_001(**kwargs):
    return await acreate(model="text-similarity-ada-001", **kwargs)


async def text_similarity_babbage_001(**kwargs):
    return await acreate(model="text-similarity-babbage-001", **kwargs)


async def text_similarity_curie_001(**kwargs):
    return await acreate(model="text-similarity-curie-001", **kwargs)


async def text_similarity_davinci_001(**kwargs):
    return await acreate(model="text-similarity-davinci-001", **kwargs)


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
'gpt_3_5_turbo_instruct',
'gpt_3_5_turbo_instruct_0914',
'ada',
'ada_similarity',
'babbage',
'babbage_002',
'curie',
'curie_instruct_beta',
'curie_search_document',
'curie_search_query',
'curie_similarity',
'davinci',
'davinci_002',
'davinci_instruct_beta',
'text_ada_001',
'text_babbage_001',
'text_curie_001',
'text_davinci_001',
'text_davinci_002',
'text_davinci_003',
'text_search_curie_doc_001',
'text_search_curie_query_001',
'text_similarity_ada_001',
'text_similarity_curie_001',
]

best_models = ['gpt_3_5_turbo_instruct',
'gpt_3_5_turbo_instruct_0914',
'davinci_instruct_beta',
'text_davinci_002',
'text_davinci_003']

ok_models = [
'curie_instruct_beta',
'curie_similarity',
'davinci_002',
'text_curie_001',
'text_similarity_curie_001',
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
    start_pos = input_str.find('{')

    # Check if '{' is not found
    if start_pos == -1:
        raise ValueError("No dictionary found in the input string.")

    # Extract the dictionary substring
    dict_str = input_str[start_pos:]

    # Safely evaluate the dictionary substring
    return ast.literal_eval(dict_str)

async def main():
    async def run_model(model):
        try:
            result = await globals()[model](prompt=email_prompt)
            if 'sender_name' in result:
                return model, result
            else:
                return None, None
        except Exception as e:
            return None, None

    # models = jinja_models

    # models = chat_models
    # models = models_returning_dict
    models = best_models
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
            # print(f"\n####################\n{model}:,")
            # print(extract_dictionary(result+"}"))
            kwargs = extract_dictionary(result+"}")
            to = f"./emails/{model}{time.time()}.py"
            email = SarahMikeEmailTemplate(**kwargs)()
            with open(to, "w") as f:
                f.write(email)

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
