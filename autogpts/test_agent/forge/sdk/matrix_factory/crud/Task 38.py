import shutil
import datetime
import os

def create_backup(source, destination):
    """
    Creates a backup of the given source directory to the specified destination directory.
    """
    # create a timestamp for the backup folder name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # create the backup folder with the timestamp as its name
    backup_folder = os.path.join(destination, timestamp)
    os.mkdir(backup_folder)
    
    # copy all files and subdirectories from the source directory to the backup folder
    shutil.copytree(source, backup_folder)
    
    # print success message
    print("Backup created successfully at {}".format(backup_folder))
    
# example usage
create_backup("my_project", "backup_folder")