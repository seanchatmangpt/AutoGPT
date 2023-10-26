
from ddd.value_objects.interview_value import InterviewValue

class Interview:
    def __init__(self, id: InterviewValue = None):
        self.id = id if id else InterviewValue()
    