import os
import time
from ibkr_parser import parse_ibkr_csv

# Folder na pulpicie, który obserwujemy
WATCH_FOLDER = r"C:\Users\mariu\OneDrive\Pulpit\Dokument IBKR do przerobienia"
# Folder RAW
RAW_BASE = r"C:\Users\mariu\data\raw"
# Plik logu
LOG_FILE = r"C:\Users\mariu\data\watcher_log.txt"

PROCESSED = set()

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

while True:
    try:
        files = [f for f in os.listdir(WATCH_FOLDER) if f.lower().endswith(".csv")]
        for file in files:
            if file not in PROCESSED:
                full_path = os.path.join(WATCH_FOLDER, file)

                # Ustal profil
                if file.lower().startswith("ibkr_"):
                    profile = "ibkr"
                else:
                    profile = file.split("_")[0].lower() + "_ibkr"

                # Utwórz folder RAW

\[profil]
                raw_profile_folder = os.path.join(RAW_BASE, profile)
                os.makedirs(raw_profile_folder, exist_ok=True)

                # Przenieś plik
                new_path = os.path.join(raw_profile_folder, file)
                os.rename(full_path, new_path)
                log(f"📂 Przeniesiono do RAW: {new_path}")

                # Uruchom parser
                parse_ibkr_csv(new_path)
                log(f"✅ Przetworzono plik: {file} dla profilu: {profile}")

                PROCESSED.add(file)

        time.sleep(5)

    except Exception as e:
        log(f"❌ Błąd: {e}")
        time.sleep(5)
