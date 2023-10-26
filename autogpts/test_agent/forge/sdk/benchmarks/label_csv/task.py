from forge.sdk.utils.file_tools import write
from forge.sdk.utils.complete import create

task =  "The csv 'input.csv' has many items. Create a 'Color' column for these items and classify them as either 'blue', 'green', or 'yellow' depending on what the most likely color is. Use lowercase letters to classify and preserve the order of the rows. The color column should be the second column. Write the output in output.csv"

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
                                                  'After writing the code. Explain your implementation\n\n```python\n# Here is the '
                                                  'perfect example implementation that follows the task exactly\n',
                   max_tokens=2500, stop=['```'])

import anyio

async def main():
    await write(file_impl, 'io_csv.py')


if __name__ == '__main__':
    anyio.run(main)
