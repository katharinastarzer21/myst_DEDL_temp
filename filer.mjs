export default {
  onClick(event) {
    const el = event.target.closest('[data-filter-tag]');
    if (!el) return;

    const tag = el.getAttribute('data-filter-tag');

    document.querySelectorAll('.notebook-card').forEach(card => {
      const tags = (card.dataset.tags || '').split(',').map(t => t.trim());
      card.style.display = (tag === 'all' || tags.includes(tag)) ? 'flex' : 'none';
    });
  }
};
