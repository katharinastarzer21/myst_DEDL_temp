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

    document.querySelectorAll('.filter-button').forEach(btn =>
      btn.classList.toggle('active', btn === el)
    );
  }
};

document.addEventListener('DOMContentLoaded', () => {
  document
    .getElementById('filter-buttons')
    ?.addEventListener('click', e => import('./filter.js').then(mod => mod.default.onClick(e)));
});
