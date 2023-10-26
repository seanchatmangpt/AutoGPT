
from ddd.value_objects.python_system_value import PythonSystemValue

class PythonSystem:
    def __init__(self, id: PythonSystemValue = None):
        self.id = id if id else PythonSystemValue()
    