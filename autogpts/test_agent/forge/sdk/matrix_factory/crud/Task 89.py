# Import the necessary modules
import sqlite3
import pandas as pd

# Define the source and destination databases
source_db = sqlite3.connect('source.db')
dest_db = sqlite3.connect('destination.db')

# Create a cursor for the source database
source_cursor = source_db.cursor()

# Execute a query to retrieve data from the source database
source_cursor.execute('SELECT * FROM table')

# Fetch all the data from the query
data = source_cursor.fetchall()

# Create a dataframe from the retrieved data
df = pd.DataFrame(data)

# Close the cursor and source database
source_cursor.close()
source_db.close()

# Create a cursor for the destination database
dest_cursor = dest_db.cursor()

# Execute a query to insert the data into the destination database
dest_cursor.executemany('INSERT INTO table VALUES (?, ?, ?)', df.values.tolist())

# Commit the changes and close the cursor and destination database
dest_db.commit()
dest_cursor.close()
dest_db.close()

# Print a success message
print('Database replication successful.')