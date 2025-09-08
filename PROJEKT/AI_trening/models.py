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

from pydantic import BaseModel

class Komenda(BaseModel):
    typ: str
    tresc: str

class Zasada(BaseModel):
    czas: str
    tresc: str

class EtapZmiana(BaseModel):
    id: str
    status: str
    nazwa: str = ""
    opis: str = ""

class Pamiec(BaseModel):
    id: str
    typ: str
    tresc: str
    czas: str

