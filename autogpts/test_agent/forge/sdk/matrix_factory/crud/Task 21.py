# Import necessary modules
import os
import sys
import subprocess

# Define function to check if command exists
def command_exists(command):
    return any(
        os.access(os.path.join(path, command), os.X_OK)
        for path in os.environ["PATH"].split(os.pathsep)
    )

# Define function to run deployment script
def run_deployment_script():
    # Check if git command exists
    if not command_exists("git"):
        print("Git is not installed. Please install Git and try again.")
        sys.exit(1)
    
    # Check if git repository exists
    if not os.path.exists(".git"):
        print("Git repository not found. Please initialize a Git repository and try again.")
        sys.exit(1)
    
    # Pull latest changes from remote repository
    subprocess.run(["git", "pull"])
    
    # Install necessary dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Run deployment script
    subprocess.run(["python", "deploy.py"])
    
# Run deployment script
run_deployment_script()