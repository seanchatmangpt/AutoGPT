import asyncio
import glob
import os
import importlib.util
import subprocess
from textwrap import dedent
from typing import Dict

from forge.sdk.abilities.code.radon_workbench import refactor_code
from forge.sdk.utils.complete import create
from forge.sdk.utils.create_prompts import create_python
from forge.sdk.utils.file_tools import write, extract_code
import inspect


class Tool:
    def __init__(self, name, description, filepath=""):
        self.name = name
        self.description = description
        self.filepath = filepath
        self.module = None


class PerfectProductionCodeAGI:
    def __init__(self):
        self.tools: Dict[str, Tool] = {}
        self.load_tools_from_folder()

    def load_tools_from_folder(self, folder_path="./tools/"):
        python_files = glob.glob(f"{folder_path}/*.py")
        for filepath in python_files:
            tool_name = os.path.basename(filepath).replace(".py", "")
            self.tools[tool_name] = Tool(
                name=tool_name,
                description=f"Loaded from {filepath}",
                filepath=filepath,
            )

    async def _generate_tool_code(self, tool_name: str):
        return await create_python(f"A full featured {tool_name} function")

    async def _save_tool_code(self, code: str, tool_name: str) -> str:
        filepath = await write(code, filename=f"./tools/{tool_name}.py")
        return filepath

    async def generate_and_save_tool(self, tool_name: str):
        code = await self._generate_tool_code(tool_name)
        filepath = await self._save_tool_code(code, tool_name)
        self.tools[tool_name] = Tool(tool_name, "Automatically generated tool", filepath)

    async def _load_module_from_file(self, filepath: str, tool_name: str):
        spec = importlib.util.spec_from_file_location(tool_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.tools[tool_name].module = module
        return module

    async def load_and_run_tool(self, tool_name: str):
        tool = self.tools.get(tool_name)
        if tool and os.path.exists(tool.filepath):
            return await self._load_module_from_file(tool.filepath, tool_name)

        await self.generate_and_save_tool(tool_name)
        return await self._load_module_from_file(self.tools[tool_name].filepath, tool_name)

    async def refactor_tool(self, tool_name: str):
        tool = self.tools.get(tool_name)
        error = """/Users/candacechatman/dev/test_agent/forge/tools/async_directory_walk.py:21: RuntimeWarning: coroutine 'to_thread' was never awaited
  async for root, dirs, files in asyncio.to_thread(os.walk, path):
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/Users/candacechatman/dev/test_agent/forge/tools/async_directory_walk.py", line 52, in <module>
    main()
  File "/Users/candacechatman/dev/test_agent/forge/tools/async_directory_walk.py", line 44, in main
    results = asyncio.run(async_directory_walk(path))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.6/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.6/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.6/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 653, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/candacechatman/dev/test_agent/forge/tools/async_directory_walk.py", line 21, in async_directory_walk
    async for root, dirs, files in asyncio.to_thread(os.walk, path):
TypeError: 'async for' requires an object with __aiter__ method, got coroutine
"""
        # code = create(inspect.getsource(tool.module) + error + "\nHow do test with command line test the main function with a python subprocess?", max_tokens=2000)
        code = create(inspect.getsource(tool.module) + error + "\nHow do I fix?", max_tokens=2000)

        code = extract_code(code)

        await write(code, filename=f"./tools/{tool_name}.py")



async def main():
    agi = PerfectProductionCodeAGI()
    loaded_module = await agi.load_and_run_tool("async_directory_walk")
    if loaded_module:
        print(f"Successfully loaded {loaded_module}")
        await agi.refactor_tool("async_directory_walk")


if __name__ == "__main__":
    # asyncio.run(main())

    filepath = "tools/async_directory_walk.py"

    result = subprocess.run(['python', filepath], stdout=subprocess.PIPE, text=True)

    # Print the output
    print(result.stdout)

    source = open(filepath).read()

    prompt = f"""
```python
# {filepath}
{source}
```

result = subprocess.run(['python', 'tools/async_directory_walk.py'], stdout=subprocess.PIPE, text=True)

# Print the output
print(result.stdout)

Returned output:
{result.stdout}

How do I fix?
"""


    instructions = create(prompt, max_tokens=2000, stop=["```"])

    print(instructions)
