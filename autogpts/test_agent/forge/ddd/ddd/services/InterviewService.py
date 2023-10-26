
from ddd.repositories.interview_repo import InterviewRepo

class InterviewService:
    def __init__(self, repo: InterviewRepo):
        self.repo = repo

    def perform_operation(self, entity):
        # Logic for performing an operation
        pass
    