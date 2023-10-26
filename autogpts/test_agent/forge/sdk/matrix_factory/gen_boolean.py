# import ast
# import os
# import time
# from asyncio import sleep
# from dataclasses import dataclass
#
# import openai
#
# # # from fgn.completion.chat import achat
# # import fgn.completion.complete as complete
#
# # Here is your PerfectProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION of your requirements.
#
# import tiktoken
#
# from typetemp.template.typed_template import TypedTemplate
#
#
# async def acreate(model, **kwargs):
#     return await complete.acreate(
#         model=model,
#         temperature=0.0,
#         max_tokens=100,
#         stop=["}"],
#         **kwargs,
#     )
#
#
# async def chat(model, **kwargs):
#     return await achat(model=model, **kwargs)
#
#
# async def gpt_3_5_turbo(**kwargs):
#     return await chat(model="gpt-3.5-turbo", **kwargs)
#
#
# async def gpt_3_5_turbo_0301(**kwargs):
#     return await chat(model="gpt-3.5-turbo-0301", **kwargs)
#
#
# async def gpt_3_5_turbo_0613(**kwargs):
#     return await chat(model="gpt-3.5-turbo-0613", **kwargs)
#
#
# async def gpt_3_5_turbo_16k(**kwargs):
#     return await chat(model="gpt-3.5-turbo-16k", **kwargs)
#
#
# async def gpt_3_5_turbo_16k_0613(**kwargs):
#     return await chat(model="gpt-3.5-turbo-16k-0613", **kwargs)
#
#
# async def gpt_4(**kwargs):
#     return await chat(model="gpt-4", **kwargs)
#
#
# async def gpt_4_0314(**kwargs):
#     return await chat(model="gpt-4-0314", **kwargs)
#
#
# async def gpt_4_0613(**kwargs):
#     return await chat(model="gpt-4-0613", **kwargs)
#
#
# async def gpt_3_5_turbo_instruct(**kwargs):
#     return await acreate(model="gpt-3.5-turbo-instruct", **kwargs)
#
#
# async def gpt_3_5_turbo_instruct_0914(**kwargs):
#     return await acreate(model="gpt-3.5-turbo-instruct-0914", **kwargs)
#
#
# async def ada(**kwargs):
#     return await acreate(model="ada", **kwargs)
#
#
# async def ada_code_search_code(**kwargs):
#     return await acreate(model="ada-code-search-code", **kwargs)
#
#
# async def ada_code_search_text(**kwargs):
#     return await acreate(model="ada-code-search-text", **kwargs)
#
#
# async def ada_search_document(**kwargs):
#     return await acreate(model="ada-search-document", **kwargs)
#
#
# async def ada_search_query(**kwargs):
#     return await acreate(model="ada-search-query", **kwargs)
#
#
# async def ada_similarity(**kwargs):
#     return await acreate(model="ada-similarity", **kwargs)
#
#
# async def babbage(**kwargs):
#     return await acreate(model="babbage", **kwargs)
#
#
# async def babbage_002(**kwargs):
#     return await acreate(model="babbage-002", **kwargs)
#
#
# async def babbage_code_search_code(**kwargs):
#     return await acreate(model="babbage-code-search-code", **kwargs)
#
#
# async def babbage_code_search_text(**kwargs):
#     return await acreate(model="babbage-code-search-text", **kwargs)
#
#
# async def babbage_search_document(**kwargs):
#     return await acreate(model="babbage-search-document", **kwargs)
#
#
# async def babbage_search_query(**kwargs):
#     return await acreate(model="babbage-search-query", **kwargs)
#
#
# async def babbage_similarity(**kwargs):
#     return await acreate(model="babbage-similarity", **kwargs)
#
#
# async def code_davinci_edit_001(**kwargs):
#     return await acreate(model="code-davinci-edit-001", **kwargs)
#
#
# async def code_search_ada_code_001(**kwargs):
#     return await acreate(model="code-search-ada-code-001", **kwargs)
#
#
# async def code_search_ada_text_001(**kwargs):
#     return await acreate(model="code-search-ada-text-001", **kwargs)
#
#
# async def code_search_babbage_code_001(**kwargs):
#     return await acreate(model="code-search-babbage-code-001", **kwargs)
#
#
# async def code_search_babbage_text_001(**kwargs):
#     return await acreate(model="code-search-babbage-text-001", **kwargs)
#
#
# async def curie(**kwargs):
#     return await acreate(model="curie", **kwargs)
#
#
# async def curie_instruct_beta(**kwargs):
#     return await acreate(model="curie-instruct-beta", **kwargs)
#
#
# async def curie_search_document(**kwargs):
#     return await acreate(model="curie-search-document", **kwargs)
#
#
# async def curie_search_query(**kwargs):
#     return await acreate(model="curie-search-query", **kwargs)
#
#
# async def curie_similarity(**kwargs):
#     return await acreate(model="curie-similarity", **kwargs)
#
#
# async def davinci(**kwargs):
#     return await acreate(model="davinci", **kwargs)
#
#
# async def davinci_002(**kwargs):
#     return await acreate(model="davinci-002", **kwargs)
#
#
# async def davinci_instruct_beta(**kwargs):
#     return await acreate(model="davinci-instruct-beta", **kwargs)
#
#
# async def davinci_search_document(**kwargs):
#     return await acreate(model="davinci-search-document", **kwargs)
#
#
# async def davinci_search_query(**kwargs):
#     return await acreate(model="davinci-search-query", **kwargs)
#
#
# async def davinci_similarity(**kwargs):
#     return await acreate(model="davinci-similarity", **kwargs)
#
#
# async def text_ada_001(**kwargs):
#     return await acreate(model="text-ada-001", **kwargs)
#
#
# async def text_babbage_001(**kwargs):
#     return await acreate(model="text-babbage-001", **kwargs)
#
#
# async def text_curie_001(**kwargs):
#     return await acreate(model="text-curie-001", **kwargs)
#
#
# async def text_davinci_001(**kwargs):
#     return await acreate(model="text-davinci-001", **kwargs)
#
#
# async def text_davinci_002(**kwargs):
#     return await acreate(model="text-davinci-002", **kwargs)
#
#
# async def text_davinci_003(**kwargs):
#     return await acreate(model="text-davinci-003", **kwargs)
#
#
# async def text_davinci_edit_001(**kwargs):
#     return await acreate(model="text-davinci-edit-001", **kwargs)
#
#
# async def text_embedding_ada_002(**kwargs):
#     return await acreate(model="text-embedding-ada-002", **kwargs)
#
#
# async def text_search_ada_doc_001(**kwargs):
#     return await acreate(model="text-search-ada-doc-001", **kwargs)
#
#
# async def text_search_ada_query_001(**kwargs):
#     return await acreate(model="text-search-ada-query-001", **kwargs)
#
#
# async def text_search_babbage_doc_001(**kwargs):
#     return await acreate(model="text-search-babbage-doc-001", **kwargs)
#
#
# async def text_search_babbage_query_001(**kwargs):
#     return await acreate(model="text-search-babbage-query-001", **kwargs)
#
#
# async def text_search_curie_doc_001(**kwargs):
#     return await acreate(model="text-search-curie-doc-001", **kwargs)
#
#
# async def text_search_curie_query_001(**kwargs):
#     return await acreate(model="text-search-curie-query-001", **kwargs)
#
#
# async def text_search_davinci_doc_001(**kwargs):
#     return await acreate(model="text-search-davinci-doc-001", **kwargs)
#
#
# async def text_search_davinci_query_001(**kwargs):
#     return await acreate(model="text-search-davinci-query-001", **kwargs)
#
#
# async def text_similarity_ada_001(**kwargs):
#     return await acreate(model="text-similarity-ada-001", **kwargs)
#
#
# async def text_similarity_babbage_001(**kwargs):
#     return await acreate(model="text-similarity-babbage-001", **kwargs)
#
#
# async def text_similarity_curie_001(**kwargs):
#     return await acreate(model="text-similarity-curie-001", **kwargs)
#
#
# async def text_similarity_davinci_001(**kwargs):
#     return await acreate(model="text-similarity-davinci-001", **kwargs)
#
#
# chat_models = [
#     "gpt_3_5_turbo",
#     "gpt_3_5_turbo_0301",
#     "gpt_3_5_turbo_0613",
#     "gpt_3_5_turbo_16k",
#     "gpt_3_5_turbo_16k_0613",
#     "gpt_4",
#     "gpt_4_0314",
#     "gpt_4_0613",
# ]
#
# models_returning_dict = [
#     "gpt_3_5_turbo_instruct",
#     "gpt_3_5_turbo_instruct_0914",
#     "ada",
#     "ada_similarity",
#     "babbage",
#     "babbage_002",
#     "curie",
#     "curie_instruct_beta",
#     "curie_search_document",
#     "curie_search_query",
#     "curie_similarity",
#     "davinci",
#     "davinci_002",
#     "davinci_instruct_beta",
#     "text_ada_001",
#     "text_babbage_001",
#     "text_curie_001",
#     "text_davinci_001",
#     "text_davinci_002",
#     "text_davinci_003",
#     "text_search_curie_doc_001",
#     "text_search_curie_query_001",
#     "text_similarity_ada_001",
#     "text_similarity_curie_001",
# ]
#
# best_models = [
#     "gpt_3_5_turbo_instruct",
#     "gpt_3_5_turbo_instruct_0914",
#     "davinci_instruct_beta",
#     "text_davinci_002",
#     "text_davinci_003",
# ]
#
# ok_models = [
#     "curie_instruct_beta",
#     "curie_similarity",
#     "davinci_002",
#     "text_curie_001",
#     "text_similarity_curie_001",
# ]
#
# all_models = [
#     # "gpt_3_5_turbo",
#     # "gpt_3_5_turbo_0301",
#     # "gpt_3_5_turbo_0613",
#     # "gpt_3_5_turbo_16k",
#     # "gpt_3_5_turbo_16k_0613",
#     "gpt_3_5_turbo_instruct",
#     "gpt_3_5_turbo_instruct_0914",
#     # "gpt_4",
#     # "gpt_4_0314",
#     # "gpt_4_0613",
#     "ada",
#     "ada_code_search_code",
#     "ada_code_search_text",
#     "ada_search_document",
#     "ada_search_query",
#     "ada_similarity",
#     "babbage",
#     "babbage_002",
#     "babbage_code_search_code",
#     "babbage_code_search_text",
#     "babbage_search_document",
#     "babbage_search_query",
#     "babbage_similarity",
#     "code_search_ada_code_001",
#     "code_search_ada_text_001",
#     "code_search_babbage_code_001",
#     "code_search_babbage_text_001",
#     "curie",
#     "curie_instruct_beta",
#     "curie_search_document",
#     "curie_search_query",
#     "curie_similarity",
#     "davinci",
#     "davinci_002",
#     "davinci_instruct_beta",
#     "davinci_search_document",
#     "davinci_search_query",
#     "davinci_similarity",
#     "text_ada_001",
#     "text_babbage_001",
#     "text_curie_001",
#     "text_davinci_001",
#     "text_davinci_002",
#     "text_davinci_003",
#     "text_embedding_ada_002",
#     "text_search_ada_doc_001",
#     "text_search_ada_query_001",
#     "text_search_babbage_doc_001",
#     "text_search_babbage_query_001",
#     "text_search_curie_doc_001",
#     "text_search_curie_query_001",
#     "text_search_davinci_doc_001",
#     "text_search_davinci_query_001",
#     "text_similarity_ada_001",
#     "text_similarity_babbage_001",
#     "text_similarity_curie_001",
#     "text_similarity_davinci_001",
# ]
#
#
# @dataclass
# class SarahMikeEmailTemplate(TypedTemplate):
#     name: str = None
#     location: str = None
#     date: str = None
#     topic: str = None
#     sender_name: str = None
#     source = """
# Dear {{ name }},
#
# I hope this message finds you well in {{ location }}.
# I wanted to remind you about our appointment on {{ date }}
# regarding {{ topic }}. Please let me know if you need to reschedule.
#
# Best regards,
# {{ sender_name }}
#     """
#
#
# async def generate_boolean(completion_function, prompt, **completion_kwargs):
#     completion_prompt = f"Based on the following text, provide a boolean response ('true' or 'false'): '{prompt}'"
#
#     result = await completion_function(prompt=completion_prompt, **completion_kwargs)
#     # Convert the result to lowercase and check against "true" and "false"
#     boolean_value = result.strip().lower() == "true"
#     return boolean_value
#
#
# async def main():
#     async def run_model(model):
#         try:
#             test_prompt = "Is Python an interpreted language?"
#             result = await generate_boolean(globals()[model], test_prompt)
#             return model, result
#         except Exception as e:
#             print(e)
#             return None, None
#
#     # models = jinja_models
#
#     # models = chat_models
#     # models = models_returning_dict
#     # models = best_models
#     models = all_models
#     start = time.time()
#
#     # Create a list of coroutines for each model
#     tasks = [run_model(model) for model in models]
#
#     # Use asyncio.gather to run all tasks concurrently
#     results = await asyncio.gather(*tasks)
#
#     # Filter out None results
#     valid_results = [(model, result) for model, result in results if model and result]
#
#     # print("models_returning_def = [")
#
#     for model, result in valid_results:
#         print(f"'{model}',")
#     print("]")
#
#     for model, result in valid_results:
#         try:
#             print(f"\n####################\n{model}:,")
#             print(result)
#
#         except Exception as e:
#             print(e)
#
#     end = time.time()
#     print(f"Duration: {end - start}")
#     print("Total models:", len(valid_results))
#
#     # results = await asyncio.gather(*[globals()[model](prompt="Hello world!") for model in models])
#     # tr
#
#     # print(results)
#
#
# if __name__ == "__main__":
#     import asyncio
#
#     asyncio.run(main())
