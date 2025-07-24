import os
import nbformat
import yaml
from pathlib import Path

GALLERY_PATH = Path("gallery_fragment.html")
ROOT_DIR = Path("production")

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
    tags_html = "".join(f"<span class='tag'>{tag}</span>" for tag in md.get("tags", []))
    author_html = f"<p class='meta'>✍️ {md.get('author', '')} | 🪪 {md.get('license', '')}</p>" if md.get("author") else ""
    return f"""
    <div class="card notebook-card" data-tags="{','.join(md.get('tags', []))}">
        <img src="{md.get('thumbnail', 'img/thumbs/default.png')}" alt="thumbnail">
        <div class="card-text">
            <h3><a href="{md['file'].replace('.ipynb', '.html')}">{md.get('title', 'Untitled')}</a></h3>
            <p>{md.get('description', '')}</p>
            {author_html}
            <div class="tags">{tags_html}</div>
        </div>
    </div>
    """

def generate_filter_buttons(unique_tags):
    buttons_html = '<div id="filter-bar">\n'
    buttons_html += '  <button onclick="filterNotebooks(\'all\')">All</button>\n'
    for tag in sorted(unique_tags):
        buttons_html += f'  <button onclick="filterNotebooks(\'{tag}\')">{tag}</button>\n'
    buttons_html += '</div>\n'
    return buttons_html

def generate_filter_script():
    return """
<script>
function filterNotebooks(tag) {
  const cards = document.querySelectorAll('.notebook-card');
  cards.forEach(card => {
    const tags = card.dataset.tags.split(',');
    if (tag === 'all' || tags.includes(tag)) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>
"""

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
    print(f"[INFO] Unique tags: {sorted(all_tags)}")

    with open(GALLERY_PATH, "w", encoding="utf-8") as f:
        f.write(generate_filter_buttons(all_tags))
        f.write('<div class="gallery">\n')
        for md in all_metadata:
            f.write(build_html_card(md))
        f.write('\n</div>\n')
        f.write(generate_filter_script())

    print(f"[INFO] Gallery written to: {GALLERY_PATH}")

if __name__ == "__main__":
    main()
