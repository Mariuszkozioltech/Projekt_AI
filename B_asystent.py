import logging

logging.basicConfig(
    filename="C:\\Projekt_AI\\logs\\app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Skrypt uruchomiony")

import os
import re
import time
import json
import shutil
import threading
import yaml
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

    arch_name = f"{os.path.splitext(os.path.basename(aktualny_plik_rozmowy))[0]}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
    shutil.copy(aktualny_plik_rozmowy, os.path.join(ARCHIWUM_DIR, arch_name))
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
        try:
            time.sleep(INTERVAL)
            ts = teraz_str()
            zapisz_notatke("🕒 Automatyczny zapis (heartbeat).", pokaz_komunikaty=False)
            zapisz_rozmowe(uzytkownik="(autozapis)")
            print(f"[{ts}] ⏱ Autozapis wykonany.")
        except Exception as e:
            print(f"⚠️ Błąd autozapisu: {e}")

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

# ---------- Etapy projektu ----------
ETAPY_PATH = "C:/Projekt_AI/etapy.yaml"
LOG_ETAPY = "C:/Projekt_AI/logs/etapy.log"

def wczytaj_etapy():
    try:
        with open(ETAPY_PATH, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"⚠️ Błąd wczytywania etapów: {e}")
        return []

def zapisz_log_etapow(wiadomosc):
    os.makedirs(os.path.dirname(LOG_ETAPY), exist_ok=True)
    with open(LOG_ETAPY, "a", encoding="utf-8") as f:
        f.write(f"[{teraz_str()}] {wiadomosc}\n")

def sprawdz_etapy():
    etapy = wczytaj_etapy()
    if not etapy:
        print(⚠️ Brak etapów do analizy.")
        return

    print("📋 Status etapów:")
    for etap in etapy:
        status = etap.get("status", "brak")
        nazwa = etap.get("nazwa", "Nieznany etap")
        if status == "todo":
            print(f"🔧 Do zrobienia: {nazwa}")
        elif status == "in_progress":
            print(f"🔄 W trakcie: {nazwa}")
        elif status == "done":
            print(f"✅ Ukończono: {nazwa}")
        else:
            print(f"❓ Nieznany status: {nazwa}")
        zapisz_log_etapow(f"{etap.get('id', 'brak')} – {status} – {nazwa}")

def sugeruj_kolejny_krok(etapy):
    priorytety = {"wysoki": 3, "sredni": 2, "niski": 1}
    kandydaci = []

    for etap in etapy:
        status = etap.get("status", "brak")
        if status != "todo":
            continue
        priorytet = etap.get("priorytet", "sredni")
        waga = priorytety.get(priorytet, 2)
        kandydaci.append((waga, etap))

    if not kandydaci:
        print("✅ Wszystkie etapy wykonane lub w trakcie.")
        return

    kandydaci.sort(reverse=True)
    najlepszy = kandydaci[0][1]
    print(f"\n💡 Sugerowany kolejny krok: {najlepszy['nazwa']}")
    print(f"📌 Status: {najlepszy['status']} | Priorytet: {najlepszy.get('priorytet', 'sredni')}")
    print(f"📝 Opis: {najlepszy.get('opis', 'Brak opisu')}")
    zapisz_log_etapow(f"Sugestia: {najlepszy['id']} – {najlepszy['nazwa']}")

def uruchom_asystenta():
    etapy = wczytaj_etapy()
    if not etapy:
        print("⚠️ Nie udało się wczytać etapów.")
        return
    sprawdz_etapy()
    sugeruj_kolejny_krok(etapy)

# ---------- Start programu ----------
if __name__ == "__main__":
    uruchom_asystenta()
