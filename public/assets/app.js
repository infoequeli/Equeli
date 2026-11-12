document.documentElement.classList.add("js");
/* Equeli – meni, glava, generativna vizualija in interaktivni vodnik. Brez piškotkov in brez zbiranja podatkov. */
(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* glava in meni */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 4); };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Zapri meni' : 'Odpri meni');
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); } });
  }

  /* konj iz točk: podatkovna vizualizacija konjske glave */
  var HEAD = new Path2D('M226 94 L236 50 L250 96 Z M112 400 C100 300 120 170 214 98 L222 42 L240 90 C262 98 282 118 296 142 C318 182 334 220 346 254 C358 290 340 314 312 310 C300 316 290 318 280 314 C268 310 262 302 260 296 C246 284 238 266 230 260 C210 262 192 252 186 236 C176 280 186 340 204 400 Z');
  var MANE = new Path2D('M216 100 C186 110 158 138 144 172 C130 208 126 252 128 304 C138 262 150 216 170 180 C186 152 202 130 224 112 Z M210 106 C170 128 140 168 126 214 C118 240 112 266 110 290 C116 256 128 222 146 190 C164 158 186 128 212 110 Z M236 94 C250 104 256 118 256 132 L246 128 C244 116 240 106 232 98 Z');
  var probe = document.createElement('canvas').getContext('2d');
  function inH(x, y) { return probe.isPointInPath(HEAD, x, y) || probe.isPointInPath(MANE, x, y); }
  document.querySelectorAll('canvas.horse-dots').forEach(function (cv) {
    var ctx = cv.getContext('2d'); if (!ctx) return;
    var s = parseFloat(cv.dataset.s || '1'), ox = parseFloat(cv.dataset.x || '0.5'), oy = parseFloat(cv.dataset.y || '0.5');
    var dots = [], w = 0, h = 0, t0 = null, visible = true, raf;
    function build() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = cv.clientWidth; h = cv.clientHeight; if (!w || !h) return;
      cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var k = (Math.min(w, h) * s) / 400, step = Math.max(4.2, Math.min(8, w / 64)), d = step / k;
      dots = [];
      for (var py = step / 2; py < h; py += step) for (var px = step / 2; px < w; px += step) {
        var hx = (px - (w * ox - 236 * k)) / k, hy = (py - (h * oy - 196 * k)) / k;
        var eye = (hx - 274) * (hx - 274) + (hy - 150) * (hy - 150) < 64, nos = (hx - 334) * (hx - 334) + (hy - 262) * (hy - 262) < 49;
        var head = probe.isPointInPath(HEAD, hx, hy), mane = probe.isPointInPath(MANE, hx, hy);
        if ((head || mane) && !eye && !nos) {
          var edge = false;
          for (var a = 0; a < 8 && !edge; a++) if (!inH(hx + d * Math.cos(a * Math.PI / 4), hy + d * Math.sin(a * Math.PI / 4))) edge = true;
          var shade = (0.35 + 0.65 * Math.min(1, Math.max(0, (hx - 110) / 230))) * (1 - Math.max(0, hy - 260) / 300);
          dots.push({ x: px, y: py, r: edge ? step * 0.29 : step * (0.13 + 0.14 * shade), o: edge ? 1 : 0.25 + 0.7 * shade, m: mane && !head ? 1 : mane ? 1 : 0, hx: hx });
        } else dots.push({ x: px, y: py, r: step * 0.1, o: 0.08, bg: 1, hx: hx });
      }
    }
    function frame(ts) {
      if (t0 === null) t0 = ts; var t = (ts - t0) / 1000;
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < dots.length; i++) {
        var p = dots[i], o = p.o;
        if (!p.bg) {
          var appear = reduce ? 1 : Math.min(1, Math.max(0, (t * 420 - (p.hx - 60)) / 120));
          var wave = reduce ? 1 : 0.82 + 0.18 * Math.sin(t * 1.4 - p.hx / 38 + p.y / 60);
          o = o * appear * wave;
          ctx.fillStyle = p.m ? 'rgba(217,171,128,' + o + ')' : 'rgba(255,255,255,' + o + ')';
        } else ctx.fillStyle = 'rgba(255,255,255,' + o + ')';
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.2832); ctx.fill();
      }
      if (!reduce && visible) raf = requestAnimationFrame(frame);
    }
    function start() { build(); cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); }
    start();
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(start, 150); });
    if ('IntersectionObserver' in window && !reduce) new IntersectionObserver(function (en) { var v = en[0].isIntersecting; if (v && !visible) { visible = true; raf = requestAnimationFrame(frame); } visible = v; }).observe(cv);
  });

})();

/* Obrazci: vodeni koraki, preverjanje in povratna informacija.
   Brez JavaScripta se pokaže celoten obrazec naenkrat. */
document.querySelectorAll('form.eform').forEach(function (f) {
  var steps = Array.prototype.slice.call(f.querySelectorAll('.fgroup:not(.consent)'));
  var consent = f.querySelector('.fgroup.consent');
  var err = f.querySelector('.form-error');
  var foot = f.querySelector('.form-foot');
  var submit = foot.querySelector('button[type=submit]');
  var cur = 0, wizard = steps.length > 1;

  function fieldsOf(el) { return Array.prototype.slice.call(el.querySelectorAll('input:not([type=hidden]):not(.hp),select,textarea')); }
  function check(el) {
    var bad = fieldsOf(el).filter(function (x) { return !x.checkValidity(); });
    if (bad.length) {
      el.classList.add('touched');
      if (err) err.hidden = false;
      bad[0].focus({ preventScroll: true });
      bad[0].scrollIntoView({ block: 'center', behavior: 'smooth' });
      return false;
    }
    el.classList.remove('touched');
    if (err) err.hidden = true;
    return true;
  }

  if (wizard) {
    f.classList.add('wizard');
    steps[steps.length - 1].appendChild(consent);
    var top = document.createElement('div');
    top.className = 'wz-top';
    top.innerHTML = '<div class="wz-meta"><b class="wz-n"></b><span class="wz-t"></span></div><div class="wz-bar" aria-hidden="true"><i></i></div>';
    f.prepend(top);
    var back = document.createElement('button');
    back.type = 'button'; back.className = 'btn btn-text btn-lg'; back.textContent = '← Nazaj';
    var next = document.createElement('button');
    next.type = 'button'; next.className = 'btn btn-dark btn-lg'; next.textContent = 'Naprej';
    var sp = document.createElement('span'); sp.className = 'sp';
    foot.innerHTML = ''; foot.append(back, sp, next, submit);

    var show = function (i, focus) {
      cur = i;
      steps.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      top.querySelector('.wz-n').textContent = 'Korak ' + (i + 1) + ' od ' + steps.length;
      top.querySelector('.wz-t').textContent = i < steps.length - 1 ? 'Naprej: ' + steps[i + 1].querySelector('h3').textContent : 'Zadnji korak';
      top.querySelector('i').style.width = ((i + 1) / steps.length * 100) + '%';
      back.hidden = i === 0;
      next.hidden = i === steps.length - 1;
      submit.hidden = i !== steps.length - 1;
      if (err) err.hidden = true;
      if (focus) {
        var h = steps[i].querySelector('h3'); h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true });
        var y = f.getBoundingClientRect().top + window.scrollY - 90;
        if (Math.abs(window.scrollY - y) > 40) window.scrollTo({ top: y, behavior: 'smooth' });
      }
    };
    next.addEventListener('click', function () { if (check(steps[cur])) show(cur + 1, true); });
    back.addEventListener('click', function () { show(cur - 1, true); });
    f.addEventListener('keydown', function (ev) {
      if (ev.key === 'Enter' && ev.target.tagName === 'INPUT' && cur < steps.length - 1) { ev.preventDefault(); next.click(); }
    });
    show(0, false);
  }

  f.addEventListener('submit', function (ev) {
    var scope = wizard ? steps[cur] : f;
    if (!check(scope) || !f.checkValidity()) { ev.preventDefault(); return; }
    submit.disabled = true; submit.textContent = 'Pošiljam …';
  });
});


/* Vodeno iskanje: korak za korakom do pristopov in centrov */
document.querySelectorAll('.finder').forEach(function (root) {
  var cfg = JSON.parse(root.querySelector('script[type="application/json"]').textContent);
  var base = root.dataset.base || '/';
  var steps = cfg.steps, M = cfg.maps, A = cfg.A;
  var body = root.querySelector('.fd-body'), back = root.querySelector('.fd-back'), next = root.querySelector('.fd-next');
  var bar = root.querySelector('.fd-bar i'), num = root.querySelector('.fd-n');
  var st = {}, i = 0;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function link(p) { if (p.charAt(0) === '/') p = p.slice(1); var h = ''; var k = p.indexOf('#'); if (k > -1) { h = p.slice(k); p = p.slice(0, k); } return base + p + (base === '/' ? '' : (p ? 'index.html' : 'index.html')) + h; }
  function val(id) { return st[id] || (steps.filter(function (s) { return s.id === id; })[0] || {}).type === 'many' ? (st[id] || []) : st[id]; }
  function ready(s) { var v = st[s.id]; if (s.optional) return true; if (s.type === 'many') return v && v.length; if (s.type === 'region') return v !== undefined; return !!v; }

  function renderStep() {
    var s = steps[i];
    num.textContent = 'Vprašanje ' + (i + 1) + ' od ' + steps.length;
    bar.style.width = ((i + 1) / (steps.length + 1) * 100) + '%';
    var v = st[s.id];
    var html = '<h3 class="fd-q" tabindex="-1">' + esc(s.q) + '</h3>' + (s.hint ? '<p class="fd-hint">' + esc(s.hint) + '</p>' : '');
    if (s.type === 'region') {
      html += '<div class="fd-opts fd-regions">' + s.opts.map(function (o) {
        var on = v === o[0]; return '<button type="button" class="fd-opt' + (o[0] === '' ? ' any' : '') + '" aria-pressed="' + on + '" data-v="' + esc(o[0]) + '">' + esc(o[1]) + '</button>'; }).join('') + '</div>';
    } else {
      html += '<div class="fd-opts' + (s.type === 'many' ? ' many' : '') + '">' + s.opts.map(function (o) {
        var on = s.type === 'many' ? (v || []).indexOf(o[0]) > -1 : v === o[0];
        return '<button type="button" class="fd-opt" aria-pressed="' + on + '" data-v="' + esc(o[0]) + '"><span class="tick" aria-hidden="true"></span>' + esc(o[1]) + '</button>'; }).join('') +
        (s.extra || []).map(function (x) { return '<a class="fd-opt link" href="' + link(x[0]) + '">' + esc(x[1]) + ' →</a>'; }).join('') + '</div>';
    }
    body.innerHTML = html;
    back.hidden = i === 0;
    next.hidden = false;
    next.textContent = i === steps.length - 1 ? 'Pokaži možnosti' : (s.optional && !(v && v.length) ? 'Preskoči' : 'Naprej');
    next.disabled = !ready(s);
  }

  function score() {
    var sc = {}, why = {};
    function add(codes, w, label) { codes.forEach(function (c, k) { sc[c] = (sc[c] || 0) + w + (k === 0 ? 1 : 0); (why[c] = why[c] || []).indexOf(label) < 0 && why[c].push(label); }); }
    (st.goals || []).forEach(function (g) { add(M.goals[g] || [], 3, M.labels[g]); });
    (st.needs || []).forEach(function (n) { add(M.needs[n] || [], 2, M.labels[n]); });
    if (st.who === 'starejsi') { add(['A', 'D'], 1, 'starejša oseba'); }
    return Object.keys(sc).sort(function (a, b) { return sc[b] - sc[a]; }).map(function (c) { return { c: c, why: why[c] }; });
  }

  function renderResult() {
    num.textContent = 'Vaše možnosti';
    bar.style.width = '100%';
    var ranked = score().slice(0, 3);
    var codes = ranked.map(function (r) { return r.c; });
    var html = '<div class="fd-res"><h3 class="fd-q" tabindex="-1">Pristopi, ki bi lahko ustrezali</h3>';
    if (!ranked.length) html += '<p class="fd-hint">Vaši izbiri ustreza več pristopov. Pišite nam in pomagamo izbrati.</p>';
    html += '<div class="fd-apps">' + ranked.map(function (r, k) {
      var a = A[r.c];
      return '<div class="fd-app' + (k === 0 ? ' top' : '') + '"><b>' + esc(a.n) + '</b><p>' + esc(a.d) + '</p><p class="fd-why"><span>Ker ste izbrali:</span> ' + esc(r.why.join(', ').toLowerCase()) + '</p><p class="fd-who"><span>Kdo izvaja:</span> ' + esc(a.w) + '</p>' +
        (r.c === 'H' ? '<a href="' + link('hipoterapija/') + '">Več o hipoterapiji →</a>' : '') + '</div>'; }).join('') + '</div>';
    var notes = [];
    (st.needs || []).concat(st.goals || []).forEach(function (n) { if (M.notes[n] && notes.indexOf(M.notes[n]) < 0) notes.push(M.notes[n]); });
    if (notes.length) html += '<div class="fd-notes"><b>Dobro je vedeti</b><ul>' + notes.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join('') + '</ul></div>';
    var guides = [];
    (st.needs || []).forEach(function (n) { if (M.guides[n] && guides.indexOf(M.guides[n]) < 0) guides.push(M.guides[n]); });
    (st.goals || []).forEach(function (g) { if (M.goalGuides[g] && guides.indexOf(M.goalGuides[g]) < 0) guides.push(M.goalGuides[g]); });
    // centri
    var pool = cfg.C.filter(function (c) { return c.g !== 'organizator' && (cfg.mode !== 'schools' || c.g !== 'javni') && c.o.some(function (o) { return codes.indexOf(o) > -1; }); });
    var reg = st.region || '';
    var local = reg ? pool.filter(function (c) { return c.r.indexOf(reg) > -1; }) : pool;
    function rank(c) { return c.o.reduce(function (s, o) { var k = codes.indexOf(o); return s + (k > -1 ? 3 - k : 0); }, 0) + (c.g === 'javni' || c.g === 'register' ? 1 : 0); }
    local.sort(function (a, b) { return rank(b) - rank(a); });
    var show = local.slice(0, 6), other = false;
    if (reg && show.length < 2) { other = true; show = show.concat(pool.filter(function (c) { return show.indexOf(c) < 0; }).sort(function (a, b) { return rank(b) - rank(a); }).slice(0, 4 - show.length)); }
    if (show.length) {
      html += '<div class="fd-centers"><b>' + (reg && !other ? 'Centri v regiji ' + esc(reg) : reg ? 'V regiji ' + esc(reg) + ' je izbira še majhna. Centri drugod:' : 'Centri s temi pristopi') + '</b><ul>' +
        show.map(function (c) { return '<li><a href="' + esc(c.u) + '" target="_blank" rel="noopener"><span class="cn">' + esc(c.n) + '</span><span class="cp">' + esc(c.p) + '</span><span class="co">' + c.o.filter(function (o) { return codes.indexOf(o) > -1; }).map(function (o) { return esc(A[o].n); }).join(' · ') + '</span></a></li>'; }).join('') + '</ul></div>';
    }
    if (guides.length) html += '<p class="fd-guides">Vodniki: ' + guides.map(function (g) { return '<a href="' + link('vodnik/' + g + '/') + '">' + esc((M.gtitle && M.gtitle[g]) || g) + '</a>'; }).join(', ') + '.</p>';
    html += '<div class="btn-row fd-cta">' + cfg.cta.map(function (c) { return '<a class="btn ' + (c[2] ? 'btn-dark' : 'btn-ghost') + '" href="' + link(c[0]) + '">' + esc(c[1]) + '</a>'; }).join('') + '<button type="button" class="btn btn-text fd-restart">Začni znova</button></div>';
    html += '<p class="fd-fine">O primernosti programa odloči usposobljen strokovnjak.</p></div>';
    body.innerHTML = html;
    back.hidden = false; next.hidden = true;
    body.querySelector('.fd-restart').addEventListener('click', function () { st = {}; i = 0; go(); });
  }

  function go(focus) {
    if (i < steps.length) renderStep(); else renderResult();
    if (focus) {
      var h = body.querySelector('.fd-q'); if (h) h.focus({ preventScroll: true });
      var y = root.getBoundingClientRect().top + window.scrollY - 90;
      if (window.scrollY > y + 10) window.scrollTo({ top: y, behavior: reduce ? 'auto' : 'smooth' });
    }
  }
  body.addEventListener('click', function (ev) {
    var b = ev.target.closest('.fd-opt[data-v]'); if (!b) return;
    var s = steps[i], v = b.dataset.v;
    if (s.type === 'many') {
      var arr = st[s.id] || [];
      if (v === 'brez') arr = arr.indexOf('brez') > -1 ? [] : ['brez'];
      else { arr = arr.filter(function (x) { return x !== 'brez'; }); var k = arr.indexOf(v); if (k > -1) arr.splice(k, 1); else arr.push(v); }
      st[s.id] = arr; renderStep();
    } else { st[s.id] = v; i++; go(true); }
  });
  next.addEventListener('click', function () { if (ready(steps[i])) { i++; go(true); } });
  back.addEventListener('click', function () { if (i > 0) { i--; go(true); } });
  go(false);
});

/* Centri: filter po pristopu in regiji */
(function () {
  var f = document.getElementById('cfilter'); if (!f) return;
  var offer = '', sel = f.querySelector('#cf-reg'), count = f.querySelector('.cf-count');
  var cards = Array.prototype.slice.call(document.querySelectorAll('.center[data-offer]'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.cgroup'));
  var empty = document.querySelector('.cf-empty');
  function apply() {
    var r = sel.value, n = 0;
    cards.forEach(function (c) {
      var ok = (!offer || c.dataset.offer.split(' ').indexOf(offer) > -1) && (!r || c.dataset.region.split('|').indexOf(r) > -1);
      c.hidden = !ok; if (ok) n++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('.center:not([hidden])'); });
    count.textContent = n + (n === 1 ? ' center' : n === 2 ? ' centra' : n < 5 && n > 2 ? ' centri' : ' centrov');
    if (empty) empty.hidden = n > 0;
  }
  f.addEventListener('click', function (e) {
    var b = e.target.closest('.cf-chip'); if (!b) return;
    offer = b.dataset.offer;
    f.querySelectorAll('.cf-chip').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    apply();
  });
  sel.addEventListener('change', apply);
  var m = location.hash.match(/^#(H|T|P|S|D|J|A)$/); if (m) { var b = f.querySelector('[data-offer="' + m[1] + '"]'); if (b) b.click(); }
  apply();
})();


/* anim-observer: animacije ob prikazu (grafi, zemljevid, štetje) */
(function () {
  var els = document.querySelectorAll('.anim'); if (!els.length) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function count(root) {
    root.querySelectorAll('[data-count]').forEach(function (n) {
      var to = +n.dataset.count; if (reduce || !to) { n.textContent = to; return; }
      var t0 = null, d = 1100;
      function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / d); n.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); }
      n.textContent = '0'; requestAnimationFrame(step);
    });
  }
  if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (en) {
    en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); count(x.target); io.unobserve(x.target); } });
  }, { threshold: 0.25 });
  els.forEach(function (e) { io.observe(e); });
})();
