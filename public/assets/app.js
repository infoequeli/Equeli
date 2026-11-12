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

  /* interaktivni vodnik */
  var guide = document.getElementById('guide');
  if (!guide) return;
  var base = guide.dataset.base || '/';
  var NEEDS = {
    avtizem: { label: 'Avtizem', who: ['otrok', 'mladostnik', 'odrasel'], url: 'vodnik/avtizem/',
      tags: ['Terapija s pomočjo konja', 'Specialnopedagoške intervencije', 'Delovna terapija s konjem'],
      q: ['Kakšne izkušnje imate z osebami z avtizmom?', 'Kako prilagodite okolje (hrup, število ljudi, potek)?', 'Je mogoč predhodni ogled?'] },
    gibanje: { label: 'Cerebralna paraliza in gibalne težave', who: ['otrok', 'mladostnik', 'odrasel'], url: 'vodnik/gibalne-tezave/',
      tags: ['Hipoterapija', 'Delovna terapija s konjem', 'Prilagojeno jahanje'],
      q: ['Kdo vodi obravnavo in kakšno usposabljanje ima?', 'Ali potrebujete mnenje zdravnika ali fizioterapevta?', 'Kako je urejeno nameščanje na konja?'] },
    adhd: { label: 'ADHD in težave s pozornostjo', who: ['otrok', 'mladostnik'], url: 'vodnik/adhd/',
      tags: ['Pedagoške intervencije', 'Terapija s pomočjo konja', 'Psihosocialne intervencije'],
      q: ['Kako je srečanje strukturirano?', 'Ali sodelujete s šolo?', 'Kako bomo spremljali napredek?'] },
    razvoj: { label: 'Downov sindrom in motnje v duševnem razvoju', who: ['otrok', 'mladostnik', 'odrasel'], url: 'vodnik/motnje-v-dusevnem-razvoju/',
      tags: ['Terapija s pomočjo konja', 'Delovna terapija s konjem', 'Prilagojeno jahanje'],
      q: ['Ali imate izkušnje s to skupino, tudi z odraslimi?', 'Ali pred vključitvijo potrebujete zdravniško mnenje?', 'So mogoči skupinski programi ali tabori?'] },
    ucne: { label: 'Učne, čustvene in vedenjske težave', who: ['otrok', 'mladostnik'], url: 'vodnik/ucne-custvene-vedenjske-tezave/',
      tags: ['Pedagoške intervencije', 'Psihosocialne intervencije', 'Terapija s pomočjo konja'],
      q: ['Kakšna je vaša temeljna stroka?', 'Kako bomo starši vključeni?', 'Ali ponujate programe za šole?'] },
    tesnoba: { label: 'Tesnoba, samopodoba in odnosi', who: ['mladostnik', 'odrasel'], url: 'vodnik/tesnoba-samopodoba-odnosi/',
      tags: ['Psihosocialne intervencije', 'Terapija s pomočjo konja', 'Aktivnosti s konji'],
      q: ['Kakšno izobrazbo imate in ste vpisani v register svoje stroke?', 'Kako je poskrbljeno za zaupnost?', 'Kdaj boste predlagali drugo obliko pomoči?'] },
    aktivnost: { label: 'Predvsem prijetna aktivnost ob konjih', who: ['otrok', 'mladostnik', 'odrasel'], url: 'vodnik/aktivnost-ob-konjih/',
      tags: ['Prilagojeno jahanje', 'Aktivnosti s konji'],
      q: ['Kakšna varnostna oprema je na voljo?', 'Koliko ljudi pomaga pri jahanju?', 'Ali so na voljo skupinski termini ali tabori?'] }
  };
  var WHO = { otrok: 'otroke', mladostnik: 'mladostnike', odrasel: 'odrasle' };
  var state = { who: null, need: null };
  var whoBox = guide.querySelector('[data-step="who"]'), needBox = guide.querySelector('[data-step="need"]'),
      needChips = needBox.querySelector('.chips'), panel = guide.querySelector('.guide-panel'), placeholder = panel.innerHTML;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function link(p) { return base + p + (base === '/' ? '' : 'index.html'); }
  function renderNeeds() {
    needChips.innerHTML = Object.keys(NEEDS).filter(function (k) { return NEEDS[k].who.indexOf(state.who) > -1; })
      .map(function (k) { return '<button type="button" class="chip" data-need="' + k + '" aria-pressed="' + (state.need === k) + '">' + esc(NEEDS[k].label) + '</button>'; }).join('') +
      '<a class="chip" href="' + link('kako-izbrati/') + '">Ne vem, kje začeti</a>';
  }
  function renderPanel() {
    var n = NEEDS[state.need];
    if (!n || n.who.indexOf(state.who) < 0) { panel.innerHTML = placeholder; return; }
    panel.innerHTML = '<p class="kicker">Začnite tukaj</p><h3>' + esc(n.label) + '</h3>' +
      '<p class="muted" style="margin-top:14px;font-size:15.5px">Pristopi, ki jih izvajalci za ' + esc(WHO[state.who]) + ' pri tem pogosto ponujajo:</p>' +
      '<div class="tags">' + n.tags.map(function (t) { return '<span class="tag">' + esc(t) + '</span>'; }).join('') + '</div>' +
      '<p style="margin-top:24px;font-weight:600;font-size:15px">Vprašanja za izvajalca</p><ul>' + n.q.map(function (q) { return '<li>' + esc(q) + '</li>'; }).join('') + '</ul>' +
      '<div class="btn-row" style="margin-top:26px"><a class="btn btn-dark btn-sm" href="' + link(n.url) + '">Odprite vodnik <span class="arr">→</span></a><a class="btn btn-ghost btn-sm" href="' + link('kontakt/') + '">Pomagamo poiskati izvajalca</a></div>' +
      '<p class="note">O primernosti programa odloči usposobljen strokovnjak.</p>';
  }
  whoBox.addEventListener('click', function (e) {
    var b = e.target.closest('[data-who]'); if (!b) return;
    state.who = b.dataset.who;
    whoBox.querySelectorAll('[data-who]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    needBox.hidden = false; renderNeeds(); renderPanel();
  });
  needBox.addEventListener('click', function (e) {
    var b = e.target.closest('[data-need]'); if (!b) return;
    state.need = b.dataset.need; renderNeeds(); renderPanel();
    if (window.innerWidth < 900) panel.scrollIntoView({ block: 'start', behavior: reduce ? 'auto' : 'smooth' });
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
