import os
import logging

# === Konfiguracja logowania ===
log_folder = "C:\\Projekt_AI\\logs"
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_folder, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

NAZWA_SKRYPTU = os.path.basename(__file__)
logging.info(f"Uruchomiono: {NAZWA_SKRYPTU}")

# === Sprawdzenie panelu WWW ===
def sprawdz_panel_www():
    print("\n🔍 Sprawdzanie panelu WWW (etap 2B):")
    folder = "C:\\Projekt_AI\\frontend"
    plik = os.path.join(folder, "frontend_api.py")
    log_path = os.path.join(log_folder, "panel_errors.log")

    print("📁 Szukam pliku:", os.path.abspath(plik))

    if os.path.exists(plik):
        print("✅ Plik istnieje.")
        logging.info("Plik frontend_api.py znaleziony.")
    else:
        print("❌ Plik nie istnieje.")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write("Brak pliku frontend_api.py\n")
        logging.warning("Brak pliku frontend_api.py")

# === Uruchomienie jako skrypt ===
if __name__ == "__main__":
    sprawdz_panel_www()
