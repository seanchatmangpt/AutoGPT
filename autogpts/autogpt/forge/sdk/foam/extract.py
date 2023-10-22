import re

from utils.file_tools import extract_code


def parse_code(response):
    """
    Parses code blocks from a string and extracts them as a list of dictionaries.

    Args:
        response (str): The input string containing code blocks.

    Returns:
        list: A list of dictionaries, each containing a 'key' and 'code' entry.
    """
    """
    Extracts multiple code blocks from a string and returns them as a single concatenated string.

    Args:
        response (str): The input string containing code blocks.

    Returns:
        str: A single string containing all the extracted code blocks concatenated together.
    """
    extract_code(response)


# Example usage:
response = """
Given the project description, here's a hypothetical DDD YAML schema for a software development process:

```yaml
aggregates:
- aggregate_business_functions:
  - contract:
      ensure:
      - condition: 'lambda result: result is not None'
      require:
      - condition: 'lambda developer, project: developer is not None and project is not None'
      definition: Assigns a developer to a project.
      name: AssignDeveloperToProject
      parameters:
      - parameter: developer
        type: Developer
      - parameter: project
        type: Project
    name: DeveloperActions
    
  entities:
  - business_functions:
    - contract:
        ensure:
        - condition: 'lambda result: result is not None'
        require:
        - condition: 'lambda story: story is not None'
      definition: Creates a story.
      name: CreateStory
      parameters:
      - parameter: storyDescription
        type: string
      - parameter: epic
        type: Epic
    definition: A Story entity that represents a unit of work on a Project.
    factories:
    - name: CreateStory
      parameters:
      - parameter: description
        type: string
      - parameter: epic
        type: Epic
    name: Story

  - business_functions:
    - contract:
        ensure:
        - condition: 'lambda result: result is True'
        require:
        - condition: 'lambda epic, project: epic is not None and project is not None'
      definition: Adds a new epic to the project.
      name: AddEpicToProject
      parameters:
      - parameter: epic
        type: Epic
      - parameter: project
        type: Project
    definition: An Epic entity that represents a larger chunk of work on a Project.
    factories:
    - name: CreateEpic
      parameters:
      - parameter: name
        type: string
      - parameter: description
        type: string
    name: Epic
    repositories:
    - methods:
      - name: find_by_name
        parameters:
        - parameter: name
          type: string
      name: EpicRepository

  root_entity: Project
  value_objects:
  - definition: A Developer value object
    name: Developer
    properties:
    - name: name
      type: string
    - name: skillSet
      type: string

  - definition: A Project value object
    name: Project
    properties:
    - name: name
      type: string
    - name: description
      type: string
    - name: team
      type: Team
```

Please note that this hypothetical DDD YAML schema follows the aggregate, entities and value object structure of DDD. More elements could be added to it based on the need of the project.
Wrote coala.yaml
```

End of file
"""

parsed_codes = parse_code(response)
print(parsed_codes)
