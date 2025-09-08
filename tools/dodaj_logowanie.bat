@echo off
cd /d "C:\Projekt_AI"

start "" "start_backend_full.bat" >> "logs\bat_log.txt" 2>&1
start "" "start_frontend_static.bat" >> "logs\bat_log.txt" 2>&1
start "" "start_asystent.bat" >> "logs\bat_log.txt" 2>&1