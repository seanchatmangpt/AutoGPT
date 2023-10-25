# Import the necessary libraries
import pandas as pd
import numpy as np
import sqlalchemy as db

# Connect to the database
engine = db.create_engine("sqlite:///my_database.db")

# Create a table in the database
with engine.connect() as conn:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            salary REAL
        )
    """
    )

# Create an index on the 'name' column
with engine.connect() as conn:
    conn.execute(
        """
        CREATE INDEX IF NOT EXISTS name_index ON my_table (name)
    """
    )
