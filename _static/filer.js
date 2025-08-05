export default {
  onClick(event) {
    const el = event.target.closest('[data-filter-tag]');
    if (!el) return;

    event.preventDefault();

    const tag = el.getAttribute('data-filter-tag');
    document.querySelectorAll('.notebook-card').forEach(card => {
      const tags = (card.dataset.tags || '').split(/\s+/);
      card.style.display = (tag === 'all' || tags.includes(tag)) ? 'flex' : 'none';
    });

    document.querySelectorAll('[data-filter-tag]').forEach(btn =>
      btn.classList.toggle('active', btn === el)
    );
  }
};

// Event-Listener aktivieren
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('filter-buttons');
  if (container) {
    container.addEventListener('click', e =>
      import('./filter.js').then(mod => mod.default.onClick(e))
    );
  }
});
