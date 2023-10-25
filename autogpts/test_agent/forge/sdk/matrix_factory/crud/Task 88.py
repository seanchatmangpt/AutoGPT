# Import the necessary modules
import psycopg2
import psycopg2.extras

# Define the database connection parameters
db_params = {
    "host": "localhost",
    "port": "5432",
    "database": "my_database",
    "user": "my_user",
    "password": "my_password",
}

# Connect to the database
conn = psycopg2.connect(**db_params)

# Set up a cursor to execute SQL queries
cur = conn.cursor()

# Create a table for the replicated data
cur.execute("CREATE TABLE replicated_data (id SERIAL PRIMARY KEY, data JSONB)")

# Set up a trigger to automatically insert new data into the replicated table
cur.execute(
    """
    CREATE TRIGGER replicate_data
    AFTER INSERT ON original_data
    FOR EACH ROW
    EXECUTE PROCEDURE replicate_data_function()
"""
)


# Define the function that will replicate the data
def replicate_data_function():
    # Get the newly inserted data
    new_data = psycopg2.extras.DictCursor.fetchone()

    # Insert the data into the replicated table
    cur.execute("INSERT INTO replicated_data (data) VALUES (%s)", (new_data,))

    # Commit the changes to the database
    conn.commit()


# Close the cursor and database connection
cur.close()
conn.close()
