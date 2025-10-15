# main.py
from file_carver import recover_files
from monitor import start_monitoring
import os

MONITORED_FOLDER = input("Enter folder to monitor: ").strip()
SNAPSHOT_FOLDER = os.path.join(MONITORED_FOLDER, ".snapshot")
RECOVERY_FOLDER = os.path.join(os.getcwd(), "Recovered")

os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)
os.makedirs(RECOVERY_FOLDER, exist_ok=True)

# Take initial snapshot of the folder
recover_files(MONITORED_FOLDER, SNAPSHOT_FOLDER)

print(f"[*] Starting File Recovery Tool on {MONITORED_FOLDER}...")
start_monitoring(MONITORED_FOLDER, SNAPSHOT_FOLDER, RECOVERY_FOLDER)
