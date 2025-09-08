import psutil
import os
from datetime import datetime

log_file = "resource_log.txt"
max_entries = 100  # ile wpisów chcesz trzymać

def log_resources():
    process = psutil.Process(os.getpid())
    ram = process.memory_info().rss / 1024 ** 2
    cpu = psutil.cpu_percent(interval=1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = f"{timestamp} | RAM: {ram:.2f} MB | CPU: {cpu:.2f}%\n"

    # Wczytaj stare wpisy
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            old_entries = f.readlines()
    else:
        old_entries = []

    # Dodaj nowy wpis na górę
    all_entries = [new_entry] + old_entries[:max_entries - 1]

    # Zapisz z powrotem
    with open(log_file, "w") as f:
        f.writelines(all_entries)

log_resources()