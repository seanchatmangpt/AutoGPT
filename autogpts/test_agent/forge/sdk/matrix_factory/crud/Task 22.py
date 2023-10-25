# Import necessary modules
import os
import sys
import subprocess


# Define function for running deployment script
def run_deployment_script(script):
    # Check if script exists
    if os.path.exists(script):
        # Run script using subprocess module
        subprocess.run(script)
    else:
        # Print error message if script does not exist
        print("Error: Script does not exist.")


# Call function with script name as argument
run_deployment_script("deploy.sh")
