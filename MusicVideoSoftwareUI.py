import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys

# Define your script names here
SCRIPTS = {
    "Generate Metadata": "Generate-Metadata.ps1",
    "Create Music Video": "Create-MusicVideo.ps1",
    "Update Project": "Update.ps1"
}

def run_script(script_name):
    if not os.path.exists(script_name):
        messagebox.showerror("Error", f"Script not found: {script_name}")
        return

    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_name], check=True)
        messagebox.showinfo("Success", f"Completed: {script_name}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def open_folder(folder):
    folder_path = os.path.abspath(folder)
    if os.path.isdir(folder_path):
        os.startfile(folder_path)
    else:
        messagebox.showerror("Error", f"Folder does not exist: {folder}")

def create_ui():
    root = tk.Tk()
    root.title("Music Video Software")
    root.geometry("400x350")
    root.configure(bg="#202020")

    tk.Label(root, text="Music Video Tool", font=("Arial", 16), bg="#202020", fg="white").pack(pady=10)

    for label, script in SCRIPTS.items():
        tk.Button(root, text=label, font=("Arial", 12), width=25, bg="#4CAF50", fg="white",
                  command=lambda s=script: run_script(s)).pack(pady=8)

    tk.Label(root, text="Folders", bg="#202020", fg="white", font=("Arial", 12)).pack(pady=(20, 5))

    for folder in ["Image", "Song-File", "Metadata", "Videos", "Archive"]:
        tk.Button(root, text=f"Open {folder}", font=("Arial", 10), width=20,
                  command=lambda f=folder: open_folder(f)).pack(pady=3)

    tk.Button(root, text="Exit", font=("Arial", 12), width=25, bg="#f44336", fg="white", command=root.quit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
