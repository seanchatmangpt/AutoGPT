# Import the necessary modules
import os
import shutil
import datetime

# Define the backup function
def backup(source, destination):
    # Create a timestamp for the backup file name
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # Create the backup file name
    backup_name = f'{source}_{timestamp}.bak'
    # Copy the source file to the destination
    shutil.copy(source, destination)
    # Print a success message
    print(f'Backup of {source} created at {destination}/{backup_name}')

# Define the source and destination paths
source = '/path/to/source/file'
destination = '/path/to/backup/directory'

# Call the backup function
backup(source, destination)