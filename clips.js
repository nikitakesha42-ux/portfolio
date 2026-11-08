/* Short silent screen recordings (video.clip).
   - Always have native controls, so anyone can pause and resume (WCAG 2.2.2).
   - Play on their own only while on screen, and never when the visitor
     prefers reduced motion. Once someone pauses a clip, it stays paused. */
(function () {
  var clips = document.querySelectorAll('video.clip');
  if (!clips.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
  clips.forEach(function (v) {
    v.muted = true;
    v.addEventListener('pause', function () { if (!v._auto) v.dataset.userPaused = '1'; v._auto = false; });
    v.addEventListener('play', function () { if (!v._auto) delete v.dataset.userPaused; v._auto = false; });
  });
  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      var v = e.target;
      if (reduce && reduce.matches) return;
      if (e.isIntersecting && e.intersectionRatio >= 0.4) {
        if (v.paused && !v.dataset.userPaused) { v._auto = true; var p = v.play(); if (p && p.catch) p.catch(function () { v._auto = false; }); }
      } else if (!v.paused) { v._auto = true; v.pause(); }
    });
  }, { threshold: [0, 0.4] });
  clips.forEach(function (v) { io.observe(v); });
})();
