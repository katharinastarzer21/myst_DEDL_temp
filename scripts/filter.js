document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll('[data-tag]');
  const boxes = document.querySelectorAll('#gallery > div');

  function filter(tag) {
    boxes.forEach(box => {
      const tags = box.dataset.tags.split(' ');
      if (tag === 'all' || tags.includes(tag)) {
        box.classList.remove('hidden');
      } else {
        box.classList.add('hidden');
      }
    });
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => filter(btn.dataset.tag));
  });

  filter('all');
});
