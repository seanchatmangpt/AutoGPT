from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class SkillMetric:
    """
    A Value Object that holds the metrics for skills. Immutable and can be used for evaluations.
    """
    skill_name: str
    rating: int
