/* "Say hi" cards: copy-email buttons that confirm in words (EN/NO). */
document.addEventListener('click', async (e) => {
  const btn = e.target.closest('.hi-copy');
  if (!btn) return;
  const text = btn.dataset.copy;
  try { await navigator.clipboard.writeText(text); }
  catch {
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.left = '-9999px';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); } catch {}
    ta.remove();
  }
  const no = document.documentElement.lang === 'nb';
  const label = btn.querySelector('.hi-copy-label');
  const prev = label.textContent;
  label.textContent = no ? 'Kopiert ✓' : 'Copied ✓';
  btn.classList.add('is-done');
  let live = btn.parentElement.querySelector('.hi-live');
  if (live) live.textContent = no ? 'E-postadressen er kopiert' : 'Email address copied';
  setTimeout(() => { label.textContent = no ? (btn.dataset.labelNo || prev) : (btn.dataset.labelEn || prev); btn.classList.remove('is-done'); }, 1800);
});
