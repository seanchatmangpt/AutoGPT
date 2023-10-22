class UserActivity:
    def __init__(self, user_id):
        self.user_id = user_id
        self.activity = []

    def add_activity(self, activity):
        self.activity.append(activity)

    def get_activity(self):
        return self.activity

    def clear_activity(self):
        self.activity = []

    def __repr__(self):
        return f"UserActivity(user_id={self.user_id}, activity={self.activity})"