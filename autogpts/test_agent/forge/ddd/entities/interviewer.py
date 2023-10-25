from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any


from ..value_objects.interview_question import InterviewQuestion


class Interviewer:
    """
    An Entity representing the interviewer who conducts the interview. Has a unique identity and can evaluate candidates.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    # Business Functions
    def ask_question(self, question: InterviewQuestion):
        """
        Asks the specified question during an interview.
        """
        # All validation logic is in the icontract decorators
        pass
