import subprocess
import sys
import os

# Get the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Function to install dependencies locally in the current directory
def install_dependencies():
    try:
        print("Installing dependencies in the current directory...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", current_dir, "GitPython", "tkinterdnd2"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

# Install dependencies
install_dependencies()

# Add the current directory to sys.path so Python can find the installed libraries
sys.path.append(current_dir)

# Confirm that everything is ready for setup
print("Setup complete! Dependencies have been installed in:", current_dir)
