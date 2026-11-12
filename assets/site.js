/* Atelier Cordeau : moteur de la maquette.
   Une seule horloge (gsap.ticker) pilote la ligne de cordeau, les lignes qui claquent et Lenis. */
(() => {
  const html = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const gsap = window.gsap;
  const ST = window.ScrollTrigger;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const done = () => html.classList.remove('intro-pending');

  /* ---------- menu mobile ---------- */
  const toggle = document.querySelector('[data-nav-toggle]');
  const list = document.querySelector('[data-nav-list]');
  if (toggle && list) {
    const set = (open) => { toggle.setAttribute('aria-expanded', String(open)); list.classList.toggle('is-open', open); };
    toggle.addEventListener('click', () => set(toggle.getAttribute('aria-expanded') !== 'true'));
    list.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { set(false); toggle.focus(); } });
  }

  /* ---------- impression des mentions légales ---------- */
  document.querySelectorAll('[data-print]').forEach((b) => b.addEventListener('click', () => window.print()));

  /* ---------- formulaire (maquette, non relié) ---------- */
  const form = document.querySelector('[data-form]');
  if (form) {
    const status = form.querySelector('[data-form-status]');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let first = null;
      form.querySelectorAll('[required]').forEach((f) => {
        const bad = f.type === 'checkbox' ? !f.checked : !f.value.trim();
        f.setAttribute('aria-invalid', String(bad));
        if (bad && !first) first = f;
      });
      if (first) { status.textContent = 'Il manque votre nom, votre téléphone ou votre accord.'; first.focus(); return; }
      status.textContent = 'Merci. Sur le vrai site, votre demande partirait à l’atelier. Ici, le formulaire est une maquette.';
    });
  }

  if (!gsap) { done(); return; }
  gsap.registerPlugin(ST);

  /* ---------- scroll doux ---------- */
  let lenis = null;
  if (!reduce && window.Lenis) {
    lenis = new window.Lenis({ autoRaf: false, lerp: 0.12 });
    lenis.on('scroll', ST.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href*="#"]');
      if (!a) return;
      const url = new URL(a.href, location.href);
      if (url.pathname !== location.pathname || !url.hash || url.hash === '#contenu') return;
      const target = document.querySelector(url.hash);
      if (!target) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: -(document.querySelector('[data-header]')?.offsetHeight || 0) - 12, duration: 1.1 });
      history.replaceState(null, '', url.hash);
    });
  }

  /* ---------- rideau entre les pages ---------- */
  const curtain = document.querySelector('.curtain');
  if (curtain && !reduce) {
    gsap.set(curtain, { xPercent: -101 });
    if (html.classList.contains('is-arriving')) {
      gsap.set(curtain, { xPercent: 0, visibility: 'visible' });
      gsap.to(curtain, { xPercent: 101, duration: 0.7, ease: 'expo.inOut', delay: 0.05, onComplete: () => { html.classList.remove('is-arriving'); gsap.set(curtain, { visibility: 'hidden' }); } });
    }
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href]');
      if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target === '_blank') return;
      const url = new URL(a.href, location.href);
      if (url.origin !== location.origin || !/\.html$|\/$/.test(url.pathname)) return;
      if (url.pathname === location.pathname) return;
      e.preventDefault();
      try { sessionStorage.setItem('cordeau-nav', '1'); } catch (_) {}
      gsap.set(curtain, { visibility: 'visible' });
      gsap.fromTo(curtain, { xPercent: -101 }, { xPercent: 0, duration: 0.5, ease: 'expo.inOut', onComplete: () => { location.href = url.href; } });
    });
    window.addEventListener('pageshow', (e) => { if (e.persisted) { html.classList.remove('is-arriving'); gsap.set(curtain, { xPercent: -101, visibility: 'hidden' }); } });
  } else { html.classList.remove('is-arriving'); }

  /* ---------- la ligne de cordeau (signature) ---------- */
  const strings = [];

  function Cordeau(el) {
    const after = el.querySelector('[data-cordeau-after]');
    const svg = el.querySelector('[data-cordeau-svg]');
    const paths = svg.querySelectorAll('path');
    const handle = el.querySelector('[data-cordeau-handle]');
    const range = el.querySelector('[data-cordeau-range]');
    const rigid = el.hasAttribute('data-rigid');
    const s = { pos: +el.dataset.start || 0.5, target: +el.dataset.start || 0.5, amp: 0, t: 0, W: 0, H: 0, hy: 0.5, visible: true, last: '' };
    const measure = () => { s.W = el.clientWidth; s.H = el.clientHeight; s.hy = parseFloat(getComputedStyle(el).getPropertyValue('--hy')) || 0.5; svg.setAttribute('viewBox', `0 0 ${s.W} ${s.H}`); s.last = ''; };
    new ResizeObserver(measure).observe(el);
    measure();
    new IntersectionObserver(([en]) => { s.visible = en.isIntersecting; }).observe(el);

    s.pluck = (k = 1) => { s.amp = Math.max(s.amp, k * Math.min(s.W, s.H) * 0.07); s.t = 0; };
    s.setTarget = (v, excite = true) => {
      v = clamp(v, 0.02, 0.98);
      if (excite && !reduce) s.amp = Math.min(Math.max(s.amp, Math.abs(v - s.target) * s.W * 0.9), Math.min(s.W, s.H) * 0.06);
      s.target = v;
      if (range) range.value = Math.round(v * 100);
    };
    s.render = (dt, time) => {
      if (!s.visible || !s.W) return;
      s.pos += (s.target - s.pos) * (reduce ? 1 : 1 - Math.exp(-dt * 12));
      s.t += dt;
      s.amp *= Math.exp(-dt * 3.4);
      const idle = reduce ? 0 : 1.1 * Math.sin(time * 1.25) + 0.5 * Math.sin(time * 2.9);
      const vib = (reduce || rigid) ? 0 : s.amp * Math.sin(s.t * Math.PI * 2 * 6.5) + idle;
      const x = s.pos * s.W, H = s.H, cx = x + vib * 2;
      const d = `M${x.toFixed(1)} -6 Q${cx.toFixed(1)} ${(H / 2).toFixed(1)} ${x.toFixed(1)} ${(H + 6).toFixed(1)}`;
      if (d === s.last) return;
      s.last = d;
      for (const p of paths) p.setAttribute('d', d);
      after.style.clipPath = `path('M${x.toFixed(1)} -6 Q${cx.toFixed(1)} ${(H / 2).toFixed(1)} ${x.toFixed(1)} ${(H + 6).toFixed(1)} L${s.W + 2} ${H + 6} L${s.W + 2} -6 Z')`;
      if (handle) handle.style.transform = `translate(${(x + vib).toFixed(1)}px, ${(H * s.hy).toFixed(1)}px)`;
    };

    if (range) {
      el.setAttribute('data-interactive', '');
      range.addEventListener('input', () => s.setTarget(range.value / 100));
      let drag = false;
      const at = (e) => { const r = el.getBoundingClientRect(); return (e.clientX - r.left) / r.width; };
      el.addEventListener('pointerdown', (e) => {
        if (e.pointerType === 'mouse' && e.button !== 0) return;
        drag = true; el.classList.add('is-dragging'); el.setPointerCapture(e.pointerId); s.setTarget(at(e));
      });
      el.addEventListener('pointermove', (e) => { if (drag) s.setTarget(at(e)); });
      const end = () => { if (drag) { drag = false; el.classList.remove('is-dragging'); s.pluck(0.35); } };
      el.addEventListener('pointerup', end);
      el.addEventListener('pointercancel', end);
    }
    strings.push(s);
    return s;
  }

  /* ---------- lignes qui claquent entre les sections ---------- */
  const snaps = [];
  document.querySelectorAll('[data-snap-line]').forEach((el) => {
    const svg = el.querySelector('svg');
    const path = el.querySelector('path');
    const s = { amp: 0, t: 0, W: 0, H: 0, drawn: reduce, visible: false, last: '' };
    const measure = () => { s.W = el.clientWidth; s.H = el.clientHeight; svg.setAttribute('viewBox', `0 0 ${s.W} ${s.H}`); s.last = ''; };
    new ResizeObserver(measure).observe(el);
    measure();
    new IntersectionObserver(([en]) => { s.visible = en.isIntersecting; }).observe(el);
    s.render = (dt) => {
      if (!s.visible || !s.W) return;
      s.t += dt; s.amp *= Math.exp(-dt * 3.6);
      const vib = (reduce || rigid) ? 0 : s.amp * Math.sin(s.t * Math.PI * 2 * 5.5);
      const y = s.H / 2;
      const d = `M0 ${y} Q${(s.W / 2).toFixed(1)} ${(y + vib * 2).toFixed(1)} ${s.W} ${y}`;
      if (d !== s.last) { path.setAttribute('d', d); s.last = d; }
    };
    if (!reduce) {
      gsap.set(path, { attr: { pathLength: 1 }, strokeDasharray: 1, strokeDashoffset: 1 });
      ST.create({
        trigger: el, start: 'top 85%', once: true,
        onEnter: () => {
          gsap.to(path, { strokeDashoffset: 0, duration: 0.55, ease: 'expo.out', onComplete: () => { s.amp = Math.min(22, s.H * 0.38); s.t = 0; } });
        },
      });
    }
    snaps.push(s);
  });

  const stages = [...document.querySelectorAll('[data-cordeau]')].map(Cordeau);

  /* une seule horloge */
  let time = 0;
  gsap.ticker.add((t, deltaMs) => {
    const dt = Math.min(deltaMs / 1000, 0.05);
    time = t;
    for (const s of strings) s.render(dt, time);
    for (const s of snaps) s.render(dt, time);
  });

  /* ---------- accueil : épinglage, la ligne avance au scroll ---------- */
  const pin = document.querySelector('[data-hero-pin]');
  if (pin && stages[0]) {
    const hero = stages[0];
    const from = hero.target, to = 0.08;
    if (!reduce) {
      const header = document.querySelector('[data-header]');
      const hint = document.querySelector('[data-hero-hint]');
      ST.create({
        trigger: pin, start: () => `top ${header ? header.offsetHeight : 0}px`, end: '+=85%', pin: true, scrub: true, invalidateOnRefresh: true,
        onUpdate: (self) => {
          hero.setTarget(from + (to - from) * self.progress);
          if (hint) hint.style.opacity = String(clamp(1 - self.progress * 4, 0, 1));
        },
        onLeave: () => hero.pluck(0.6),
      });
      // intro : le titre monte, la ligne claque
      const lines = pin.querySelectorAll('.hero-title .line > span');
      gsap.set(lines, { y: 0, yPercent: 105 }); done();
      gsap.to(lines, { yPercent: 0, duration: 1.1, ease: 'expo.out', stagger: 0.08, delay: 0.15 });
      gsap.from(pin.querySelectorAll('.hero-sub, .hero-actions'), { autoAlpha: 0, y: 14, duration: 0.8, ease: 'expo.out', stagger: 0.06, delay: 0.45 });
      gsap.delayedCall(0.2, () => hero.pluck(1));
    } else { done(); }
  } else { done(); }

  /* ---------- réalisation : petite démonstration du glissement ---------- */
  const caseStage = document.querySelector('.cordeau-case');
  if (caseStage && !reduce) {
    const target = stages[0];
    if (target) {
      gsap.delayedCall(0.5, () => target.pluck(0.8));
      const proxy = { v: target.target };
      gsap.timeline({ delay: 0.9 })
        .to(proxy, { v: 0.32, duration: 0.7, ease: 'expo.inOut', onUpdate: () => target.setTarget(proxy.v, false) })
        .to(proxy, { v: 0.5, duration: 0.8, ease: 'expo.out', onUpdate: () => target.setTarget(proxy.v, false), onComplete: () => target.pluck(0.4) });
    }
  }

  /* ---------- titres de section : entrée unique ---------- */
  if (!reduce) {
    document.querySelectorAll('.display-l, .case-title, .contact-page h1, .nf h1').forEach((h) => {
      gsap.from(h, { y: 28, autoAlpha: 0, duration: 0.9, ease: 'expo.out', scrollTrigger: { trigger: h, start: 'top 88%', once: true } });
    });
    gsap.from('.step', { y: 24, autoAlpha: 0, duration: 0.8, ease: 'expo.out', stagger: 0.07, scrollTrigger: { trigger: '.steps', start: 'top 80%', once: true } });
  }

  addEventListener('load', () => ST.refresh());
})();
