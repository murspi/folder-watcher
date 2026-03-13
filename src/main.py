import json
import os
from watcher import start_watching

def load_config():
    # Get the project root (one level above /src)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, "config.json")

    print("Loading config from:", config_path)

    with open(config_path) as f:
        return json.load(f)

def main():
    config = load_config()
    folder = config["watch_folder"]

    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)

    start_watching(folder)

if __name__ == "__main__":
    main()
