import os
import re
import time
import json
import shutil
import threading
from datetime import datetime, timedelta

# ---------- Konfiguracja ----------
CONFIG_PATH = "C:/Projekt_AI/config.json"

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

os.makedirs(NOTATKI_DIR, exist_ok=True)
os.makedirs(os.path.dirname(ZASADY_FILE), exist_ok=True)
os.makedirs(ARCHIWUM_DIR, exist_ok=True)

def teraz_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ---------- Rozmowy ----------
ROZMOWY_DIR = "C:/Projekt_AI/Rozmowy"
os.makedirs(ROZMOWY_DIR, exist_ok=True)

PRZERWA_NA_NOWA_ROZMOWE = timedelta(hours=2)
aktualny_plik_rozmowy = None
ostatni_wpis_czas = None

def nowy_plik_rozmowy():
    global aktualny_plik_rozmowy
    aktualny_plik_rozmowy = os.path.join(
        ROZMOWY_DIR,
        f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_chat.md"
    )
    with open(aktualny_plik_rozmowy, "w", encoding="utf-8") as f:
        f.write(f"# Rozmowa rozpoczęta: {teraz_str()}\n")
    print(f"🆕 Utworzono nowy plik rozmowy: {aktualny_plik_rozmowy}")

def zapisz_rozmowe(uzytkownik=None, ai=None):
    global ostatni_wpis_czas
    teraz = datetime.now()
    if (ostatni_wpis_czas is None) or (teraz - ostatni_wpis_czas > PRZERWA_NA_NOWA_ROZMOWE):
        nowy_plik_rozmowy()

    with open(aktualny_plik_rozmowy, "a", encoding="utf-8") as f:
        if uzytkownik is not None:
            f.write(f"[{teraz_str()}] U: {uzytkownik}\n")
        if ai is not None:
            f.write(f"[{teraz_str()}] AI: {ai}\n")

    # Unikalna kopia pliku rozmowy w archiwum
    arch_name = f"{os.path.splitext(os.path.basename(aktualny_plik_rozmowy))[0]}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
    shutil.copy(
        aktualny_plik_rozmowy,
        os.path.join(ARCHIWUM_DIR, arch_name)
    )

    ostatni_wpis_czas = teraz

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

def zapisz_notatke(tresc, pokaz_komunikaty=True):
    plik = dzien_plik()
    with open(plik, "a", encoding="utf-8") as f:
        f.write(f"\n[{teraz_str()}]\n{tresc}\n")
    if pokaz_komunikaty:
        print("💾 Notatka zapisana.")
    kopiuj_do_archiwum(silent=not pokaz_komunikaty)

# ---------- Autozapis ----------
def autozapis_loop():
    while True:
        time.sleep(INTERVAL)
        ts = teraz_str()
        zapisz_notatke("🕒 Automatyczny zapis (heartbeat).", pokaz_komunikaty=False)
        zapisz_rozmowe(uzytkownik="(autozapis)")
        print(f"[{ts}] ⏱ Autozapis wykonany.")

# ---------- Parsowanie komend ----------
RE_ZASADA = re.compile(
    r'^(?:ZAPISZ_ZASADA|zapisz\s+ta?\s+zasade|zapisz\s+zasade|zasada)\s*:?\s*(.*)$',
    re.IGNORECASE
)

def probuj_zapisac_zasade(wpis):
    m = RE_ZASADA.match(wpis.strip())
    if not m:
        return False, None
    tresc = m.group(1).strip()
    if not tresc:
        print("⚠️ Podaj treść zasady po komendzie, np.: zapisz zasade: Hasła zmieniamy co 90 dni.")
        return True, None
    zapisz_zasade(tresc, pokaz_komunikaty=True)
    return True, tresc

# ---------- Tryb interaktywny ----------
def tryb_ciagly():
    print("🔄 Tryb notatek i zasad uruchomiony.")
    print("• Wpisuj notatki (zostaną zapisane).")
    print("• Komendy zasad: 'zapisz zasade ...' / 'zapisz ta zasade ...' / 'ZAPISZ_ZASADA: ...'")
    print("• Wpisz 0 aby zakończyć.\n")

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

        czy_zasada, tresc_zasady = probuj_zapisac_zasade(wpis)
        if czy_zasada:
            zapisz_rozmowe(uzytkownik=(tresc_zasady or wpis))
            continue

        if wpis:
            zapisz_notatke(f"U: {wpis}", pokaz_komunikaty=True)
            zapisz_rozmowe(uzytkownik=wpis)
        else:
            zapisz_notatke("🕒 Ręczny zapis (pusta linia).", pokaz_komunikaty=False)
            zapisz_rozmowe(uzytkownik="(pusta linia)")

if __name__ == "__main__":
    tryb_ciagly()
