import shutil
import os

def backup(src, dest):
    shutil.copytree(src, dest)
    
def main():
    src = input("Enter source directory: ")
    dest = input("Enter destination directory: ")
    backup(src, dest)
    
if __name__ == "__main__":
    main()