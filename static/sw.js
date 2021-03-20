const staticCacheName = 'site-static-v1';
const assets = [

    '/',
    '../',
    '../app.py',
    '../templates/index.html',
    '../templates/data.html',
    '../uploads',
    '../static/images/xls.png',
    '../static/main.js',
    '../static/manifest.json',
    '../static/sw.js',
    '../static/styles.css',
    'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap',
    'https://kit.fontawesome.com/6daa7dc696.js'

];


// install event
self.addEventListener('install', evt => {
    evt.waitUntil(
        caches.open(staticCacheName).then((cache) => {
            console.log('caching shell assets');
            cache.addAll(assets);
        })
    );
});
// activate event
self.addEventListener('activate', evt => {
    evt.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(keys
                .filter(key => key !== staticCacheName)
                .map(key => caches.delete(key))
            );
        })
    );
});
// When we change the name we could have multiple cache, to avoid that we need to delet the old cache, so with this function we check the key that is our cache naming, if it is different from the actual naming we delete it, in this way we will always have only the last updated cache.
// fetch event
self.addEventListener('fetch', evt => {
    evt.respondWith(
        caches.match(evt.request).then(cacheRes => {
            return cacheRes || fetch(evt.request);
        })
    );
});