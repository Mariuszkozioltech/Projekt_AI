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

import yaml
import os
import json

ETAPY_PATH = "C:\\Projekt_AI\\etapy.yaml"

def wczytaj_etapy():
    with open(ETAPY_PATH, "r", encoding="utf-8") as f:
        dane = yaml.safe_load(f)
    return dane.get("etapy", [])

def pokaz_status():
    etapy = wczytaj_etapy()
    print("📋 Status etapów projektu:")
    for etap in etapy:
        print(f"- [{etap['status']}] {etap['id']} – {etap['nazwa']}")

def dodaj_etap(id, nazwa, opis="Brak opisu"):
    etapy = wczytaj_etapy()
    nowy = {
        "id": id,
        "nazwa": nazwa,
        "opis": opis,
        "status": "todo"
    }
    etapy.append(nowy)
    with open(ETAPY_PATH, "w", encoding="utf-8") as f:
        yaml.dump({"etapy": etapy}, f, allow_unicode=True)
    print(f"✅ Dodano nowy etap: {id} – {nazwa}")

def podpowiedz_kolejny():
    etapy = wczytaj_etapy()
    for etap in etapy:
        if etap["status"] == "in_progress":
            print(f"🔄 Aktualnie pracujesz nad: {etap['id']} – {etap['nazwa']}")
            return
    for etap in etapy:
        if etap["status"] == "todo":
            print(f"➡️ Kolejny sugerowany etap: {etap['id']} – {etap['nazwa']}")
            return
    print("🎉 Wszystkie etapy ukończone!")

# Przykładowe uruchomienie
def instrukcja_dla_etapu(etap_id):
    instrukcje = {
        "2B": [
            "🔧 Sprawdź, czy folder 'frontend' istnieje",
            "📦 Upewnij się, że masz plik 'frontend_api.py'",
            "🖥️ Uruchom panel na porcie 5173",
            "🧪 Przetestuj przyciski: polityki, logi, status",
            "❌ Jeśli coś nie działa, zapisz błąd do 'logs/panel_errors.log'"
        ],
        "3": [
            "🔌 Stwórz endpointy: /status, /log, /ask",
            "🔐 Dodaj autoryzację ról: admin, user",
            "📈 Włącz heartbeat co 15s"
        ]
    }
    if etap_id in instrukcje:
        print(f"\n📘 Instrukcje dla etapu {etap_id}:")
        for krok in instrukcje[etap_id]:
            print(krok)
import os

def sprawdz_panel_www():
    print("\n🔍 Sprawdzanie panelu WWW (etap 2B):")
    folder = "C:\\Projekt_AI\\frontend"
    plik = "C:\\Projekt_AI\\frontend\\frontend_api.py"
    log_path = "C:\\Projekt_AI\\logs\\panel_errors.log"

    błędy = []

    if not os.path.exists(folder):
        błędy.append("❌ Brak folderu 'frontend'")
    else:
        print("✅ Folder 'frontend' istnieje")

    if not os.path.exists(plik):
        błędy.append("❌ Brak pliku 'frontend_api.py'")
    else:
        print("✅ Plik 'frontend_api.py' istnieje")

    if błędy:
        print("\n⚠️ Wykryto problemy:")
        for błąd in błędy:
            print(błąd)
        with open(log_path, "a", encoding="utf-8") as f:
            for błąd in błędy:
                f.write(błąd + "\n")
        print(f"📝 Błędy zapisano do logu: {log_path}")
    else:
        print("🎉 Panel wygląda poprawnie!")
def wczytaj_plan_asystenta():
    plan_path = "C:\\Projekt_AI\\config\\asystent_plan.yaml"
    if not os.path.exists(plan_path):
        print("⚠️ Brak pliku asystent_plan.yaml")
        return []
    with open(plan_path, "r", encoding="utf-8") as f:
        dane = yaml.safe_load(f)
    return dane.get("zadania", [])
def pokaz_zadania_asystenta():
    zadania = wczytaj_plan_asystenta()
    print("\n🧠 Zadania AI-asystenta:")
    for zad in zadania:
        print(f"- [{zad['status']}] {zad['id']} – {zad['nazwa']}")
def oznacz_zadanie(zadanie_id, nowy_status):
    plan_path = "C:\\Projekt_AI\\config\\asystent_plan.yaml"
    if not os.path.exists(plan_path):
        print("⚠️ Brak pliku asystent_plan.yaml")
        return
    with open(plan_path, "r", encoding="utf-8") as f:
        dane = yaml.safe_load(f)

    zadania = dane.get("zadania", [])
    znaleziono = False
    for zad in zadania:
        if zad["id"] == zadanie_id:
            zad["status"] = nowy_status
            znaleziono = True
            break

    if znaleziono:
        with open(plan_path, "w", encoding="utf-8") as f:
            yaml.dump(dane, f, allow_unicode=True)
        print(f"✅ Zaktualizowano zadanie {zadanie_id} → {nowy_status}")
    else:
        print(f"❌ Nie znaleziono zadania o ID: {zadanie_id}")
import requests
import subprocess

def sprawdz_panel_www_dzialanie():
    print("\n🌐 Sprawdzanie działania panelu WWW...")
    try:
        response = requests.get("http://localhost:5173", timeout=3)
        if response.status_code == 200:
            print("✅ Panel WWW działa poprawnie.")
        else:
            print(f"⚠️ Panel WWW zwrócił kod: {response.status_code}")
    except:
        print("❌ Panel WWW nie działa — próbuję go uruchomić...")
        uruchom_panel_www()

def uruchom_panel_www():
    panel_script = "C:\\Projekt_AI\\start_panel.bat"
    if os.path.exists(panel_script):
        subprocess.Popen(panel_script, shell=True)
        print("🖥️ Panel został uruchomiony przez start_panel.bat")
    else:
        print("⚠️ Nie znaleziono pliku start_panel.bat — uruchom ręcznie lub dodaj go.")
def wczytaj_pamiec():
    path = "C:\\Projekt_AI\\memory\\memory_index.json"
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def zapisz_pamiec(klucz, wartosc):
    path = "C:\\Projekt_AI\\memory\\memory_index.json"
    pamiec = wczytaj_pamiec()
    pamiec[klucz] = wartosc
    with open(path, "w", encoding="utf-8") as f:
        json.dump(pamiec, f, ensure_ascii=False, indent=2)
    print(f"🧠 Zapamiętano: {klucz} → {wartosc}")
def wykonaj_makro(nazwa):
    path = "C:\\Projekt_AI\\config\\makra.yaml"
    if not os.path.exists(path):
        print("⚠️ Brak pliku makra.yaml")
        return
    with open(path, "r", encoding="utf-8") as f:
        dane = yaml.safe_load(f)
    makra = dane.get("makra", [])
    for makro in makra:
        if makro["nazwa"] == nazwa:
            print(f"\n🚀 Wykonywanie makra: {nazwa}")
            for krok in makro["kroki"]:
                try:
                    globals()[krok]()  # wywołuje funkcję o nazwie 'krok'
                except Exception as e:
                    print(f"❌ Błąd w kroku '{krok}': {e}")
            return
    print(f"❌ Nie znaleziono makra o nazwie: {nazwa}")
def dodaj_zasade_testowa():
    zasada = {
        "czas": "2025-08-30T13:45:00",
        "tresc": "Testowa zasada dodana przez makro"
    }
    payload = {
        "ilosc": 1,
        "zasady": [zasada]
    }
    try:
        response = requests.post("http://127.0.0.1:8000/dodaj_zasade", json=payload)
        if response.status_code == 200:
            print("✅ Dodano zasadę testową przez makro.")
        else:
            print(f"⚠️ Błąd dodawania zasady: {response.status_code}")
    except Exception as e:
        print(f"❌ Nie udało się połączyć z backendem: {e}")


if __name__ == "__main__":
    oznacz_zadanie("A6", "done")
    pokaz_status()
    podpowiedz_kolejny()
    instrukcja_dla_etapu("2B")
    sprawdz_panel_www()
    pokaz_zadania_asystenta()
    sprawdz_panel_www_dzialanie()
    zapisz_pamiec("ostatni_etap", "2B")
    wykonaj_makro("sprawdz_panel")
    wykonaj_makro("dodaj_zasade_testowa")
    # dodaj_etap("2C", "Nowy pomysł", "Opis nowego etapu")
