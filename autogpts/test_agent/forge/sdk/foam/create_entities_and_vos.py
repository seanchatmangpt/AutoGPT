# I have IMPLEMENTED your PerfectPythonProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION code of your requirements.
from textwrap import dedent, indent
from typing import Dict, List, Set

import autopep8
import inflection
import yaml
from icontract import ensure, require
from jinja2 import Environment, FileSystemLoader, select_autoescape

from foam.pickle_cache import auto_lru_cache
from llm.complete import create as llm_create
from py_module import PyModule
from typetemp.environment.typed_environment import TypedEnvironment
from utils.file_tools import get_project_root


def setup_jinja_environment(template_folder_path: str) -> Environment:
    return TypedEnvironment(
        loader=FileSystemLoader(template_folder_path),
        autoescape=select_autoescape(["html", "xml"]),
    )


env = setup_jinja_environment(get_project_root() + "/foam/templates")

from redbaron import RedBaron


@auto_lru_cache
def create(
    prompt: str,
    model="3i",
    temperature=0,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
):
    print("Creating...")
    return llm_create(
        prompt=prompt,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
    )


def generate_example_code(module: PyModule, context: dict) -> str:
    template = env.get_template("example_business_function_prompt.jinja")

    prompt = template.render(context)

    # example_code = create(prompt, stop=["```", "\n\n"], max_tokens=1000)
    example_code = create(prompt, stop=["```"], max_tokens=2000)
    example_code = autopep8.fix_code(example_code)

    defs = RedBaron(example_code).find_all("def")
    # print(indent(example_code, "    "))

    for node in defs:
        module[node.name] = node.dumps()
    # module.save()


def replace_placeholder_with_example(module: PyModule, value_objects):
    # Locate placeholder comments
    for function_node in module.red.find_all("DefNode"):
        if "__" in function_node.name:
            continue

        # Get the source of the entire function
        context = {
            "module_source": str(module),
            "function_source": function_node.dumps(),
            "function_name": function_node.name,
            "value_objects": value_objects,
        }

        generate_example_code(module, context)


def prepare_import_statements(spec: Dict) -> Dict[str, List[str]]:
    """
    Prepare import statements for each entity and value object.
    """
    import_statements = {}

    all_entities = {e["name"] for e in spec.get("entities", [])}
    all_value_objects = {v["name"] for v in spec.get("value_objects", [])}

    for entity in all_entities:
        imports_for_entity = set()  # Use a set to avoid duplicates

        # Get business functions for the entity
        bfs_for_entity = [bf for bf in spec.get("business_functions", []) if bf["entity"] == entity]

        for bf in bfs_for_entity:
            parameters = bf.get("parameters", [])
            for param in parameters:
                param_type = param["type"]
                if param_type in all_entities:
                    imports_for_entity.add(
                        f"from .{inflection.underscore(param_type)} import {param_type}"
                    )
                if param_type in all_value_objects:
                    imports_for_entity.add(
                        f"from ..value_objects.{inflection.underscore(param_type)} import {param_type}"
                    )

        # Convert the set to a list for easier usage in templates
        import_statements[entity] = list(imports_for_entity)

    for value_object in all_value_objects:
        value_object_imports = set()
        properties = [p for p in spec.get("value_objects", []) if p["name"] == value_object][0].get(
            "properties", []
        )
        for prop in properties:
            if "List" in prop["type"]:
                value_object_imports.add("from typing import List")

        import_statements[value_object] = list(value_object_imports)

    return import_statements


@require(lambda spec: spec is not None and len(spec) > 0, "yaml_path must not be empty")
@ensure(lambda result: all(code for code in result), "All rendered code must be non-empty")
def generate_entities_and_functions(spec: dict, import_statements: dict, value_objects: dict):
    template = env.get_template("entity_with_business_function_template.jinja")

    # Parse each Entity and its associated Business Functions
    for entity in spec.get("entities", []):
        entity_name = entity.get("name")
        entity_definition = entity.get("definition")

        business_functions_for_entity = [
            bf for bf in spec.get("business_functions", []) if bf.get("entity") == entity_name
        ]

        context = {
            "entity_name": entity_name,
            "entity_definition": entity_definition,
            "business_functions": business_functions_for_entity,
            "import_statements": import_statements.get(entity_name, []),
        }

        # Render the code for each entity
        code = template.render(context)

        module = PyModule(f"./entities/{inflection.underscore(entity_name)}.py", code)
        module.save()

        replace_placeholder_with_example(module, value_objects)


def generate_value_objects(spec, import_statements: dict) -> dict:
    template = env.get_template("value_object_template.jinja")

    rendered_classes = {}

    for value_object in spec.get("value_objects", []):
        value_object_name = value_object.get("name")
        value_object_definition = value_object.get("definition")
        value_object_properties = value_object.get("properties")

        context = {
            "value_object_name": value_object_name,
            "value_object_definition": value_object_definition,
            "properties": value_object_properties,
            "import_statements": import_statements.get(value_object_name, []),
        }

        code = template.render(context)

        module = PyModule(f"./value_objects/{inflection.underscore(value_object_name)}.py", code)
        module.save()

        rendered_classes[value_object_name] = code

    return rendered_classes


def write_file(directory: str, file_name: str, code: str):
    with open(f"{directory}/{inflection.underscore(file_name)}.py", "w") as file:
        file.write(code)


def main(spec: dict):
    try:
        import_statements = prepare_import_statements(spec)

        value_objects = generate_value_objects(spec, import_statements)

        entities = generate_entities_and_functions(spec, import_statements, value_objects)

        print("Code generation successful.", value_objects, entities)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Load YAML content
    with open("software_domain.yaml", "r") as file:
        software_domain_spec = yaml.safe_load(file)
    main(software_domain_spec)
