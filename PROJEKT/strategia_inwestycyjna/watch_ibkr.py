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

import os
import time
import shutil
from ibkr_parser import parse_ibkr_csv

# Folder obserwowany (na pulpicie)
WATCH_FOLDER = r"C:\Users\mariu\OneDrive\Pulpit\Dokument IBKR do przerobienia"
# Folder RAW (poufne dane)
RAW_BASE = r"C:\Users\mariu\data\raw"
# Log (opcjonalnie)
LOG_FILE = r"C:\Projekt_AI\watcher_log.txt"

PROCESSED = set()

def log(msg: str):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

def detect_profile(file_name: str) -> str:
    name_no_ext = os.path.splitext(file_name)[0]
    if name_no_ext.lower().startswith("ibkr_"):
        return "ibkr"
    if "_" in name_no_ext:
        first = name_no_ext.split("_")[0]
        if first.isdigit() and len(first) == 4:
            return f"{first}_ibkr"
        return f"{first.lower()}_ibkr"
    return f"{name_no_ext.lower()}_ibkr"

def move_to_raw_nested(full_path: str, profile: str) -> str:
    base_name = os.path.splitext(os.path.basename(full_path))[0]
    raw_profile_folder = os.path.join(RAW_BASE, profile, base_name)
    os.makedirs(raw_profile_folder, exist_ok=True)
    dest_path = os.path.join(raw_profile_folder, os.path.basename(full_path))
    shutil.move(full_path, dest_path)
    return dest_path

def main():
    log(f"👀 Monitoruję folder: {WATCH_FOLDER}")
    while True:
        try:
            files = [f for f in os.listdir(WATCH_FOLDER) if f.lower().endswith(".csv")]
            for file in files:
                if file in PROCESSED:
                    continue
                full_path = os.path.join(WATCH_FOLDER, file)
                if not os.path.isfile(full_path):
                    continue

                profile = detect_profile(file)
                new_path = move_to_raw_nested(full_path, profile)
                log(f"📂 Przeniesiono do RAW: {new_path}")

                try:
                    parse_ibkr_csv(new_path)
                    log(f"✅ Przetworzono plik: {file} (profil: {profile})")
                except Exception as e:
                    log(f"❌ Błąd parsera dla {file}: {e}")

                PROCESSED.add(file)

            time.sleep(3)
        except KeyboardInterrupt:
            log("🛑 Zatrzymano watcher.")
            break
        except Exception as e:
            log(f"❌ Błąd watchera: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
