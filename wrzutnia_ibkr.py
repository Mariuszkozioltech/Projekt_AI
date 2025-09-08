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

import sys
import os
import shutil
import pandas as pd
import time

print("🚀 wrzutnia_ibkr.py został uruchomiony.")

def parse_ibkr_csv(filepath):
    print(f"📥 Próba wczytania pliku: {filepath}")

    # Sprawdzenie, czy plik nie jest pusty
    if os.path.getsize(filepath) == 0:
        print("⚠️ Plik jest pusty — brak danych do przetworzenia.")
        return

    try:
        df = pd.read_csv(filepath)
        print("📊 Wczytano dane:")
        print(df.head())  # Pokazuje tylko pierwsze 5 wierszy
    except Exception as e:
        print(f"❌ Błąd podczas wczytywania pliku: {e}")

def move_file_to_archive(filepath):
    archive_dir = r"C:\Projekt_AI\PROJEKT\strategia_inwestycyjna\Dokument IBKR archiwum"
    filename = os.path.basename(filepath)
    destination = os.path.join(archive_dir, filename)

    # Sprawdzenie, czy folder archiwum istnieje
    if not os.path.exists(archive_dir):
        print(f"📁 Folder archiwum nie istnieje: {archive_dir}")
        os.makedirs(archive_dir, exist_ok=True)
        print("📁 Folder został utworzony automatycznie.")

    try:
        shutil.move(filepath, destination)
        print(f"✅ Plik przeniesiony do archiwum: {destination}")
    except Exception as e:
        print(f"❌ Błąd podczas przenoszenia pliku: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Nie podano ścieżki do pliku jako argument.")
    else:
        filepath = sys.argv[1]

        # Poczekaj chwilę, jeśli plik dopiero się zapisuje
        time.sleep(2)

        if not os.path.exists(filepath):
            print(f"❗ Plik nie istnieje: {filepath}")
            sys.exit(1)

        parse_ibkr_csv(filepath)
        move_file_to_archive(filepath)


