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

# {toctree} children extrahieren und immer /notebooks/ davorhängen
toctree_block = re.search(r"```{toctree}.*?\n(.*?)```", content, re.DOTALL)
children = []
if toctree_block:
    for line in toctree_block.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith(":") or line.startswith("#"):
            continue
        # Nur Dateinamen zulassen, kein kompletter Pfad
        file_name = os.path.basename(line)
        child_path = f"production/{COOKBOOK_NAME}/notebooks/{file_name}"
        children.append({"file": child_path})

with open("myst.yml", "r", encoding="utf-8") as f:
    myst_yml = yaml.safe_load(f)

project = myst_yml.get("project", {})
toc = project.get("toc", [])

if not any(entry.get("file") == index_path for entry in toc):
    new_entry = {
        "title": title,
        "children": index_path
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