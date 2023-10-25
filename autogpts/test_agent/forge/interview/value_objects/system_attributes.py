from dataclasses import dataclass, field
from typing import List

from typing import List


@dataclass(frozen=True)
class SystemAttributes:
    """
    A Value Object encapsulating Python system attributes like architecture type, dependencies, etc. Immutable.
    """
    architecture_type: str
    dependencies: List[str]
