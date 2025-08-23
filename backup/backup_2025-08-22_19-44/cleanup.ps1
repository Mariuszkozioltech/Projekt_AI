# cleanup.ps1

# Sciezki do katalogow
$BackupDir = "C:\Projekt_AI\backup"
$LogDir    = "C:\Projekt_AI\logi"

Write-Host "=== USUWANIE STARYCH BACKUPOW ==="
if (Test-Path $BackupDir) {
    # Pobierz katalogi z glownego folderu backup i posortuj wg daty najnowszego pliku w srodku
    $backups = Get-ChildItem -Path $BackupDir -Directory |
        Sort-Object {
            (Get-ChildItem -Path $_.FullName -File -Recurse |
             Sort-Object LastWriteTime -Descending |
             Select-Object -First 1).LastWriteTime
        } -Descending

    if ($backups.Count -gt 1) {
        $backups | Select-Object -Skip 1 | ForEach-Object {
            try {
                Remove-Item $_.FullName -Recurse -Force
                Write-Host ("Usunieto backup: " + $_.FullName)
            } catch {
                Write-Host ("Blad usuwania " + $_.FullName + ": " + $_)
            }
        }
    } else {
        Write-Host "Brak starych backupow do usuniecia."
    }
} else {
    Write-Host "Katalog backup nie istnieje."
}

Write-Host "=== USUWANIE STARYCH LOGOW ==="
if (Test-Path $LogDir) {
    $logs = Get-ChildItem -Path $LogDir -Filter *.log -File |
            Sort-Object LastWriteTime -Descending
    if ($logs.Count -gt 1) {
        $logs | Select-Object -Skip 1 | ForEach-Object {
            try {
                Remove-Item $_.FullName -Force
                Write-Host ("Usunieto log: " + $_.FullName)
            } catch {
                Write-Host ("Blad usuwania " + $_.FullName + ": " + $_)
            }
        }
    } else {
        Write-Host "Brak starych logow do usuniecia."
    }
} else {
    Write-Host "Katalog logow nie istnieje."
}

Write-Host "Czyszczenie zakonczone"
