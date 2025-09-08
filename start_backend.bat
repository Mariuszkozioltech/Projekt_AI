@echo off
cd /d C:\Projekt_AI\backend_api
uvicorn main:app --host 127.0.0.1 --port 8000
