import nbformat
import sys
import yaml

def extract_yaml_from_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            content = cell.source.strip()
            if content.startswith('---') and content.count('---') >= 2:
                parts = content.split('---')
                yaml_block = parts[1]
                try:
                    return yaml.safe_load(yaml_block)
                except yaml.YAMLError as e:
                    print(f"YAML parsing error in {notebook_path}: {e}")
                    return None
            break
    return None


def generate_html_card(meta, notebook_path):
    title = meta.get("title", "Untitled")
    subtitle = meta.get("subtitle", "")
    author = meta.get("author", "")
    tags = meta.get("tags", [])
    thumbnail = meta.get("thumbnail", "")
    href = notebook_path.replace("\\", "/")  # ensure POSIX-style path

    tags_html = ''.join(f'<span class="tag">{tag}</span>' for tag in tags)

    html = f'''
<div class="notebook-card" data-tags="{' '.join(tags)}" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="{thumbnail}" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>{title}</strong><br>
    {subtitle}
    <div style="margin: 6px 0;">
      {tags_html}
    </div>
    <a href="{href}" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
'''
    return html.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_notebook_card.py <notebook_path>")
        sys.exit(1)

    notebook_path = sys.argv[1]

    meta = extract_yaml_from_notebook(notebook_path)
    if meta is None:
        print("No YAML metadata found in the first Markdown cell.")
        sys.exit(1)

    html_card = generate_html_card(meta, notebook_path)

    output_path = "notebook_card.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_card)

    print(f"HTML card written to {output_path}")
