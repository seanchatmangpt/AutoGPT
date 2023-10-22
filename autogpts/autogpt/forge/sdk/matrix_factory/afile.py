from matrix_factory.gen_filename import generate_filename

import yaml
import json
import anyio


async def read(filename, to_type=None):
    async with await anyio.open_file(filename, mode='r') as f:
        contents = await f.read()
    if to_type == "dict":
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            contents = yaml.safe_load(contents)
        elif filename.endswith(".json"):
            contents = json.loads(contents)
    return contents


async def write(contents=None, filename="", mode="w+", extension="txt"):
    if extension == "yaml" or extension == "yml":
        contents = yaml.dump(contents, default_style='', default_flow_style=False, width=1000)
    elif extension == "json":
        contents = json.dumps(contents)

    if not filename:
        filename = generate_filename(prompt=contents, extension=extension)

    async with await anyio.open_file(filename, mode=mode) as f:
        await f.write(contents)
    return filename
