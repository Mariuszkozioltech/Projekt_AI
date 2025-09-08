@echo off
set SERVICE_NAME=Watcher_IBKR

echo 🔴 Zatrzymywanie usługi %SERVICE_NAME%...
sc stop %SERVICE_NAME%

echo 🗑 Usuwanie usługi %SERVICE_NAME%...
sc delete %SERVICE_NAME%

echo ✅ Usługa %SERVICE_NAME% została usunięta z systemu.
pause
