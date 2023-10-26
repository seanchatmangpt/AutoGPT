
from ddd.value_objects.interviewer_value import InterviewerValue

class Interviewer:
    def __init__(self, id: InterviewerValue = None):
        self.id = id if id else InterviewerValue()
    