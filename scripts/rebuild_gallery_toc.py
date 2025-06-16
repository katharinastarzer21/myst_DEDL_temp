import os
import yaml

toc = []

# Alle Ordner in production/ durchgehen
for cook_name in sorted(os.listdir("production")):
    cook_path = os.path.join("production", cook_name)
    index_md = os.path.join(cook_path, "index.md")
    if os.path.isdir(cook_path) and os.path.exists(index_md):
        toc.append({
            "title": cook_name,
            "file": f"production/{cook_name}/index.md"
        })
        print(f"✅ Cookbook erkannt: {cook_name}")
    else:
        print(f"⚠️ Überspringe {cook_name}, kein index.md gefunden.")

# Schreibe myst.yml
myst_yml = {
    "root": "index.md",
    "toc": toc
}

with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)
print(f"✅ myst.yml mit {len(toc)} Cookbooks geschrieben!")