# Import the necessary modules
import pandas as pd
import numpy as np

# Create a test database
df = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                   'name': ['John', 'Jane', 'Bob', 'Alice', 'Mark'],
                   'age': [25, 30, 40, 35, 28],
                   'salary': [50000, 60000, 80000, 70000, 55000]})

# Set the index to be the 'id' column
df.set_index('id', inplace=True)

# Print the first 5 rows of the database
print(df.head())

# Sort the database by 'age' in descending order
df.sort_values(by='age', ascending=False, inplace=True)

# Print the first 5 rows of the sorted database
print(df.head())

# Reset the index to be the default integer index
df.reset_index(drop=True, inplace=True)

# Print the first 5 rows of the database with the default index
print(df.head())