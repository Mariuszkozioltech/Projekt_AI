import logging

logging.basicConfig(
    filename="C:\\Projekt_AI\\logs\\app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Skrypt uruchomiony")

from datetime import datetime

def zapisz_zasade_do_md(sciezka_pliku, tresc_zasady):
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            linie = f.readlines()
    except FileNotFoundError:
        linie = ["# 🧠 Rozmowa z dnia {}\n\n".format(datetime.now().strftime("%Y-%m-%d")),
                 "## 🔄 Tryb: Notatki i Zasady\n\n"]

    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    zasada_linia = f"- {tresc_zasady} {timestamp}\n"

    # Szukamy sekcji 📜 Zasady
    indeks = None
    for i, linia in enumerate(linie):
        if linia.strip() == "### 📜 Zasady":
            indeks = i
            break

    if indeks is not None:
        for j in range(indeks + 1, len(linie)):
            if linie[j].startswith("### "):
                linie.insert(j, zasada_linia)
                break
        else:
            linie.append(zasada_linia)
    else:
        linie.append("### 📜 Zasady\n")
        linie.append(zasada_linia)

    with open(sciezka_pliku, "w", encoding="utf-8") as f:
        f.writelines(linie)

    print("✅ Zasada zapisana do pliku:", tresc_zasady)

# Wywołanie funkcji:
plik_md = "C:/Projekt_AI/Rozmowy/2025-08-22_23-21-14_chat.md"
zapisz_zasade_do_md(plik_md, "jestem w biorze to pracuje")
