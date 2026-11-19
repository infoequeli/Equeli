/* Equeli – interaktivni zemljevid mreže sodelovanj (Leaflet + OpenStreetMap). */
(function () {
  function start() {
    var el = document.getElementById('nmap');
    var raw = document.getElementById('nmap-data');
    if (!el || !raw || !window.L) return;
    var D = JSON.parse(raw.textContent);
    var COL = { c: '#2e6260', s: '#c2742f', z: '#5b6bb5', d: '#8a5aa8' };
    var map = L.map(el, { scrollWheelZoom: false, minZoom: 7, maxZoom: 15 }).setView([46.12, 14.82], 8);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18, attribution: '&copy; OpenStreetMap'
    }).addTo(map);
    el.addEventListener('click', function () { map.scrollWheelZoom.enable(); });

    function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    var byName = {}, lines = [], markers = [];
    D.nodes.forEach(function (n) { byName[n.n] = n; n.links = []; });
    D.links.forEach(function (l) {
      if (!byName[l.a] || !byName[l.b]) return;
      byName[l.a].links.push({ o: l.b, w: l.w, v: l.v, r: l.r });
      byName[l.b].links.push({ o: l.a, w: l.w, v: l.v, r: l.r });
      var ln = L.polyline([byName[l.a].ll, byName[l.b].ll], { color: '#4f8f8c', weight: 2, opacity: 0.45 }).addTo(map);
      ln._a = l.a; ln._b = l.b; lines.push(ln);
    });

    function popup(n) {
      var h = '<div class="np"><b>' + esc(n.n) + '</b><span>' + esc(n.k) + ' · ' + esc(n.p) + '</span>';
      if (n.u) h += '<a href="' + esc(n.u) + '" target="_blank" rel="noopener">Spletna stran ↗</a>';
      if (n.links.length) {
        h += '<p>Sodeluje z:</p><ul>';
        n.links.forEach(function (x) {
          h += '<li><button type="button" data-go="' + esc(x.o) + '">' + esc(x.o) + '</button> <em>' + esc(x.w) + ' · ' + esc(x.v) + '</em>' +
            (x.r ? ' <a href="' + esc(x.r) + '">Poročilo</a>' : '') + '</li>';
        });
        h += '</ul>';
      } else {
        h += '<p>Sodelovanj še nimamo zapisanih.</p>';
      }
      return h + '</div>';
    }
    D.nodes.forEach(function (n) {
      var m = L.circleMarker(n.ll, { radius: n.t === 'c' ? 9 : 7, color: '#fff', weight: 2, fillColor: COL[n.t], fillOpacity: 0.95 })
        .addTo(map).bindPopup(popup(n), { maxWidth: 300 });
      m.on('popupopen', function () { focus(n.n); });
      m.on('popupclose', function () { focus(null); });
      m._n = n; markers.push(m);
    });
    function focus(name) {
      lines.forEach(function (ln) {
        var on = !name || ln._a === name || ln._b === name;
        ln.setStyle({ opacity: on ? (name ? 0.9 : 0.45) : 0.08, weight: name && on ? 3 : 2 });
      });
    }
    function go(name) {
      var m = markers.filter(function (x) { return x._n.n === name; })[0];
      if (!m) return;
      map.flyTo(m.getLatLng(), Math.max(map.getZoom(), 10), { duration: 0.6 });
      setTimeout(function () { m.openPopup(); }, 650);
    }
    el.addEventListener('click', function (ev) {
      var b = ev.target.closest && ev.target.closest('[data-go]');
      if (b) go(b.getAttribute('data-go'));
    });

    var q = document.getElementById('nmap-q'), res = document.getElementById('nmap-res');
    var filt = 'all';
    function norm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
    function apply() {
      var t = norm(q.value.trim()), hits = [];
      markers.forEach(function (m) {
        var n = m._n;
        var okT = filt === 'all' || n.t === filt;
        var okQ = !t || norm(n.n + ' ' + n.p + ' ' + n.k + ' ' + n.links.map(function (x) { return x.o; }).join(' ')).indexOf(t) >= 0;
        var show = okT && okQ;
        if (show) { if (!map.hasLayer(m)) m.addTo(map); hits.push(n); } else if (map.hasLayer(m)) map.removeLayer(m);
      });
      res.innerHTML = '';
      if (t || filt !== 'all') {
        if (!hits.length) { res.innerHTML = '<li class="empty">Ni zadetkov. Poskusite z imenom kraja.</li>'; return; }
        hits.slice(0, 12).forEach(function (n) {
          var li = document.createElement('li');
          li.innerHTML = '<button type="button" data-go="' + esc(n.n) + '"><i class="dot ' + n.t + '"></i>' + esc(n.n) + '<span>' + esc(n.p) + '</span></button>';
          res.appendChild(li);
        });
      }
    }
    res.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-go]');
      if (b) { go(b.getAttribute('data-go')); el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
    });
    q.addEventListener('input', apply);
    document.querySelectorAll('.nmap-f button').forEach(function (b) {
      b.addEventListener('click', function () {
        filt = b.getAttribute('data-f');
        document.querySelectorAll('.nmap-f button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        apply();
      });
    });
  }
  if (window.L) start(); else window.addEventListener('load', start);
})();
