import logging
import json
import os
from watcher import start_watching

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOGS_DIR, "events.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config():
    config_path = os.path.join(BASE_DIR, "config.json")
    with open(config_path) as f:
        return json.load(f)

def main():
    config = load_config()
    folder = os.path.join(BASE_DIR, config["watch_folder"])

    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)

    start_watching(folder)

if __name__ == "__main__":
    main()
