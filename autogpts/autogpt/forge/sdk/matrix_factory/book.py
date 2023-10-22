import os
import time
from anyio import run, create_task_group

from fgn.completion.complete import acreate
from matrix_factory.chat_helpers import best_models, ok_models
from matrix_factory.gen_full import data

AUTHORS = [
    ("Luciano Ramalho", "Fluent Python"),
    ("Vaughn Vernon", "Implementing Domain Driven Design"),
    ("David Thomas", "The Pragmatic Programmer"),
    ("Andrew Hunt", "The Pragmatic Programmer")
]

MODELS = best_models

def cycle_authors():
    idx = 0
    while True:
        yield AUTHORS[idx % len(AUTHORS)]
        idx += 1

def construct_author_prompt(author, book, module, content):
    prompt_map = {
        "Luciano Ramalho": f"""From a Pythonic perspective, when considering "{module}" with features {content['features']}, here is my DDD design using Python's strengths\n\n```python\n\n""",
        "Vaughn Vernon": f"""From a Domain Driven Design standpoint, here is how the bounded context python "{module}" be shaped considering these features {content['features']}\n\n```python\n\n""",
        "David Thomas": f"""Given the tenets of The Pragmatic Programmer, this is my advice for implementing the React "{module}" with features {content['features']} in a maintainable and efficient manner\n\n```javascript\n\nimport React from 'react';\n\n""",
        "Andrew Hunt": f"""From a pragmatic perspective, here is how we ensure that the README "{module}" with features {content['features']} is both robust and user-centric\n\n```markdown\n\n"""
    }

    return f"{author} (author of {book}) '{prompt_map[author]}'"

async def generate_template_with_model(model, prompt, results):
    try:
        result = await acreate(model=model, prompt=prompt, temperature=1.0, max_tokens=250)
        results.append(result)
    except Exception as e:
        print(f"Error: {e}")
        results.append("")

def round_robin_models():
    idx = 0
    while True:
        yield MODELS[idx % len(MODELS)]
        idx += 1

async def main():
    start = time.time()
    model_selector = round_robin_models()
    author_cycle = cycle_authors()
    results = []

    print("Generating Conversational Content...")

    async with create_task_group() as tg:
        for module, content in data.items():
            for _ in AUTHORS:
                author, book = next(author_cycle)
                model = next(model_selector)
                prompt = construct_author_prompt(author, book, module, content)
                tg.start_soon(generate_template_with_model, model, prompt, results)

    end = time.time()
    print(f"Total time taken: {end - start} seconds")

    for i in range(0, len(results), 4):
        combined_result = "\n\n".join(results[i:i+4])
        with open(os.path.join("advanced", f"conversation_module_{i // 4 + 1}.md"), "w") as file:
            file.write(combined_result)

run(main)
