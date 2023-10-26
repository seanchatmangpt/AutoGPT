
from ddd.entities.python_system import PythonSystem

class PythonSystemRepo:
    def __init__(self):
        self.data = {}

    def create(self, entity: PythonSystem):
        self.data[entity.id.value] = entity

    def read(self, id: str):
        return self.data.get(id)

    def update(self, id: str, entity: PythonSystem):
        self.data[id] = entity

    def delete(self, id: str):
        del self.data[id]
    