
from ddd.value_objects.candidate_value import CandidateValue

class Candidate:
    def __init__(self, id: CandidateValue = None):
        self.id = id if id else CandidateValue()
    