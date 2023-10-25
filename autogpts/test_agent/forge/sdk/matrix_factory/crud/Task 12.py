# Import React
import React


# Define a function to create a React component
def create_component(name, props, children):
    # Return a React component with the given name, props, and children
    return React.createElement(name, props, children)


# Create a component named "TestComponent" with props and children
TestComponent = create_component(
    "TestComponent", {"prop1": "value1", "prop2": "value2"}, ["Child1", "Child2"]
)

# Render the component
React.render(TestComponent)
