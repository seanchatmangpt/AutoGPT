from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Date:
    """
    A Value Object representing a date in the context of project milestones or deadlines. It is immutable and provides date-related functionalities.
    """

    year: int
    month: int
    day: int
