import os
import json


# This script take a Folder with json files and make an INTL txt followed by this format:
# [Name of the json file]
# line from the json file
# translated version of the line
# ...........



def extract_strings(obj):
    strings = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str):
                v = v.replace('\n', '\\n')
                v = v.replace('\t', '\\t')
                strings.append(f"{v}")
                strings.append(f"{v}")
            else:
                strings.extend(extract_strings(v))
    elif isinstance(obj, list):
        for item in obj:
            strings.extend(extract_strings(item))
    return strings

def json2INTL(folder_path, output_file="output.txt"):
    with open(output_file, "w", encoding="utf-8") as out:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".json"):
                path = os.path.join(folder_path, filename)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    out.write(f"[{os.path.splitext(filename)[0]}]\n")
                    for line in extract_strings(data):
                        out.write(line + "\n")
                    out.write("\n")
                except Exception as e:
                    print(f"Erreur sur {filename}: {e}")

if __name__ == "__main__":
    dossier = input("Folder containing the JSON files:")
    json2INTL(dossier)
    print("Output.txt file created.")
