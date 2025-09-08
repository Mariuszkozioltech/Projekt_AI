
@echo off
cd /d "C:\Projekt_AI\frontend"
python -m http.server 5173 >> "..\logs\frontend_log.txt" 2>&1
