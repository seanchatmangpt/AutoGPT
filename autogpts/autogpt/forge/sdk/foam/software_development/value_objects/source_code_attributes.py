from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class SourceCodeAttributes:
    """
    A Value Object representing source code within a software project. It encapsulates code-related properties and is immutable.
    """

    filepath: str
    classes: List[str]
    functions: List[str]
    imports: List[str]
