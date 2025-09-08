import os
import csv
from datetime import datetime
import hashlib
import logging

def wczytaj_cache():
    cache_path = os.path.join(LOG_FOLDER, "cache.csv")
    if not os.path.exists(cache_path):
        return
    with open(cache_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                CACHE_HASHY.add(parts[2])  # hash

def get_file_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return "Błąd haszowania"

# 🔧 Konfiguracja
PROJEKT_FOLDER = "C:\\Projekt_AI"
LOG_FOLDER = os.path.join(PROJEKT_FOLDER, "logi_analizy")
RAPORT_CSV = os.path.join(LOG_FOLDER, "raport_zbiorczy.csv")
DRY_RUN = True  # Zmień na False, jeśli chcesz faktycznie modyfikować pliki

# 📝 Logowanie do pliku
logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "asystent_log.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 📁 Foldery klasyfikacji
KLASYFIKACJE = {
    "dodane": [],
    "zmienione": [],
    "oczekujące": [],
    "duplikaty": [],
    "poprawne": [],
    "błędy": [],
    "inne": []
}
WSZYSTKIE_HASHY = {}

CACHE_HASHY = set()

# 📄 Kod logowania do wstawienia
LOG_CODE = '''# === AUTOLOG START ===
import logging
import os
log_folder = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_folder, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_folder, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info(f"Uruchomiono: {os.path.basename(__file__)}")
# === AUTOLOG END ===
'''

with open("C:\\Projekt_AI\\logi_analizy\\vbs_log.txt", "a", encoding="utf-8") as f:
    f.write("✅ Skrypt uruchomiony z Harmonogramu\n")

print("🔧 Skrypt uruchomiony — start analizy")

def analizuj_plik(full_path):
    try:
        ext = os.path.splitext(full_path)[1].lower()
        if ext not in [".py"]:
            return "inne", f"Zarejestrowano plik {ext} (bez analizy)"
        ext = os.path.splitext(full_path)[1].lower()
        if ext != ".py":
            return "inne", f"Zarejestrowano plik {ext} (bez analizy)"
        # 🔍 Próba odczytu pliku z obsługą różnych kodowań
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(full_path, "r", encoding="utf-8-sig") as f:
                    content = f.read()
            except Exception as e:
                return "błędy", f"Błąd dekodowania: {e}"

        # 🔒 Pominięcie własnego pliku'
        if "dodaj_logowanie.py" in full_path:
            return "błędy", "Pominięto własny plik"

        # 🔎 Klasyfikacja
        if "# === AUTOLOG START ===" in content:
            return "poprawne", "Logowanie już dodane"

        if "logging" in content and "basicConfig" in content:
            return "zmienione", "Inne logowanie wykryte"

        if content.strip().startswith("import logging"):
            return "oczekujące", "Logowanie nie na początku"

        return "dodane", "Dodano logowanie"

    except Exception as e:
        return "błędy", f"Błąd: {e}"

def dodaj_logowanie(folder, dry_run=True):
    os.makedirs(LOG_FOLDER, exist_ok=True)
    for root, dirs, files in os.walk(folder):
        # ❌ Pomijaj foldery zawierające "backup"
        if "backup" in root.lower():
            continue

        for file in files:
            print(f"🔍 Przetwarzam plik: {file}")
            full_path = os.path.join(root, file)
            status, opis = analizuj_plik(full_path)
            print(f"📦 {file} → {status} | {opis}")
            hash_val = get_file_hash(full_path)

            if hash_val in CACHE_HASHY:
                continue  # Pomijamy plik, bo już był analizowany

            if hash_val in WSZYSTKIE_HASHY:
                KLASYFIKACJE["duplikaty"].append((file, full_path, f"Duplikat pliku: {WSZYSTKIE_HASHY[hash_val]}"))
            else:
                WSZYSTKIE_HASHY[hash_val] = file
                KLASYFIKACJE[status].append((file, full_path, opis))

                if status == "dodane" and not dry_run:
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(LOG_CODE + content)
                    except Exception as e:
                        KLASYFIKACJE["błędy"].append((file, full_path, f"Błąd zapisu: {e}"))

def generuj_raport_csv():
    with open(RAPORT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        teraz = datetime.now()

def zapisz_cache():
    teraz = datetime.now()
    cache_path = os.path.join(LOG_FOLDER, "cache.csv")
    with open(cache_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for status, pliki in KLASYFIKACJE.items():
            for file, path, opis in pliki:
                hash_val = get_file_hash(path)
                writer.writerow([file, path, hash_val])

        # 🔹 Nagłówek zbiorczy
        total = sum(len(pliki) for pliki in KLASYFIKACJE.values())
        writer.writerow(["Raport wygenerowany", teraz.strftime("%Y-%m-%d %H:%M:%S")])
        writer.writerow(["Liczba plików przeanalizowanych", total])
        for status in KLASYFIKACJE:
            writer.writerow(["Pliki w kategorii " + status.capitalize(), len(KLASYFIKACJE[status])])
        writer.writerow([])

        # 🔹 Tabela szczegółowa
        writer.writerow(["Nazwa pliku", "Lokalizacja", "Data", "Godzina", "Status", "Opis", "Hash", "Link"])
        for status, pliki in sorted(KLASYFIKACJE.items()):
            for file, path, opis in sorted(pliki, key=lambda x: x[0]):
                hash_val = get_file_hash(path)
                link = f"file:///{path.replace(os.sep, '/')}"
                writer.writerow([
                    file,
                    path,
                    teraz.strftime("%Y-%m-%d"),
                    teraz.strftime("%H:%M:%S"),
                    status.upper(),
                    opis,
                    hash_val,
                    link
                ])

    # 🔹 Osobne raporty per kategoria
    for status, pliki in KLASYFIKACJE.items():
        if pliki:
            with open(os.path.join(LOG_FOLDER, f"{status}.csv"), "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["Nazwa pliku", "Lokalizacja", "Opis"])
                for file, path, opis in sorted(pliki, key=lambda x: x[0]):
                    w.writerow([file, path, opis])

def utworz_foldery_klasyfikacji():
    wczytaj_cache()
    for folder in KLASYFIKACJE.keys():
        os.makedirs(os.path.join(LOG_FOLDER, folder), exist_ok=True)

def uruchom():
    print("🔧 Funkcja uruchom() została wywołana")
    if not os.path.exists(PROJEKT_FOLDER):
        print(f"❌ Folder projektu nie istnieje: {PROJEKT_FOLDER}")
        return
    utworz_foldery_klasyfikacji()
    dodaj_logowanie(PROJEKT_FOLDER, dry_run=DRY_RUN)
    generuj_raport_csv()

    for kategoria, lista in KLASYFIKACJE.items():
        if lista:
            print(f"\n📁 {kategoria.upper()} ({len(lista)} plików):")
            for file, path, opis in lista:
                print(f" - {file} | {opis}")

    zapisz_cache()
    print(f"✅ Raport wygenerowany: {RAPORT_CSV}")

if __name__ == "__main__":
    uruchom()

if all(len(lista) == 0 for lista in KLASYFIKACJE.values()):
    print("⚠️ Skrypt zakończył się bez działania — brak plików do analizy")

