import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# -----------------------------
# API-Key aus .env laden
# -----------------------------
load_dotenv()
API_KEY = os.getenv("DOG_API_KEY")

if not API_KEY:
    raise ValueError("Bitte lege einen API-Key in der .env-Datei an: DOG_API_KEY=dein_api_key")

# -----------------------------
# 1) Datenabruf
# -----------------------------
url = "https://api.thedogapi.com/v1/breeds"
headers = {"x-api-key": API_KEY}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Fehler beim Abruf: {response.status_code}")

data = response.json()

# -----------------------------
# 2) Erste Übersicht
# -----------------------------
print(f"Anzahl der Einträge: {len(data)}\n")
print("Beispiel-Einträge:")
for entry in data[:3]:
    print(entry)
print("\nVerfügbare Keys:", list(data[0].keys()))

# -----------------------------
# 3) Filterung & Auswahl
# -----------------------------
# Wir wählen id, name, temperament
df = pd.DataFrame(data)
df_filtered = df[['id', 'name', 'temperament']]

# Beispiel-Filter: alle Rassen mit "Bulldog"
filter_term = "Bulldog"
df_filtered = df_filtered[df_filtered['name'].str.contains(filter_term, case=False)]

print("\nGefilterte Ergebnisse:")
print(df_filtered.head())

# -----------------------------
# 4) Export
# -----------------------------
os.makedirs("results", exist_ok=True)
df_filtered.to_csv("results/dog_breeds.csv", index=False, encoding="utf-8")
print("\nCSV exportiert: results/dog_breeds.csv")

# -----------------------------
# 5) Visualisierung
# -----------------------------
# Länge der Namen als Beispiel
df_filtered['name_length'] = df_filtered['name'].apply(len)

# Balkendiagramm
plt.figure(figsize=(8, 4))
plt.bar(df_filtered['name'], df_filtered['name_length'])
plt.xticks(rotation=45, ha='right')
plt.title("Länge der Hundenamen (Bar Chart)")
plt.tight_layout()
plt.savefig("results/name_length_bar.png")
plt.close()

# Liniendiagramm
plt.figure(figsize=(8, 4))
plt.plot(df_filtered['name'], df_filtered['name_length'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("Länge der Hundenamen (Line Chart)")
plt.tight_layout()
plt.savefig("results/name_length_line.png")
plt.close()

print("Diagramme gespeichert: results/name_length_bar.png & results/name_length_line.png")