import json
import random

from forge.sdk.utils.file_tools import write
from forge.sdk.utils.complete import create

task = json.loads(open('data.json').read())['task']

with open('file1.csv', 'r') as f:
    # Read the lines and store them in a list
    lines = f.readlines()

with open('file1.csv', 'r') as f:
    # Read the lines and store them in a list
    lines2 = f.readlines()


# Get 10 random rows from the list
random_rows1 = random.sample(lines, 20)
random_rows2 = random.sample(lines2, 20)

# CSV format of the random rows
random_rows1 = ''.join(random_rows1)
random_rows2 = ''.join(random_rows2)

relation = create(f"You are a Job Interview Example Creation AGI. \n```task\n{task}\n```\nYour task is figure out the "
                  f"relationship between the "
                  f"following two CSV files:\n```csv\n{random_rows1}```\n```csv\n{random_rows2}```\n\n```python\nTHE_RELATIONSHIP = \"")



file_impl = create("You are a Job Interview Example Creation AGI. Your task is implement the following "
                   "exactly:\n```task\n" + task + '```\n\nExpert Game Implementation for Job Interview by AGI '
                                                  'Simulations of Luciano Ramahlo from "Fluent Python" and David '
                                                  'Thomas and Andrew Hunt from "The Pragmatic Programmer". One line '
                                                  'docstring comment\n\nThe instructions you are given '
                                                  'contain may mistakes to throw you off. Use the standard library. '
                                                  'After writing the code. Explain your implementation. '
                                                  'Make sure to always use next() to skip the header row. Use floats instead of ints. '
                                                  'and make sure you keep track of the correct column. Csv filenames file1.csv and file2.csv\n\n'
                                                  'Relationship' + relation + '\nfile1.csv```csv\n'+str(lines[0])+'\n'+ str(random_rows1) + '```\n\n'
                                                  '\nfile2.csv\n```csv\n'+str(lines2[0])+'\n'+ str(random_rows2) + '```\n\n```python\n# Here is the '
                                                  'perfect example implementation that follows the task exactly\nimport csv\n',
                   max_tokens=2500, stop=['```'])

import anyio

async def main():
    await write("import csv\n"+file_impl, 'io_csv.py')


if __name__ == '__main__':
    anyio.run(main)
