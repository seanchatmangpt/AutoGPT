import yaml


def extract_yaml(markdown):
    """Extracts YAML from a Markdown string."""
    start = markdown.find("---")
    end = markdown.find("---", start + 1)
    yaml_string = markdown[start + 3 : end]
    return yaml.load(yaml_string)
