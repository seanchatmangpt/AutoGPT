import ast

from fgn.completion.chat import achat
import fgn.completion.complete as complete

async def main():
    ...


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


async def acreate(model, **kwargs):
    return await complete.acreate(
        model=model,
        temperature=0.0,
        max_tokens=100,
        stop=["}"],
        **kwargs,
    )


async def create_dict(model, prompt, **kwargs):
    question = f"Generate a Python dictionary from:\n\n'{prompt}'" \
               f"\n\nPlease produce the perfect Python dictionary based on the given data:"
    result = await complete.acreate(
        model=model,
        temperature=0.0,
        stop=["}"],
        **kwargs,
    )

    return extract_dictionary(result)

async def generate_boolean(
    completion_function,
    prompt,
    **completion_kwargs
):

    completion_prompt = (
        f"Based on the following text, provide a boolean response ('true' or 'false'): '{prompt}'"
    )

    result = await completion_function(prompt=completion_prompt, **completion_kwargs)
    # Convert the result to lowercase and check against "true" and "false"
    boolean_value = result.strip().lower() == "true"
    return boolean_value

# async def create_bool(model, **kwargs):



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

gpt_4_models = [
    "gpt-4",
    "gpt-4-0314",
    "gpt-4-0613",
]

chat_models = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-0301",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-16k-0613",
    "gpt-4",
    "gpt-4-0314",
    "gpt-4-0613",
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

instruct_models = [
    'gpt-3.5-turbo-instruct',
    'gpt-3.5-turbo-instruct-0914',
]

best_models = ['gpt-3.5-turbo-instruct',
               'gpt-3.5-turbo-instruct-0914',
               'davinci-instruct-beta',
               'text-davinci-002',
               'text-davinci-003']

ok_models = [
    'curie-instruct-beta',
    'curie-similarity',
    'davinci-002',
    'text-curie-001',
    'text-similarity-curie-001',
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



if __name__ == "__main__":
    import asyncio
    asyncio.run(main())