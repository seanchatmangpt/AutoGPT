"""foam CLI."""
import typer
import yaml
from icontract import ensure, require
from jinja2 import Environment, FileSystemLoader
from loguru import logger

app = typer.Typer()


@app.command()
def say(message: str = "") -> None:
    """Say a message."""
    typer.echo(message)


# Logger Initialization
logger.add("enterprise_log.log")
logger.info("Logger Initialized.")


# 1. YAML Reader
@require(lambda file_path: file_path is not None and len(file_path) > 0)
@ensure(lambda result: result is not None)
def read_yaml(file_path: str):
    """
    Reads a YAML file into Python objects.
    """
    logger.info(f"Reading YAML file from {file_path}")
    with open(file_path, "r") as file:
        result = yaml.safe_load(file)
    logger.info("Finished reading YAML file.")
    return result


# 2. Jinja Template Loader
@require(lambda template_folder: template_folder is not None and len(template_folder) > 0)
def load_jinja_templates(template_folder: str) -> Environment:
    """
    Loads Jinja2 templates from a specified folder.
    """
    logger.info(f"Loading Jinja templates from {template_folder}")
    env = Environment(loader=FileSystemLoader(template_folder))
    logger.info("Finished loading Jinja templates.")
    return env


# 3. DDD Object Creation (Omitted due to complexity)
# ... (Convert YAML data into DDD Python objects)


# 4. Code Generator
@require(lambda yaml_object, template_env: yaml_object is not None and template_env is not None)
def generate_code(yaml_object, template_env: Environment):
    """
    Generates code from the DDD Python objects using Jinja templates.
    """
    logger.info("Generating code.")
    for key, value in yaml_object.items():
        template = template_env.get_template(f"{key}.j2")
        yield template.render(value)


# 5. File Writer
@require(lambda code_snippets, output_path: code_snippets is not None and output_path is not None)
def write_to_disk(code_snippets, output_path: str):
    """
    Writes the generated code snippets to disk.
    """
    logger.info("Writing code snippets to disk.")
    for snippet in code_snippets:
        with open(output_path, "w") as f:
            f.write(snippet)
    logger.info("Finished writing to disk.")


# 6. Testing Setup (Omitted, as pytest will be used externally)

# 7. Automated Tests (Omitted, as pytest will be used externally)


# 8. Main Execution
@app.command()
def main(yaml_file_path: str, template_folder_path: str, output_folder_path: str):
    """
    Ties all components together to execute end-to-end.
    """
    logger.info("Main execution started.")

    # Read YAML
    domain_definitions = read_yaml(yaml_file_path)

    # Load Templates
    env = load_jinja_templates(template_folder_path)

    # Generate Code
    code_snippets = generate_code(domain_definitions, env)

    # Write to Disk
    write_to_disk(code_snippets, output_folder_path)

    logger.info("Main execution completed.")


if __name__ == "__main__":
    app()
