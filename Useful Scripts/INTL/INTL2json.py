import os
import json


# This script take an INTL txt followed by this format:
# [Name of the json file]
# line from the json file
# translated version of the line
# ...........
# And make the translated json thank to the original one

def load_translations(txt_path):
    translations = {}
    current_file = None
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("[") and line.endswith("]"):
            current_file = line[1:-1]
            translations[current_file] = {}
            i += 1
            continue
        if current_file and i + 1 < len(lines):
            src = lines[i]
            dst = lines[i + 1]
            translations[current_file][src] = dst
            i += 2
        else:
            i += 1
    return translations

def replace_strings(obj, mapping):
    if isinstance(obj, dict):
        new = {}
        for k, v in obj.items():
            if isinstance(v, str):
                val = v.replace('\n', '\\n').replace('\t', '\\t')
                if val in mapping:
                    new_val = mapping[val].replace('\\n', '\n').replace('\\t', '\t')
                    new[k] = new_val
                else:
                    new[k] = v
            else:
                new[k] = replace_strings(v, mapping)
        return new
    elif isinstance(obj, list):
        return [replace_strings(item, mapping) for item in obj]
    return obj

def INTL2json(input_folder, txt_file, output_folder="output_json"):
    os.makedirs(output_folder, exist_ok=True)
    translations = load_translations(txt_file)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".json"):
            name = os.path.splitext(filename)[0]
            if name in translations:
                with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                    data = json.load(f)
                new_data = replace_strings(data, translations[name])
                with open(os.path.join(output_folder, filename), "w", encoding="utf-8") as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    dossier = input("Folder containing the original JSON files:")
    txt = input("Translation .txt file:")
    INTL2json(dossier, txt)
    print("Translated JSON files generated in the 'output_json' folder.")
