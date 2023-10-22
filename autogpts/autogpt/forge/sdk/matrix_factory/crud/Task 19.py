# Import the necessary modules
import React from 'react';
import styled from 'styled-components';

# Create a styled component
const StyledApp = styled.div`
  background-color: #fff;
  color: #000;
  font-size: 16px;
`;

# Define the React app component
const App = () => {
  return (
    <StyledApp>
      <h1>Hello World!</h1>
    </StyledApp>
  );
};

# Export the component
export default App;