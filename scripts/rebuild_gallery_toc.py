import os
import yaml

PROD_DIR = "production"
MYST_YML = "myst.yml"

toc = []
for name in sorted(os.listdir(PROD_DIR)):
    path = os.path.join(PROD_DIR, name)
    index_md = os.path.join(path, "index.md")
    if os.path.isdir(path) and os.path.exists(index_md):
        # Try to get title from first headline, fallback to folder name
        with open(index_md, encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    title = line.lstrip("#").strip()
                    break
            else:
                title = name
        toc.append({
            "title": title,
            "file": f"{PROD_DIR}/{name}/index.md"
        })

myst = {
    "version": 1,
    "project": {"title": "DEDL Cookbook Gallery", "toc": toc},
    "site": {"template": "book-theme"}
}

with open(MYST_YML, "w", encoding="utf-8") as f:
    yaml.dump(myst, f, sort_keys=False, allow_unicode=True)