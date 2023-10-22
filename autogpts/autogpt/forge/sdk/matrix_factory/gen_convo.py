import os
import time

import curio

from curio import TaskGroup

from fgn.completion.chat import achat
from matrix_factory.chat_helpers import best_models, ok_models, chat_models
from matrix_factory.gen_full import data

# ... [rest of the imports from your code]


AUTHORS = [
    ("Luciano Ramalho", "Fluent Python"),
    ("Vaughn Vernon", "Implementing Domain Driven Design"),
    ("David Thomas", "The Pragmatic Programmer"),
    ("Andrew Hunt", "The Pragmatic Programmer")
]

# MODELS = chat_models
MODELS = ok_models

# We use an iterator to cycle through the authors in the conversation
def cycle_authors():
    idx = 0
    while True:
        yield AUTHORS[idx % len(AUTHORS)]
        idx += 1


def construct_author_prompt(author, book, module, content):
    """Constructs a prompt based on the author's perspective and expertise."""

    prompt_map = {
        "Luciano Ramalho": f"""From a Pythonic perspective, when considering "{module}" with features {content['features']}, here is my DDD design using Python's strengths\n\n```python\n\n""",
        "Vaughn Vernon": f"""From a Domain Driven Design standpoint, here is how the bounded context python "{module}" be shaped considering these features {content['features']}\n\n```python\n\n""",
        "David Thomas": f"""Given the tenets of The Pragmatic Programmer, this is my advice for implementing the React "{module}" with features {content['features']} in a maintainable and efficient manner\n\n```javascript\n\nimport React from 'react';\n\n""",
        "Andrew Hunt": f"""From a pragmatic perspective, here is how we ensure that the README "{module}" with features {content['features']} is both robust and user-centric\n\n```markdown\n\n"""
    }

    return f"{author} (author of {book}) '{prompt_map[author]}'"


def round_robin_models():
    """A generator that yields models in a round-robin fashion."""
    idx = 0
    while True:
        yield MODELS[idx % len(MODELS)]
        idx += 1

async def generate_template_with_model(model, prompt):
    try:
        result = await achat(model=model, prompt=prompt)
        print("Result: ", result)
    except Exception as e:
        print(f"Error: {e}")
        result = ""
    return result



async def process_data():
    results = []
    async with TaskGroup() as group:
        for module, content in data.items():
            for _ in AUTHORS:
                author, book = next(cycle_authors())
                model = next(round_robin_models())
                prompt = construct_author_prompt(author, book, module, content)
                results.append(await group.spawn(generate_template_with_model, model, prompt))
    return [await res for res in results]

def save_to_file(results):
    for i in range(0, len(results), 4):
        combined_result = "\n\n".join(results[i:i+4])
        with open(os.path.join("advanced", f"conversation_module_{i // 4 + 1}.md"), "w") as file:
            file.write(combined_result)

async def main():
    start = time.time()

    print("Generating Conversational Content...")
    results = await process_data()

    end = time.time()
    print(f"Total time taken: {end - start} seconds")

    save_to_file(results)

# Execute
curio.run(main())