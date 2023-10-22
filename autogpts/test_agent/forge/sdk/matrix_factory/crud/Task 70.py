class User:
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def remove_permission(self, permission):
        self.permissions.remove(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class Permission:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class PermissionSystem:
    def __init__(self):
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def remove_permission(self, permission):
        self.permissions.remove(permission)

    def has_permission(self, user, permission):
        return user.has_permission(permission)

    def grant_permission(self, user, permission):
        user.add_permission(permission)

    def revoke_permission(self, user, permission):
        user.remove_permission(permission)