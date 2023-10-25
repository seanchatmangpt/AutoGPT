class UserFeedbackSystem:
    def __init__(self):
        self.feedback = []

    def add_feedback(self, feedback):
        self.feedback.append(feedback)

    def get_feedback(self):
        return self.feedback

    def clear_feedback(self):
        self.feedback = []
