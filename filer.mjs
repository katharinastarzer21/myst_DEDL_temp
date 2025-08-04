export default {
  onClick(event) {
    const el = event.target;
    if (!el.matches('[data-filter-tag]')) return;

    const tag = el.getAttribute('data-filter-tag');
    document.querySelectorAll('.card').forEach(card => {
      const tags = (card.dataset.tags || '').split(',').map(t => t.trim());
      card.style.display = (tag === 'all' || tags.includes(tag)) ? 'flex' : 'none';
    });
  }
};
