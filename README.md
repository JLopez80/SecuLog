# SecuLog
A Python-based file monitoring and recovery tool designed for digital forensics and security analysis. It continiously monitors a directory for suspicious activity such as rapid file deletion. It also logs every event and automatically recovers deleted files from a stored snapshot.

## Requirements
Make sure the following requirements are met:
- **Python 3.8 or higher** 
  - Install Python from: [python.org](https://www.python.org/downloads/)
    
- **Watchdog library** - Used to monitor folder events in real time
  ```bash
       pip install watchdog
  
- **Standard Python libraries** - Necessary for this project (comes included with Python by default)
  - os
  - shutil
  - hashlib
  - logging
  - time
  - collection

## Getting Started
Once you've confirmed that all requirements are installed, follow these steps (can be done in terminal or code editor. Up to preference):
1. **Create the Project Folder**
   - Choose a location on your computer where you want to keep SecuLog.
   - Create a folder with your preferred name.
     - Example for Terminal:
       ```bash
           mkdir SecuLog
           cd SecuLog
   - Place Python files into this folder.
     - [main.py](main.py)
     - [monitor.py](monitory.py)
     - [file_carver.py](file_carver.py)
       - **✅ Note:** The project will automatically create the folders .snapshot/ and Recovered/ when you run it, so you don’t need to create them manually.  

2. **Run the Project**
   - Run the main program:
     - Terminal Example:
        ```bash
            python main.py
     - > ⚠️ On some systems, you may need to use python3 instead of python:
        ```bash
            python3 main.py
      
   - When prompted, enter the folder you want to monitor.
     - Example:
       ```bash
           Enter folder: C:\Users\YourName\Documents
       
   - After selecting the folder, the program will:
     - Take initial snapshot of existing files in that folder (only **.jpg**, **.jpeg**, **.png**, and **.pdf**)
     - Start monitoring the folder for file deletions
     - Automatically recovers deleted files if suspicious (rapid deletion)
     - Log all actions in **activity_log.txt**
    
3. **Check Results**

       

    





