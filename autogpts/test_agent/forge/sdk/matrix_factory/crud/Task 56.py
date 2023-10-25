# Import the necessary modules
import os
import shutil


# Define the file storage system class
class FileStorageSystem:
    # Initialize the class with a root directory
    def __init__(self, root_dir):
        self.root_dir = root_dir

    # Method to create a new directory
    def create_dir(self, dir_name):
        # Use os.path.join to create a path to the new directory
        new_dir = os.path.join(self.root_dir, dir_name)
        # Use os.makedirs to create the new directory
        os.makedirs(new_dir)

    # Method to copy a file from one location to another
    def copy_file(self, source, destination):
        # Use shutil.copy to copy the file
        shutil.copy(source, destination)

    # Method to move a file from one location to another
    def move_file(self, source, destination):
        # Use shutil.move to move the file
        shutil.move(source, destination)

    # Method to delete a file
    def delete_file(self, file_name):
        # Use os.remove to delete the file
        os.remove(file_name)

    # Method to delete a directory
    def delete_dir(self, dir_name):
        # Use shutil.rmtree to delete the directory and all its contents
        shutil.rmtree(dir_name)


# Create an instance of the FileStorageSystem class with a root directory
file_storage = FileStorageSystem("root_dir")

# Create a new directory called "documents"
file_storage.create_dir("documents")

# Copy a file from "source_dir" to "documents"
file_storage.copy_file("source_dir/file.txt", "documents/file.txt")

# Move a file from "documents" to "destination_dir"
file_storage.move_file("documents/file.txt", "destination_dir/file.txt")

# Delete the file "file.txt"
file_storage.delete_file("file.txt")

# Delete the directory "documents"
file_storage.delete_dir("documents")
