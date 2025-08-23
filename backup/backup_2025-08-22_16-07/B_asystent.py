import time
import json
import os
from datetime import datetime
import shutil

# Wczytaj konfigurację
with open("C:/Projekt_AI/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

INTERVAL = config["interwal_zapisu_minuty"] * 60
NOTATKI_DIR = config["sciezka_notatek"]
ZASADY_FILE = config["sciezka_zasad"]
ARCHIWUM_DIR = config["sciezka_archiwum"]

def zapisz_zasade(tresc):
    with open(ZASADY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[DATA: {datetime.now().strftime('%Y-%m-%d %H:%M')}]\n")
        f.write(f"ZASADA: {tresc}\nPOWÓD:\nPRZYKŁAD:\n")
    print("✅ Zasada zapisana.")

def zapisz_notatke(tresc):
    filename = os.path.join(NOTATKI_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.md")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now().strftime('%H:%M')}]\n{tresc}\n")
    print("💾 Notatka zapisana.")

def kopiuj_do_archiwum():
    src = os.path.join(NOTATKI_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.md")
    dst = os.path.join(ARCHIWUM_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M')}_kopiuj.md")
    if os.path.exists(src):
        shutil.copy(src, dst)
        print("📁 Kopia notatki zapisana w Archiwum.")

def tryb_ciagly():
    print("🔄 Tryb notatek uruchomiony. Co 10 minut zapisuję wpis.")
    while True:
        print("\nWpisz wiadomość lub 'ZAPISZ_ZASADA: ...'")
        wpis = input("> ").strip()
        if wpis.startswith("ZAPISZ_ZASADA:"):
            zasada = wpis.replace("ZAPISZ_ZASADA:", "").strip()
            zapisz_zasade(zasada)
        elif wpis:
            zapisz_notatke(f"U: {wpis}")
        else:
            zapisz_notatke("🕒 Automatyczny zapis bez wpisu.")
        kopiuj_do_archiwum()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    tryb_ciagly()
