# Folder Watcher

A Python tool that monitors a folder for file events (create, delete, modify, move) and automatically processes new files.

## Features
- Detects file creation, deletion, modification, and movement
- Automatically moves new files to `/processed`
- Logs all events to `/logs/events.log`
- Moves problematic files to `/logs/bad_files`
- Uses project-root-based paths for reliability
- Clean logging using Python's `logging` module

## Project Structure
folder-watcher/
│
├── logs/               # Event logs + bad_files/
├── processed/          # Successfully processed files
├── src/
│   ├── main.py         # Entry point
│   ├── watcher.py      # Watchdog observer setup
│   ├── handler.py      # Event handler logic
│
├── watch-folder/       # Folder being monitored
├── config.json         # Configuration
├── requirements.txt
└── README.md

## Configuration
config.json:
{
    "watch_folder": "watch-folder"
}

## Setup
python -m venv venv
pip install -r requirements.txt

## Run
python src/main.py