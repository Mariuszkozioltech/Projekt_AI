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
import csv
import shutil
from datetime import datetime
import pandas as pd

# Ścieżki projektu
PROJECT_BASE = r"C:\Projekt_AI\PROJEKT\strategia_inwestycyjna"
DANE_BASE = os.path.join(PROJECT_BASE, "Dane")
ARCHIWUM_BASE = os.path.join(PROJECT_BASE, "Dokument IBKR archiwum")

# Mapowanie nazw sekcji -> "skrót" do nazw plików
SECTION_ALIASES = {
    "Trades": "trades",
    "Mark-to-Market Performance Summary": "m2m",
    "Dividends": "dividends",
    "Withholding Tax": "withholding_tax",
    "Interest": "interest",
    "Fees": "fees",
    "Change in Dividend Accruals": "dividend_accruals",
    "Borrow Fee Details": "borrow_fees",
    "Stock Yield Enhancement Program Securities Lent": "syep_lent",
    "Stock Yield Enhancement Program Securities Lent Activity": "syep_lent_activity",
    "Deposits & Withdrawals": "deposits_withdrawals",
    "Realized & Unrealized Performance Summary": "realized_unrealized",
}

# Heurystyki nazw kolumn z datą
DATE_COLUMN_CANDIDATES = [
    "Date", "Settle Date", "Value Date", "Trade Date", "Date/Time", "Date Time", "Time"
]

# Heurystyki nazw kolumn z tickerem
TICKER_COLUMN_CANDIDATES = ["Symbol", "Underlying", "Asset", "Ticker"]


def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def _safe_filename(name: str) -> str:
    return "".join(c for c in name if c.isalnum() or c in ("-", "_", ".")).strip()


def _detect_date_column(columns):
    low = [c.lower() for c in columns]
    for cand in DATE_COLUMN_CANDIDATES:
        if cand.lower() in low:
            return columns[low.index(cand.lower())]
    # fallback: brak kolumny daty
    return None


def _detect_ticker_column(columns):
    low = [c.lower() for c in columns]
    for cand in TICKER_COLUMN_CANDIDATES:
        if cand.lower() in low:
            return columns[low.index(cand.lower())]
    return None


def _parse_dates(df: pd.DataFrame, date_col) -> pd.DataFrame:
    # jeśli brak kolumny lub nazwa nie jest stringiem → nic nie rób
    if not date_col or not isinstance(date_col, str) or date_col not in df.columns:
        return df

    col = df[date_col]

    # upewnij się, że mamy Series tekstowy
    if not pd.api.types.is_string_dtype(col):
        col = col.astype(str)

    # usuń przecinki i spacje
    col = col.str.replace(",", "", regex=False).str.strip()

    # konwersja na datetime
    df[date_col] = pd.to_datetime(col, errors="coerce")
    return df


def _save_all_and_by_year(df: pd.DataFrame, base_folder: str, alias: str):
    # zapis "all"
    _ensure_dir(base_folder)
    all_path = os.path.join(base_folder, f"{alias}_all.csv")
    df.to_csv(all_path, index=False, encoding="utf-8-sig")

    # podział na lata (jeśli jest kolumna daty)
    date_col = _detect_date_column(df.columns)
    if date_col:
        df = _parse_dates(df, date_col)
        if date_col in df.columns:
            df["Year"] = df[date_col].dt.year
            for year, grp in df.groupby("Year", dropna=True):
                if pd.isna(year):
                    continue
                year_folder = os.path.join(base_folder, str(int(year)))
                _ensure_dir(year_folder)
                year_path = os.path.join(year_folder, f"{alias}_{int(year)}.csv")
                grp.drop(columns=["Year"]).to_csv(year_path, index=False, encoding="utf-8-sig")


def _save_by_ticker_and_year(df: pd.DataFrame, base_folder: str, alias: str):
    ticker_col = _detect_ticker_column(df.columns)
    if not ticker_col:
        return
    date_col = _detect_date_column(df.columns)
    if date_col:
        df = _parse_dates(df, date_col)

    if date_col in df.columns:
        df["Year"] = df[date_col].dt.year
        groups = df.groupby([ticker_col, "Year"], dropna=True)
        for (ticker, year), grp in groups:
            if not isinstance(ticker, str):
                ticker = str(ticker)
            if pd.isna(year):
                continue
            year_folder = os.path.join(base_folder, str(int(year)))
            _ensure_dir(year_folder)
            fname = f"{_safe_filename(ticker)}_{alias}_{int(year)}.csv"
            grp.drop(columns=["Year"]).to_csv(os.path.join(year_folder, fname), index=False, encoding="utf-8-sig")
    else:
        # bez daty: zapis tylko per ticker
        for ticker, grp in df.groupby(ticker_col, dropna=True):
            if not isinstance(ticker, str):
                ticker = str(ticker)
            fname = f"{_safe_filename(ticker)}_{alias}.csv"
            grp.to_csv(os.path.join(base_folder, fname), index=False, encoding="utf-8-sig")


def parse_ibkr_csv(file_path: str):
    # profil bierzemy z nazwy folderu nadrzędnego w RAW:
    # ...\raw

    profile = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
    if not profile:
        profile = "ibkr"

    dane_folder = os.path.join(DANE_BASE, profile)
    archiwum_folder = os.path.join(ARCHIWUM_BASE, profile)
    _ensure_dir(dane_folder)
    _ensure_dir(archiwum_folder)

    # Kontenery na nagłówki i wiersze
    headers = {}
    rows = {section: [] for section in SECTION_ALIASES.keys()}

    # Czytaj bezpiecznie z csv.reader (obsługa cytowań, przecinków w polach)
    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 2:
                continue
            section = row[0].strip()
            kind = row[1].strip()

            if section not in SECTION_ALIASES:
                continue

            if kind == "Header":
                headers[section] = row[2:]
            elif kind == "Data":
                if section in headers:
                    rows[section].append(row[2:])

    # Zapis sekcji
    for section, alias in SECTION_ALIASES.items():
        if rows.get(section) and headers.get(section):
            df = pd.DataFrame(rows[section], columns=headers[section])
            df = df.loc[:, ~(df.isna() | (df.astype(str).str.strip() == "")).all(axis=0)]
            section_folder = os.path.join(dane_folder, alias)
            _save_all_and_by_year(df, section_folder, alias)
            if section in ("Trades", "Mark-to-Market Performance Summary"):
                _save_by_ticker_and_year(df, section_folder, alias)

    # Archiwizacja oryginału z datownikiem
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = os.path.splitext(os.path.basename(file_path))[0]
    archived_name = f"{base}_{ts}.csv"
    shutil.copy2(file_path, os.path.join(archiwum_folder, archived_name))
    print(f"📦 Skopiowano do archiwum: {os.path.join(archiwum_folder, archived_name)}")