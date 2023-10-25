# Import the necessary modules
import sqlite3

# Connect to the database
conn = sqlite3.connect("mydatabase.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"""
)

# Insert data into the table
cursor.execute("""INSERT INTO users VALUES (1, 'John Smith', 'john@example.com')""")
cursor.execute("""INSERT INTO users VALUES (2, 'Jane Doe', 'jane@example.com')""")

# Save changes
conn.commit()

# Close the connection
conn.close()
