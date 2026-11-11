/* "Off screen" photo wall: shuffle the polaroids, and make the strip keyboard-scrollable when it scrolls (phones). */
(function () {
  const wall = document.querySelector('.offscreen-wall');
  const btn = document.querySelector('.os-shuffle');
  if (!wall || !btn) return;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  btn.hidden = false;

  btn.addEventListener('click', () => {
    const items = [...wall.children];
    const first = new Map(items.map((el) => [el, el.getBoundingClientRect()]));
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [items[i], items[j]] = [items[j], items[i]];
    }
    items.forEach((el) => {
      el.style.setProperty('--r', (Math.random() * 9 - 4.5).toFixed(1) + 'deg');
      el.style.setProperty('--y', Math.round(Math.random() * 14 - 4) + 'px');
      wall.appendChild(el);
    });
    if (reduce.matches || !wall.animate) return;
    items.forEach((el, i) => {
      const a = first.get(el), b = el.getBoundingClientRect();
      const dx = a.left - b.left, dy = a.top - b.top;
      if (!dx && !dy) return;
      el.animate([{ translate: dx + 'px ' + dy + 'px' }, { translate: '0 0' }],
        { duration: 560, delay: i * 30, easing: 'cubic-bezier(.2,.8,.2,1.1)', fill: 'backwards' });
    });
  });

  // On phones the wall is a sideways strip: let keyboard users focus and scroll it.
  const sync = () => {
    const scrolls = getComputedStyle(wall).overflowX === 'auto' && wall.scrollWidth > wall.clientWidth + 2;
    if (scrolls) wall.setAttribute('tabindex', '0');
    else wall.removeAttribute('tabindex');
  };
  sync();
  window.addEventListener('resize', sync);
})();
