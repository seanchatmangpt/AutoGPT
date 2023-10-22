# Import the venv module
import venv

# Create a virtual environment named "my_env"
venv.create("my_env")

# Activate the virtual environment
source my_env/bin/activate

# Install necessary packages
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate