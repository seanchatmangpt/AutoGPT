# Import necessary modules
import os
import sys
import subprocess

# Define function to deploy app to server
def deploy_app():
    # Change directory to app folder
    os.chdir("app_folder")
    
    # Pull latest changes from remote repository
    subprocess.run(["git", "pull"])
    
    # Install any necessary dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Restart server
    subprocess.run(["systemctl", "restart", "app_server"])
    
    # Print success message
    print("App successfully deployed to server!")
    
# Call function to deploy app
deploy_app()