Set WshShell = CreateObject("WScript.Shell")

' 🔧 Ścieżka do Pythona — potwierdzona
pythonPath = "C:\Users\mariu\AppData\Local\Programs\Python\Python313\python.exe"

' 🔧 Ścieżka do skryptu
scriptPath = "C:\Projekt_AI\tools\dodaj_logowanie.py"

' 🔧 Ścieżka do logu
logPath = "C:\Projekt_AI\logi_analizy\vbs_log.txt"

' 🔧 Komenda uruchamiająca
command = "cmd /c """ & pythonPath & """ """ & scriptPath & """ > """ & logPath & """ 2>&1"

' 🔧 Uruchomienie z widocznym oknem (1) lub w tle (0)
WshShell.Run command, 1
