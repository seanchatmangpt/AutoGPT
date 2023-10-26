import json

from forge.sdk.utils.file_tools import write
from forge.sdk.utils.complete import create

task = json.loads(open('data.json').read())['task']

with open('file1.csv', 'r') as f:
    # Read the lines and store them in a list
    lines = f.readlines()

file_impl = create("You are a Job Interview Example Creation AGI. Your task is implement the following "
                   "exactly:\n```task\n" + task + '```\n\nExpert Game Implementation for Job Interview by AGI '
                                                  'Simulations of Luciano Ramahlo from "Fluent Python" and David '
                                                  'Thomas and Andrew Hunt from "The Pragmatic Programmer". One line '
                                                  'docstring comment\n\nAlways ensure that functions return all '
                                                  'necessary data that callers might need for further operations. '
                                                  'Before finalizing a function, double-check if the return value '
                                                  'facilitates all intended interactions.  Make sure that all '
                                                  'variables are referenced properly. The instructions you are given '
                                                  'contain mistakes to throw you off. Use the standard library. '
                                                  'After writing the code. Explain your implementation. CSV Preview```csv\n'+ str(lines[:2]) + '```\n\n```python\n# Here is the '
                                                  'perfect example implementation that follows the task exactly\n',
                   max_tokens=2500, stop=['```'])

import anyio

async def main():
    await write(file_impl, 'io_csv.py')


if __name__ == '__main__':
    anyio.run(main)
