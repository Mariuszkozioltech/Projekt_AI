import os
import csv
import json
import yaml
import logging
import psutil
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # ← TO JEST KLUCZOWE

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ścieżki do plików i folderów (JEDNA definicja)
ETAPY_FILE   = os.path.join("C:", "Projekt_AI", "etapy.yaml")
BACKUP_FILE  = os.path.join("C:", "Projekt_AI", "etapy_backup.yaml")
LOG_FILE     = os.path.join("C:", "Projekt_AI", "etapy_log.yaml")
ZASADY_FILE  = os.path.join("C:", "Projekt_AI", "zasady.json")
MEMORY_FILE  = os.path.join("C:", "Projekt_AI", "pamiec.json")

MATERIALS_DIR = os.path.join("C:", "Projekt_AI", "materials")
INCOMING_DIR  = os.path.join(MATERIALS_DIR, "incoming")
PROCESSED_DIR = os.path.join(MATERIALS_DIR, "processed")
REJECTED_DIR  = os.path.join(MATERIALS_DIR, "rejected")
NOTES_DIR     = os.path.join(MATERIALS_DIR, "notes")
INDEX_DIR     = os.path.join(MATERIALS_DIR, "index")

MATERIALS_INDEX = os.path.join(INDEX_DIR, "materials.json")
CHUNKS_INDEX    = os.path.join(INDEX_DIR, "chunks.json")
NOTES_INDEX     = os.path.join(INDEX_DIR, "notes.json")
AI_TASKS_FILE   = os.path.join(MATERIALS_DIR, "zadania_ai.json")

# Modele

class EtapZmiana(BaseModel):
    id: str = Field(..., description="Unikalny identyfikator etapu")
    nazwa: str = Field(..., description="Nazwa etapu")
    opis: str = Field(..., description="Opis etapu")
    status: str = Field(..., description="Status etapu (np. 'czeka', 'w trakcie')")
    priorytet: int = Field(0, description="Priorytet etapu (liczba całkowita)")

# Inicjalizacja struktur
def ensure_materials_dirs():
    for d in [MATERIALS_DIR, INCOMING_DIR, PROCESSED_DIR, REJECTED_DIR, NOTES_DIR, INDEX_DIR]:
        os.makedirs(d, exist_ok=True)

def ensure_materials_files():
    for p, default in [
        (MATERIALS_INDEX, []),
        (CHUNKS_INDEX, []),
        (NOTES_INDEX, []),
        (AI_TASKS_FILE, [])
    ]:
        if not os.path.exists(p):
            with open(p, "w", encoding="utf-8") as f:
                json.dump(default, f, ensure_ascii=False, indent=2)

ensure_materials_dirs()
ensure_materials_files()

# from pydantic import BaseModel, Field  # już zaimportowane wcześniej

# === MODELE ===
class Pamiec(BaseModel):
    id: str = Field(..., description="Unikalny identyfikator wpisu pamięci")
    tresc: str = Field(..., description="Treść wpisu")
    etap: str = Field(..., description="Powiązany etap")

# === FUNKCJE POMOCNICZE ===
def zrob_backup_etapow():
    if os.path.exists(ETAPY_FILE):
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = f.read()
        with open(BACKUP_FILE, "w", encoding="utf-8") as f:
            f.write(dane)

def loguj_zmiane(opis):
    wpis = {"czas": datetime.now().isoformat(), "opis": opis}
    logi = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logi = yaml.safe_load(f)
                if not isinstance(logi, list):
                    logi = []
        except yaml.YAMLError:
            logi = []
    logi.append(wpis)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        yaml.dump(logi, f, allow_unicode=True)

def ensure_materials_dirs():
    for d in [MATERIALS_DIR, INCOMING_DIR, PROCESSED_DIR, REJECTED_DIR, NOTES_DIR, INDEX_DIR]:
        os.makedirs(d, exist_ok=True)

def ensure_materials_files():
    for p in [MATERIALS_INDEX, CHUNKS_INDEX, NOTES_INDEX, AI_TASKS_FILE]:
        if not os.path.exists(p):
            with open(p, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

# 🔧 Inicjalizacja folderów i plików
ensure_materials_dirs()
ensure_materials_files()

def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# === ENDPOINTY SYSTEMOWE ===
@app.get(
    "/status",
    summary="Sprawdź status API",
    description="Zwraca informację o działaniu serwera oraz aktualny czas.",
    tags=["System"]
)
def status():
    return {"status": "działa", "czas": datetime.now().isoformat()}

@app.get(
    "/zasady",
    summary="Pobierz zasady",
    description="Zwraca listę zasad zapisanych w pliku zasady.json.",
    tags=["Zasady"]
)
def get_zasady():
    if os.path.exists(ZASADY_FILE):
        with open(ZASADY_FILE, "r", encoding="utf-8") as f:
            return json.load(f) or []
    return []

from fastapi.responses import JSONResponse

@app.post(
    "/chat",
    summary="Prosty czat z AI",
    description="Przyjmuje wiadomość i historię, zwraca odpowiedź tekstową jako JSON.",
    tags=["System"]
)
def chat(wiadomosc: dict):
    tekst = wiadomosc.get("wiadomosc", "")
    historia = wiadomosc.get("historia", [])
    odpowiedz = f"Rozumiem: {tekst}. Co chcesz dalej zrobić?"
    return JSONResponse(
        content={"odpowiedz": odpowiedz},
        media_type="application/json; charset=utf-8"
    )

@app.post(
    "/dodaj_zasade",
    summary="Dodaj zasadę",
    description="Dodaje nową zasadę do pliku zasady.json. Wymaga pola 'czas' i 'treść'.",
    tags=["Zasady"]
)
async def dodaj_zasade(request: Request):
    body = await request.json()
    if not body.get("zasady"):
        return {"status": "błąd", "error": "Brak zasad do dodania"}
    nowa_zasada = body["zasady"][0]
    zasady = get_zasady()
    zasady.append(nowa_zasada)
    with open(ZASADY_FILE, "w", encoding="utf-8") as f:
        json.dump(zasady, f, ensure_ascii=False, indent=2)
    return {"status": "dodano"}

@app.post(
    "/usun_zasade",
    summary="Usuń zasadę",
    description="Usuwa zasadę z pliku zasady.json na podstawie pola 'czas'.",
    tags=["Zasady"]
)
async def usun_zasade(request: Request):
    body = await request.json()
    czas_do_usuniecia = body.get("czas")
    zasady = get_zasady()
    nowe_zasady = [z for z in zasady if z["czas"] != czas_do_usuniecia]
    with open(ZASADY_FILE, "w", encoding="utf-8") as f:
        json.dump(nowe_zasady, f, ensure_ascii=False, indent=2)
    return {"status": "usunieto"}

from fastapi.responses import JSONResponse

@app.post(
    "/dodaj_zasade",
    summary="Dodaj zasadę",
    description="Dodaje nową zasadę do pliku zasady.json. Wymaga pola 'czas' i 'treść'.",
    tags=["Zasady"]
)
async def dodaj_zasade(request: Request):
    body = await request.json()
    if not body.get("zasady"):
        return {"status": "błąd", "error": "Brak zasad do dodania"}
    nowa_zasada = body["zasady"][0]
    zasady = get_zasady()
    zasady.append(nowa_zasada)
    with open(ZASADY_FILE, "w", encoding="utf-8") as f:
        json.dump(zasady, f, ensure_ascii=False, indent=2)
    return {"status": "dodano"}

@app.post(
    "/usun_zasade",
    summary="Usuń zasadę",
    description="Usuwa zasadę z pliku zasady.json na podstawie pola 'czas'.",
    tags=["Zasady"]
)
async def usun_zasade(request: Request):
    body = await request.json()
    czas_do_usuniecia = body.get("czas")
    zasady = get_zasady()
    nowe_zasady = [z for z in zasady if z["czas"] != czas_do_usuniecia]
    with open(ZASADY_FILE, "w", encoding="utf-8") as f:
        json.dump(nowe_zasady, f, ensure_ascii=False, indent=2)
    return {"status": "usunieto"}

# === PAMIĘĆ ===

@app.get(
    "/pamiec",
    summary="Pamięć AI",
    description="Zwraca zapisane dane pamięci z pliku pamiec.json. Używane do śledzenia etapów i historii.",
    tags=["Pamięć"]
)
def get_pamiec():
    if not os.path.exists(MEMORY_FILE):
        return {"pamiec": [], "ostatni_etap": ""}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f) or {"pamiec": [], "ostatni_etap": ""}
    except json.JSONDecodeError:
        return {"pamiec": [], "ostatni_etap": ""}

@app.post(
    "/pamiec/dodaj",
    summary="Dodaj wpis do pamięci",
    description="Dodaje nowy wpis do pliku pamiec.json. Wpis zawiera ID, treść i etap.",
    tags=["Pamięć"]
)
def dodaj_pamiec(p: Pamiec):
    try:
        if not os.path.exists(MEMORY_FILE):
            dane = {"pamiec": [], "ostatni_etap": ""}
        else:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                dane = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        dane = {"pamiec": [], "ostatni_etap": ""}
    dane["pamiec"].append(p.dict())
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)
    return {"status": "dodano"}

@app.post(
    "/usun_pamiec",
    summary="Usuń wpis z pamięci",
    description="Usuwa wpis z pliku pamiec.json na podstawie ID. Jeśli ID nie istnieje, nic się nie zmienia.",
    tags=["Pamięć"]
)
async def usun_pamiec(request: Request):
    body = await request.json()
    id_do_usuniecia = body.get("id")
    if not id_do_usuniecia:
        return {"status": "brak ID do usunięcia"}
    if not os.path.exists(MEMORY_FILE):
        return {"status": "brak pliku pamięci"}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            dane = json.load(f)
            if not isinstance(dane, dict):
                dane = {"pamiec": []}
    except (FileNotFoundError, json.JSONDecodeError):
        dane = {"pamiec": []}
    dane["pamiec"] = [p for p in dane.get("pamiec", []) if p.get("id") != id_do_usuniecia]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)
    return {"status": "usunieto"}

# === PAMIĘĆ ===

@app.post(
    "/usun_pamiec",
    summary="Usuń wpis z pamięci",
    description="Usuwa wpis z pliku pamiec.json na podstawie ID. Jeśli ID nie istnieje, nic się nie zmienia.",
    tags=["Pamięć"]
)
async def usun_pamiec(request: Request):
    body = await request.json()
    id_do_usuniecia = body.get("id")
    if not id_do_usuniecia:
        return {"status": "brak ID do usunięcia"}
    if not os.path.exists(MEMORY_FILE):
        return {"status": "brak pliku pamięci"}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            dane = json.load(f)
            if not isinstance(dane, dict):
                dane = {"pamiec": []}
    except (FileNotFoundError, json.JSONDecodeError):
        dane = {"pamiec": []}
    dane["pamiec"] = [p for p in dane.get("pamiec", []) if p.get("id") != id_do_usuniecia]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)
    return {"status": "usunieto"}

# === MATERIAŁY ===

@app.get(
    "/materialy",
    summary="Lista materiałów",
    description="Zwraca wszystkie materiały zapisane w pliku materials.json.",
    tags=["Materiały"]
)
def list_materialy():
    return read_json(MATERIALS_INDEX)

@app.post(
    "/materialy/odswiez",
    summary="Odśwież listę materiałów",
    description="Przeszukuje folder incoming i dodaje nowe pliki do indeksu materials.json, jeśli nie były wcześniej zarejestrowane.",
    tags=["Materiały"]
)
def odswiez_materialy():
    logging.info("Wywołano: /materialy/odswiez")
    try:
        materials = read_json(MATERIALS_INDEX)
    except Exception:
        materials = []

    known = {m.get("sciezka") for m in materials if "sciezka" in m}

    for root, _, files in os.walk(INCOMING_DIR):
        for name in files:
            sciezka = os.path.join(root, name)
            if sciezka in known:
                continue

            material_id = f"mat_{int(datetime.now().timestamp() * 1000)}"
            rel = os.path.relpath(sciezka, MATERIALS_DIR)
            tagi = []
            parts = rel.split(os.sep)
            if len(parts) > 2:
                tagi.append(parts[1])

            materials.append({
                "id": material_id,
                "nazwa": name,
                "sciezka": sciezka,
                "typ": os.path.splitext(name)[1].lower().replace(".", ""),
                "status": "incoming",
                "tagi": tagi,
                "data_dodania": datetime.now().isoformat()
            })

    write_json(MATERIALS_INDEX, materials)
    logging.info(f"Zaktualizowano materiały: {len(materials)} pozycji")
    return {"ok": True, "count": len(materials)}

# === MATERIAŁY ===

@app.post(
    "/materialy/oznacz",
    summary="Oznacz materiał",
    description="Zmienia status materiału na podstawie jego ID. Status może być np. 'incoming', 'processed', 'rejected'.",
    tags=["Materiały"]
)
async def oznacz_material(request: Request):
    logging.info("Wywołano: /materialy/oznacz")
    body = await request.json()
    material_id = body.get("id")
    status = body.get("status")

    if not material_id or not status:
        return {"ok": False, "error": "Brak ID lub statusu"}

    materials = read_json(MATERIALS_INDEX)
    znaleziono = False

    for m in materials:
        if m.get("id") == material_id:
            m["status"] = status
            znaleziono = True
            break

    if not znaleziono:
        return {"ok": False, "error": f"Nie znaleziono materiału o ID {material_id}"}

    write_json(MATERIALS_INDEX, materials)
    logging.info(f"Oznaczono materiał {material_id} jako {status}")
    return {"ok": True}

# === IMPORT Z INTERNETU ===

@app.get(
    "/import_material/test",
    summary="Testowy materiał",
    description="Zwraca przykładowy obiekt materiału w formacie Markdown.",
    tags=["Materiały"]
)
def test_import():
    return {
        "title": "Przykładowy materiał",
        "temat": "python",
        "plik": "Przyklad.md",
        "status": "incoming"
    }

@app.post(
    "/import_material",
    summary="Importuj materiał z internetu",
    description="Pobiera zawartość strony WWW (nagłówki, paragrafy, kod, obrazki), zapisuje jako plik Markdown i dodaje do indeksu materiałów.",
    tags=["Materiały"]
)
async def import_material(request: Request):
    logging.info("Wywołano: /import_material")
    body = await request.json()
    url = body.get("url")

    if not url:
        return {"ok": False, "error": "Brak adresu URL"}

    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return {"ok": False, "error": f"Błąd HTTP: {res.status_code}"}

        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else "materiał"
        tekst = []

        for tag in soup.find_all(["h1", "h2", "h3", "p", "li", "pre", "code", "img"]):
            if tag.name == "img" and tag.get("src"):
                tekst.append(f"![obrazek]({tag['src']})")
            elif tag.name in ["h1", "h2", "h3"]:
                tekst.append(f"\n## {tag.get_text().strip()}\n")
            elif tag.name in ["pre", "code"]:
                tekst.append(f"\n```\n{tag.get_text().strip()}\n```\n")
            else:
                tekst.append(tag.get_text().strip())

        full_text = "\n".join(tekst)
        if not full_text.strip():
            return {"ok": False, "error": "Brak treści do zapisania."}

        temat = "python" if "python" in full_text.lower() else "inwestycje" if "invest" in full_text.lower() else "materiały"
        folder = os.path.join(MATERIALS_DIR, "incoming", temat)
        os.makedirs(folder, exist_ok=True)

        plik_nazwa = f"{title[:40].replace(' ', '_')}.md"
        sciezka = os.path.join(folder, plik_nazwa)

        if os.path.exists(sciezka):
            return {"ok": False, "error": "Plik już istnieje"}

        with open(sciezka, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n{full_text}")

        materials = read_json(MATERIALS_INDEX)
        materials.append({
            "id": f"mat_{int(datetime.now().timestamp() * 1000)}",
            "nazwa": plik_nazwa,
            "sciezka": sciezka,
            "typ": "md",
            "status": "incoming",
            "tagi": [temat],
            "data_dodania": datetime.now().isoformat()
        })
        write_json(MATERIALS_INDEX, materials)

        logging.info(f"Zaimportowano materiał: {plik_nazwa}")
        return {
            "ok": True,
            "plik": plik_nazwa,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        logging.error(f"Błąd importu materiału: {e}")
        return {"ok": False, "error": str(e)}

        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else "materiał"
        tekst = []

        # 🔍 Pobierz nagłówki, paragrafy, listy, kod, obrazki
        for tag in soup.find_all(["h1", "h2", "h3", "p", "li", "pre", "code", "img"]):
            if tag.name == "img" and tag.get("src"):
                tekst.append(f"![obrazek]({tag['src']})")
            elif tag.name in ["h1", "h2", "h3"]:
                tekst.append(f"\n## {tag.get_text().strip()}\n")
            elif tag.name in ["pre", "code"]:
                tekst.append(f"\n```\n{tag.get_text().strip()}\n```\n")
            else:
                tekst.append(tag.get_text().strip())

        full_text = "\n".join(tekst)
        if not full_text.strip():
            return {"ok": False, "error": "Brak treści do zapisania."}

        # 🧠 Rozpoznaj temat
        temat = "materiały"  # domyślnie
        if "ai" in full_text.lower():
            temat = "sztuczna_inteligencja"
        elif "finance" in full_text.lower():
            temat = "finanse"
        elif "data" in full_text.lower():
            temat = "dane"

        folder = os.path.join(MATERIALS_DIR, "incoming", temat)
        os.makedirs(folder, exist_ok=True)

        # 📝 Nazwa pliku
        plik_nazwa = f"{title[:40].replace(' ', '_')}.md"
        sciezka = os.path.join(folder, plik_nazwa)

        if os.path.exists(sciezka):
            return {"ok": False, "error": "Plik już istnieje"}

        with open(sciezka, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n{full_text}")

        # 📦 Zapisz do indeksu
        materials = read_json(MATERIALS_INDEX)
        materials.append({
            "id": f"mat_{int(datetime.now().timestamp() * 1000)}",
            "nazwa": plik_nazwa,
            "sciezka": sciezka,
            "typ": "md",
            "status": "incoming",
            "tagi": [temat],
            "data_dodania": datetime.now().isoformat()
        })
        write_json(MATERIALS_INDEX, materials)

        logging.info(f"Zaimportowano materiał: {plik_nazwa}")
        return {
            "ok": True,
            "plik": plik_nazwa,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        logging.error(f"Błąd importu materiału: {e}")
        return {"ok": False, "error": str(e)}

# === ŹRÓDŁA I ZADANIA AI ===

SOURCES_FILE = r"C:\Projekt_AI\PROJEKT\AI_trening\sources.json"

def read_sources():
    if not os.path.exists(SOURCES_FILE):
        return []
    try:
        with open(SOURCES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_sources(data):
    with open(SOURCES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.get(
    "/sources",
    summary="Lista źródeł",
    description="Zwraca listę zapisanych źródeł z pliku sources.json.",
    tags=["Źródła"]
)
def get_sources():
    return read_sources()

@app.post(
    "/sources/add",
    summary="Dodaj nowe źródło",
    description="Dodaje nowe źródło URL do pliku sources.json. Wymaga poprawnego adresu URL.",
    tags=["Źródła"]
)
async def add_source(request: Request):
    body = await request.json()
    url = body.get("url")
    if not url or not isinstance(url, str) or not url.strip():
        return {"ok": False, "error": "Nieprawidłowy URL"}

    sources = read_sources()
    new_source = {
        "id": f"src_{int(datetime.now().timestamp() * 1000)}",
        "url": url.strip(),
        "data_dodania": datetime.now().isoformat()
    }
    sources.insert(0, new_source)
    write_sources(sources)
    logging.info(f"Dodano źródło: {new_source['id']} - {new_source['url']}")
    return {"ok": True}

@app.get(
    "/zadania_ai",
    summary="Lista zadań AI",
    description="Zwraca listę zadań AI zapisanych w pliku zadania_ai.json.",
    tags=["AI"]
)
def pobierz_zadania_ai():
    try:
        with open(AI_TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.get(
    "/kolejny_krok",
    summary="Kolejny krok w projekcie",
    description="Podpowiada kolejny krok w tworzeniu aplikacji AI.",
    tags=["System"]
)
def kolejny_krok():
    return {
        "krok": "Stwórz plik 'main.py' w folderze projektu",
        "uzasadnienie": "To będzie główny plik aplikacji, w którym rozpoczniesz kodowanie logiki AI."
    }

# === ŹRÓDŁA ===

@app.post(
    "/sources/remove",
    summary="Usuń źródło",
    description="Usuwa źródło z pliku sources.json na podstawie jego ID.",
    tags=["Źródła"]
)
async def remove_source(request: Request):
    body = await request.json()
    id_ = body.get("id")
    if not id_:
        return {"ok": False, "error": "Brak ID źródła"}

    sources = read_sources()
    if not any(s.get("id") == id_ for s in sources):
        return {"ok": False, "error": "Nie znaleziono źródła o podanym ID"}

    sources = [s for s in sources if s.get("id") != id_]
    write_sources(sources)
    logging.info(f"Usunięto źródło: {id_}")
    return {"ok": True}

# === ZADANIA AI ===

@app.get(
    "/ai/tasks",
    summary="Lista zadań AI",
    description="Zwraca wszystkie zadania AI zapisane w pliku zadania_ai.json.",
    tags=["AI"]
)
def list_ai_tasks():
    return read_json(AI_TASKS_FILE)

@app.post(
    "/ai/tasks/dodaj",
    summary="Dodaj zadanie AI",
    description="Dodaje nowe zadanie AI do pliku zadania_ai.json. Wymaga typu i wejścia jako słownik.",
    tags=["AI"]
)
async def add_ai_task(request: Request):
    body = await request.json()
    if not body.get("typ"):
        return {"ok": False, "error": "Brak typu zadania"}
    if not isinstance(body.get("wejscie", {}), dict):
        return {"ok": False, "error": "Pole 'wejscie' musi być słownikiem"}

    t = {
        "id": f"task_{int(datetime.now().timestamp() * 1000)}",
        "typ": body.get("typ"),
        "wejscie": body.get("wejscie", {}),
        "opis": body.get("opis", ""),
        "status": "czeka",
        "data": datetime.now().isoformat()
    }
    tasks = read_json(AI_TASKS_FILE)
    tasks.append(t)
    write_json(AI_TASKS_FILE, tasks)
    logging.info(f"Dodano zadanie AI: {t['id']} ({t['typ']})")
    return {"ok": True, "id": t["id"]}

@app.post(
    "/ai/tasks/akcja",
    summary="Zmień status zadania AI",
    description="Aktualizuje status zadania AI na podstawie jego ID i decyzji (np. 'czeka', 'w trakcie', 'zakończono').",
    tags=["AI"]
)
async def act_ai_task(request: Request):
    body = await request.json()
    task_id = body.get("id")
    decyzja = body.get("decyzja")

    if not task_id or not decyzja:
        return {"ok": False, "error": "Brak ID zadania lub decyzji"}

    tasks = read_json(AI_TASKS_FILE)
    znaleziono = False

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = decyzja
            znaleziono = True
            break

    if not znaleziono:
        return {"ok": False, "error": "Nie znaleziono zadania o podanym ID"}

    write_json(AI_TASKS_FILE, tasks)
    logging.info(f"Zmieniono status zadania {task_id} na {decyzja}")
    return {"ok": True}

 # === ETAPY ===

@app.get(
    "/etapy",
    summary="Lista etapów",
    description="Zwraca wszystkie etapy zapisane w pliku etapy.yaml.",
    tags=["Etapy"]
)
def get_etapy():
    if not os.path.exists(ETAPY_FILE):
        return []
    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return []
    return dane.get("etapy", [])

@app.post(
    "/dodaj_etap",
    summary="Dodaj nowy etap",
    description="Dodaje nowy etap do pliku etapy.yaml. Wymaga pól: id, nazwa, opis, status, priorytet.",
    tags=["Etapy"]
)
def dodaj_etap(e: dict = Body(...)):
    logging.info("Wywołano: /dodaj_etap")
    if "id" not in e:
        return {"status": "błąd", "error": "Brak ID etapu"}

    zrob_backup_etapow()
    loguj_zmiane(f"Dodano etap {e.get('id', 'brak_id')}")

    if not os.path.exists(ETAPY_FILE):
        etapy = []
    else:
        try:
            with open(ETAPY_FILE, "r", encoding="utf-8") as f:
                dane = yaml.safe_load(f) or {}
        except yaml.YAMLError:
            dane = {}
        etapy = dane.get("etapy", [])

    etapy.append(e)
    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    return {"status": "dodano"}

@app.post(
    "/usun_etap",
    summary="Usuń etap",
    description="Usuwa etap z pliku etapy.yaml na podstawie jego ID.",
    tags=["Etapy"]
)
def usun_etap(e: dict = Body(...)):
    logging.info("Wywołano: /usun_etap")
    if "id" not in e:
        return {"status": "błąd", "error": "Brak ID etapu"}

    zrob_backup_etapow()
    loguj_zmiane(f"Usunięto etap {e['id']}")

    if not os.path.exists(ETAPY_FILE):
        return {"status": "brak pliku"}

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return {"status": "błąd", "error": "Nie można odczytać pliku YAML"}

    etapy = dane.get("etapy", [])
    nowe = [etap for etap in etapy if etap.get("id") != e["id"]]

    if len(nowe) == len(etapy):
        return {"status": f"Nie znaleziono etapu o ID {e['id']}"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": nowe}, f, allow_unicode=True)

    return {"status": f"Etap {e['id']} usunięty"}
   
@app.post(
    "/edytuj_etap",
    summary="Edytuj istniejący etap",
    description="Aktualizuje dane etapu w pliku etapy.yaml na podstawie jego ID. Można zmienić nazwę, opis, status i priorytet.",
    tags=["Etapy"]
)
def edytuj_etap(e: EtapZmiana):
    zrob_backup_etapow()
    loguj_zmiane(f"Edytowano etap {e.id}")

    if not os.path.exists(ETAPY_FILE):
        return {"status": "brak pliku"}

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return {"status": "błąd", "error": "Nie można odczytać pliku YAML"}

    etapy = dane.get("etapy", [])
    znaleziono = False

    for etap in etapy:
        if etap.get("id") == e.id:
            etap["nazwa"] = e.nazwa
            etap["opis"] = e.opis
            etap["status"] = e.status
            etap["priorytet"] = e.priorytet
            znaleziono = True
            break

    if not znaleziono:
        return {"status": f"Nie znaleziono etapu o ID {e.id}"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    return {"status": f"Etap {e.id} zaktualizowany"}

@app.post(
    "/zmien_status",
    summary="Zmień status etapu",
    description="Zmienia status etapu w pliku etapy.yaml na podstawie jego ID.",
    tags=["Etapy"]
)
async def zmien_status(request: Request):
    logging.info("Wywołano: /zmien_status")
    body = await request.json()
    id = body.get("id")
    status = body.get("status")

    if not id or not status:
        return {"status": "Brak ID lub statusu"}

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return {"status": "błąd", "error": "Nie można odczytać pliku YAML"}

    etapy = dane.get("etapy", [])
    znaleziono = False

    for etap in etapy:
        if etap.get("id") == id:
            etap["status"] = status
            znaleziono = True
            break

    if not znaleziono:
        return {"status": f"Nie znaleziono etapu o ID {id}"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    return {"status": f"Status etapu {id} zmieniony na {status}"}

@app.post(
    "/zmien_priorytet",
    summary="Zmień priorytet etapu",
    description="Aktualizuje priorytet wybranego etapu w pliku etapy.yaml na podstawie jego ID.",
    tags=["Etapy"]
)
async def zmien_priorytet(request: Request):
    body = await request.json()
    id = body.get("id")
    priorytet = body.get("priorytet")

    if not id or priorytet is None:
        return {"status": "błąd", "error": "Brak ID lub priorytetu"}

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except FileNotFoundError:
        logging.error(f"Plik {ETAPY_FILE} nie istnieje.")
        return JSONResponse(
            content={"status": "błąd", "error": "Brak pliku etapów"},
            status_code=404
        )
    except yaml.YAMLError as e:
        logging.error(f"Błąd YAML: {e}")
        return JSONResponse(
            content={"status": "błąd", "error": "Niepoprawny format YAML"},
            status_code=400
        )

    etapy = dane.get("etapy", [])
    znaleziono = False

    for etap in etapy:
        if etap.get("id") == id:
            etap["priorytet"] = priorytet
            znaleziono = True
            break

    if not znaleziono:
        return {"status": f"Nie znaleziono etapu o ID {id}"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    logging.info(f"Zmieniono priorytet etapu {id} na {priorytet}")
    return {"status": f"Priorytet etapu {id} zmieniony na {priorytet}"}


@app.post(
    "/zapisz_etap",
    summary="Zapisz zmiany etapu",
    description="Zapisuje zmieniony status i priorytet etapu w pliku etapy.yaml na podstawie jego ID.",
    tags=["Etapy"]
)
async def zapisz_etap(request: Request):
    logging.info("Wywołano: /zapisz_etap")
    body = await request.json()
    id = body.get("id")
    status = body.get("status")
    priorytet = body.get("priorytet")

    if not id or status is None or priorytet is None:
        return {"status": "Brak ID, statusu lub priorytetu"}

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except FileNotFoundError:
        logging.error(f"Plik {ETAPY_FILE} nie istnieje.")
        return JSONResponse(
            content={"status": "błąd", "error": "Brak pliku etapów"},
            status_code=404
        )
    except yaml.YAMLError as e:
        logging.error(f"Błąd YAML: {e}")
        return JSONResponse(
            content={"status": "błąd", "error": "Niepoprawny format YAML"},
            status_code=400
        )

    etapy = dane.get("etapy", [])
    znaleziono = False

    for etap in etapy:
        if etap.get("id") == id:
            etap["status"] = status
            etap["priorytet"] = priorytet
            znaleziono = True
            break

    if not znaleziono:
        return {"status": f"Nie znaleziono etapu o ID {id}"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    logging.info(f"Zapisano etap {id} ze statusem '{status}' i priorytetem '{priorytet}'")
    return {"status": f"Etap {id} zapisany"}

@app.post(
    "/zapisz_kolejnosc",
    summary="Zapisz kolejność etapów",
    description="Zapisuje nową kolejność etapów na podstawie listy ID. Etapy nieujęte w liście pozostają na końcu w oryginalnej kolejności.",
    tags=["Etapy"]
)
async def zapisz_kolejnosc(request: Request):
    body = await request.json()
    nowa_kolejnosc = body.get("kolejnosc", [])

    logging.info(f"🧩 Kolejność otrzymana: {nowa_kolejnosc}")

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        logging.error(f"Błąd YAML: {e}")
        dane = {}

    etapy = dane.get("etapy", [])
    uporzadkowane = [etap for id_ in nowa_kolejnosc for etap in etapy if etap.get("id") == id_]
    pozostale = [etap for etap in etapy if etap.get("id") not in nowa_kolejnosc]
    final = uporzadkowane + pozostale

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": final}, f, allow_unicode=True)

    logging.info("Zapisano nową kolejność etapów")
    return {"status": "kolejnosc zapisana", "kolejnosc": nowa_kolejnosc}


@app.post(
    "/oznacz_etap",
    summary="Oznacz status etapu",
    description="Zmienia status istniejącego etapu w pliku etapy.yaml na podstawie jego ID.",
    tags=["Etapy"]
)
def oznacz_etap(e: EtapZmiana):
    if not os.path.exists(ETAPY_FILE):
        return {"status": "brak pliku"}

    try:
        with open(ETAPY_FILE, "r", encoding="utf-8") as f:
            dane = yaml.safe_load(f) or {}
    except FileNotFoundError:
        logging.error(f"Plik {ETAPY_FILE} nie istnieje.")
        return JSONResponse(content={"status": "błąd", "error": "Brak pliku etapów"}, status_code=404)
    except yaml.YAMLError as e:
        logging.error(f"Błąd YAML: {e}")
        return JSONResponse(content={"status": "błąd", "error": "Niepoprawny format YAML"}, status_code=400)

    etapy = dane.get("etapy", [])
    znaleziono = False

    for etap in etapy:
        if etap.get("id") == e.id:
            etap["status"] = e.status
            znaleziono = True
            break

    if not znaleziono:
        return {"status": f"Nie znaleziono etapu o ID {e.id}"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    return {"status": f"Etap {e.id} oznaczony jako {e.status}"}


@app.post(
    "/dopasuj_etapy",
    summary="Załaduj etapy z pliku bazowego",
    description="Zastępuje bieżące etapy tymi z pliku etapy_baza.yaml. Używane do przywracania lub synchronizacji danych.",
    tags=["Etapy"]
)
def dopasuj_etapy():
    zrob_backup_etapow()
    loguj_zmiane("Załadowano etapy z etapy_baza.yaml")

    baza_path = os.path.join("C:", "Projekt_AI", "etapy_baza.yaml")
    if not os.path.exists(baza_path):
        return {"status": "Brak pliku etapy_baza.yaml"}

    try:
        with open(baza_path, "r", encoding="utf-8") as f:
            etapy = yaml.safe_load(f)
    except yaml.YAMLError as e:
        logging.error(f"Błąd YAML: {e}")
        return {"status": "Błąd: nie można odczytać pliku etapy_baza.yaml"}

    if not isinstance(etapy, list):
        return {"status": "Błąd: etapy_baza.yaml musi zawierać listę etapów"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    return {"status": "Etapy zostały załadowane z etapy_baza.yaml"}

def ocena_pewnosci(odpowiedz: str, dane: dict, temat: str) -> str:
    wazne_tematy = ["pieniądze", "spotkanie", "wyjazd", "decyzja", "termin"]
    if temat.lower() in wazne_tematy:
        if not dane or "brak" in odpowiedz.lower():
            return "❓ Nie mam wystarczających informacji, by potwierdzić."
        if "na podstawie" in odpowiedz.lower():
            return "✅ Potwierdzam na podstawie dostępnych danych."
        return "⚠️ Nie jestem pewien, ale oto co wiem..."
    return ""  # nie pokazuj nic, jeśli temat nie jest ważny

@app.post(
    "/dopasuj_etapy",
    summary="Załaduj etapy z pliku bazowego",
    description="Zastępuje bieżące etapy tymi z pliku etapy_baza.yaml. Używane do przywracania lub synchronizacji danych.",
    tags=["Etapy"]
)
def dopasuj_etapy():
    zrob_backup_etapow()
    loguj_zmiane("Załadowano etapy z etapy_baza.yaml")

    baza_path = os.path.join("C:", "Projekt_AI", "etapy_baza.yaml")
    if not os.path.exists(baza_path):
        return {"status": "Brak pliku etapy_baza.yaml"}

    try:
        with open(baza_path, "r", encoding="utf-8") as f:
            etapy = yaml.safe_load(f)
    except yaml.YAMLError as e:
        logging.error(f"Błąd YAML: {e}")
        return {"status": "Błąd: nie można odczytać pliku etapy_baza.yaml"}

    if not isinstance(etapy, list):
        return {"status": "Błąd: etapy_baza.yaml musi zawierać listę etapów"}

    with open(ETAPY_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)

    return {"status": "Etapy zostały załadowane z etapy_baza.yaml"}


@app.get(
    "/ping",
    summary="Sprawdź połączenie",
    description="Prosty test połączenia z serwerem. Zwraca 'pong=True'.",
    tags=["System"]
)
def ping():
    logging.info("Wywołano: /ping")
    logging.info("Odpowiedź: pong=True")
    return JSONResponse(content={"pong": True}, status_code=200)


RAPORT_CSV = os.path.join("C:", "Projekt_AI", "logi_analizy", "raport_zbiorczy.csv")

@app.get(
    "/raport",
    summary="Pobierz raport z analizy kodu",
    description="Zwraca pełny raport z pliku raport_zbiorczy.csv jako lista rekordów.",
    tags=["Raport"]
)
def get_raport():
    if not os.path.exists(RAPORT_CSV):
        return {"status": "brak raportu"}
    with open(RAPORT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dane = [row for row in reader if row.get("Nazwa pliku")]
    return {"raport": dane}


@app.get(
    "/plik/{nazwa}",
    summary="Szczegóły pliku z raportu",
    description="Zwraca dane dla konkretnego pliku z raportu na podstawie jego nazwy.",
    tags=["Raport"]
)
def get_plik(nazwa: str):
    if not os.path.exists(RAPORT_CSV):
        return {"status": "brak raportu"}
    with open(RAPORT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Nazwa pliku") == nazwa:
                return {"plik": row}
    return {"status": f"Nie znaleziono pliku: {nazwa}"}


@app.get(
    "/statystyki_raportu",
    summary="Statystyki raportu",
    description="Zwraca liczbę plików w każdej kategorii z raportu zbiorczego.",
    tags=["Raport"]
)
def statystyki_raportu():
    if not os.path.exists(RAPORT_CSV):
        return {"status": "brak raportu"}
    statystyki = {}
    with open(RAPORT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            status = row.get("Status", "nieznany").lower()
            statystyki[status] = statystyki.get(status, 0) + 1
    return {"statystyki": statystyki}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

@app.post("/analizuj_material")
def analizuj_material(dane: dict):
    folder = os.path.join("C:", "Projekt_AI", "PROJEKT", "AI_trening", "materials", "incoming")
    os.makedirs(folder, exist_ok=True)
    teraz = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{teraz}_material.json"
    path = os.path.join(folder, filename)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False, indent=2)
        return {"status": "Materiał zapisany", "plik": filename}
    except Exception as e:
        return {"status": "Błąd zapisu", "error": str(e)}


