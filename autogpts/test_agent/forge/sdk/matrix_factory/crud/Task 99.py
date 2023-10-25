# Import the necessary modules
import os
import shutil
import datetime

# Define the source and destination directories
source_dir = "/home/user/test_data"
dest_dir = "/home/user/backup"

# Create a timestamp for the backup folder
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Create the backup folder with the timestamp
backup_dir = os.path.join(dest_dir, timestamp)

# Create the backup folder if it doesn't exist
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

# Loop through the files in the source directory
for file in os.listdir(source_dir):
    # Create the full path for each file
    file_path = os.path.join(source_dir, file)
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Copy the file to the backup folder
        shutil.copy(file_path, backup_dir)

# Print a success message
print("Backup completed successfully.")
