import os
import yaml

PROD_DIR = "production"
MYST_YML = "myst.yml"

toc = []
for name in sorted(os.listdir(PROD_DIR)):
    path = os.path.join(PROD_DIR, name)
    if not os.path.isdir(path):
        continue

    # Find index.md or README.md as the main file
    main_file = None
    for fname in ("index.md", "README.md"):
        if os.path.exists(os.path.join(path, fname)):
            main_file = fname
            break
    if not main_file:
        continue  # skip if no main file

    # Title from first headline, fallback to folder name
    with open(os.path.join(path, main_file), encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("#"):
                title = line.lstrip("#").strip()
                break
        else:
            title = name

    # Find children: all .md or .ipynb except main_file
    children = []
    for fname in sorted(os.listdir(path)):
        if fname == main_file:
            continue
        if fname.endswith((".md", ".ipynb")):
            children.append({"file": f"{PROD_DIR}/{name}/{fname}"})

    toc.append({
        "title": title,
        "file": f"{PROD_DIR}/{name}/{main_file}",
        "children": children if children else None
    })

# Remove empty children (optional, keeps YAML clean)
for entry in toc:
    if entry.get("children") is None:
        del entry["children"]

myst = {
    "version": 1,
    "project": {"title": "DEDL notebook gallery", "toc": toc},
    "site": {
        "template": "book-theme",
        "options": {
            "style": "./_static/custom.css",
            "favicon": "./img/EUMETSAT-icon.ico",
            "logo": "./img/logo_bar.png"
        }
    }
}

with open(MYST_YML, "w", encoding="utf-8") as f:
    yaml.dump(myst, f, sort_keys=False, allow_unicode=True)