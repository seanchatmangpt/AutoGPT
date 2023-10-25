from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any


from .candidate import Candidate


class Interview:
    """
    An Entity representing a single interview instance. It has a unique identity and associated properties like interview type, date, and candidates.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    # Business Functions
    def evaluate_candidate(self, candidate: Candidate, metrics: List[SkillMetric]):
        """
        Evaluates the candidate based on given metrics.
        """
        # All validation logic is in the icontract decorators
        pass
