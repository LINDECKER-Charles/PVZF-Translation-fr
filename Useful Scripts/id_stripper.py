import os
import json
import csv

# === SET WORKING DIRECTORY TO SCRIPT LOCATION ===
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# === SET LANGUAGE ===
language = "English"

# === DEFINE PATHS ===
base_dir = os.path.abspath(os.path.join("..", "PvZ_Fusion_Translator", "Localization", language, "Almanac"))
zombies_json = os.path.join(base_dir, "ZombieStringsTranslate.json")
plants_json = os.path.join(base_dir, "LawnStringsTranslate.json")
zombies_csv = os.path.join(base_dir, "zombies_id.csv")
plants_csv = os.path.join(base_dir, "plants_id.csv")

# === VERIFY TARGET DIRECTORY EXISTS ===
if not os.path.exists(base_dir):
    print(f"❌ Target Almanac folder not found:\n{base_dir}")
    exit()

print(f"📂 Working in: {base_dir}\n")

# === FUNCTION: EXTRACT TO CSV ===
def extract_to_csv(json_path, csv_path, list_key, id_key, name_key):
    if not os.path.exists(json_path):
        print(f"⚠️ {os.path.basename(json_path)} not found — skipping.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get(list_key, [])
    # Sort by ID, but store as (name, id)
    rows = sorted([(entry.get(name_key, ""), entry.get(id_key, "")) for entry in entries], key=lambda x: x[1])

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "id"])
        writer.writerows(rows)

    print(f"✅ Extracted {len(rows)} {list_key} → {os.path.basename(csv_path)}")

# === RUN EXTRACTIONS ===
extract_to_csv(zombies_json, zombies_csv, "zombies", "theZombieType", "name")
extract_to_csv(plants_json, plants_csv, "plants", "seedType", "name")
