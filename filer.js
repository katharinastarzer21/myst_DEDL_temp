document.addEventListener("DOMContentLoaded", () => {
  const cards = Array.from(document.querySelectorAll('.notebook-card'));
  const allTags = new Set();

  cards.forEach(card => {
    const tags = card.dataset.tags.split(/\s+/);
    tags.forEach(tag => allTags.add(tag));
  });

  const controls = document.getElementById('tag-filter-controls');
  if (!controls) return;

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
        card.style.display = activeTags.length === 0 || visible ? 'block' : 'none';
      });
    });

    controls.appendChild(btn);
  });
});
