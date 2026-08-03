/* 33bots — LT landing: navigation, reveal, counters, ROI calculator, lead form */
(function () {
  'use strict';

  /* Kur siunčiama forma. Įrašykite savo endpoint'ą (Formspree, Make, n8n, savo API).
     Kol tuščias — forma parodo mailto atsarginį variantą. */
  var FORM_ENDPOINT = '';
  var FALLBACK_EMAIL = 'info@33bots.lt';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header ---------- */
  var header = document.getElementById('header');
  var onScroll = function () {
    header.classList.toggle('scrolled', window.scrollY > 12);
    if (sticky) sticky.classList.toggle('show', window.scrollY > 700);
  };
  var sticky = document.querySelector('.sticky-cta');
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile nav ---------- */
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');
  var setNav = function (open) {
    nav.classList.toggle('open', open);
    document.body.classList.toggle('nav-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Uždaryti meniu' : 'Atidaryti meniu');
  };
  burger.addEventListener('click', function () {
    setNav(burger.getAttribute('aria-expanded') !== 'true');
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') setNav(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      setNav(false);
      burger.focus();
    }
  });
  window.addEventListener('resize', function () {
    if (window.innerWidth > 780 && nav.classList.contains('open')) setNav(false);
  });

  /* ---------- Reveal on scroll ---------- */
  var revealTargets = document.querySelectorAll(
    '.section > .container > *, .pain, .card, .steps li, .case, .plan, .faq details, .lead-form'
  );
  if (!reduceMotion && 'IntersectionObserver' in window) {
    revealTargets.forEach(function (el) { el.classList.add('reveal'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, i) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        setTimeout(function () { el.classList.add('in'); }, Math.min(i * 60, 240));
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealTargets.forEach(function (el) { io.observe(el); });

    // Saugiklis: jei observeris nesuveiktų (netikėtas viewport'as, crawler'is,
    // ekrano nuotraukų įrankis), turinys vis tiek tampa matomas.
    window.addEventListener('load', function () {
      setTimeout(function () {
        revealTargets.forEach(function (el) { el.classList.add('in'); });
      }, 3000);
    });
  }

  /* ---------- Counters ---------- */
  var counters = document.querySelectorAll('[data-count]');
  var runCounter = function (el) {
    var target = parseFloat(el.dataset.count);
    var suffix = el.dataset.suffix || '+';
    if (reduceMotion) { el.textContent = target + suffix; return; }
    var start = performance.now();
    var dur = 1200;
    var tick = function (now) {
      var p = Math.min((now - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        runCounter(entry.target);
        co.unobserve(entry.target);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { co.observe(el); });
  } else {
    counters.forEach(runCounter);
  }

  /* ---------- ROI skaičiuoklė ---------- */
  var calc = document.getElementById('calc');
  if (calc) {
    var UPLIFT = 0.30;        // konservatyvus konversijos prieaugis
    var IMPLEMENTATION = 2100; // bazinė diegimo kaina, €
    var eur = new Intl.NumberFormat('lt-LT', {
      style: 'currency', currency: 'EUR', maximumFractionDigits: 0
    });
    var num = new Intl.NumberFormat('lt-LT', { maximumFractionDigits: 0 });

    var val = function (id) {
      var n = parseFloat(document.getElementById(id).value);
      return isFinite(n) && n > 0 ? n : 0;
    };

    var update = function () {
      var visitors = val('c-visitors');
      var conv = Math.min(val('c-conv'), 100) / 100;
      var deal = val('c-value');
      var close = Math.min(val('c-close'), 100) / 100;

      var extraLeads = visitors * conv * UPLIFT;
      var extraRevenue = extraLeads * close * deal;

      document.getElementById('r-leads').textContent = num.format(Math.round(extraLeads));
      document.getElementById('r-rev').textContent = eur.format(Math.round(extraRevenue));

      var payback = document.getElementById('r-payback');
      if (extraRevenue <= 0) {
        payback.textContent = '—';
      } else {
        var months = IMPLEMENTATION / extraRevenue;
        payback.textContent = months < 1
          ? 'mažiau nei 1 mėn.'
          : (Math.round(months * 10) / 10).toString().replace('.', ',') + ' mėn.';
      }
    };

    calc.addEventListener('input', update);
    calc.addEventListener('submit', function (e) { e.preventDefault(); });
    update();
  }

  /* ---------- Lead forma ---------- */
  var form = document.getElementById('lead-form');
  if (form) {
    var status = document.getElementById('form-status');

    var showError = function (input, message) {
      var box = form.querySelector('.err[data-for="' + input.id + '"]');
      if (box) box.textContent = message || '';
      input.setAttribute('aria-invalid', message ? 'true' : 'false');
    };

    var validate = function () {
      var ok = true;
      var name = document.getElementById('f-name');
      var email = document.getElementById('f-email');
      var gdpr = document.getElementById('f-gdpr');

      if (!name.value.trim()) { showError(name, 'Įveskite vardą.'); ok = false; }
      else showError(name, '');

      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) {
        showError(email, 'Įveskite galiojantį el. pašto adresą.');
        ok = false;
      } else showError(email, '');

      if (!gdpr.checked) { showError(gdpr, 'Reikalingas sutikimas.'); ok = false; }
      else showError(gdpr, '');

      return ok;
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form-status';
      status.textContent = '';

      if (!validate()) {
        status.className = 'form-status error';
        status.textContent = 'Patikrinkite pažymėtus laukus.';
        var firstBad = form.querySelector('[aria-invalid="true"]');
        if (firstBad) firstBad.focus();
        return;
      }

      // Honeypot — botai pildo paslėptą lauką
      if (form.elements.website && form.elements.website.value) return;

      var data = Object.fromEntries(new FormData(form).entries());
      delete data.website;

      if (!FORM_ENDPOINT) {
        var body = Object.keys(data)
          .filter(function (k) { return k !== 'gdpr' && data[k]; })
          .map(function (k) { return k + ': ' + data[k]; })
          .join('\n');
        window.location.href = 'mailto:' + FALLBACK_EMAIL +
          '?subject=' + encodeURIComponent('Užklausa iš 33bots.lt') +
          '&body=' + encodeURIComponent(body);
        status.textContent = 'Atidarome jūsų pašto programą. Nepavyko? Rašykite ' + FALLBACK_EMAIL;
        return;
      }

      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      var label = btn.textContent;
      btn.textContent = 'Siunčiama…';

      fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(data)
      })
        .then(function (res) {
          if (!res.ok) throw new Error('HTTP ' + res.status);
          form.reset();
          status.textContent = 'Ačiū! Susisieksime per 24 val. darbo dienomis.';
        })
        .catch(function () {
          status.className = 'form-status error';
          status.textContent = 'Nepavyko išsiųsti. Parašykite mums: ' + FALLBACK_EMAIL;
        })
        .finally(function () {
          btn.disabled = false;
          btn.textContent = label;
        });
    });
  }

  /* ---------- Metai footeryje ---------- */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
