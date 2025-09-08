# Uruchom backend FastAPI w osobnym oknie PowerShell i otwórz dokumentację
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'cd C:\Projekt_AI\backend_api; Start-Process "http://127.0.0.1:8000/docs"; uvicorn main:app --reload --host 127.0.0.1 --port 8000'
