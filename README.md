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
