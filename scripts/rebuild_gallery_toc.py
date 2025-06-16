import os
import yaml
import re

COOKBOOK_NAME = os.environ["COOKBOOK_NAME"]
index_path = f"production/{COOKBOOK_NAME}/index.md"

# 1. Titel und {toctree}-Kinder aus index.md holen
with open(index_path, encoding="utf-8") as f:
    content = f.read()

# Titel extrahieren
match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
title = match.group(1).strip() if match else COOKBOOK_NAME

# {toctree} Kinder extrahieren
toctree_block = re.search(r"```{toctree}.*?\n(.*?)```", content, re.DOTALL)
children = []
if toctree_block:
    # Jede nicht-leere Zeile als Kind, mit passendem Pfad
    for line in toctree_block.group(1).splitlines():
        line = line.strip()
        if line:
            # Relativen Pfad zum Cookbook-Ordner aufbauen
            if not line.startswith("production/"):
                file_in_cookbook = f"production/{COOKBOOK_NAME}/{line}"
            else:
                file_in_cookbook = line
            children.append({"file": file_in_cookbook})

# 2. myst.yml laden
with open("myst.yml", "r", encoding="utf-8") as f:
    myst_yml = yaml.safe_load(f)

toc = myst_yml.get("toc", [])
new_entry = {
    "title": title,
    "file": index_path
}
if children:
    new_entry["children"] = children

toc.append(new_entry)
myst_yml["toc"] = toc

# 3. myst.yml zurückschreiben (site-Block & andere Einstellungen bleiben erhalten)
with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)

print(f"✅ Cookbook '{title}' mit {len(children)} children zur myst.yml hinzugefügt!")