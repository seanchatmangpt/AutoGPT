
from ddd.entities.interviewer import Interviewer

class InterviewerAggregate:
    def __init__(self, root_entity: Interviewer):
        self.root_entity = root_entity
    