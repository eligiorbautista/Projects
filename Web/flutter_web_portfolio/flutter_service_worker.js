'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"assets/AssetManifest.bin": "b61324ff8006d46eeef406ccfbf13a14",
"assets/AssetManifest.json": "32bffccbc53a5a38f7219a71c37d1ebe",
"assets/assets/icons/facebook.png": "d4e6e19c3754e67eb655b9a82f5e85cc",
"assets/assets/icons/github.png": "2f169363a397e8d8b8923a427d180966",
"assets/assets/icons/instagram.png": "fae2d2ffae24c3e0ef0c4d1a91fac74e",
"assets/assets/icons/portfolio.png": "c20cd8c80a4a1a6016ad6126370bfaaf",
"assets/assets/images/computer.jpg": "12cd120d910034b9471e1aadb17b3dde",
"assets/assets/images/desktop.jpg": "c3b5b0fd41ca1bb66c526029970b11fc",
"assets/assets/images/eli.jpg": "8ba023386d5809dfaa300f3fbc3029e1",
"assets/assets/images/eli0.jpg": "88dc9b356e34d6b1ed54c272d9b1c262",
"assets/assets/images/eli10.jpg": "b9bb8e08ad8cf85a5376b279d2e605bc",
"assets/assets/images/eli11.jpg": "ad347738d76f6a6809b4f36cee8b0e5f",
"assets/assets/images/eli2.jpg": "95311637b73c71971ef6627a19cc0570",
"assets/assets/images/eli3.jpg": "fcb86a9a75614fcd90dfb0c607b2c070",
"assets/assets/images/eli4.jpg": "8012369c7c99832ab18a5e416c15caef",
"assets/assets/images/eli5.jpg": "fcb86a9a75614fcd90dfb0c607b2c070",
"assets/assets/images/eli6.jpg": "5f7143776d947f80bcd8d7685971c633",
"assets/assets/images/eli7.jpg": "05400650c055f5a11f677853cc95e15a",
"assets/assets/images/eli8.jpg": "ab87e6d97cc92b557b5dc7760dbbf7d3",
"assets/assets/images/eli9.jpg": "c684a63c2cc212ab526e588e97efd02f",
"assets/assets/images/laptop.jpg": "975e7b16721683efc3cd1e8ca880bdb8",
"assets/assets/images/received_710150807507074.jpeg": "91051d263a214268f3f4c2fa2de17ed2",
"assets/assets/images/repair.png": "4bd99eea961b3aabe243ef3f17be8ae5",
"assets/assets/images/repair2.png": "df8d74b298e05205c9f2878ddece83d2",
"assets/assets/images/repair3.png": "d714de3aeef84321ad49624669d288e0",
"assets/assets/images/repair4.png": "b6cc8ab65a7895a779a4051c00f6c8f9",
"assets/assets/images/repair5.png": "85673fbe0bcf3a1494a0ae3c456be7e4",
"assets/assets/images/repair6.png": "3c95ef1ef6378d17b8a0e46e35329690",
"assets/assets/images/repair7.jpg": "7b9f51e54a1fa61a35ec6c65db4b4fa4",
"assets/assets/images/repair8.png": "241fc36257fea76cc041d2747a92ada3",
"assets/assets/images/sis-1.png": "0c0d04fb41631efdc56ca9f1e38c8313",
"assets/assets/images/sis-2.png": "651072c34ce3c2c3eeae861f4ec4a1a7",
"assets/assets/images/story_trim.png": "368310200ce2d481b726bc4599613a5e",
"assets/assets/images/tb-2.png": "c152408a1fa642ec37e395f68a637d10",
"assets/assets/images/ytd-1.png": "a01a0f4e7dd3245621b79cad1e62dbbb",
"assets/FontManifest.json": "f65eb5d86c682d0152f5ba7eb5d102a2",
"assets/fonts/klavika-medium.otf": "c328903f663345462a6036978dfbc7e7",
"assets/fonts/MaterialIcons-Regular.otf": "e626480e1445ea6b7e04a9f17fb5ad03",
"assets/NOTICES": "4021c93219a957628bc5d41940140145",
"assets/packages/fluttertoast/assets/toastify.css": "a85675050054f179444bc5ad70ffc635",
"assets/packages/fluttertoast/assets/toastify.js": "e7006a0a033d834ef9414d48db3be6fc",
"assets/shaders/ink_sparkle.frag": "f8b80e740d33eb157090be4e995febdf",
"canvaskit/canvaskit.js": "45bec3a754fba62b2d8f23c38895f029",
"canvaskit/canvaskit.wasm": "e5b1f72690096075e25fe1f481cb6ce6",
"canvaskit/chromium/canvaskit.js": "6bdd0526762a124b0745c05281c8a53e",
"canvaskit/chromium/canvaskit.wasm": "347841c04107bb5a17164bee251d8307",
"canvaskit/skwasm.js": "831c0eebc8462d12790b0fadf3ab6a8a",
"canvaskit/skwasm.wasm": "2cb965595f656f0c58ad6bb5988f8280",
"canvaskit/skwasm.worker.js": "7ec8c65402d6cd2a341a5d66aa3d021f",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"flutter.js": "6b515e434cea20006b3ef1726d2c8894",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"index.html": "2ffc4f75458f735937481474efd90c00",
"/": "2ffc4f75458f735937481474efd90c00",
"main.dart.js": "0881ea48cd19d09b04e0e373381a3f93",
"manifest.json": "e74af8957b5899dc6da961caee768ec9",
"version.json": "009c9e65172e010890f7f65fde438006"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"assets/AssetManifest.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
