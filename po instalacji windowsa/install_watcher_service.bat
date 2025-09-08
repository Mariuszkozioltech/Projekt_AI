@echo off
REM === KONFIGURACJA ===
set PYTHON_PATH=C:\Users\mariu\AppData\Local\Programs\Python\Python313\python.exe
set SCRIPT_PATH=C:\Projekt_AI\PROJEKT\strategia_inwestycyjna\watch_ibkr.py
set SERVICE_NAME=Watcher_IBKR

REM === TWORZENIE USŁUGI ===
sc create %SERVICE_NAME% binPath= "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" start= auto
sc description %SERVICE_NAME% "Automatyczny watcher IBKR - przenosi i przetwarza pliki"
sc start %SERVICE_NAME%

echo.
echo ✅ Usługa %SERVICE_NAME% została utworzona i uruchomiona.
echo Działa w tle i startuje automatycznie przy uruchomieniu systemu.
pause
