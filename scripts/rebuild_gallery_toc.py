import os
import yaml
import re

COOKBOOK_NAME = os.environ["COOKBOOK_NAME"]
index_path = f"production/{COOKBOOK_NAME}/index.md"

with open(index_path, encoding="utf-8") as f:
    content = f.read()

# Titel extrahieren
match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
title = match.group(1).strip() if match else COOKBOOK_NAME

# {toctree} children extrahieren
toctree_block = re.search(r"```{toctree}.*?\n(.*?)```", content, re.DOTALL)
children = []
if toctree_block:
    # Alle Zeilen im Block holen
    for line in toctree_block.group(1).splitlines():
        line = line.strip()
        # Nur Zeilen, die wie ein (Notebook-)Pfad aussehen (keine Optionen, kein :maxdepth:)
        if line and not line.startswith(":") and not line.startswith("#"):
            # Optional: Nur .md oder .ipynb aufnehmen
            if line.endswith(".md") or line.endswith(".ipynb"):
                children.append({"file": f"production/{COOKBOOK_NAME}/{line}"})

# myst.yml laden
with open("myst.yml", "r", encoding="utf-8") as f:
    myst_yml = yaml.safe_load(f)

project = myst_yml.get("project", {})
toc = project.get("toc", [])

if not any(entry.get("file") == index_path for entry in toc):
    new_entry = {
        "title": title,
        "file": index_path
    }
    if children:
        new_entry["children"] = children
    toc.append(new_entry)
    project["toc"] = toc
    myst_yml["project"] = project

    with open("myst.yml", "w", encoding="utf-8") as f:
        yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Cookbook '{title}' der myst.yml (project.toc) hinzugefügt!")
else:
    print(f"ℹ️ Cookbook '{title}' ist bereits im TOC.")