from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()
SECRET_PASSWORD = "TwojeSuperHaslo"

@app.middleware("http")
async def check_password(request: Request, call_next):
    if request.url.path.startswith("/zasady") or request.url.path.startswith("/dodaj_zasade"):
        password = request.headers.get("X-Password")
        if password != SECRET_PASSWORD:
            raise HTTPException(status_code=401, detail="Nieprawidłowe hasło")
    response = await call_next(request)
    return response


from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ← pozwala na połączenia z dowolnego źródła
    allow_methods=["*"],  # ← pozwala na wszystkie metody: GET, POST, OPTIONS itd.
    allow_headers=["*"],  # ← pozwala na wszystkie nagłówki
)

# === MODELE DANYCH ===

class Komenda(BaseModel):
    typ: str
    tresc: str

class Zasada(BaseModel):
    czas: str
    tresc: str

# === ZMIENNE GLOBALNE ===

logi = []
ZASADY_FILE = "zasady.json"

# === ENDPOINT: STATUS ===

@app.get("/status")
def status():
    return {
        "status": "działa",
        "czas": datetime.now().isoformat()
    }

# === ENDPOINT: LOGOWANIE DOWOLNYCH DANYCH ===

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

# === ENDPOINT: KOMENDA (logowanie komend) ===

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

# === ENDPOINT: ZASADY (odczyt i zapis do pliku) ===

@app.get("/zasady")
def get_zasady():
    if os.path.exists(ZASADY_FILE):
        with open(ZASADY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.post("/dodaj_zasade")
async def dodaj_zasade(request: Request):
    body = await request.json()
    nowa_zasada = body["zasady"][0]
    zasady = get_zasady()
    zasady.append(nowa_zasada)
    with open(ZASADY_FILE, "w", encoding="utf-8") as f:
        json.dump(zasady, f, ensure_ascii=False, indent=2)
    return {"status": "dodano"}

@app.post("/usun_zasade")
async def usun_zasade(request: Request):
    body = await request.json()
    czas_do_usuniecia = body.get("czas")
    zasady = get_zasady()
    nowe_zasady = [z for z in zasady if z["czas"] != czas_do_usuniecia]
    with open(ZASADY_FILE, "w", encoding="utf-8") as f:
        json.dump(nowe_zasady, f, ensure_ascii=False, indent=2)
    return {"status": "usunieto"}


