@echo off
REM start.bat � uniwersalny skrypt backupu, przywracania, analizy oraz hash�w
REM Autor: [Tw�j zesp�/projekt]
REM Opis: Kompleksowy system backupowy na Windows (PL), pe�na dokumentacja w komentarzach

CHCP 65001 >nul
setlocal EnableExtensions EnableDelayedExpansion

REM ------------------------------------------------------------------------
REM Sekcja 1 KONFIGURACJA � ustawienia domy�lne i katalogi
:KONFIGURACJA
cls
set "BACKUP_DIR=%~dp0backup"
set "DATA_ANALYSIS_DIR=%~dp0dane_analizy"
set "LOG_DIR=%~dp0logi"
set "DOCS_DIR=%~dp0dokumentacja"
set "WORK_DIR=%~dp0praca"
set "SCENARIOS_DIR=%~dp0scenariusze"
set "STRATEGY_DIR=%~dp0strategia"
set "MEDIA_DIR=%~dp0multimedia"
set "COMM_DIR=%~dp0komunikacja"

set "SOURCE_DIR=C:\Projekt_AI"
set "RESTORE_DIR=%~dp0przywroc"

for %%D in (
    "%BACKUP_DIR%"
    "%DATA_ANALYSIS_DIR%"
    "%LOG_DIR%"
    "%DOCS_DIR%"
    "%WORK_DIR%"
    "%SCENARIOS_DIR%"
    "%STRATEGY_DIR%"
    "%MEDIA_DIR%"
    "%COMM_DIR%"
    "%RESTORE_DIR%"
) do (
    if not exist %%~D mkdir %%~D
)

if /i "%~1"=="shutdown" goto BACKUP_SHUTDOWN

if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

REM ------------------------------------------------------------------------
REM Sekcja 2 MENU � g��wne menu programucls
:MENU
cls
echo.
echo ==========================
echo    SYSTEM BACKUPOWY v1
echo ==========================
echo.
echo 1) Backup danych
echo 2) Przywracanie danych
echo 3) Analiza log�w backupu
echo 4) Hashowanie pliku
echo 5) Konfiguracja katalog�w
echo 6) Otw�rz foldery
echo 00) Wyj�cie
echo.
set /p CHOICE="Wybierz operacj� (0-6): "
if "!CHOICE!"=="1" goto BACKUP
if "!CHOICE!"=="2" goto RESTORE
if "!CHOICE!"=="3" goto ANALYZA
if "!CHOICE!"=="4" goto HASH
if "!CHOICE!"=="5" goto KONFIG
if "!CHOICE!"=="6" goto FOLDERY
if "!CHOICE!"=="00" goto KONIEC
echo B��dny wyb�r, spr�buj ponownie.
timeout /t 1 >nul
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 3 BACKUP � tworzenie kopii zapasowej
:Backup
cls
echo --- BACKUP DANYCH ---
set "HH=%TIME:~0,2%"
if "%HH:~0,1%"==" " set "HH=0%HH:~1,1%"
set "BACKUP_TIMESTAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%_%HH%-%TIME:~3,2%"
set "BACKUP_DIR=%~dp0backup\backup_%BACKUP_TIMESTAMP%"
mkdir "%BACKUP_DIR%"
set "LOGFILE=%LOG_DIR%\backup_%BACKUP_TIMESTAMP%.log"
echo Rozpoczynam backup...
robocopy "%SOURCE_DIR%" "%BACKUP_DIR%" /MIR /DCOPY:T /COPY:DAT /R:3 /W:5 /TEE ^
 /XD "%SOURCE_DIR%\backup" "%SOURCE_DIR%\multimedia" /LOG+:"%LOGFILE%" >nul
echo [%DATE% %TIME%] Backup zako�czony z kodem %ERRORLEVEL% >> "%LOGFILE%"
if %ERRORLEVEL% GEQ 8 (
    echo [B��D] Backup zako�czony z b��dem. Sprawd� log: %LOGFILE%
) else (
    echo Backup zako�czony sukcesem. Log: %LOGFILE%
)
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 4 RESTORE
:RESTORE
cls
echo --- PRZYWRACANIE DANYCH ---
echo Docelowy katalog: %RESTORE_DIR%
if not exist "%RESTORE_DIR%" mkdir "%RESTORE_DIR%"
echo Przywrocic z:
echo 1) Ostatniego backupu (%BACKUP_DIR%)
echo 2) Wybra� inn� �cie�k�
echo 0) Powr�t
set /p RCH="Wybierz opcj�: "

if /i "%RCH%"=="1" (
    set "SRC_RESTORE=%BACKUP_DIR%"
) else if /i "%RCH%"=="2" (
    start "" "%BACKUP_DIR%"
    echo.
    echo Przeci�gnij tutaj wybrany folder backupu i naci�nij ENTER:
    set /p SRC_RESTORE=
    if not exist "!SRC_RESTORE!" (
        echo Podany katalog nie istnieje.
        pause
        goto RESTORE
    )
) else (
    goto MENU
)

set "HH=%TIME:~0,2%"
if "%HH:~0,1%"==" " set "HH=0%HH:~1,1%"
set "REST_TIMESTAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%_%HH%-%TIME:~3,2%"

set "LOGFILE=%LOG_DIR%\restore_%REST_TIMESTAMP%.log"
robocopy "%SRC_RESTORE%" "%RESTORE_DIR%" /MIR /DCOPY:T /COPY:DAT /R:3 /W:5 /TEE /LOG+:"%LOGFILE%"
set ERRLVL=%ERRORLEVEL%
echo [%DATE% %TIME%] Restore zako�czony z kodem %ERRLVL% >> "%LOGFILE%"
if %ERRLVL% GEQ 8 (
    echo [B��D] Przywracanie z b��dem. Sprawd� log: %LOGFILE%
) else (
    echo Przywracanie zako�czone sukcesem. Log: %LOGFILE%
)
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 5 ANALIZA � przegl�d i analiza plik�w log�w
:ANALIZA
cls
echo --- ANALIZA LOG�W ---
dir "%LOG_DIR%\backup_*.log" /b
set /p ANLFILE="Podaj nazw� pliku logu lub ENTER (najnowszy): "
if "!ANLFILE!"=="" (
    for /f "delims=" %%f in ('dir /b /o-d "%LOG_DIR%\backup_*.log"') do (
        set "ANLFILE=%%f"
        goto ANA1
    )
)
:ANA1
if not exist "%LOG_DIR%\!ANLFILE!" (
    echo Log !ANLFILE! nie istnieje.
    pause
    goto MENU
)
findstr /i /c:"ERROR" "%LOG_DIR%\!ANLFILE!"
findstr /i /c:"copied" "%LOG_DIR%\!ANLFILE!"
findstr /i /c:"Extra" "%LOG_DIR%\!ANLFILE!"
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 6 HASH � obliczanie sumy kontrolnej pliku
:HASH
cls
echo --- HASHOWANIE PLIKU ---
set /p HASHFILE="Podaj �cie�k� do pliku: "
if not exist "!HASHFILE!" (
    echo Plik nie istnieje: !HASHFILE!
    pause
    goto MENU
)
echo 1) MD5
echo 2) SHA1
echo 3) SHA256
set /p HASHTYPE="Tw�j wyb�r: "
if "!HASHTYPE!"=="1" set "ALG=MD5"
if "!HASHTYPE!"=="2" set "ALG=SHA1"
if "!HASHTYPE!"=="3" set "ALG=SHA256"
if not defined ALG goto MENU
certutil -hashfile "!HASHFILE!" !ALG!
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 7 KONFIG � zmiana �cie�ek katalog�w
:KONFIG
cls
echo --- KONFIGURACJA KATALOG�W ---
echo 1) Backup:     %BACKUP_DIR%
echo 2) �r�d�o:     %SOURCE_DIR%
echo 3) Restore do: %RESTORE_DIR%
echo 4) Logi:       %LOG_DIR%
echo 0) Powr�t
echo 00) Wyj�cie
set /p KONFVAL="Numer do zmiany: "
if /i "%KONFVAL%"=="1" set /p "BACKUP_DIR=Nowa �cie�ka: "
if /i "%KONFVAL%"=="2" set /p "SOURCE_DIR=Nowa �cie�ka: "
if /i "%KONFVAL%"=="3" set /p "RESTORE_DIR=Nowa �cie�ka: "
if "%KONFVAL%"=="0" goto MENU
if "%KONFVAL%"=="00" goto KONIEC
goto KONFIG
:KONIEC
exit