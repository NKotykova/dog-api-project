# Projekt: Dog API Demonstration

Dieses Projekt zeigt, wie man die Dog API (https://api.thedogapi.com/v1) nutzt, Daten abruft, filtert und visualisiert.

---

## Projektstruktur

my-dog-project/
│
├─ main.py # Haupt-Python-Skript für API-Abfragen
├─ .env.example # Beispiel für Umgebungsvariablen (API-Key)
├─ requirements.txt # Benötigte Python-Pakete
└─ README.md # Projektbeschreibung


### .gitignore

```gitignore
# Byte-compilierte / optimierte / DLL-Dateien
__pycache__/       # Ordner mit automatisch generierten Python-Bytecode-Dateien
*.py[cod]          # Python-Bytecode-Dateien (.pyc, .pyo, .pyd)
*$py.class         # Bytecode-Dateien von Jython

# Jupyter Notebook Checkpoints
*.ipynb            # Temporäre Checkpoint-Dateien von Jupyter

# Umgebungsvariablen
.env               # Enthält sensible API-Keys


### Nutzung
1.API-Key eintragen
Kopiere .env.example zu .env und trage deinen Dog API-Key ein:
DOG_API_KEY="dein_api_key_hier"

2.Abhängigkeiten installieren
pip install -r requirements.txt

3.Skript ausführen
python main.py

4. Ergebnisse
- Daten werden gefiltert nach Rasse
- Ergebnis wird als CSV-Datei gespeichert
- Visualisierung: Balkendiagramm und Liniendiagramm der Hunderassen

Hinweise
- API-Dokumentation: https://thedogapi.com
- Rate-Limits beachten
- Keine sensiblen Daten im Repository speichern