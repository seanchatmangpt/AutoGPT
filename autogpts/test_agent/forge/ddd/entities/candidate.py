from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any


class Candidate:
    """
    An Entity representing an interviewee. It has a unique identity and is evaluated based on different skills and metrics.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity
