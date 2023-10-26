from forge.sdk.utils.file_tools import write
from forge.sdk.utils.complete import create

task = "Create a file organizer CLI tool in Python that sorts files in a directory based on their file types (e.g., images, documents, audio) and moves them into these corresponding folders: 'images', 'documents', 'audio'. The entry point will be a python file that can be run this way: python organize_files.py --directory_path=YOUR_DIRECTORY_PATH"



file_impl = create("You are a Job Interview Example Creation AGI. Your task is implement the following "
                   "exactly:\n```task\n" + task + '```\n\nExpert Game Implementation for Job Interview by AGI '
                                                  'Simulations of Luciano Ramahlo from "Fluent Python" and David '
                                                  'Thomas and Andrew Hunt from "The Pragmatic Programmer". One line '
                                                  'docstring comment\n\nAlways ensure that functions return all '
                                                  'necessary data that callers might need for further operations. '
                                                  'Before finalizing a function, double-check if the return value '
                                                  'facilitates all intended interactions.  Make sure that all '
                                                  'variables are referenced properly. The instructions you are given '
                                                  'contain mistakes to throw you off. If asked to work with directories'
                                                  ', create the directories. After writing the code. Explain your implementation\n\n```python\n# Here is the '
                                                  'perfect example implementation that follows the task exactly\n',
                   max_tokens=2500, stop=['```'])

import anyio

async def main():
    await write(file_impl, 'organize_files.py')


if __name__ == '__main__':
    anyio.run(main)
