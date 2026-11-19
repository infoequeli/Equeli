/* Equeli – mreža sodelovanj: klik na regijo in iskanje po seznamu. */
(function () {
  var q = document.getElementById('nmap-q');
  if (!q) return;
  var regs = [].slice.call(document.querySelectorAll('.nw-reg'));
  var dots = [].slice.call(document.querySelectorAll('.nw-grid .rm-dot'));
  var sel = document.getElementById('nmap-sel'), all = document.getElementById('nmap-all');
  var region = null;
  function norm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  var empty = document.createElement('p'); empty.className = 'nw-empty'; empty.hidden = true;
  empty.textContent = 'Ni zadetkov. Poskusite z imenom kraja ali centra.';
  if (regs[0]) regs[0].parentNode.insertBefore(empty, regs[0]);
  function apply() {
    var t = norm(q.value.trim()), any = false;
    regs.forEach(function (r) {
      var okR = !region || r.getAttribute('data-r') === region, vis = 0;
      [].slice.call(r.querySelectorAll('.nw-i')).forEach(function (it) {
        var ok = okR && (!t || norm(it.textContent + ' ' + r.getAttribute('data-r')).indexOf(t) >= 0);
        it.hidden = !ok; if (ok) vis++;
      });
      r.hidden = !vis; if (vis) any = true;
    });
    empty.hidden = any;
    dots.forEach(function (d) { d.classList.toggle('on', d.getAttribute('data-r') === region); });
    if (sel) { sel.hidden = !region; sel.querySelector('span').textContent = region ? 'Prikazana regija: ' + region + '.' : ''; }
  }
  dots.forEach(function (d) {
    d.setAttribute('tabindex', '0'); d.setAttribute('role', 'button');
    function pick() { region = region === d.getAttribute('data-r') ? null : d.getAttribute('data-r'); apply(); }
    d.addEventListener('click', pick);
    d.addEventListener('keydown', function (ev) { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); pick(); } });
  });
  if (all) all.addEventListener('click', function () { region = null; apply(); });
  q.addEventListener('input', apply);
})();
