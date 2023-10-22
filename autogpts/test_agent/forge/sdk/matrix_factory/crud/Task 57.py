# Import the necessary modules
import os
import shutil

# Define the class for the file storage system
class FileStorageSystem:
    
    # Initialize the class with a root directory
    def __init__(self, root_dir):
        self.root_dir = root_dir
    
    # Method to create a new file
    def create_file(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        with open(file_path, 'w') as f:
            f.write('')
    
    # Method to delete an existing file
    def delete_file(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        os.remove(file_path)
    
    # Method to copy a file to a new location
    def copy_file(self, file_name, new_dir):
        file_path = os.path.join(self.root_dir, file_name)
        shutil.copy(file_path, new_dir)
    
    # Method to move a file to a new location
    def move_file(self, file_name, new_dir):
        file_path = os.path.join(self.root_dir, file_name)
        shutil.move(file_path, new_dir)
    
    # Method to rename a file
    def rename_file(self, file_name, new_name):
        file_path = os.path.join(self.root_dir, file_name)
        new_path = os.path.join(self.root_dir, new_name)
        os.rename(file_path, new_path)
    
    # Method to check if a file exists
    def file_exists(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        return os.path.exists(file_path)
    
    # Method to get the size of a file
    def get_file_size(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        return os.path.getsize(file_path)
    
    # Method to list all files in the root directory
    def list_files(self):
        return os.listdir(self.root_dir)