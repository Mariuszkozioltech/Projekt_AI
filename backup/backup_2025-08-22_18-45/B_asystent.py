import os
import re
import time
import json
import shutil
import threading
from datetime import datetime

# ---------- Konfiguracja ----------
CONFIG_PATH = "C:/Projekt_AI/config.json"

# Wczytaj konfigurację z bezpiecznymi domyślnymi wartościami
def load_config():
    defaults = {
        "interwal_zapisu_minuty": 10,
        "sciezka_notatek": "C:/Projekt_AI/Notatki",
        "sciezka_zasad": "C:/Projekt_AI/Zasady/ustalenia.md",
        "sciezka_archiwum": "C:/Projekt_AI/Archiwum"
    }
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            for k, v in defaults.items():
                if k not in data:
                    data[k] = v
            return data
    except Exception:
        return defaults

config = load_config()
INTERVAL = max(1, int(config.get("interwal_zapisu_minuty", 10))) * 60
NOTATKI_DIR = config["sciezka_notatek"]
ZASADY_FILE = config["sciezka_zasad"]
ARCHIWUM_DIR = config["sciezka_archiwum"]

# Upewnij się, że katalogi istnieją
os.makedirs(NOTATKI_DIR, exist_ok=True)
os.makedirs(os.path.dirname(ZASADY_FILE), exist_ok=True)
os.makedirs(ARCHIWUM_DIR, exist_ok=True)

# ---------- Pomocnicze ----------
def teraz_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def dzien_plik():
    return os.path.join(NOTATKI_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.md")

def kopiuj_do_archiwum(silent=False):
    src = dzien_plik()
    if os.path.exists(src):
        dst = os.path.join(ARCHIWUM_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_kopiuj.md")
        shutil.copy(src, dst)
        if not silent:
            print("📁 Kopia notatki zapisana w Archiwum.")

# ---------- Zapisy ----------
def zapisz_zasade(tresc, pokaz_komunikaty=True):
    with open(ZASADY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[DATA: {teraz_str()}]\n")
        f.write(f"ZASADA: {tresc}\nPOWÓD:\nPRZYKŁAD:\n")
    if pokaz_komunikaty:
        print("✅ Zasada zapisana.")
    kopiuj_do_archiwum(silent=not pokaz_komunikaty)
    if pokaz_komunikaty:
        print("📁 Kopia notatki zapisana w Archiwum.")

def zapisz_notatke(tresc, pokaz_komunikaty=True):
    plik = dzien_plik()
    with open(plik, "a", encoding="utf-8") as f:
        f.write(f"\n[{teraz_str()}]\n{tresc}\n")
    if pokaz_komunikaty:
        print("💾 Notatka zapisana.")
    kopiuj_do_archiwum(silent=not pokaz_komunikaty)
    if pokaz_komunikaty:
        print("📁 Kopia notatki zapisana w Archiwum.")

# ---------- Autozapis w tle ----------
def autozapis_loop():
    while True:
        time.sleep(INTERVAL)
        ts = teraz_str()
        zapisz_notatke("🕒 Automatyczny zapis (heartbeat).", pokaz_komunikaty=False)
        print(f"[{ts}] ⏱ Autozapis wykonany.")

# ---------- Parsowanie komend ----------
# Akceptuj:
# - "ZAPISZ_ZASADA: treść" lub "ZAPISZ_ZASADA treść"
# - "zapisz zasade: treść" lub "zapisz zasade treść"
# - "zapisz ta zasade: treść" lub "zapisz ta zasade treść"
# - "zasada: treść" lub "zasada treść"
RE_ZASADA = re.compile(
    r'^(?:ZAPISZ_ZASADA|zapisz\s+ta?\s+zasade|zasada)\s*:?\s*(.*)$',
    re.IGNORECASE
)

def probuj_zapisac_zasade(wpis):
    m = RE_ZASADA.match(wpis.strip())
    if not m:
        return False
    tresc = m.group(1).strip()
    if not tresc:
        print("⚠️ Podaj treść zasady po komendzie, np.: zapisz zasade: Hasła zmieniamy co 90 dni.")
        return True
    zapisz_zasade(tresc, pokaz_komunikaty=True)
    return True

# ---------- Tryb interaktywny ----------
def tryb_ciagly():
    print("🔄 Tryb notatek i zasad uruchomiony.")
    print("• Wpisuj notatki (zostaną zapisane).")
    print("• Komendy zasad: 'zapisz zasade ...' / 'zapisz ta zasade ...' / 'ZAPISZ_ZASADA: ...'")
    print("• Wpisz 0 aby zakończyć.\n")

    # Start autozapisu w tle
    threading.Thread(target=autozapis_loop, daemon=True).start()

    while True:
        try:
            wpis = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Zakończono tryb notatek.")
            break

        if wpis == "0":
            print("👋 Zakończono tryb notatek.")
            break

        # Zasada?
        if probuj_zapisac_zasade(wpis):
            continue  # <-- to zatrzymuje zapis do notatek

        # Zwykła notatka (wraz z prefiksem U: dla czytelności źródła)
        if wpis:
            zapisz_notatke(f"U: {wpis}", pokaz_komunikaty=True)
        else:
            # Pusta linia = szybki ręczny 'heartbeat'
            zapisz_notatke("🕒 Ręczny zapis (pusta linia).", pokaz_komunikaty=False)

if __name__ == "__main__":
    tryb_ciagly()
