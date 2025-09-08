import logging
import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

log_folder = "C:\\Projekt_AI\\logs"
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_folder, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info(f"Uruchomiono: {os.path.basename(__file__)}")

app = FastAPI()

# === Model danych dla komendy ===
class Komenda(BaseModel):
    typ: str
    tresc: str

# === Lista do przechowywania logów ===
logi = []

# === Endpoint: status API ===
@app.get("/status")
def status():
    return {
        "status": "działa",
        "czas": datetime.now().isoformat()
    }

# === Endpoint: logowanie dowolnych danych ===
@app.post("/log")
async def dodaj_log(request: Request):
    try:
        body = await request.json()
    except Exception as e:
        return {"status": "błąd", "info": f"Błędny JSON: {str(e)}"}

    logi.append({
        "czas": datetime.now().isoformat(),
        "dane": body
    })
    return {
        "ok": True,
        "ilosc_logow": len(logi)
    }

# === Endpoint: odbieranie komend ===
@app.post("/komenda")
def odbierz_komende(k: Komenda):
    if not k.typ or not k.tresc:
        return {"status": "błąd", "info": "Brak typu lub treści komendy"}

    logi.append({
        "czas": datetime.now().isoformat(),
        "komenda": k.dict()
    })
    return {
        "status": "komenda przyjęta",
        "typ": k.typ,
        "tresc": k.tresc
    }

# === Endpoint: pobieranie tylko zasad ===
@app.get("/zasady")
def pobierz_zasady():
    zasady = []
    for wpis in logi:
        komenda = wpis.get("komenda")
        if komenda and komenda.get("typ") == "zasada":
            zasady.append({
                "czas": wpis["czas"],
                "tresc": komenda["tresc"]
            })

    if not zasady:
        return {"status": "brak", "info": "Nie znaleziono zasad"}

    return {
        "ilosc": len(zasady),
        "zasady": zasady
    }
