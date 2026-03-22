import os
import shutil
import logging
from watchdog.events import FileSystemEventHandler
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGS_DIR = os.path.join(BASE_DIR, "logs")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
BAD_FILES_DIR = os.path.join(LOGS_DIR, "bad_files")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(BAD_FILES_DIR, exist_ok=True)
class FileHandler(FileSystemEventHandler):

    def process_file(self, src_path):
        filename = os.path.basename(src_path)
        dest_path = os.path.join(PROCESSED_DIR, filename)

        try:
            shutil.move(src_path, dest_path)
            logging.info(f"Processed file: {filename}")

        except Exception as e:
            logging.error(f"Failed to process file: {src_path}")

            try:
                bad_path = os.path.join(BAD_FILES_DIR, filename)
                shutil.move(src_path, bad_path)
            except:
                logging.error(f"Failed to move bad file: {src_path}")

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            logging.info(f"File moved: {event.src_path} → {event.dest_path}")