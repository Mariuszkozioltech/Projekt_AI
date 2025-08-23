@echo off
title SYSTEM BACKUP – PROJEKT AI
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul

REM ====== ŚCIEŻKI ======
set "ROOT=%~dp0"
set "BASE=C:\Projekt_AI\PROJEKT"
set "START_BAT=%~f0"
set "BACKUP_START=%BASE%\backup\start"
set "BACKUP_FULL=%BASE%\backup\pelne"
set "LAST_HASH_FILE=%BACKUP_START%\last_hash.txt"

REM ====== Struktura PROJEKT ======
for %%D in (
    "strategia_inwestycyjna\materiały"
    "strategia_inwestycyjna\raporty"
    "praca\projekty"
    "praca\raporty"
    "dom\kamery"
    "dom\glosniki"
    "dom\swiatla"
    "dom\czujniki"
    "dom\garaz_ogrod"
    "komunikacja\powiadomienia"
    "komunikacja\skrypty"
    "zdjecia_i_filmy\wycieczki"
    "zdjecia_i_filmy\wydarzenia"
    "zdjecia_i_filmy\albumy_z_opisami"
    "AI_trening\notatki"
    "AI_trening\przyklady"
) do if not exist "%BASE%\%%~D" mkdir "%BASE%\%%~D"

mkdir "%BACKUP_START%" 2>nul
mkdir "%BACKUP_FULL%" 2>nul

echo Struktura PROJEKT została przygotowana w: %BASE%

REM ====== Autostart: auto-backup start.bat + dzienny pełny backup ======
call :AutoBackupStartBat
call :DailyFullBackup

:MENU
cls
call :GetTimestamp NOW "yyyy-MM-dd HH:mm:ss"
echo ================================
echo MENU GLOWNE – %NOW%
echo ================================
echo 1 - BACKUP (podmenu)
echo 2 - Otworz folder Analiza Startowa i utworz raport
echo 3 - Uruchom analize danych (analiza.py)
echo 4 - Zakoncz
echo ================================
set "wybor="
set /p "wybor=Wybierz opcje: "

if "%wybor%"=="1" goto BACKUP_MENU
if "%wybor%"=="2" goto ANALIZA_STARTOWA
if "%wybor%"=="3" goto ANALIZA_DANYCH
if "%wybor%"=="4" goto END

echo Nieprawidlowy wybor.
pause
goto MENU

:BACKUP_MENU
cls
call :GetTimestamp NOW "yyyy-MM-dd HH:mm:ss"
echo ================================
echo MENU BACKUP – %NOW%
echo ================================
echo 1 - Wykonaj oba backupy (pelny + start.bat)
echo 2 - Wykonaj backup tylko start.bat
echo 3 - Wykonaj pelny backup projektu teraz
echo 4 - Przywroc plik start.bat z kopii
echo 5 - Przywroc pelny backup projektu
echo 6 - Przywroc wskazany plik lub folder z backupu
echo 7 - Otworz folder backupow
echo 8 - Cofnij do poprzedniego menu
echo 9 - Powrot do menu glownego
echo ================================
set "bwybor="
set /p "bwybor=Wybierz opcje: "

if "%bwybor%"=="1" (
    call :GetTimestamp TS "yyyy-MM-dd_HH-mm"
    call :SafeManualBackupStartBat "%TS%"
    call :RunFullBackup manual "%TS%"
    goto BACKUP_MENU
)
if "%bwybor%"=="2" (
    call :GetTimestamp TS "yyyy-MM-dd_HH-mm"
    call :SafeManualBackupStartBat "%TS%"
    goto BACKUP_MENU
)
if "%bwybor%"=="3" (
    call :GetTimestamp TS "yyyy-MM-dd_HH-mm"
    call :RunFullBackup manual "%TS%"
    goto BACKUP_MENU
)
if "%bwybor%"=="4" call :RestoreStartBat & goto BACKUP_MENU
if "%bwybor%"=="5" call :RestoreFullProject & goto BACKUP_MENU
if "%bwybor%"=="6" call :RestoreCustom & goto BACKUP_MENU
if "%bwybor%"=="7" call :OpenBackupFolders & goto BACKUP_MENU
if "%bwybor%"=="8" goto MENU
if "%bwybor%"=="9" goto MENU

echo Nieprawidlowy wybor.
pause
goto BACKUP_MENU

:RestoreCustom
echo.
set /p "src=Podaj pelna sciezke do pliku lub folderu w backupie: "
if not exist "%src%" (
    echo Nie znaleziono: %src%
    pause
    goto BACKUP_MENU
)
echo.
set /p "dest=Podaj folder docelowy (Enter = katalog projektu): "
if not defined dest set "dest=%BASE%"
if exist "%src%\*" (
    robocopy "%src%" "%dest%" /E /R:1 /W:1 /NFL /NDL /NP >nul
) else (
    copy /Y "%src%" "%dest%" >nul
)
echo Gotowe.
pause
goto BACKUP_MENU

REM ======================== AKCJE BACKUP ========================

:SafeManualBackupStartBat
set "TS=%~1"
if not defined TS exit /b
if not exist "%BACKUP_START%" mkdir "%BACKUP_START%"
copy /y "%START_BAT%" "%BACKUP_START%\%TS%_start_manual.bat" >nul
if exist "%BACKUP_START%\%TS%_start_manual.bat" (
  echo OK: Utworzono: "%BACKUP_START%\%TS%_start_manual.bat"
) else (
  echo BLAD: Nie udalo sie skopiowac "%START_BAT%" do "%BACKUP_START%"
)
pause
exit /b

:RunFullBackup
set "TS=%~2"
if not defined TS exit /b
set "DEST=%BACKUP_FULL%\%TS%_pelny"
mkdir "%DEST%" 2>nul
robocopy "%BASE%" "%DEST%" /E /XJ /R:1 /W:1 /XD "%BASE%\backup" "%BASE%\zdjecia_i_filmy" /NFL /NDL /NP >nul
copy /Y "%START_BAT%" "%BACKUP_START%\%TS%_start.bat" >nul
set "RC=%ERRORLEVEL%"
if %RC% GEQ 8 (
    echo [BŁĄD] Robocopy przerwane (kod: %RC%)
) else if %RC% GTR 0 (
    echo [UWAGA] Backup z ostrzeżeniami (kod: %RC%)
) else (
    echo [OK] Pelny backup zakonczony: "%DEST%"
)
pause
exit /b

:RestoreStartBat
explorer "%BACKUP_START%"
echo.
set /p "file=Ścieżka/nazwa: "
if not exist "%file%" (
    if exist "%BACKUP_START%\%file%" (
        set "file=%BACKUP_START%\%file%"
    ) else (
        echo [BŁĄD] Nie znaleziono pliku!
        pause
        goto BACKUP_MENU
    )
)
if /I not "%~xfile%"==".bat" (
    echo [BŁĄD] To nie jest plik .bat
    pause
    goto BACKUP_MENU
)
copy /Y "%file%" "%START_BAT%" >nul
echo [OK] Przywrócono start.bat z: %file%
pause
goto BACKUP_MENU

:RestoreFullProject
explorer "%BACKUP_FULL%"
echo.
set /p "folder=Ścieżka: "
if not exist "%folder%" (
    echo [BŁĄD] Podana ścieżka nie istnieje!
    pause
    goto BACKUP_MENU
)
robocopy "%folder%" "%BASE%" /E /DCOPY:AT /COPY:DAT /R:0 /W:0 /IS /IT
if exist "%BACKUP_START%\%~nxfolder%_start.bat" (
    copy /Y "%BACKUP_START%\%~nxfolder%_start.bat" "%START_BAT%" >nul
)
echo [OK] Przywrócono pełny backup z: %folder%
pause
goto BACKUP_MENU

:OpenBackupFolders
explorer "%BACKUP_START%"
explorer "%BACKUP_FULL%"
exit /b

REM ======================== INNE FUNKCJE ========================

