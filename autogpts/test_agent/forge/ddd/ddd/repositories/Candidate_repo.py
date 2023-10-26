
from ddd.entities.candidate import Candidate

class CandidateRepo:
    def __init__(self):
        self.data = {}

    def create(self, entity: Candidate):
        self.data[entity.id.value] = entity

    def read(self, id: str):
        return self.data.get(id)

    def update(self, id: str, entity: Candidate):
        self.data[id] = entity

    def delete(self, id: str):
        del self.data[id]
    