import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import configparser
import os

try:
    with open('installed.txt', 'r') as file:
        version = file.read()
except FileNotFoundError:
    print("FaceDriver does not appear to have installed correctly.")
    print("Please try to install it again.")
    print("https://github.com/anothermartz/FaceDriver/issues")
    input()
    exit()

print("opening GUI")

runfile = 'run.txt'
if os.path.exists(runfile):
    os.remove(runfile)

import webbrowser

def open_github_link(event):
    webbrowser.open("https://github.com/anothermartz/FaceDriver?tab=readme-ov-file#advanced-tweaking")

def read_config():
    # Read the config.ini file
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

def save_config(config):
    # Save the updated config back to config.ini
    with open("config.ini", "w") as config_file:
        config.write(config_file)

def open_Driven_file():
    file_path = filedialog.askopenfilename(title="Select a Driven file", filetypes=[("All files", "*.*")])
    if file_path:
        Driven_file_var.set(file_path)
        
def open_Driving_file():
    file_path = filedialog.askopenfilename(title="Select a Driving file", filetypes=[("All files", "*.*")])
    if file_path:
        Driving_file_var.set(file_path)        

def open_Output_file():
    file_path = filedialog.asksaveasfilename(
        title="Select output video file",
        filetypes=[("MP4 files", "*.mp4")],
        defaultextension=".mp4"
    )
    if file_path:
        # Ensure the file path ends with .mp4
        if not file_path.lower().endswith('.mp4'):
            file_path += '.mp4'
        Output_file_var.set(file_path)


def start_FaceDriver():
    # Start FaceDriver processing
    print("Saving config")
    config["OPTIONS"]["Driven_file"] = str(Driven_file_var.get())
    config["OPTIONS"]["Driving_file"] = str(Driving_file_var.get())
    config["OPTIONS"]["Output_file"] = str(Output_file_var.get())
    save_config(config)  # Save the updated config

    # Check if the output file already exists
    output_file_path = Output_file_var.get()
    if os.path.exists(output_file_path):
        response = messagebox.askyesno("File Exists", f"The file '{output_file_path}' already exists. Do you want to overwrite it?")
        if not response:
            return

    with open("run.txt", "w") as f:
        f.write("run")
        exit()


root = tk.Tk()
root.title("FaceDriver GUI")
root.geometry("625x200")
root.configure(bg="lightblue")

# Read the existing config.ini
config = read_config()

row=0
tk.Label(root, text=version, bg="lightblue").grid(row=row, column=0, sticky="nw")
# Create a label for Driven file
row+=1
Driven_label = tk.Label(root, text="Driven File Path:", bg="lightblue")
Driven_label.grid(row=row, column=0, sticky="w", padx=5)

# Entry widget for Driven file path
Driven_file_var = tk.StringVar()
Driven_entry = tk.Entry(root, textvariable=Driven_file_var, width=80)
Driven_entry.grid(row=row, column=1, sticky="w")

# Create a button to open the file dialog
select_button = tk.Button(root, text="...", command=open_Driven_file)
select_button.grid(row=row, column=1, sticky="w", padx=490)

# Set the default value based on the existing config
Driven_file_var.set(config["OPTIONS"].get("Driven_file", ""))

# String input for Driving_file
row+=1

# Create a label for the input box
Driving_file_label = tk.Label(root, text="Driving File Path:", bg="lightblue")
Driving_file_label.grid(row=row, column=0, sticky="w", padx=5)

# Create an input box for the Driving file path
Driving_file_var = tk.StringVar()
Driving_file_entry = tk.Entry(root, textvariable=Driving_file_var, width=80)
Driving_file_entry.grid(row=row, column=1, sticky="w")

# Create a button to open the file dialog
select_button = tk.Button(root, text="...", command=open_Driving_file)
select_button.grid(row=row, column=1, sticky="w", padx=490)

# Set the initial value from the 'config' dictionary (if available)
Driving_file_var.set(config["OPTIONS"].get("Driving_file", ""))

# Output_file
row+=1
Output_file_label = tk.Label(root, text="Output File Path:", bg="lightblue")
Output_file_label.grid(row=row, column=0, sticky="w", padx=5)
Output_file_var = tk.StringVar()
Output_file_entry = tk.Entry(root, textvariable=Output_file_var, width=80)
Output_file_entry.grid(row=row, column=1, sticky="w")
select_button = tk.Button(root, text="...", command=open_Output_file)
select_button.grid(row=row, column=1, sticky="w", padx=490)
Output_file_var.set(config["OPTIONS"].get("Output_file", ""))

row+=1
tk.Label(root, text="", bg="lightblue").grid(row=row, column=0, sticky="nw")

# Button to start FaceDriver
row+=1
start_button = tk.Button(root, text="Start FaceDriver", command=start_FaceDriver, bg="#5af269", font=("Arial", 16))
start_button.grid(row=row, column=0, sticky="w", padx=225, columnspan=2)

row+=1
tk.Label(root, text="", bg="lightblue").grid(row=row, column=0, sticky="nw")

# Increase spacing between all rows (uniformly)
for row in range(row):
    root.rowconfigure(row, weight=1)


root.mainloop()

install .y - version = 'v0.0.1'
# write a file to signify setup is done
with open("installed.txt", "w") as f:
    f.write(version)
print("Installation complete!")
run_loop.bat - @echo off
:run_loop
call GUI.py

if exist "run.txt" (
	echo starting Easy-Wav2Lip...
	python run.py
	goto run_loop
	)

run_loop.sh - #!/bin/bash

while true; do
    python GUI.py

    if [ -f "run.txt" ]; then
        echo "Starting Easy-Wav2Lip..."
        python run.py
    else
        break  # Exit the loop when "run.txt" does not exist
    fi
done
