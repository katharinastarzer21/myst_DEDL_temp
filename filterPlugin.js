export default {
  onPageLoad() {
    const buttons = document.querySelectorAll('.tag-button');
    const items = document.querySelectorAll('.gallery-item');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const tag = btn.dataset.tag;

        items.forEach(item => {
          const tags = item.dataset.tags.split(' ');
          if (tag === 'all' || tags.includes(tag)) {
            item.style.display = 'block';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }
};