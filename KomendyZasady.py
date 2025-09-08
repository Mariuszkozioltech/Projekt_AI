import logging

logging.basicConfig(
    filename="C:\\Projekt_AI\\logs\\app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Skrypt uruchomiony")

import re
import requests
from datetime import datetime

# === Funkcja: zapis do pliku .md ===
def zapisz_zasade_do_md(sciezka_pliku, tresc_zasady):
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            linie = f.readlines()
    except FileNotFoundError:
        linie = ["# 🧠 Rozmowa z dnia {}\n\n".format(datetime.now().strftime("%Y-%m-%d")),
                 "## 🔄 Tryb: Notatki i Zasady\n\n"]

    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    zasada_linia = f"- {tresc_zasady} {timestamp}\n"

    indeks = None
    for i, linia in enumerate(linie):
        if linia.strip() == "### 📜 Zasady":
            indeks = i
            break

    if indeks is not None:
        for j in range(indeks + 1, len(linie)):
            if linie[j].startswith("### "):
                linie.insert(j, zasada_li nie nia)
                break
        else:
            linie.append(zasada_linia)
    else:
        linie.append("### 📜 Zasady\n")
        linie.append(zasada_linia)

    with open(sciezka_pliku, "w", encoding="utf-8") as f:
        f.writelines(linie)

    print("✅ Zasada zapisana do pliku:", tresc_zasady)

# === Funkcja: wysyłanie komendy do backendu ===
def wyslij_komende(typ, tresc):
    url = "http://127.0.0.1:8000/komenda"
    payload = {
        "typ": typ,
        "tresc": tresc
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("✅ Komenda wysłana:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ Błąd przy wysyłaniu komendy:", e)

# === Funkcja: rozpoznawanie komendy z tekstu ===
def rozpoznaj_i_zapisz(wpis, sciezka_md):
    wzorzec = re.compile(r'^(?:ZAPISZ_ZASADA|zapisz\s+ta?\s+zasade|zapisz\s+zasade|zasada)\s*:?\s*(.*)$', re.IGNORECASE)
    dopasowanie = wzorzec.match(wpis.strip())
    if dopasowanie:
        tresc = dopasowanie.group(1).strip()
        if tresc:
            zapisz_zasade_do_md(sciezka_md, tresc)
            wyslij_komende("zasada", tresc)
        else:
            print("⚠️ Brak treści zasady.")
    else:
        print("⛔ Nie rozpoznano komendy.")

# === Test ===
plik_md = "C:/Projekt_AI/Rozmowy/2025-08-22_23-21-14_chat.md"
rozpoznaj_i_zapisz("ZAPISZ_ZASADA: Hasła zmieniamy co 90 dni", plik_md)

