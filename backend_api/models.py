from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

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
    body = await request.json()
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
    return {
        "ilosc": len(zasady),
        "zasady": zasady
    }
