import os
import yaml
import re

COOKBOOK_NAME = os.environ["COOKBOOK_NAME"]
index_path = f"production/{COOKBOOK_NAME}/index.md"

# 1. Titel & {toctree}-Kinder aus index.md holen
with open(index_path, encoding="utf-8") as f:
    content = f.read()

# Titel extrahieren
match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
title = match.group(1).strip() if match else COOKBOOK_NAME

# {toctree} children extrahieren
toctree = re.search(r"```{toctree}.*?\n(.*?)```", content, re.DOTALL)
children = []
if toctree:
    for line in toctree.group(1).splitlines():
        line = line.strip()
        if line:
            children.append({"file": f"production/{COOKBOOK_NAME}/{line}"})

# 2. myst.yml laden
with open("myst.yml", "r", encoding="utf-8") as f:
    myst_yml = yaml.safe_load(f)

toc = myst_yml.get("toc", [])
# Prüfe, ob Eintrag schon existiert (optional, falls keine Dopplung gewünscht)
if not any(entry.get("file") == index_path for entry in toc):
    new_entry = {
        "title": title,
        "file": index_path
    }
    if children:
        new_entry["children"] = children
    toc.append(new_entry)
    myst_yml["toc"] = toc

    # 3. myst.yml zurückschreiben
    with open("myst.yml", "w", encoding="utf-8") as f:
        yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Cookbook '{title}' der myst.yml hinzugefügt!")
else:
    print(f"ℹ️ Cookbook '{title}' ist bereits im TOC.")
