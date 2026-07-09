/* Agnes Mortgage — scripts.js */
(function () {
  "use strict";
  var LANGS = ["en", "de", "es", "hu"];
  var LANG_NAMES = { en: "English", de: "Deutsch", es: "Español", hu: "Magyar" };
  var FLAG_SVG = {
    en: '<svg class="flag lang-flag" viewBox="0 0 60 42"><rect width="60" height="42" fill="#012169"/><path d="M0,0 60,42 M60,0 0,42" stroke="#fff" stroke-width="8"/><path d="M0,0 60,42 M60,0 0,42" stroke="#C8102E" stroke-width="4"/><path d="M30,0 V42 M0,21 H60" stroke="#fff" stroke-width="12"/><path d="M30,0 V42 M0,21 H60" stroke="#C8102E" stroke-width="7"/></svg>',
    de: '<svg class="flag lang-flag" viewBox="0 0 60 42"><rect width="60" height="14" fill="#000"/><rect y="14" width="60" height="14" fill="#DD0000"/><rect y="28" width="60" height="14" fill="#FFCE00"/></svg>',
    es: '<svg class="flag lang-flag" viewBox="0 0 60 42"><rect width="60" height="42" fill="#AA151B"/><rect y="10.5" width="60" height="21" fill="#F1BF00"/></svg>',
    hu: '<svg class="flag lang-flag" viewBox="0 0 60 42"><rect width="60" height="14" fill="#CE2939"/><rect y="14" width="60" height="14" fill="#fff"/><rect y="28" width="60" height="14" fill="#477050"/></svg>'
  };

  /* ---------- Language system (data-attribute toggle) ---------- */
  function currentLang() {
    var saved = null;
    try { saved = localStorage.getItem("am-lang"); } catch (e) {}
    return LANGS.indexOf(saved) !== -1 ? saved : null;
  }

  function applyLang(lang) {
    if (LANGS.indexOf(lang) === -1) lang = "en";
    document.documentElement.setAttribute("lang", lang);
    document.querySelectorAll("[data-" + lang + "]").forEach(function (el) {
      var val = el.getAttribute("data-" + lang);
      if (val !== null) el.innerHTML = val;
    });
    document.querySelectorAll("[data-" + lang + "-ph]").forEach(function (el) {
      el.setAttribute("placeholder", el.getAttribute("data-" + lang + "-ph"));
    });
    document.querySelectorAll(".lang-menu button").forEach(function (b) {
      b.classList.toggle("active", b.getAttribute("data-lang") === lang);
    });
    var label = document.querySelector(".lang-btn .lang-label");
    if (label) label.textContent = lang.toUpperCase();
    var flagSlot = document.querySelector(".lang-btn .lang-flag");
    if (flagSlot && FLAG_SVG[lang]) {
      var tmp = document.createElement("div");
      tmp.innerHTML = FLAG_SVG[lang];
      flagSlot.replaceWith(tmp.firstChild);
    }
    try { localStorage.setItem("am-lang", lang); } catch (e) {}
  }

  function initLang() {
    var gate = document.getElementById("langGate");
    var saved = currentLang();
    if (saved) {
      if (gate) gate.classList.add("hidden");
      applyLang(saved);
    } else if (gate) {
      gate.classList.remove("hidden");
      gate.querySelectorAll("button[data-lang]").forEach(function (b) {
        b.addEventListener("click", function () {
          applyLang(b.getAttribute("data-lang"));
          gate.classList.add("hidden");
        });
      });
    } else {
      applyLang("en");
    }
    var sw = document.querySelector(".lang-switch");
    if (sw) {
      sw.querySelector(".lang-btn").addEventListener("click", function (e) {
        e.stopPropagation();
        sw.classList.toggle("open");
      });
      sw.querySelectorAll(".lang-menu button").forEach(function (b) {
        b.addEventListener("click", function () {
          applyLang(b.getAttribute("data-lang"));
          sw.classList.remove("open");
        });
      });
      document.addEventListener("click", function () { sw.classList.remove("open"); });
    }
  }

  /* ---------- Header ---------- */
  function initHeader() {
    var header = document.querySelector(".site-header");
    if (header) {
      window.addEventListener("scroll", function () {
        header.classList.toggle("scrolled", window.scrollY > 10);
      }, { passive: true });
    }
    var burger = document.querySelector(".nav-burger");
    var nav = document.querySelector(".main-nav");
    if (burger && nav) {
      burger.addEventListener("click", function () {
        burger.classList.toggle("open");
        nav.classList.toggle("open");
      });
    }
    document.querySelectorAll(".nav-item-drop").forEach(function (item) {
      var toggle = item.querySelector(".drop-toggle");
      if (!toggle) return;
      toggle.addEventListener("click", function (e) {
        e.stopPropagation();
        document.querySelectorAll(".nav-item-drop.open").forEach(function (o) {
          if (o !== item) o.classList.remove("open");
        });
        item.classList.toggle("open");
      });
    });
    document.addEventListener("click", function () {
      document.querySelectorAll(".nav-item-drop.open").forEach(function (o) { o.classList.remove("open"); });
    });
  }

  /* ---------- Reveal on scroll (class-based; always runs) ---------- */
  function initReveal() {
    var items = document.querySelectorAll(".reveal-item");
    if (!items.length) return;
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (i) { i.classList.add("revealed"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("revealed"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (i) { io.observe(i); });
  }

  /* ---------- Reviews marquee: shuffle + seamless infinite loop ---------- */
  function initMarquee() {
    var track = document.querySelector(".marquee-track");
    if (!track) return;
    var cards = Array.prototype.slice.call(track.children);
    for (var i = cards.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      track.appendChild(cards[j]);
      cards.splice(j, 1);
    }
    track.innerHTML += track.innerHTML; /* duplicate for seamless -50% loop */
  }

  /* ---------- FAQ accordion ---------- */
  function initFaq() {
    document.querySelectorAll(".faq-item").forEach(function (item) {
      var q = item.querySelector(".faq-q");
      var a = item.querySelector(".faq-a");
      if (!q || !a) return;
      q.addEventListener("click", function () {
        var open = item.classList.contains("open");
        document.querySelectorAll(".faq-item.open").forEach(function (o) {
          o.classList.remove("open");
          o.querySelector(".faq-a").style.maxHeight = null;
        });
        if (!open) {
          item.classList.add("open");
          a.style.maxHeight = a.scrollHeight + "px";
        }
      });
    });
  }

  /* ---------- Hero video fallback ---------- */
  function initHeroVideo() {
    var video = document.querySelector(".hero-media video");
    if (!video) return;
    video.addEventListener("error", function () { video.style.display = "none"; }, true);
    var src = video.querySelector("source");
    if (src) src.addEventListener("error", function () { video.style.display = "none"; });
  }

  /* ---------- Web3Forms contact ---------- */
  function initForm() {
    var form = document.getElementById("contactForm");
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      var btn = form.querySelector("button[type=submit]");
      btn.disabled = true;
      status.className = "form-status";
      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        body: new FormData(form)
      }).then(function (r) { return r.json(); }).then(function (data) {
        if (data.success) {
          status.classList.add("ok");
          status.textContent = status.getAttribute("data-ok") || "Thank you — we will be in touch shortly.";
          form.reset();
        } else { throw new Error(); }
      }).catch(function () {
        status.classList.add("err");
        status.textContent = status.getAttribute("data-err") || "Something went wrong. Please try again or call us.";
      }).finally(function () { btn.disabled = false; });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initLang();
    initHeader();
    initReveal();
    initMarquee();
    initFaq();
    initHeroVideo();
    initForm();
  });
})();
