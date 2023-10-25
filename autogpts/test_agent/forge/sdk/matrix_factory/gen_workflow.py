import os
import os
import time
import yaml
import asyncio
from jinja2 import Environment, FileSystemLoader

from fgn.completion.chat import achat
from fgn.completion.complete import acreate
from matrix_factory.afile import write, read
from matrix_factory.chat_helpers import best_models, ok_models, chat_models
from matrix_factory.gen_full import data
import yaml
from lchop.context.work_context import default_work_context, load_workflow
from lchop.tasks.template_tasks import *
from lchop.tasks.home_task_execution_results import *

from matrix_factory.gen_full import data

given_input = data

prompt = f"""
Objective:
Transform the given input (whether it's Python code, project documentation, or another form of structured data) into a workflow YAML format matching the specified structure.

Sample Output:
```yaml
workflow:
  - name: "installation"
    description: "To install the project, follow these steps:"
    params:
      clone_command: "git clone https://link-to-project"
      navigate_command: "cd project-directory"
  - name: "fetch_items"
    description: "Endpoint to fetch all items."
    params:
      method: "GET"
      endpoint: "/api/items"
```

Given Input:
{given_input}

Using the provided guidelines, transform the given input into the desired YAML format.
```yaml\n
"""


async def main():
    # abs_path = os.path.abspath(__file__)

    # wf_path = os.path.join()
    # gen_path = os.path.join()
    #
    # result = generate_task_code_from_workflow(
    #     wf_path, gen_path, default_work_context()
    # )
    # print(result)
    print("Generating workflow...")
    result = await acreate(
        prompt=prompt, model=best_models[0], stop=["```"], max_tokens=2500
    )
    # result = await achat(prompt=prompt, model=chat_models[-1])
    # result = "workflow:\n" + result
    # print(result)

    await write(
        result,
        "/Users/candacechatman/dev/linkml-projects/matrix-factory/src/matrix_factory/home_page_workflow.yaml",
    )

    # result = await read(")

    print("Generating tasks...")
    # result = await generate_task_code_from_workflow(workflow=result, task_code_path=None, work_ctx=default_work_context())
    # print(result)
    await load_workflow(
        filepath="/Users/candacechatman/dev/linkml-projects/matrix-factory/src/lchop/workflows/generate_workflow_workflow.yaml"
    )
    print("Done.")


async def main2():
    workflow = await read("home_page_workflow.yaml")
    print(workflow)
    await load_workflow(yaml_string=workflow)


# Example usage
if __name__ == "__main__":
    asyncio.run(main2())
