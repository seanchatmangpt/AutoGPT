from collections import defaultdict

from fgn.completion.complete import create
from matrix_factory.sfile import write, read

# original_yaml = """language_llm:
#   core_component: 'Processed ["Wrote to hello_world.txt", "Read from hello_world.txt", "Deleted hello_world.txt"]'
#
# memory_modules:
#   ShortTermWorkingMemory:
#     data: ['Wrote to hello_world.txt', 'Read from hello_world.txt', 'Deleted hello_world.txt']
#   LongTermMemories:
#     Episodic:
#       episodes: ['Met with John', 'Attended PyCon 2023', 'Wrote a research paper on AGI']
#     Semantic:
#       knowledge:
#         'Luciano Ramalho': 'Author of Fluent Python',
#         'Python': 'An interpreted, high-level, general-purpose programming language.',
#         'Domain Driven Design': 'An approach to software design and development.'
#     Procedural:
#       procedures:
#         'file_creation': 'Use the open method with the "w" flag.',
#         'file_reading': 'Use the open method with the "r" flag.',
#         'file_deletion': 'Use the os.remove method.'
#
# action_space:
#   ExternalActions:
#     Grounding:
#       physical_environments: 'Interaction with physical environment simulated. E.g., Robots, IoT devices.'
#       dialogue_with_humans_or_other_agents: 'Simulated dialogue system with humans or other agents.'
#       digital_environments: 'Interaction with software systems, APIs, and other digital tools.'
#   InternalActions:
#     retrieval: 'Use keys to retrieve data from memory stores.',
#     reasoning: 'Process data, derive conclusions or inferences.',
#     learning: 'Ingest new data into memory based on experiences.'
#
# decision_making:
#   planning:
#     proposal: 'Propose a set of possible actions based on input data.',
#     evaluation: 'Evaluate the feasibility and effectiveness of proposed actions.',
#     selection: 'Select the best action based on evaluation metrics.'
#   execution:
#     status: 'Executed the plan of reading the file hello_world.txt and processing its content.',
#     result: 'Successfully processed the data and stored the result in memory.'
# """
#
# modified_yaml = """language_llm:
#   core_component: 'Processed ["Wrote to hello_world.txt", "Read from hello_world.txt", "Deleted hello_world.txt", "Initialized Flask React CRUD application", "Configured Flask backend", "Set up React frontend", "Implemented CRUD operations"]'
#
# memory_modules:
#   ShortTermWorkingMemory:
#     data: ['Wrote to hello_world.txt', 'Read from hello_world.txt', 'Deleted hello_world.txt', 'Initialized Flask React CRUD application', 'Configured Flask backend', 'Set up React frontend', 'Implemented CRUD operations']
#   LongTermMemories:
#     Episodic:
#       episodes: ['Met with John', 'Attended PyCon 2023', 'Wrote a research paper on AGI', 'Created a Flask React CRUD application']
#     Semantic:
#       knowledge:
#         'Luciano Ramalho': 'Author of Fluent Python',
#         'Python': 'An interpreted, high-level, general-purpose programming language.',
#         'Domain Driven Design': 'An approach to software design and development.',
#         'Flask': 'A micro web framework written in Python.',
#         'React': 'A JavaScript library for building user interfaces.'
#     Procedural:
#       procedures:
#         'file_creation': 'Use the open method with the "w" flag.',
#         'file_reading': 'Use the open method with the "r" flag.',
#         'file_deletion': 'Use the os.remove method.',
#         'flask_app_initialization': 'Use Flask to initialize a new application.',
#         'react_app_initialization': 'Use create-react-app to set up a new React application.',
#         'crud_implementation': 'Implement Create, Read, Update, Delete operations for the application.'
#
# action_space:
#   ExternalActions:
#     Grounding:
#       physical_environments: 'Interaction with physical environment simulated. E.g., Robots, IoT devices.'
#       dialogue_with_humans_or_other_agents: 'Simulated dialogue system with humans or other agents.'
#       digital_environments: 'Interaction with software systems, APIs, and other digital tools.'
#   InternalActions:
#     retrieval: 'Use keys to retrieve data from memory stores.',
#     reasoning: 'Process data, derive conclusions or inferences.',
#     learning: 'Ingest new data into memory based on experiences.'
#
# decision_making:
#   planning:
#     proposal: 'Propose a set of possible actions based on input data.',
#     evaluation: 'Evaluate the feasibility and effectiveness of proposed actions.',
#     selection: 'Select the best action based on evaluation metrics.'
#   execution:
#     status: 'Executed the plan of creating a Flask React CRUD application along with previous actions.',
#     result: 'Successfully initialized and set up a CRUD application and stored the related actions in memory.'
# """

import yaml


def yaml_diff(yaml1, yaml2):
    """
    Compare two YAML strings and return the differences.

    Parameters:
    - yaml1 (str): First YAML string
    - yaml2 (str): Second YAML string

    Returns:
    - dict: Differences between the two YAMLs
    """
    # Parse the YAML strings
    data1 = yaml.safe_load(yaml1)
    data2 = yaml.safe_load(yaml2)

    # Recursive function to compare dictionaries
    def compare_dicts(dict1, dict2):
        diff = {}
        for key in dict1.keys() | dict2.keys():
            if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
                # If both values are dictionaries, recursively compare them
                sub_diff = compare_dicts(dict1.get(key, {}), dict2.get(key, {}))
                if sub_diff:
                    diff[key] = sub_diff
            else:
                if dict1.get(key) != dict2.get(key):
                    # If values are different, record the difference
                    diff[key] = {
                        'yaml_str1': dict1.get(key),
                        'yaml_str2': dict2.get(key)
                    }
        return diff

    # Use the recursive function to compare the top-level dictionaries
    differences = compare_dicts(data1, data2)

    return differences


# differences = yaml_diff(original_yaml, modified_yaml)
# for key, (original_value, modified_value) in differences.items():
#     print(f"Path: {key}\nOriginal Value: {original_value}\nModified Value: {modified_value}\n")

def fix_yaml(bad_yaml):
    return create(prompt=f"Fix the following YAML:\n\n```yaml\n{bad_yaml}\n\n```yaml\n", stop=["```"], max_tokens=2000)


# fixed_yaml = fix_yaml(original_yaml)

# write(fixed_yaml, "/Users/candacechatman/dev/linkml-projects/matrix-factory/src/matrix_factory/first_agent_state.yaml")

# fixed_yaml = fix_yaml(modified_yaml)

# write(fixed_yaml, "/Users/candacechatman/dev/linkml-projects/matrix-factory/src/matrix_factory/second_agent_state.yaml")

original_yaml = read("/Users/candacechatman/dev/linkml-projects/matrix-factory/src/matrix_factory/first_agent_state.yaml")

modified_yaml = read("/Users/candacechatman/dev/linkml-projects/matrix-factory/src/matrix_factory/second_agent_state.yaml")

write(yaml_diff(original_yaml, modified_yaml), filename="diff.yaml", extension="yaml")

print(read("diff.yaml", to_type="dict"))


import anyio

"""What is the starting state of this agent?"""

anyio.