# monitor.py
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from collections import deque
import logging
from file_carver import recover_files
import os

# Logging setup
logging.basicConfig(
    filename="activity_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Threshold for rapid deletions
DELETION_THRESHOLD = 4
TIME_WINDOW = 60  # seconds

class DeletionHandler(FileSystemEventHandler):
    def __init__(self, folder_to_monitor, snapshot_folder, recovery_folder):
        super().__init__()
        self.folder_to_monitor = folder_to_monitor
        self.snapshot_folder = snapshot_folder
        self.recovery_folder = recovery_folder
        self.deletion_times = deque()

    def on_deleted(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            
            # Log every deletion
            logging.info(f"Deleted file: {filename}")
            print(f"[-] Deleted: {filename}")

            current_time = time.time()
            self.deletion_times.append(current_time)

            # Remove old deletions outside the TIME_WINDOW
            while self.deletion_times and current_time - self.deletion_times[0] > TIME_WINDOW:
                self.deletion_times.popleft()

            # Rapid deletion alert
            if len(self.deletion_times) >= DELETION_THRESHOLD:
                logging.warning(f"Rapid deletions detected: {len(self.deletion_times)} files in {TIME_WINDOW} seconds")
                print("[!] Rapid deletions detected!")

                # Recover files
                recovered = recover_files(self.snapshot_folder, self.recovery_folder)
                
                # Already logged in recover_files
                self.deletion_times.clear()

def start_monitoring(folder_to_monitor, snapshot_folder, recovery_folder):
    event_handler = DeletionHandler(folder_to_monitor, snapshot_folder, recovery_folder)
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=False)
    observer.start()
    print(f"[+] Monitoring started on {folder_to_monitor}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
