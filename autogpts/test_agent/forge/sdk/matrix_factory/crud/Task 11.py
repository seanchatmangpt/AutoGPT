# Create components for each database model


class DatabaseModel:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def get_components(self):
        return self.components

    def __repr__(self):
        return f"{self.name} Database Model"


class Component:
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type

    def __repr__(self):
        return f"{self.name} ({self.data_type})"


# Example usage:

# Create a User database model with two components: username and password
user_model = DatabaseModel(
    "User", [Component("username", "string"), Component("password", "string")]
)

# Add a new component to the User model
user_model.add_component(Component("email", "string"))

# Print the components of the User model
print(user_model.get_components())

# Remove the password component from the User model
user_model.remove_component(Component("password", "string"))

# Print the updated components of the User model
print(user_model.get_components())

# Output:
# [username (string), password (string), email (string)]
# [username (string), email (string)]
