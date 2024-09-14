# FaceSync

![FaceSync Banner](https://via.placeholder.com/800x200.png?text=FaceSync+Banner)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Introduction

**FaceSync** is a powerful tool designed to transfer facial animations from one video (Driving) to another (Driven). Whether you're looking to create deepfake videos, enhance animations, or synchronize expressions, FaceSync provides an intuitive graphical user interface (GUI) to simplify the process.

## Features

- **User-Friendly GUI:** Easily select and manage your Driving and Driven videos.
- **Configuration Management:** Save and load your project settings effortlessly.
- **Output Customization:** Choose your desired output file format and location.
- **Error Handling:** Prevent accidental overwrites and handle missing installations gracefully.
- **Continuous Operation:** Scripts to keep the application running smoothly on both Windows and Ubuntu.

## Installation

Follow these steps to set up **FaceSync** on your Ubuntu system.

### Prerequisites

- **Python 3.x** installed on your system.
- **Git** installed for version control.
- **Required Python Packages:**
  - `tkinter`
  - `configparser`

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/FaceSync.git
   cd FaceSync
Install Python Packages

bash
Copy code
sudo apt update
sudo apt install python3-pip python3-tk
pip3 install -r requirements.txt
If you don't have a requirements.txt, you can manually install the necessary packages:

bash
Copy code
pip3 install tkinter configparser
Run the Installation Script

bash
Copy code
./install.sh
This will create an installed.txt file to signify successful installation.

Set Up the Execution Loop

Ensure that run_loop.sh is executable:

bash
Copy code
chmod +x run_loop.sh
Start the Application

bash
Copy code
./run_loop.sh
Usage
Launching the GUI

Run the following command to open the FaceSync GUI:

bash
Copy code
python3 GUI.py
Selecting Files

Driven File: The video whose face you want to animate.
Driving File: The video providing the facial movements.
Output File: Specify the location and name for the resulting video.
Starting the Process

Click the "Start FaceSync" button to begin the facial animation transfer. The application will handle the processing and save the output video to your specified location.

Configuration
FaceSync uses a config.ini file to store your project settings. This ensures that your selected files and preferences are saved for future use.

config.ini Structure
ini
Copy code
[OPTIONS]
Driven_file = /path/to/driven_video.mp4
Driving_file = /path/to/driving_video.mp4
Output_file = /path/to/output_video.mp4
You can manually edit this file if needed or use the GUI to manage configurations.

Contributing
Contributions are welcome! If you'd like to improve FaceSync, please follow these steps:

Fork the Repository

Create a Feature Branch

bash
Copy code
git checkout -b feature/YourFeatureName
Commit Your Changes

bash
Copy code
git commit -m "Add Your Feature"
Push to the Branch

bash
Copy code
git push origin feature/YourFeatureName
Open a Pull Request

Provide a clear description of your changes and why they're beneficial.

License
This project is licensed under the MIT License.
