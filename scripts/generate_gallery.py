import os
import nbformat
import yaml
from pathlib import Path

GALLERY_PATH = Path("index.html")
ROOT_DIR = Path("production")

HTML_HEADER = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Notebook Gallery</title>
    <link rel="icon" href="img/EUMETSAT-icon.ico">
    <link rel="stylesheet" href="_static/custom.css">
    <script src="filter.js"></script>
    <style>
      .gallery {
        display: flex;
        flex-direction: column;
        gap: 20px;
        max-width: 1000px;
        margin: auto;
        padding: 40px 20px;
      }
      .notebook-card {
        display: flex;
        align-items: flex-start;
        border: 1px solid #cddff1;
        border-radius: 6px;
        padding: 14px 20px;
        background-color: #f9fbfe;
        box-shadow: 1px 1px 4px #dfeaf5;
      }
      .notebook-card img {
        width: 100px;
        height: 80px;
        object-fit: contain;
        border-radius: 6px;
        margin-right: 32px;
      }
      .notebook-card .tags span {
        display: inline-block;
        background-color: #e6f0fa;
        border-radius: 10px;
        padding: 3px 10px;
        margin: 2px;
        font-size: 0.75em;
      }
    </style>
  </head>
  <body>
    <h1 style="text-align:center">DEDL Notebook Gallery</h1>
    <div id="filter-bar" style="text-align:center; margin-bottom: 20px;">
      <button class="filter-button" onclick="filterNotebooks('all')">All</button>
    </div>
    <div class="gallery">
'''

HTML_FOOTER = '''
    </div>
  </body>
</html>
'''

def extract_metadata_from_notebook(nb_path):
    try:
        nb = nbformat.read(nb_path, as_version=4)
        first_cell = nb.cells[0]
        if first_cell.cell_type == "markdown" and first_cell.source.strip().startswith("---"):
            parts = first_cell.source.strip().split('---')
            if len(parts) >= 3:
                yaml_content = parts[1]
                metadata = yaml.safe_load(yaml_content)
                metadata["file"] = str(nb_path).replace("\\", "/")
                return metadata
    except Exception as e:
        print(f"[WARN] {nb_path}: {e}")
    return None

def build_html_card(md):
    tags_html = "".join(f"<span>{tag}</span>" for tag in md.get("tags", []))
    tags_data = " ".join(md.get("tags", []))
    thumbnail = md.get("thumbnail", "img/thumbs/default.png")
    author_html = f"<p class='meta'>✍️ {md.get('author', '')} | 🪪 {md.get('license', '')}</p>" if md.get("author") else ""
    return f'''
      <div class="notebook-card" data-tags="{tags_data}">
        <img src="{thumbnail}" alt="Notebook Thumbnail">
        <div>
          <strong>{md.get('title', 'Untitled')}</strong><br>
          {md.get('description', '')}
          {author_html}
          <div class="tags">{tags_html}</div>
          <a href="{md['file'].replace('.ipynb', '.html')}" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
        </div>
      </div>
    '''

def main():
    print("[INFO] Scanning notebooks...")
    all_metadata = []
    all_tags = set()
    for path in ROOT_DIR.rglob("*.ipynb"):
        md = extract_metadata_from_notebook(path)
        if md:
            all_metadata.append(md)
            all_tags.update(md.get("tags", []))

    print(f"[INFO] {len(all_metadata)} notebooks with metadata found.")

    with open(GALLERY_PATH, "w", encoding="utf-8") as f:
        f.write(HTML_HEADER)

        # Add buttons dynamically
        for tag in sorted(all_tags):
            f.write(f'<button class="filter-button" onclick="filterNotebooks(\'{tag}\')">{tag}</button>\n')

        for md in all_metadata:
            f.write(build_html_card(md))

        f.write(HTML_FOOTER)

    print(f"[INFO] Gallery written to: {GALLERY_PATH}")

if __name__ == "__main__":
    main()
