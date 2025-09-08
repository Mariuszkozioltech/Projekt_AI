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
import pandas as pd

def get_latest_csv(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
    return os.path.join(folder, files[0]) if files else None

def clean_data(filepath, columns):
    df = pd.read_csv(filepath, on_bad_lines='skip')
    return df[[col for col in columns if col in df.columns]]

def save_to_json(df, target_path):
    # Tworzy folder docelowy, jeśli nie istnieje
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    df.to_json(target_path, orient='records')

# Główna logika
source = r'C:\Users\mariu\data\raw'
target = r'C:\Projekt_AI\PROJEKT\strategia_inwestycyjna\Dane\ibkr_clean.json'
expected_cols = ['Date', 'Symbol', 'Action', 'Price', 'Quantity', 'Amount']

latest = get_latest_csv(source)
if latest:
    print(f'Przetwarzam: {latest}')
    df_clean = clean_data(latest, expected_cols)
    save_to_json(df_clean, target)
    print(f'Zapisano do: {target}')
else:
    print('Brak plików CSV.')
