from pathlib import Path
    import shutil
    import argparse
    
    args = argparse.ArgumentParser()
    args.add_argument('--directory_path', help='directory path to the folder you want to organize')
    args = args.parse_args()
    
    def directory_organizer(directory):
        '''Sorts files into folders based on their file types.
        
        Args:
            directory (str): path to the directory you want to organize.
        Returns:
            images (list): list of image files.
            documents (list): list of documents.
            audio (list): list of audio files.
        '''
        images = []
        documents = []
        audio = []
        
        for filepath in Path(directory).iterdir():
            if filepath.suffix == '.jpg' or filepath.suffix == '.png':
                images.append(filepath)
            elif filepath.suffix == '.pdf' or filepath.suffix == '.docx':
                documents.append(filepath)
            elif filepath.suffix == '.mp3' or filepath.suffix == '.wav':
                audio.append(filepath)
        
        return images, documents, audio
    
    def move_files(filetype_list, folder_name):
        '''Moves files into specified folder.
        
        Args:
            filetype_list (list): list of file paths.
            folder_name (str): name of the folder.
        Returns:
            None
        '''
        for filepath in filetype_list:
            shutil.move(filepath, folder_name)
    
    if args.directory_path:
        images, documents, audio = directory_organizer(args.directory_path)
        
        move_files(images, 'images')
        move_files(documents, 'documents')
        move_files(audio, 'audio')