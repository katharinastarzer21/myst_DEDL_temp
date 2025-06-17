import os
import yaml

COOKBOOK_NAME = os.environ["COOKBOOK_TITLE"]
ROOT_PATH = os.environ["ROOT_PATH"]

cookbook_dir = f"production/{ROOT_PATH}"
readme_file = f"{cookbook_dir}/README.md"
gallery_file = f"{cookbook_dir}/gallery.md"
notebooks_dir = f"{cookbook_dir}/notebooks"

notebook_files = []
if os.path.isdir(notebooks_dir):
    for f in sorted(os.listdir(notebooks_dir)):
        if f.endswith(".ipynb"):
            notebook_files.append({"file": f"{notebooks_dir}/{f}"})

title = COOKBOOK_NAME

with open("myst.yml", "r", encoding="utf-8") as f:
    myst_yml = yaml.safe_load(f)

project = myst_yml.get("project", {})
toc = project.get("toc", [])

if not any(entry.get("title") == title for entry in toc):
   
    new_entry = {
        "title": title,
        "children": [
            {"file": readme_file},
            {
                "file": gallery_file,
                "children": notebook_files
            }
        ]
    }
    toc.append(new_entry)
    project["toc"] = toc
    myst_yml["project"] = project

    with open("myst.yml", "w", encoding="utf-8") as f:
        yaml.dump(myst_yml, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Cookbook '{title}' als Section korrekt in myst.yml eingetragen!")
else:
    print(f"ℹ️ Cookbook '{title}' ist bereits im TOC.")