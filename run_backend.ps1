$ErrorActionPreference = "Stop"

# Utwórz i/lub aktywuj wirtualne środowisko
if (-not (Test-Path .\.venv\Scripts\Activate.ps1)) {
  python -m venv .venv
}
. .\.venv\Scripts\Activate.ps1

# Zainstaluj zależności backendu
if (Test-Path .\backend_api\requirements.txt) {
  pip install -r .\backend_api\requirements.txt
} else {
  Write-Host "Uwaga: brak backend_api\requirements.txt — pomijam instalację."
}

# Start serwera
Set-Location .\backend_api
uvicorn main:app --host 0.0.0.0 --port 8000
