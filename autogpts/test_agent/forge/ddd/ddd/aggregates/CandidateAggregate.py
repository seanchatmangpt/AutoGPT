
from ddd.entities.candidate import Candidate

class CandidateAggregate:
    def __init__(self, root_entity: Candidate):
        self.root_entity = root_entity
    