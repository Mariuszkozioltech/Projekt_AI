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

import json
import os

input_path = "C:\\Projekt_AI\\PROJEKT\\strategia_inwestycyjna\\Dane\\ibkr_clean.json"
output_path = "C:\\Projekt_AI\\PROJEKT\\praca\\raporty\\ibkr_report.json"

with open(input_path, "r") as f:
    data = json.load(f)

report = []
for row in data:
    try:
        buy_price = float(row.get("BuyPrice", 0))
        sell_price = float(row.get("SellPrice", 0))
        quantity = int(row.get("Quantity", 0))
        profit = (sell_price - buy_price) * quantity
        score = "✅" if profit > 0 else "⚠️"
        report.append({
            "Symbol": row.get("Symbol", "N/A"),
            "Buy": buy_price,
            "Sell": sell_price,
            "Qty": quantity,
            "Profit": round(profit, 2),
            "Score": score
        })
    except Exception as e:
        print(f"Błąd w wierszu: {row} → {e}")

with open(output_path, "w") as f:
    json.dump(report, f, indent=2)

print(f"Zapisano raport do: {output_path}")
