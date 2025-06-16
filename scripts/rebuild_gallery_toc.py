import os

def update_toctree(cookbook_path, notebooks_subdir="notebooks"):
    index_path = os.path.join(cookbook_path, "index.md")
    if not os.path.exists(index_path):
        index_path = os.path.join(cookbook_path, "README.md")
        if not os.path.exists(index_path):
            raise FileNotFoundError("No index.md or README.md found in " + cookbook_path)

    # Finde alle ipynb/md im notebooks_subdir
    notebooks_path = os.path.join(cookbook_path, notebooks_subdir)
    files = []
    if os.path.exists(notebooks_path):
        for fname in sorted(os.listdir(notebooks_path)):
            if fname.endswith((".ipynb", ".md")):
                files.append(f"{notebooks_subdir}/{fname}")

    # Baue neuen toctree-Block
    toctree_block = "```{toctree}\n:maxdepth: 2\n\n"
    for f in files:
        toctree_block += f"{f}\n"
    toctree_block += "```\n"

    # Lies die alte index.md ein
    with open(index_path, encoding="utf-8") as f:
        content = f.read()

    # Ersetze alten toctree (oder hänge neuen an)
    import re
    new_content, n = re.subn(
        r"```{toctree}.*?```", toctree_block, content, flags=re.DOTALL
    )
    if n == 0:
        # Kein toctree gefunden, hänge an
        new_content = content.strip() + "\n\n" + toctree_block

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)

# Beispiel-Aufruf:
# update_toctree("production/MEIN_COOKBOOK")