# Importing standard library modules.
# Importing built-in functions.

# Defining the list of features.
features = [
    'Debugging tools',
    'Code completion',
    'Automatic code generation',
    'Task Management',
    'Task assignment and tracking',
    'Integration with version control systems'
]

# Defining the list of scenarios for each feature.
# Using a dictionary to group the scenarios by feature.
scenarios = {
    'Debugging tools': [
        'The system should provide tools for debugging Python code, such as breakpoints and stepping through code'
    ],
    'Code completion': [
        'As a developer, I want the IDE'
    ],
    'Automatic code generation': [
        'The system should automatically generate code based on the parsed task descriptions, reducing the amount of'
    ],
    'Task Management': [
        'The system should allow users to create, assign, and prioritize tasks',
        'Users'
    ],
    'Task assignment and tracking': [
        'The system should allow users to assign tasks to specific team members and track their progress'
    ],
    'Integration with version control systems': [
        'The system should integrate with version control systems for seamless collaboration and code versioning'
    ]
}

# Defining the list of metrics and reports for each feature.
# Using a dictionary to group the metrics and reports by feature.
reports = {
    'Debugging tools': [
        'Code complexity',
        'Lines of code',
        'Test coverage'
    ],
    'Code completion': [
        'Code complexity',
        'Execution time',
        'Memory usage',
        'Other relevant performance metrics'
    ],
    'Automatic code generation': [
        'Code complexity',
        'Code coverage',
        'Memory usage'
    ],
    'Task Management': [
        'Code complexity',
        'Code coverage',
        'Execution time'
    ],
    'Task assignment and tracking': [
        'Code complexity',
        'Code coverage',
        'Execution time'
    ],
    'Integration with version control systems': [
        'Code complexity',
        'Code coverage',
        'Execution time'
    ]
}

# Defining the list of tasks for the Task Management feature.
tasks = [
    'Create tasks',
    'Assign tasks',
    'Prioritize tasks'
]

# Defining the engine function that takes in a list of features, scenarios, reports, and tasks.
def engine(features, scenarios, reports, tasks):
    # Iterating through each feature.
    for feature in features:
        # Printing the feature name.
        print(f'Feature: {feature}')
        # Iterating through each scenario for the current feature.
        for scenario in scenarios[feature]:
            # Printing the scenario.
            print(f'Scenario: {scenario}')
        # Checking if the current feature is Task Management.
        if feature == 'Task Management':
            # Iterating through each task.
            for task in tasks:
                # Printing the task.
                print(f'Scenario: Users should be able to {task}.')
        # Iterating through each metric or report for the current feature.
        for metric in reports[feature]:
            # Printing the metric or report.
            print(f'  - {metric}.')
        # Adding an empty line for formatting.
        print()

# Calling the engine function with the defined lists.
engine(features, scenarios, reports, tasks)