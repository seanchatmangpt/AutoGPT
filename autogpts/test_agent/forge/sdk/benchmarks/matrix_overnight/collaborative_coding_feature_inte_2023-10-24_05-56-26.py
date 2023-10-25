# Collaborative coding feature
def collaborative_coding(code):
    """
    Generates code for collaborative coding feature.
    :param code: Original code to be edited and collaborated on.
    :return: Edited and optimized code.
    """
    suggestions = optimize(code)
    return suggestions


# Integration with machine learning libraries feature
def generate_metrics(metrics):
    """
    Generates and displays specified metrics in a user-friendly format.
    :param metrics: Metrics to be generated and displayed.
    :return: User-friendly display of generated metrics.
    """
    results = generate_metrics(metrics)
    display_results(results)


# Project management and task assignment feature
def assign_task(task, team_member):
    """
    Assigns a task to a team member.
    :param task: Task to be assigned.
    :param team_member: Team member to assign task to.
    :return: None
    """
    team_member.task = task


def track_progress(team_member):
    """
    Tracks the progress of a team member's assigned task.
    :param team_member: Team member whose progress is being tracked.
    :return: Progress of assigned task.
    """
    return team_member.task.progress


# User authentication feature
def authenticate_user(username, password):
    """
    Authenticates a user's identity.
    :param username: Username of user.
    :param password: Password of user.
    :return: Boolean indicating if authentication was successful.
    """
    if username == "admin" and password == "password":
        return True
    else:
        return False


# Collaborative code editing feature
def edit_code(code):
    """
    Allows multiple developers to simultaneously edit and collaborate on code.
    :param code: Original code to be edited.
    :return: Edited and optimized code.
    """
    suggestions = optimize(code)
    return suggestions


def optimize(code):
    """
    Offers suggestions to optimize code for performance and maintainability.
    :param code: Original code to be optimized.
    :return: Optimized code.
    """
    suggestions = analyze_code(code)
    suggestions = refactor_code(suggestions)
    return suggestions


def analyze_code(code):
    """
    Generates metrics and reports on code complexity, code coverage, and performance benchmarks.
    :param code: Code to be analyzed.
    :return: Metrics and reports on code.
    """
    complexity = calculate_complexity(code)
    coverage = calculate_coverage(code)
    performance = calculate_performance(code)
    return (complexity, coverage, performance)


def refactor_code(suggestions):
    """
    Automatically refactors code based on suggestions.
    :param suggestions: Suggestions for code optimization.
    :return: Refactored code.
    """
    code = apply_suggestions(suggestions)
    update_dependencies(code)
    return code


def apply_suggestions(suggestions):
    """
    Applies suggestions to optimize code.
    :param suggestions: Suggestions for code optimization.
    :return: Optimized code.
    """
    code = suggestions
    return code


def update_dependencies(code):
    """
    Updates any dependencies affected by code refactoring.
    :param code: Code that has been refactored.
    :return: None
    """
    dependencies = find_dependencies(code)
    update_dependencies(dependencies)


# Collaboration and project management feature
def collaborate(users):
    """
    Allows multiple users to collaborate on a project.
    :param users: List of users collaborating on the project.
    :return: None
    """
    project = create_project()
    for user in users:
        user.join_project(project)


def create_project():
    """
    Creates a new project.
    :return: New project.
    """
    project = Project()
    return project


class Project:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the project.
        :param task: Task to be added.
        :return: None
        """
        self.tasks.append(task)


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def join_project(self, project):
        """
        Joins a project and adds assigned tasks to user's task list.
        :param project: Project to join.
        :return: None
        """
        self.project = project
        for task in project.tasks:
            self.tasks.append(task)


class Task:
    def __init__(self, name):
        self.name = name
        self.progress = 0

    def update_progress(self):
        """
        Updates the progress of the task.
        :return: None
        """
        self.progress += 1
