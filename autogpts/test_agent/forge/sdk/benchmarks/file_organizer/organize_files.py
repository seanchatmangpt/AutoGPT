import os
import argparse
import shutil

# Create a parser to handle command line arguments
parser = argparse.ArgumentParser(description='Organize files in a directory based on their file types.')
parser.add_argument('--directory_path', type=str, help='Path to the directory containing the files to be organized.')
args = parser.parse_args()

# Get the directory path from the command line argument
directory_path = args.directory_path

# Create the necessary folders if they don't already exist
if not os.path.exists(os.path.join(directory_path, 'images')):
    os.mkdir(os.path.join(directory_path, 'images'))
if not os.path.exists(os.path.join(directory_path, 'documents')):
    os.mkdir(os.path.join(directory_path, 'documents'))
if not os.path.exists(os.path.join(directory_path, 'audio')):
    os.mkdir(os.path.join(directory_path, 'audio'))

# Loop through all files in the directory
for file in os.listdir(directory_path):
    # Get the file extension
    file_extension = os.path.splitext(file)[1]

    # Move the file to the corresponding folder based on its extension
    if file_extension in ['.jpg', '.png', '.gif']:
        shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, 'images'))
    elif file_extension in ['.doc', '.pdf', '.txt']:
        shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, 'documents'))
    elif file_extension in ['.mp3', '.wav', '.aac']:
        shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, 'audio'))

# Print a success message
print('Files successfully organized in the directory: {}'.format(directory_path))