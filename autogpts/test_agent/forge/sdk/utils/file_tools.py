import json
import re
from pathlib import Path
from time import gmtime, strftime

import anyio
import openai
import yaml
from icontract import require, ensure

from forge.sdk.utils.models import get_model


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


@require(lambda prompt: isinstance(prompt, str))
@ensure(lambda result: isinstance(result, str))
async def generate_filename(
    prompt,
    prefix="",
    suffix="",
    extension="txt",
    min_chars=20,
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


def extract_filename(text: str, allowed_extensions=None) -> str:
    """
    Extracts a filename from a text, aligning with Pythonic practices as advocated
    by Luciano Ramalho in "Fluent Python". It can also filter the search based on a list of allowed extensions.

    Args:
        text (str): The text from which to extract the filename.
        allowed_extensions (List[str], optional): A list of allowed file extensions (without the dot). Defaults to None.

    Returns:
        str: The extracted filename.

    Raises:
        ValueError: If no filename with allowed extensions is found.
    """

    # Create the regex pattern based on allowed extensions
    if allowed_extensions is None:
        allowed_extensions = ["py"]

    if allowed_extensions:
        pattern = rf'\b\w+[-\w]*\.({"|".join(allowed_extensions)})\b'
    else:
        pattern = r"\b\w+[-\w]*(\.\w+)\b"

    match = re.search(pattern, text)

    if match:
        return match.group(0)
    else:
        raise ValueError("No filename with allowed extensions found.")


async def read(filename, to_type=None):
    async with await anyio.open_file(filename, mode="r") as f:
        contents = await f.read()
    if to_type == "dict":
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            contents = yaml.safe_load(contents)
        elif filename.endswith(".json"):
            contents = json.loads(contents)
    return contents


async def write(
    contents=None, filename=None, mode="w+", extension="txt", time_stamp=False, path=""
):
    if extension == "yaml" or extension == "yml":
        contents = yaml.dump(
            contents, default_style="", default_flow_style=False, width=1000
        )
    elif extension == "json":
        contents = json.dumps(contents)

    if not filename:
        filename = await generate_filename(
            prompt=contents, extension=extension, time_stamp=time_stamp
        )

    async with await anyio.open_file(path+filename, mode=mode) as f:
        await f.write(contents)
    return filename


def extract_code(text: str) -> str:
    # Use a regular expression to find code blocks enclosed in triple backticks.
    text_code = re.findall(r"```([\s\S]+?)```", text)

    if not text_code:
        return text

    # Concatenate all the code blocks together with double newline separators.
    concatenated_code = "\n\n".join(
        [code[code.index("\n") + 1 :] for code in text_code]
    )

    return concatenated_code


# project root directory
# Path: src/utils/file_tools.py
def get_project_root() -> str:
    return str(Path(__file__).parent.parent.parent)


def main():
    print(get_project_root())


if __name__ == '__main__':
    main()
