
from ddd.entities.interview import Interview

class InterviewRepo:
    def __init__(self):
        self.data = {}

    def create(self, entity: Interview):
        self.data[entity.id.value] = entity

    def read(self, id: str):
        return self.data.get(id)

    def update(self, id: str, entity: Interview):
        self.data[id] = entity

    def delete(self, id: str):
        del self.data[id]
    