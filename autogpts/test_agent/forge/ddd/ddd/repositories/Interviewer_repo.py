
from ddd.entities.interviewer import Interviewer

class InterviewerRepo:
    def __init__(self):
        self.data = {}

    def create(self, entity: Interviewer):
        self.data[entity.id.value] = entity

    def read(self, id: str):
        return self.data.get(id)

    def update(self, id: str, entity: Interviewer):
        self.data[id] = entity

    def delete(self, id: str):
        del self.data[id]
    