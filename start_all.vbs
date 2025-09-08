
import logging
import os

log_folder = "C:\\Projekt_AI\\logs"
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_folder, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Uruchomiono: NAZWA_SKRYPTU.py")

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Projekt_AI\start_all.bat" & chr(34), 0
