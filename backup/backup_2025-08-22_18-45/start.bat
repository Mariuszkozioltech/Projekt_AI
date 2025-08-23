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
echo.

REM === G��wne katalogi (ustawienia domy�lne) ===
set "BACKUP_DIR=%~dp0backup"
set "DATA_ANALYSIS_DIR=%~dp0dane_analizy"
set "LOG_DIR=%~dp0logi"
set "DOCS_DIR=%~dp0dokumentacja"
set "WORK_DIR=%~dp0praca"
set "SCENARIOS_DIR=%~dp0scenariusze"
set "STRATEGY_DIR=%~dp0strategia"
set "MEDIA_DIR=%~dp0multimedia"
set "COMM_DIR=%~dp0komunikacja"

REM === Katalog �r�d�owy i przywracania ===
set "SOURCE_DIR=C:\Projekt_AI"
set "RESTORE_DIR=%~dp0przywroc"

REM === Tworzenie katalog�w, je�li nie istniej� ===
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

REM === Tryb backupu z wy��czeniem komputera po zako�czeniu ===
if /i "%~1"=="shutdown" goto BACKUP_SHUTDOWN

REM === Dodatkowe zabezpieczenie dla katalog�w krytycznych ===
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

REM ------------------------------------------------------------------------
REM Sekcja 2 MENU � g��wne menu programu
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
echo 7) Tryb notatek w czasie rzeczywistym
echo 00) Wyj�cie
echo.
set /p CHOICE="Wybierz operacj� (0-7): "
if "!CHOICE!"=="1" goto BACKUP
if "!CHOICE!"=="2" goto RESTORE
if "!CHOICE!"=="3" goto ANALIZA
if "!CHOICE!"=="4" goto HASH
if "!CHOICE!"=="5" goto KONFIG6
if "!CHOICE!"=="6" goto FOLDERY
if "!CHOICE!"=="7" goto NOTATKI
if "!CHOICE!"=="00" goto KONIEC
echo B��dny wyb�r, spr�buj ponownie.
timeout /t 1 >nul
:FOLDERY
start "" "%BACKUP_DIR%"
start "" "%LOG_DIR%"
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 3 BACKUP � tworzenie kopii zapasowej
:BACKUP
cls
echo --- BACKUP DANYCH ---
echo.

REM �cie�ki docelowe
set "SOURCE_DIR=C:\Projekt_AI"
set "BACKUP_DIR=C:\Projekt_AI\backup"
set "LOG_DIR=C:\Projekt_AI\logi"

REM Tworzenie katalog�w je�li nie istniej�
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

REM Tworzenie znacznika czasu niezale�nie od ustawie� regionalnych
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH-mm"') do set "BACKUP_TIMESTAMP=%%i"

REM Docelowy katalog backupu z dat� i godzin�
set "BACKUP_TARGET=%BACKUP_DIR%\backup_%BACKUP_TIMESTAMP%"
mkdir "%BACKUP_TARGET%"

REM Plik logu
set "LOGFILE=%LOG_DIR%\backup_%BACKUP_TIMESTAMP%.log"

echo Rozpoczynam backup do: "%BACKUP_TARGET%" ...
robocopy "%SOURCE_DIR%" "%BACKUP_TARGET%" /MIR /DCOPY:T /COPY:DAT /R:3 /W:5 /TEE ^
 /XD "%SOURCE_DIR%\backup" "%SOURCE_DIR%\multimedia" /LOG+:"%LOGFILE%"

echo [%DATE% %TIME%] Backup zako�czony z kodem %ERRORLEVEL% >> "%LOGFILE%"
if %ERRORLEVEL% GEQ 8 (
    echo [B��D] Backup zako�czony z b��dem. Sprawd� log: %LOGFILE%
) else (
    echo Backup zako�czony sukcesem. Log: %LOGFILE%
)
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 4 RESTORE � przywracanie danych
:RESTORE
cls
echo --- PRZYWRACANIE BACKUPU ---
echo.
set "BACKUP_DIR=C:\Projekt_AI\backup"
set "RESTORE_TARGET=C:\Projekt_AI"

echo 1 - Przywr�� najnowszy backup
echo 2 - Otw�rz folder backup�w i wybierz r�cznie
echo 0 - Powr�t do menu
echo.
set /p "MODE=Tw�j wyb�r (0/1/2): "

if "%MODE%"=="0" goto MENU
if "%MODE%"=="1" goto RESTORE_LATEST
if "%MODE%"=="2" goto RESTORE_MANUAL
goto MENU

:RESTORE_LATEST
REM Znajd� najnowszy katalog backupu
for /f "delims=" %%i in ('dir "%BACKUP_DIR%" /ad /b /o-n') do (
    set "LATEST_BACKUP=%%i"
    goto :found_latest
)
:found_latest
if not defined LATEST_BACKUP (
    echo Brak dost�pnych backup�w.
    pause
    goto MENU
)
echo Najnowszy backup to: "%LATEST_BACKUP%"
set /p "CONFIRM=Czy chcesz go przywr�ci�? (T/N): "
if /i "%CONFIRM%" NEQ "T" goto MENU
robocopy "%BACKUP_DIR%\%LATEST_BACKUP%" "%RESTORE_TARGET%" /MIR /R:3 /W:5 /TEE
echo Przywracanie zako�czone.
pause
goto MENU

:RESTORE_MANUAL
REM Otw�rz folder backup�w w Eksploratorze
start "" "%BACKUP_DIR%"
echo.
echo Otworzy�em folder backup�w.
echo Przeci�gnij tutaj wybrany folder lub plik i wci�nij ENTER:
set /p "CUSTOM_PATH=�cie�ka: "
if "%CUSTOM_PATH%"=="" goto MENU
if not exist "%CUSTOM_PATH%" (
    echo Podana �cie�ka nie istnieje.
    pause
    goto MENU
)
set /p "CONFIRM=Czy chcesz przywr�ci� z '%CUSTOM_PATH%'? (T/N): "
if /i "%CONFIRM%" NEQ "T" goto MENU
robocopy "%CUSTOM_PATH%" "%RESTORE_TARGET%" /MIR /R:3 /W:5 /TEE
echo Przywracanie zako�czone.
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 5 ANALIZA � przegl�d i analiza plik�w log�w
:ANALIZA
cls
echo --- ANALIZA LOG�W ---
echo.

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
echo.

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
REM Sekcja 7 NOTATKI � uruchamianie trybu zapisu notatek i zasad
:NOTATKI
cls
echo --- TRYB NOTATEK W CZASIE RZECZYWISTYM ---
echo.
echo Ten tryb uruchamia skrypt B_asystent.py, kt�ry:
echo - co okre�lony czas (z config.json) dopisuje nowe wpisy do Notatki\YYYY-MM-DD.md
echo - reaguje na komend� ZAPISZ_ZASADA: ... i dopisuje do Zasady\ustalenia.md
echo.

REM Uruchomienie skryptu Pythona
REM Upewnij si�, �e python.exe jest w PATH lub podaj pe�n� �cie�k�
pushd "C:\Projekt_AI"
start "" python "B_asystent.py"
popd

echo Skrypt zosta� uruchomiony w nowym oknie. Mo�esz wr�ci� do menu.
pause
goto MENU

REM ------------------------------------------------------------------------
REM Sekcja 8 KONFIG � zmiana �cie�ek katalog�w
:KONFIG
cls
echo --- KONFIGURACJA KATALOG�W ---
echo.

echo 1) Backup:     %BACKUP_DIR%
echo 2) �r�d�o:     %SOURCE_DIR%
echo 3) Restore do: %RESTORE_DIR%
echo 4) Logi:       %LOG_DIR%
echo 0) Powr�t
echo 00) Wyj�cie
set /p KONFVAL="Numer do zmiany: "
if /i "%KONFVAL%"=="1" call :ZMIEN_SCIEZKE BACKUP_DIR
if /i "%KONFVAL%"=="2" call :ZMIEN_SCIEZKE SOURCE_DIR
if /i "%KONFVAL%"=="3" call :ZMIEN_SCIEZKE RESTORE_DIR
if /i "%KONFVAL%"=="4" call :ZMIEN_SCIEZKE LOG_DIR
if "%KONFVAL%"=="0" goto MENU
if "%KONFVAL%"=="00" goto KONIEC

:ZMIEN_SCIEZKE
set "VAR_NAME=%~1"
set /p "NEW_PATH=Nowa �cie�ka: "

REM Sprawd�, czy wpisano pe�n� �cie�k� (np. C:\co�tam)
echo %NEW_PATH% | findstr /R "^[A-Za-z]:\\" >nul
if errorlevel 1 (
    echo B��D: Podaj pe�n� �cie�k�, np. C:\MojePliki
    pause
    goto :EOF
)

REM Utw�rz folder, je�li nie istnieje
if not exist "%NEW_PATH%" (
    echo Folder nie istnieje. Tworz�...
    mkdir "%NEW_PATH%"
)

set "%VAR_NAME%=%NEW_PATH%"
echo Zmieniono ustawienie %VAR_NAME% na: %NEW_PATH%
pause
goto :EOF

REM ------------------------------------------------------------------------
REM Sekcja 9 FOLDERY � szybkie otwieranie katalog�w
:FOLDERY
cls
echo --- OTWIERANIE FOLDER�W ---
echo.

echo 1) Backup
echo 2) Praca (�r�d�o)
echo 3) Logi
echo 4) Dane analizy
echo 5) Dokumentacja
echo 6) Scenariusze
echo 7) Strategia
echo 8) Multimedia
echo 9) Komunikacja
echo 0) Powr�t
echo 00) Wyj�cie
set /p FCH="Wybierz: "
if /i "!FCH!"=="1" start "" "%BACKUP_DIR%"
if /i "!FCH!"=="2" start "" "%SOURCE_DIR%"
if /i "!FCH!"=="3" start "" "%LOG_DIR%"
if /i "!FCH!"=="4" start "" "%DATA_ANALYSIS_DIR%"
if /i "!FCH!"=="5" start "" "%DOCS_DIR%"
if /i "!FCH!"=="6" start "" "%SCENARIOS_DIR%"
if /i "!FCH!"=="7" start "" "%STRATEGY_DIR%"
if /i "!FCH!"=="8" start "" "%MEDIA_DIR%"
if /i "!FCH!"=="9" start "" "%COMM_DIR%"
if /i "!FCH!"=="0" goto MENU
if /i "!FCH!"=="00" goto KONIEC
goto FOLDERY


REM ------------------------------------------------------------------------
REM Sekcja 10 KONIEC � zako�czenie programu
:KONIEC
cls
echo Zamykanie programu...
timeout /t 2 >nul
exit
