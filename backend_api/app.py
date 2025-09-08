import logging
import os
from flask import Flask, request, jsonify
import yaml

log_folder = "C:\\Projekt_AI\\logs"
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_folder, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info(f"Uruchomiono: {os.path.basename(__file__)}")

app = Flask(__name__)
ETAPY_PATH = "C:/Projekt_AI/etapy.yaml"


@app.route("/etapy", methods=["GET"])
def pobierz_etapy():
    try:
        with open(ETAPY_PATH, "r", encoding="utf-8") as f:
            etapy = yaml.safe_load(f) or []
    except FileNotFoundError:
        return jsonify({"status": "błąd", "info": "Plik etapów nie istnieje"})
    except yaml.YAMLError as e:
        return jsonify({"status": "błąd", "info": f"Błąd YAML: {str(e)}"})

    if not isinstance(etapy, list):
        return jsonify({"status": "błąd", "info": "Niepoprawna struktura danych"})

    return jsonify(etapy)


@app.route("/update-status", methods=["POST"])
def update_status():
    data = request.json
    etap_id = data.get("id")
    nowy_status = data.get("status")

    if not etap_id or nowy_status is None:
        return jsonify({"status": "błąd", "info": "Brak ID lub statusu"})

    try:
        with open(ETAPY_PATH, "r", encoding="utf-8") as f:
            etapy = yaml.safe_load(f) or []
    except FileNotFoundError:
        return jsonify({"status": "błąd", "info": "Plik etapów nie istnieje"})
    except yaml.YAMLError as e:
        return jsonify({"status": "błąd", "info": f"Błąd YAML: {str(e)}"})

    znaleziono = False
    for etap in etapy:
        if etap["id"] == etap_id:
            etap["status"] = nowy_status
            znaleziono = True
            break

    if not znaleziono:
        return jsonify({"status": "błąd", "info": "Nie znaleziono etapu"})

    with open(ETAPY_PATH, "w", encoding="utf-8") as f:
        yaml.dump(etapy, f, allow_unicode=True)

    logging.info(f"Zmieniono status etapu {etap_id} na {nowy_status}")
    return jsonify({"status": "ok", "id": etap_id, "nowy_status": nowy_status})


@app.route("/update-priorytet", methods=["POST"])
def update_priorytet():
    data = request.json
    etap_id = data.get("id")
    nowy_priorytet = data.get("priorytet")

    if not etap_id or nowy_priorytet is None:
        return jsonify({"status": "błąd", "info": "Brak ID lub priorytetu"})

    try:
        with open(ETAPY_PATH, "r", encoding="utf-8") as f:
            etapy = yaml.safe_load(f) or []
    except FileNotFoundError:
        return jsonify({"status": "błąd", "info": "Plik etapów nie istnieje"})
    except yaml.YAMLError as e:
        return jsonify({"status": "błąd", "info": f"Błąd YAML: {str(e)}"})

    znaleziono = False
    for etap in etapy:
        if etap["id"] == etap_id:
            etap["priorytet"] = nowy_priorytet
            znaleziono = True
            break

    if not znaleziono:
        return jsonify({"status": "błąd", "info": "Nie znaleziono etapu"})

    with open(ETAPY_PATH, "w", encoding="utf-8") as f:
        yaml.dump(etapy, f, allow_unicode=True)

    logging.info(f"Zmieniono priorytet etapu {etap_id} na {nowy_priorytet}")
    return jsonify({"status": "ok", "id": etap_id, "priorytet": nowy_priorytet})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
