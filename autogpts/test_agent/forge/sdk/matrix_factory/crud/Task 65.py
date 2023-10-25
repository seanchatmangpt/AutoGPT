# Import the necessary modules
import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


# Define the database migration function
def migrate_database():
    # Get the current working directory
    current_dir = os.getcwd()
    # Create a new directory for the migration files
    migration_dir = os.path.join(current_dir, "migrations")
    # Check if the migration directory already exists
    if not os.path.exists(migration_dir):
        # If not, create it
        os.mkdir(migration_dir)
    # Get the list of files in the current directory
    files = os.listdir(current_dir)
    # Loop through the files
    for file in files:
        # Check if the file is a SQL file
        if file.endswith(".sql"):
            # If so, move it to the migration directory
            os.rename(
                os.path.join(current_dir, file), os.path.join(migration_dir, file)
            )
    # Log a message indicating the migration was successful
    logging.info("Database migration completed successfully.")


# Call the database migration function
migrate_database()
