import sys
import os
import subprocess
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import git

# Add the current directory to the Python path so that installed dependencies can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Function to check for updates from the GitHub repository
def check_for_updates():
    print("Checking for updates...")
    try:
        # Initialize the Git repository object
        repo = git.Repo(current_dir)

        # Check the current commit hash locally
        local_commit = repo.commit("HEAD")

        # Fetch the latest commits from the origin
        repo.remotes.origin.fetch()

        # Check the latest commit on the remote master branch (main branch)
        remote_commit = repo.commit("origin/main")

        # If the local and remote commits are different, updates are available
        if local_commit.hexsha != remote_commit.hexsha:
            print("Update available!")
        else:
            print("No updates available.")
    except git.exc.InvalidGitRepositoryError:
        print("Not a valid Git repository!")
    except Exception as e:
        print(f"Error checking for updates: {e}")

# Function to set up the GUI
def setup_gui():
    root = TkinterDnD.Tk()

    root.title("Music Video Software")

    # Add a label
    label = tk.Label(root, text="Welcome to the Music Video Software", font=("Arial", 16))
    label.pack(padx=20, pady=20)

    # Setup drag-and-drop functionality
    def on_drop(event):
        print(f"File dropped: {event.data}")
        # Process the file drop (you can modify this based on your needs)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', on_drop)

    # Check for updates
    check_for_updates()

    # Run the GUI
    root.mainloop()

# Main entry point for the launcher
if __name__ == "__main__":
    setup_gui()
