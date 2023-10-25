from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class InterviewQuestion:
    """
    A Value Object representing a single interview question. It encapsulates question-related attributes and is immutable.
    """
    title: str
    difficulty: str
    domain: str
