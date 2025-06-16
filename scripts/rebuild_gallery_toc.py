import yaml
import os
import re

COOKBOOK_NAME = os.environ["COOKBOOK_NAME"]  # Wird vom Workflow gesetzt
index_path = f"production/{COOKBOOK_NAME}/index.md"

# 1. Titel aus index.md holen
with open(index_path, encoding="utf-8") as f:
    content = f.read()
match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
if match:
    title = match.group(1).strip()
else:
    title = COOKBOOK_NAME  # Fallback

# 2. myst.yml laden
with open("myst.yml", "r", encoding="utf-8") as f:
    myst_yml = yaml.safe_load(f)
toc = myst_yml.get("toc", [])
toc.append({
    "title": title,
    "file": index_path
})
myst_yml["toc"] = toc

# 3. myst.yml zurückschreiben
with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)

print(f"✅ Cookbook '{title}' zur myst.yml hinzugefügt!")