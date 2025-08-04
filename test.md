# Notebook Gallery

<a href="#" onclick="event.preventDefault(); Array.from(document.querySelectorAll('.notebook-card')).forEach(card => {
  const tags = card.dataset.tags || '';
  card.style.display = tags.includes('HDA') ? 'flex' : 'none';
});">Nur HDA anzeigen</a>

&nbsp;|&nbsp;

<a href="#" onclick="event.preventDefault(); Array.from(document.querySelectorAll('.notebook-card')).forEach(card => {
  card.style.display = 'flex';
});">Alle anzeigen</a>

<hr>

<div class="notebook-card" data-tags="HDA Core API" style="display: flex;">
  📘 Notebook 1 – HDA
</div>
<div class="notebook-card" data-tags="DataCube" style="display: flex;">
  📗 Notebook 2 – DataCube
</div>
