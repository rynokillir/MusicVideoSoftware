import os
import sys
import subprocess
import pkg_resources
import platform

# Function to install packages using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Function to check if Python is installed
def check_python_installation():
    try:
        subprocess.check_call([sys.executable, "--version"])
        print(f"Python is installed: {sys.version}")
    except subprocess.CalledProcessError:
        print("Python is not installed. Please install Python first.")
        sys.exit(1)

# Function to install dependencies from requirements.txt
def install_requirements():
    print("Installing required packages from requirements.txt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Function to check if the required Python packages are installed
def check_requirements():
    try:
        pkg_resources.require(["tkinterdnd2", "GitPython"])
        print("Required Python libraries are installed.")
    except pkg_resources.DistributionNotFound:
        print("Required libraries not found. Installing...")
        install_requirements()

# Function to update the repository from GitHub
def update_repo():
    try:
        import git
        repo_path = os.path.dirname(os.path.realpath(__file__))
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        print("Checking for updates from GitHub...")
        origin.fetch()
        current_commit = repo.head.commit
        remote_commit = repo.commit('origin/master')

        if current_commit != remote_commit:
            print("Updates available. Pulling latest changes...")
            origin.pull()
        else:
            print("No updates available.")
    except ImportError:
        print("GitPython is not installed. Installing GitPython...")
        install_package("GitPython")

# Main setup function
def main():
    print("Setting up Music Video Software...")

    # Check for Python installation
    check_python_installation()

    # Check if required libraries are installed
    check_requirements()

    # Update the repository
    update_repo()

    print("Setup complete! You can now run the application.")

if __name__ == "__main__":
    main()
