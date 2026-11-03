/* Prompt Library — service worker
 *
 * Scope: only the Prompt Library app and its direct dependencies. Everything
 * else on the portfolio (case pages, index, etc.) falls through to the network
 * as if no service worker were installed.
 *
 * Strategy:
 *  - app shell (HTML, manifest, icons, Google Fonts):  cache-first with background revalidate
 *  - prompts.json (source of truth):                    network-first with cache fallback
 *  - anything else:                                     bypass
 */
const VERSION    = 'pl-sw-v1';
const APP_CACHE  = `pl-app-${VERSION}`;
const DATA_CACHE = `pl-data-${VERSION}`;

const APP_SHELL = [
  './prompt-library-app.html',
  './prompt-library.webmanifest',
  './assets/pl-pwa/icon-192.png',
  './assets/pl-pwa/icon-512.png',
  './assets/pl-pwa/icon-maskable-512.png',
];
const DATA_URL = './assets/prompts.json';

/* INSTALL — warm the app shell and the data cache so first offline load works. */
self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const [appCache, dataCache] = await Promise.all([
      caches.open(APP_CACHE),
      caches.open(DATA_CACHE),
    ]);
    await Promise.all([
      appCache.addAll(APP_SHELL).catch(() => {}),       // don't fail install if a file is missing
      fetch(DATA_URL, { cache: 'no-store' })
        .then(r => r.ok && dataCache.put(DATA_URL, r.clone()))
        .catch(() => {}),
    ]);
    self.skipWaiting();
  })());
});

/* ACTIVATE — clean up old caches when the SW version bumps. */
self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(
      keys.filter(k => k.startsWith('pl-') && !k.endsWith(VERSION))
          .map(k => caches.delete(k))
    );
    await self.clients.claim();
  })());
});

/* FETCH — targeted, scope-limited routing. */
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) {
    // Google Fonts etc. — let the browser handle it (HTTP cache is fine).
    return;
  }

  const path = url.pathname;

  // prompts.json → network-first, cache fallback
  if (path.endsWith('/assets/prompts.json')) {
    event.respondWith(networkFirst(req));
    return;
  }
  // app shell → cache-first with background revalidate
  if (
    path.endsWith('/prompt-library-app.html') ||
    path.endsWith('/prompt-library.webmanifest') ||
    path.includes('/assets/pl-pwa/')
  ) {
    event.respondWith(cacheFirst(req));
    return;
  }
  // Anything else on the portfolio — bypass, no SW involvement.
});

async function networkFirst(request) {
  const cache = await caches.open(DATA_CACHE);
  try {
    const fresh = await fetch(request, { cache: 'no-store' });
    if (fresh.ok) cache.put(request, fresh.clone());
    return fresh;
  } catch {
    const cached = await cache.match(request);
    if (cached) return cached;
    throw new Error('offline and no cached copy');
  }
}

async function cacheFirst(request) {
  const cache = await caches.open(APP_CACHE);
  const cached = await cache.match(request);
  const networkFetch = fetch(request).then(resp => {
    if (resp.ok) cache.put(request, resp.clone());
    return resp;
  }).catch(() => null);
  return cached || (await networkFetch) || new Response('offline', { status: 503 });
}
