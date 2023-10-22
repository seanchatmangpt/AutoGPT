import json
import re
from pathlib import Path
from time import gmtime, strftime

import anyio
import openai
import yaml

from .models import get_model

# async def generate_extension(
#         prompt,
#         prefix="",
#         suffix="",
#         min_chars=30,
#         max_chars=60,
#         char_limit=300,
#         time_stamp=False,
#         **completion_kwargs
# ) -> str:
#     prompt = prompt[:char_limit]
#
#     completion_prompt = (
#         f"Generate an appropriate file extension based on the text: '{prompt}'. "
#     )
#
#     await acreate(prompt=completion_prompt)
#
#
#
#     extension = response.choices[0].text.strip()
#
#     # Post-process the extension
#     extension = re.sub(r"[^a-zA-Z0-9_]", "", extension)
#
#     file_name = ""
#     if prefix:
#         file_name = f"{prefix}_{file_name}"
#
#     if suffix:
#         file_name = f"{file_name}_{suffix}"
#
#     if time_stamp:
#         file_name = f"{file_name}_{strftime('%Y-%m-%d_%H-%M-%S', gmtime())}"
#
#     if extension:
#         file_name = f"{file_name}.{extension}"
#
#     return file_name


async def generate_filename(
    prompt,
    prefix="",
    suffix="",
    extension="txt",
    min_chars=30,
    max_chars=60,
    char_limit=300,
    time_stamp=False,
    **completion_kwargs,
) -> str:
    prompt = prompt[:char_limit]

    completion_prompt = (
        f"Generate a concise filename based on the text: '{prompt}'. "
        f"The filename should:\n"
        f"- Be in lowercase letters.\n"
        f"- Have at least {min_chars} characters.\n"
        f"- Have at most {max_chars} characters.\n"
        f"- Use underscores as separators.\n"
        f"- Exclude file extensions.\n"
        "Suggested filename:"
    )

    response = await openai.Completion.acreate(
        model=get_model("3i"),
        prompt=completion_prompt,
        temperature=0,
        max_tokens=max_chars * 2,
        stop=["\n"],
    )

    file_name = response.choices[0].text.strip()

    # Post-process the filename
    file_name = re.sub(r"[^a-zA-Z0-9_]", "", file_name)
    file_name = file_name[:max_chars]

    if prefix:
        file_name = f"{prefix}_{file_name}"

    if suffix:
        file_name = f"{file_name}_{suffix}"

    if time_stamp:
        file_name = f"{file_name}_{strftime('%Y-%m-%d_%H-%M-%S', gmtime())}"

    if extension:
        file_name = f"{file_name}.{extension}"

    return file_name


async def read(filename, to_type=None):
    async with await anyio.open_file(filename, mode="r") as f:
        contents = await f.read()
    if to_type == "dict":
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            contents = yaml.safe_load(contents)
        elif filename.endswith(".json"):
            contents = json.loads(contents)
    return contents


async def write(contents=None, filename=None, mode="w+", extension="txt"):
    if extension == "yaml" or extension == "yml":
        contents = yaml.dump(contents, default_style="", default_flow_style=False, width=1000)
    elif extension == "json":
        contents = json.dumps(contents)

    if not filename:
        filename = generate_filename(prompt=contents, extension=extension)

    async with await anyio.open_file(filename, mode=mode) as f:
        await f.write(contents)
    return filename


def extract_code(text: str) -> str:
    # Use a regular expression to find code blocks enclosed in triple backticks.
    text_code = re.findall(r"```([\s\S]+?)```", text)

    # If no code blocks are found, return an empty string.
    if not text_code:
        return ""

    # Concatenate all the code blocks together with double newline separators.
    concatenated_code = "\n\n".join([code[code.index("\n") + 1 :] for code in text_code])

    return concatenated_code


# project root directory
# Path: src/utils/file_tools.py
def get_project_root() -> str:
    return str(Path(__file__).parent.parent)
