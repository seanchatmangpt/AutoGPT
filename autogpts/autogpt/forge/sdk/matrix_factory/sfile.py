from fgn.utils.llm_operations import generate_filename
import yaml
import json


def read(filename, to_type=None):
    with open(filename, mode='r') as f:
        contents = f.read()
    if to_type == "dict":
        # Check the extension
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            contents = yaml.safe_load(contents)
        elif filename.endswith(".json"):
            contents = json.loads(contents)

    return contents


def write(contents=None, filename="", mode="w+", extension="txt"):
    # the extension is yaml then try to convert the contents to yaml
    if extension == "yaml" or extension == "yml":
        contents = yaml.dump(contents, default_style='', default_flow_style=False, width=1000)
    elif extension == "json":
        contents = json.dumps(contents)

    if not filename:
        filename = generate_filename(prompt=contents, extension=extension)

    with open(filename, mode=mode) as f:
        f.write(contents)
    return filename
