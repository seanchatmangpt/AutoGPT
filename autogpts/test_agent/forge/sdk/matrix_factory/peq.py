import os

import anyio
from redbaron import RedBaron


class PeqDef:
    def __init__(self, filepath):
        self.filepath = filepath
        self.red = None
        anyio.run(self._load_from_file)

    async def _load_from_file(self):
        if not os.path.exists(self.filepath):
            async with await anyio.open_file(self.filepath, "w") as f:
                await f.write("")
        async with await anyio.open_file(self.filepath, "r") as f:
            content = await f.read()
        if content.strip():
            self.red = RedBaron(content)
        else:
            self.red = RedBaron("")  # Initialize with an empty RedBaron instance

    async def _save_to_file(self, content):
        async with await anyio.open_file(self.filepath, "w") as f:
            await f.write(content)

    def __setitem__(self, key, value):
        new_func = RedBaron(value).find("def")

        if self.red:
            existing_func = self.red.find("def", name=key)
            if existing_func:
                existing_func.replace(new_func)
            else:
                self.red.append(new_func)

                # Add any imports from the new code at the top if they don't already exist
                for node in RedBaron(value):
                    if node.type == "import" or node.type == "from_import":
                        self.red.insert(0, node)
        else:
            self.red = RedBaron(value)

        anyio.run(self._save_to_file, self.red.dumps())


class PeqClass:
    def __init__(self, filepath):
        self.filepath = filepath
        self.red = None

        anyio.run(self._load_from_file)

    async def _load_from_file(self):
        # If the file doesn't exist, create it asynchronously
        if not os.path.exists(self.filepath):
            async with await anyio.open_file(self.filepath, "w") as f:
                await f.write("")
        async with await anyio.open_file(self.filepath, "r") as f:
            content = await f.read()
        if content.strip():
            self.red = RedBaron(content)
        else:
            self.red = RedBaron("")  # Initialize with an empty RedBaron instance

    async def _save_to_file(self, content):
        async with await anyio.open_file(self.filepath, "w") as f:
            await f.write(content)

    def __setitem__(self, key, value):
        new_class = RedBaron(value).find("class")

        if self.red:
            existing_class = self.red.find("class", name=key)
            if existing_class:
                existing_class.replace(new_class)
            else:
                self.red.append(new_class)

                # Add any imports from the new code at the top if they don't already exist
                for node in RedBaron(value):
                    if (
                        node.type == "import" or node.type == "from_import"
                    ) and not self.red.find_all(type=node.type, value=node.value):
                        self.red.insert(0, node)
        else:
            self.red = RedBaron(value)

        anyio.run(self._save_to_file, self.red.dumps())


# Test

test_filepath = "test_module.py"


peq = PeqDef(filepath=test_filepath)

# Adding a function with imports and decorator
peq[
    "decorated_function"
] = """
from functools import wraps

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Before function call')
        result = f(*args, **kwargs)
        print('After function call')
        return result
    return wrapper

@decorator
def decorated_function():
    print('Function body')
"""
#
# # Asserting the function was added
# with open(test_filepath, 'r') as f:
#     content = f.read()
#     assert "def decorated_function():" in content, "Function not found in the file."
#
# print("Function with imports and decorator added successfully!")
#
# test_filepath = 'test_module2.py'
#
# peq = PeqClass(filepath=test_filepath)
#
#
# # Adding a class
# peq["Person"] = """
# from dataclasses import dataclass
#
# @dataclass
# class Person:
#     name: str
#     age: int
# """
#
# # Asserting the class was added
# with open(test_filepath, 'r') as f:
#     content = f.read()
#     assert "class Person:" in content, "Class not found in the file."
#
# print("Class added successfully!")
#
# # Replacing the Person class
# peq["Person"] = """
# from dataclasses import dataclass
#
# @dataclass
# class Person:
#     full_name: str
#     birth_year: int
# """
#
#
# # Replacing the Person class
# peq["Dog"] = """
# @dataclass
# class Dog:
#     full_name: str
#     birth_year: int
# """
#
# # Asserting the class was replaced
# with open(test_filepath, 'r') as f:
#     content = f.read()
#     assert "full_name: str" in content, "Class attribute 'full_name' not found in the file."
#     assert "birth_year: int" in content, "Class attribute 'birth_year' not found in the file."
#
# print("Class replaced successfully!")
