import os
import yaml

# Lade bestehendes myst.yml, falls vorhanden
if os.path.exists("myst.yml"):
    with open("myst.yml", "r", encoding="utf-8") as f:
        myst_yml = yaml.safe_load(f)
    toc = myst_yml.get("toc", [])
    # Build set of existing files for quick lookup
    existing_files = {entry["file"] for entry in toc if "file" in entry}
else:
    myst_yml = {
        "config": {"version": 2},
        "root": "index.md",
        "toc": []
    }
    toc = []
    existing_files = set()

# Alle Ordner in production/ prüfen
for cook_name in sorted(os.listdir("production")):
    cook_path = os.path.join("production", cook_name)
    index_md = os.path.join(cook_path, "index.md")
    toc_file = f"production/{cook_name}/index.md"
    if os.path.isdir(cook_path) and os.path.exists(index_md):
        if toc_file not in existing_files:
            toc.append({
                "title": cook_name,
                "file": toc_file
            })
            print(f"➕ Neuer Eintrag: {toc_file}")
        else:
            print(f"✔️ Bereits vorhanden: {toc_file}")

# Aktuelles myst_yml aktualisieren
myst_yml["toc"] = toc

# Schreibe myst.yml zurück
with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)

print(f"✅ myst.yml aktualisiert. ({len(toc)} Einträge)")