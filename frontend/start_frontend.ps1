# === start_frontend.ps1 ===
$frontendPath = "C:\Projekt_AI\frontend"
$indexFile = Join-Path $frontendPath "index.html"
$logFile = "C:\Projekt_AI\logs\app.log"

# Tworzenie folderu logów jeśli nie istnieje
if (!(Test-Path "C:\Projekt_AI\logs")) {
    New-Item -ItemType Directory -Path "C:\Projekt_AI\logs" | Out-Null
}

# Logowanie uruchomienia
Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - INFO - Uruchomiono start_frontend.ps1"

# Sprawdzenie czy plik index.html istnieje
if (Test-Path $indexFile) {
    Write-Host "✅ Uruchamiam frontend..."
    Start-Process $indexFile
} else {
    Write-Host "❌ Nie znaleziono pliku index.html w folderze frontend."
    Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - ERROR - Brak pliku index.html"
}
