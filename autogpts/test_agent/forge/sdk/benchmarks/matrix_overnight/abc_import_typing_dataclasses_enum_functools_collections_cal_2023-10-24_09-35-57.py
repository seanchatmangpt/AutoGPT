from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
from enum import Enum
from functools import partial
from collections import defaultdict
from collections.abc import Callable
from typing import Tuple, Dict
from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str


class Error(Exception):
    pass


class AuthenticationError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Authentication Error: {self.message}"


class UserAuthentication:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, username: str, password: str):
        self.users.append(User(username, password))

    def authenticate(self, username: str, password: str) -> bool:
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False


class TaskPriority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


@dataclass
class Task:
    name: str
    priority: TaskPriority


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, name: str, priority: TaskPriority):
        self.tasks.append(Task(name, priority))

    def assign_task(self, username: str, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.assignee = username


class CodeProfiler:
    def __init__(self):
        self.metrics: Dict[str, List[float]] = defaultdict(list)

    def profile(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            self.metrics["execution_time"].append(end_time - start_time)

        return wrapper

    def analyze(self) -> Dict[str, float]:
        analysis: Dict[str, float] = {}
        for metric, values in self.metrics.items():
            analysis[metric] = sum(values) / len(values)
        return analysis

    def suggest_optimizations(self) -> str:
        # dummy function, can be replaced with actual optimization suggestions
        return "No optimizations suggested"


class TaskManagerTests:
    def __init__(self):
        self.task_manager = TaskManager()

    def test_task_assignment(self):
        self.task_manager.add_task("test task", TaskPriority.MEDIUM)
        self.task_manager.assign_task("testuser", "test task")
        assert self.task_manager.tasks[0].assignee == "testuser"


class UserAuthenticationTests:
    def __init__(self):
        self.user_authentication = UserAuthentication()

    def test_add_user(self):
        self.user_authentication.add_user("testuser", "testpassword")
        assert len(self.user_authentication.users) == 1

    def test_authentication(self):
        self.user_authentication.add_user("testuser", "testpassword")
        assert self.user_authentication.authenticate("testuser", "testpassword") == True


if __name__ == "__main__":
    # Example usage
    user_authentication = UserAuthentication()
    user_authentication.add_user("testuser", "testpassword")
    try:
        if user_authentication.authenticate("testuser", "testpassword"):
            print("User authenticated")
        else:
            raise AuthenticationError("Incorrect username or password")
    except AuthenticationError as e:
        print(e)

    # Automated testing
    test_classes = [UserAuthenticationTests, TaskManagerTests]
    for test_class in test_classes:
        test_instance = test_class()
        for test_method in dir(test_instance):
            if test_method.startswith("test"):
                getattr(test_instance, test_method)()

    # Code profiling
    code_profiler = CodeProfiler()
    function_to_profile = code_profiler.profile(TaskManagerTests().test_task_assignment)
    function_to_profile()
    print(code_profiler.analyze())
    print(code_profiler.suggest_optimizations())
