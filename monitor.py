# monitor.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class DeletionHandler(FileSystemEventHandler):
    def __init__(self, alert_callback):
        super().__init__()
        self.deleted_files = []
        self.alert_callback = alert_callback
        self.time_window = 60  # seconds
        self.threshold = 4     # files deleted in 1 minute

    def on_deleted(self, event):
        if not event.is_directory:
            self.deleted_files.append(time.time())
            self.cleanup_old_events()
            if len(self.deleted_files) >= self.threshold:
                self.alert_callback(self.deleted_files)

    def cleanup_old_events(self):
        now = time.time()
        self.deleted_files = [t for t in self.deleted_files if now - t < self.time_window]

def start_monitoring(folder_to_watch, alert_callback):
    event_handler = DeletionHandler(alert_callback)
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()
    print(f"[+] Monitoring started on {folder_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
