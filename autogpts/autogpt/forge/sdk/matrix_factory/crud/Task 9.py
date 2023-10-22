# Import the necessary modules
import React from 'react';
import ReactDOM from 'react-dom';

# Create a React component
class App extends React.Component:
    def render(self):
        return (
            <div>
                <h1>Hello World!</h1>
            </div>
        )

# Render the component to the DOM
ReactDOM.render(<App />, document.getElementById('root'))