from collections import namedtuple

CodeImprovement = namedtuple('CodeImprovement', ['suggestion', 'code'])

# File structure
# - 'Features'
# - 'Metrics and Reports'
# - 'Tasks'

# Features
features = ['Code Generation Engine', 'Code Completion in IDE', 'Code Profiling and Optimization Tools',
            'User-Friendly Error Messages', 'Task Assignment and Tracking', 'User Authentication',
            'Task Prioritization', 'Task Scheduling']

# Suggestions for code improvements
code_improvements = [
    CodeImprovement('Use standard library and built-in functions', 'import'),
    CodeImprovement('Use functional programming without classes', 'def'),
    CodeImprovement('Leverage Python features effectively', 'with'),
    CodeImprovement('Ensure code is idiomatic and concise', 'lambda'),
    CodeImprovement('Use relevant performance metrics to improve code quality', 'metrics'),
    CodeImprovement('Implement user authentication for secure access', 'if-else'),
    CodeImprovement('Allow users to rank tasks in order of importance', 'sorted'),
    CodeImprovement('Create a clear and concise error message for system errors', 'raise')
]

# Metrics and Reports
metrics = ['Execution Time', 'Memory Usage', 'Code Complexity', 'Code Coverage']

# Tasks
tasks = ['Code Generation from Python', 'Code Completion Suggestions', 'Profiling and Optimization',
         'Error Message Generation', 'Task Assignment and Tracking', 'User Authentication',
         'Task Prioritization', 'Task Scheduling']

# Features
print('Features:')
for feature in features:
    print('- {}'.format(feature))

# Suggestions for code improvements
print('\nCode Improvements:')
for improvement in code_improvements:
    print('- {}: {}'.format(improvement.suggestion, improvement.code))

# Metrics and Reports
print('\nMetrics:')
for metric in metrics:
    print('- {}'.format(metric))

# Tasks
print('\nTasks:')
for task in tasks:
    print('- {}'.format(task))