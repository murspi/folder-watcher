import os
import shutil
from watchdog.events import FileSystemEventHandler
from datetime import datetime

LOGS_DIR = "logs"
PROCESSED_DIR = "processed"
BAD_FILES_DIR = os.path.join(LOGS_DIR, "bad_files")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(BAD_FILES_DIR, exist_ok=True)

def log_event(message, log_file="events.log"):
    log_path = os.path.join(LOGS_DIR, log_file)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

class FileHandler(FileSystemEventHandler):

    def process_file(self, src_path):
        filename = os.path.basename(src_path)
        dest_path = os.path.join(PROCESSED_DIR, filename)

        try:
            shutil.move(src_path, dest_path)
            log_event(f"Processed file: {filename}")

        except Exception as e:
            log_event(f"Failed to move bad file: {src_path}", log_file="bad_files.log")

            try:
                bad_path = os.path.join(BAD_FILES_DIR, filename)
                shutil.move(src_path, bad_path)
            except:
                log_event(f"Failed to move bad file: {src_path}", log_file="bad_files.log")

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            log_event(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            log_event(f"File modified: {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            log_event(f"File moved: {event.src_path} → {event.dest_path}")