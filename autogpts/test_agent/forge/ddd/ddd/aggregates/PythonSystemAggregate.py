
from ddd.entities.python_system import PythonSystem

class PythonSystemAggregate:
    def __init__(self, root_entity: PythonSystem):
        self.root_entity = root_entity
    