class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def update_email(self, new_email):
        self.email = new_email

    def update_password(self, new_password):
        self.password = new_password

    def __repr__(self):
        return f"User: {self.username}, Email: {self.email}, Password: {self.password}"


user = UserProfile("JohnDoe", "johndoe@example.com", "password123")
print(user)

user.update_email("johndoe2@example.com")
user.update_password("newpassword456")
print(user)
