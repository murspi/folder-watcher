# Folder Watcher

A Python tool that monitors a folder for file events (create, delete, modify, move)
and automatically processes new files.

## Features
- Detects file creation, deletion, modification, and movement
- Automatically moves new files to /processed
- Logs all events to /logs
- Moves problematic files to /logs/bad_files

## Setup
1. Create a virtual environment
2. Install dependencies:
   pip install -r requirements.txt

## Run
python src/main.py