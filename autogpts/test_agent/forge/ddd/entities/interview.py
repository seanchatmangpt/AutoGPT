from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any
from .candidate import Candidate
from ..value_objects.skill_metric import SkillMetric


class Interview:
    """
    An Entity representing a single interview instance. It has a unique identity and associated properties like interview type, date, and candidates.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    @require(lambda candidate, metrics: candidate is not None and metrics
             is not None)
    @ensure(lambda result: result >= 0 and result <= 100)
    def evaluate_candidate(candidate: Candidate, metrics: List[SkillMetric]
                           ) -> int:
        """
    Evaluates the candidate based on given metrics.
    """
        total_score = 0
        for metric in metrics:
            total_score += metric.rating
        total_questions = 0
        for question in candidate.questions:
            total_questions += 1
        average_score = total_score / total_questions
        final_score = average_score * 100
        return final_score
