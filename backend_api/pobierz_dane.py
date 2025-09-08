import os
import re
import csv
import logging

# === Konfiguracja logowania ===
log_folder = r"C:\Projekt_AI\logs"
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_folder, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info(f"Uruchomiono: {os.path.basename(__file__)}")

# === Ścieżki projektu ===
FOLDER_WEJSCIOWY = r"C:\Projekt_AI\PROJEKT\strategia_inwestycyjna\Dokument IBKR archiwum\ibkr"
FOLDER_DOCELOWY = r"C:\Projekt_AI\PROJEKT\strategia_inwestycyjna\Dane"

# === Pomocnicze ===
NAZWA_WZORZEC = re.compile(r"^(?P<rok>\d{4})_(?P<imie>[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ0-9\-]+)\.csv$")

def bezpieczna_nazwa(nazwa: str) -> str:
    return re.sub(r'[^\w\-]', '_', nazwa)

def zapisz_wiersz(folder_roku_imie: str, ticker: str, typ: str, data: str, szczegoly: str) -> None:
    ticker_norm = (ticker or "brak").strip().lower()
    typ_norm = (typ or "nieznany").strip().lower()
    nazwa_pliku = f"{bezpieczna_nazwa(ticker_norm)}_{bezpieczna_nazwa(typ_norm)}.csv"
    sciezka = os.path.join(folder_roku_imie, nazwa_pliku)

    try:
        os.makedirs(folder_roku_imie, exist_ok=True)
        plik_istnieje = os.path.isfile(sciezka)

        with open(sciezka, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not plik_istnieje:
                writer.writerow(["data", "ticker", "typ", "szczegoly"])
            writer.writerow([data, ticker_norm.upper(), typ_norm, szczegoly])

        logging.info(f"[{folder_roku_imie}] Zapisano: {sciezka} | {data} | {ticker_norm.upper()} | {typ_norm}")
        print(f"✅ Zapisano do: {sciezka}")

    except Exception as e:
        logging.error(f"Błąd zapisu do pliku {sciezka}: {e}")
        print(f"❌ Błąd zapisu do: {sciezka} → {e}")

def wykryj_delimiter(sciezka: str) -> str:
    with open(sciezka, "r", encoding="utf-8", newline="") as f:
        sample = f.read(2048)
    if sample.count(";") > sample.count(","):
        return ";"
    return ","

def czytaj_wiersze(sciezka: str):
    delimiter = wykryj_delimiter(sciezka)
    with open(sciezka, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        reader.fieldnames = [h.lower() for h in reader.fieldnames] if reader.fieldnames else []
        for row in reader:
            yield {k.lower(): (v or "").strip() for k, v in row.items()}

def przetworz_plik(sciezka_pliku: str, nazwa_pliku: str) -> None:
    logging.info(f"--- Rozpoczynam przetwarzanie pliku: {nazwa_pliku} ---")

    dop = NAZWA_WZORZEC.match(nazwa_pliku)
    if not dop:
        logging.warning(f"Pominięto plik o niepasującej nazwie: {nazwa_pliku}")
        return

    imie = dop.group("imie").lower()
    licznik = 0
    puste_wiersze = 0

    for row in czytaj_wiersze(sciezka_pliku):
        data = row.get("data", "") or row.get("date", "") or row.get("czas", "") or row.get("time", "")
        rok_z_daty = data[:4] if len(data) >= 4 and data[:4].isdigit() else "brak"
        folder_roku_imie = os.path.join(FOLDER_DOCELOWY, f"{rok_z_daty}_{imie}")

        try:
            os.makedirs(folder_roku_imie, exist_ok=True)
        except Exception as e:
            logging.error(f"Nie można utworzyć folderu {folder_roku_imie}: {e}")
            continue

        ticker = row.get("ticker", "") or row.get("symbol", "") or row.get("instrument", "") or "brak"
        typ = row.get("typ", "")
        szczegoly = row.get("szczegoly", "")

        if not typ:
            if "dividend" in row or "dywidenda" in row:
                typ = "dywidenda"
            elif "call" in (row.get("opcja", "") + row.get("typ_opcji", "")).lower():
                typ = "call"
            elif "put" in (row.get("opcja", "") + row.get("typ_opcji", "")).lower():
                typ = "put"
            elif {"open", "close", "volume"}.issubset(set(row.keys())):
                typ = "akcje"
            elif "koszt" in (row.get("kategoria", "") + row.get("typ_operacji", "")).lower():
                typ = "koszt"
            else:
                typ = "nieznany"

        if not szczegoly:
            kandydaci = ["open", "close", "volume", "strike", "expiry", "dividend", "kwota", "opis", "kategoria"]
            pary = [f"{k}={row[k]}" for k in kandydaci if k in row and row[k]]
            szczegoly = "; ".join(pary) if pary else ""

        if not ticker and not typ and not data and not szczegoly:
            puste_wiersze += 1
            logging.warning(f"Pominięto pusty wiersz w pliku {nazwa_pliku}")
            continue

        zapisz_wiersz(folder_roku_imie, ticker, typ, data, szczegoly)
        licznik += 1

    logging.info(f"Przetworzono plik: {nazwa_pliku} | wpisów: {licznik} | pustych: {puste_wiersze}")
    print(f"✅ Przetworzono: {nazwa_pliku} → {folder_roku_imie} | wpisów: {licznik}")
    logging.info(f"--- Zakończono przetwarzanie pliku: {nazwa_pliku} ---")

def main():
    if not os.path.isdir(FOLDER_WEJSCIOWY):
        print(f"❌ Brak folderu wejściowego: {FOLDER_WEJSCIOWY}")
        logging.error(f"Brak folderu wejściowego: {FOLDER_WEJSCIOWY}")
        return

    os.makedirs(FOLDER_DOCELOWY, exist_ok=True)

    pliki = [n for n in os.listdir(FOLDER_WEJSCIOWY) if n.lower().endswith(".csv")]
    if not pliki:
        print("⚠️ Brak plików CSV do przetworzenia.")
        logging.warning("Brak plików CSV do przetworzenia.")
        return

    for nazwa_pliku in sorted(pliki):
        sciezka_pliku = os.path.join(FOLDER_WEJSCIOWY, nazwa_pliku)
        try:
            przetworz_plik(sciezka_pliku, nazwa_pliku)
        except Exception as e:
            logging.exception(f"Błąd podczas przetwarzania {nazwa_pliku}: {e}")
            print(f"❌ Błąd w pliku {nazwa_pliku}: {e}")

if __name__ == "__main__":
    main()
