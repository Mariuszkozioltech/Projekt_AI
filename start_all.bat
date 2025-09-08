@echo off
cd /d "C:\Projekt_AI"

echo === START BACKEND === >> logs\bat_log.txt
call "start_backend_full.bat" >> logs\bat_log.txt 2>&1

echo === START FRONTEND === >> logs\bat_log.txt
call "start_frontend_static.bat" >> logs\bat_log.txt 2>&1

echo === START ASYSTENT === >> logs\bat_log.txt
call "start_asystent.bat" >> logs\bat_log.txt 2>&1
