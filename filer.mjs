export default {
  onClick(event) {
    const button = event.target;

    if (!button.matches('[data-filter-tag]')) return;

    const tag = button.getAttribute('data-filter-tag');

    // Karten filtern
    document.querySelectorAll('.notebook-card').forEach(card => {
      const tags = card.dataset.tags || '';
      if (tag === 'all' || tags.includes(tag)) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }
};
