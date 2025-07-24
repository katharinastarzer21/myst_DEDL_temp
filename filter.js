function filterNotebooks(tag) {
  document.querySelectorAll('.notebook-card').forEach(card => {
    const tags = card.dataset.tags || '';
    card.style.display = (tag === 'all' || tags.includes(tag)) ? 'flex' : 'none';
  });
}
