@echo off
cd /d "%~dp0"
echo Starting Agnes Mortgage local server at http://localhost:8000
start "" http://localhost:8000
python local-server.py
