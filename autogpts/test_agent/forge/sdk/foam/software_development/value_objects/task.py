from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Task:
    """
    A Value Object representing a task or work item within a software project. It encapsulates task-related attributes and behaviors and is immutable.
    """

    title: str
    description: str
