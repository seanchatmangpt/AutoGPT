
from ddd.entities.interview import Interview

class InterviewAggregate:
    def __init__(self, root_entity: Interview):
        self.root_entity = root_entity
    