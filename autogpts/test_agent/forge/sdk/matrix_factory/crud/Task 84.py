# Import the necessary modules
import os
import shutil
import datetime

# Define the source and destination directories
source_dir = "/path/to/database"
dest_dir = "/path/to/backup"

# Create a timestamp for the backup file name
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Create a backup file name using the timestamp
backup_name = f"database_backup_{timestamp}.zip"

# Create the full path for the backup file
backup_path = os.path.join(dest_dir, backup_name)

# Use shutil to create a zip file of the database directory
shutil.make_archive(backup_path, "zip", source_dir)

# Print a success message
print(f"Backup of database created at {backup_path}")
