# Notebook Gallery

<div id="tag-filter-controls"></div>

<!-- Sample notebook cards -->
<div class="notebook-card" data-tags="DataCube Digital Twin">
  <strong>Notebook 1</strong><br>
  Tags: DataCube, Digital Twin<br>
  <a href="#">View Notebook</a>
</div>

<div class="notebook-card" data-tags="STAC HDA">
  <strong>Notebook 2</strong><br>
  Tags: STAC, HDA<br>
  <a href="#">View Notebook</a>
</div>

<div class="notebook-card" data-tags="HDA Core API">
  <strong>Notebook 3</strong><br>
  Tags: HDA, Core API<br>
  <a href="#">View Notebook</a>
</div>

<!-- JavaScript filter logic -->
<script>
document.addEventListener("DOMContentLoaded", () => {
  const cards = Array.from(document.querySelectorAll('.notebook-card'));
  const allTags = new Set();

  cards.forEach(card => {
    const tags = card.dataset.tags.split(/\s+/);
    tags.forEach(tag => allTags.add(tag));
  });

  const controls = document.getElementById('tag-filter-controls');
  allTags.forEach(tag => {
    const btn = document.createElement('button');
    btn.textContent = tag;
    btn.style.margin = '0 6px 6px 0';
    btn.style.padding = '4px 10px';
    btn.style.cursor = 'pointer';
    btn.dataset.tag = tag;

    btn.addEventListener('click', () => {
      const active = btn.classList.toggle('active');
      const activeTags = Array.from(controls.querySelectorAll('.active')).map(b => b.dataset.tag);

      cards.forEach(card => {
        const cardTags = card.dataset.tags.split(/\s+/);
        const visible = activeTags.every(t => cardTags.includes(t));
        card.style.display = activeTags.length === 0 || visible ? 'flex' : 'none';
      });
    });

    controls.appendChild(btn);
  });
});
</script>

<style>
.notebook-card {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  display: flex;
}
#tag-filter-controls {
  margin-bottom: 12px;
}
#tag-filter-controls button.active {
  background-color: #1d70b8;
  color: white;
  border: none;
}
</style>
