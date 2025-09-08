
@echo off
cd /d "C:\Projekt_AI"
powershell -WindowStyle Hidden -Command "python asystent_etapowy.py" >> "logs\asystent_log.txt" 2>&1
