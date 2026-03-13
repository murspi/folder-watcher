import time
from watchdog.observers import Observer
from handler import FileHandler

def start_watching(path):

    event_handler = FileHandler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f"Watching folder: {path} (Press Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping watcher...")
        observer.stop()

    observer.join()

