/* Agnes Mortgage — calculators.js (loaded only on /calculators) */
(function () {
  "use strict";

  var gbp = function (n) {
    return "£" + Math.round(n).toLocaleString("en-GB");
  };

  /* ---------- tabs ---------- */
  document.querySelectorAll(".calc-tab").forEach(function (tab) {
    tab.addEventListener("click", function () {
      document.querySelectorAll(".calc-tab").forEach(function (t) { t.classList.remove("active"); });
      document.querySelectorAll(".calc-panel").forEach(function (p) { p.classList.remove("active"); });
      tab.classList.add("active");
      document.getElementById("panel-" + tab.getAttribute("data-panel")).classList.add("active");
    });
  });

  /* ---------- segmented controls ---------- */
  function segValue(id) {
    var active = document.querySelector("#" + id + " button.active");
    return active ? active.getAttribute("data-val") : null;
  }
  document.querySelectorAll(".calc-seg").forEach(function (seg) {
    seg.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        seg.querySelectorAll("button").forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        recalcAll();
      });
    });
  });

  /* ---------- range fill + live output ---------- */
  function bindRange(id, outId, fmt) {
    var el = document.getElementById(id);
    var out = document.getElementById(outId);
    if (!el) return;
    function update() {
      var pct = ((el.value - el.min) / (el.max - el.min)) * 100;
      el.style.setProperty("--fill", pct + "%");
      if (out) out.textContent = fmt(parseFloat(el.value));
      recalcAll();
    }
    el.addEventListener("input", update);
    update();
  }

  /* ---------- 1. repayment ---------- */
  function calcRepay() {
    var P = parseFloat(document.getElementById("repay-amount").value);
    var annual = parseFloat(document.getElementById("repay-rate").value) / 100;
    var years = parseInt(document.getElementById("repay-term").value, 10);
    var io = segValue("repay-type") === "io";
    var r = annual / 12, n = years * 12, monthly;
    if (io) {
      monthly = P * r;
    } else if (r === 0) {
      monthly = P / n;
    } else {
      monthly = P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
    }
    var total = io ? monthly * n + P : monthly * n;
    document.getElementById("repay-big").textContent = gbp(monthly);
    document.getElementById("repay-total").textContent = gbp(total);
    document.getElementById("repay-interest").textContent = gbp(total - P);
  }

  /* ---------- 2. borrowing ---------- */
  function calcBorrow() {
    var inc = parseFloat(document.getElementById("borrow-inc1").value) +
              parseFloat(document.getElementById("borrow-inc2").value);
    var typ = inc * 4.5, max = inc * 5.5;
    document.getElementById("borrow-big").textContent = gbp(inc * 4.0) + " – " + gbp(max);
    document.getElementById("borrow-typ").textContent = gbp(typ);
    document.getElementById("borrow-max").textContent = gbp(max);
  }

  /* ---------- 3. SDLT (England & NI, from April 2025) ---------- */
  function sdltBands(price, type) {
    var bands;
    if (type === "ftb" && price <= 500000) {
      bands = [[300000, 0], [500000, 0.05]];
    } else {
      bands = [[125000, 0], [250000, 0.02], [925000, 0.05], [1500000, 0.10], [Infinity, 0.12]];
    }
    var surcharge = type === "additional" ? 0.05 : 0;
    var rows = [], prev = 0, total = 0;
    for (var i = 0; i < bands.length; i++) {
      var cap = bands[i][0], rate = bands[i][1] + surcharge;
      var slice = Math.max(0, Math.min(price, cap) - prev);
      if (slice > 0 && rate > 0) {
        rows.push([prev, Math.min(price, cap), rate, slice * rate]);
        total += slice * rate;
      } else if (slice > 0 && rate === 0) {
        rows.push([prev, Math.min(price, cap), 0, 0]);
      }
      prev = cap;
      if (price <= cap) break;
    }
    return { total: total, rows: rows };
  }

  function calcSdlt() {
    var price = parseFloat(document.getElementById("sdlt-price").value);
    var type = segValue("sdlt-type");
    var res = sdltBands(price, type);
    document.getElementById("sdlt-big").textContent = gbp(res.total);
    var wrap = document.getElementById("sdlt-bands");
    wrap.innerHTML = res.rows.map(function (r) {
      return '<div class="calc-row"><span>' + gbp(r[0]) + " – " + gbp(r[1]) +
             " @ " + (r[2] * 100).toFixed(0) + "%</span><b>" + gbp(r[3]) + "</b></div>";
    }).join("");
  }

  /* ---------- 4. buy-to-let ICR ---------- */
  function calcBtl() {
    var value = parseFloat(document.getElementById("btl-value").value);
    var rent = parseFloat(document.getElementById("btl-rent").value);
    var tax = segValue("btl-tax");
    var stressRate = 0.055; // 5.5% stress test
    var icr = (tax === "higher") ? 1.45 : 1.25; // 125% basic/Ltd, 145% higher
    var ltv = 0.75;
    var loan = value * ltv;
    var deposit = value - loan;
    var monthlyMortgage = (loan * stressRate) / 12;
    var rentNeeded = monthlyMortgage * icr;
    var passes = rent >= rentNeeded;
    document.getElementById("btl-loan").textContent = gbp(loan);
    document.getElementById("btl-deposit").textContent = gbp(deposit);
    document.getElementById("btl-monthly").textContent = gbp(monthlyMortgage) + " / mo";
    document.getElementById("btl-needed").textContent = gbp(rentNeeded) + " / mo";
    document.getElementById("btl-big").textContent = passes ? "✓ Rent covers the mortgage" : "✗ Rent falls short";
    document.getElementById("btl-big").style.background = passes
      ? "linear-gradient(120deg,#7ecba1,#2ecc71)" : "linear-gradient(120deg,#e88,#c0392b)";
    document.getElementById("btl-big").style.webkitBackgroundClip = "text";
    document.getElementById("btl-big").style.backgroundClip = "text";
    document.getElementById("btl-big").style.color = "transparent";
  }

  function recalcAll() {
    try { calcRepay(); calcBorrow(); calcSdlt(); calcBtl(); } catch (e) {}
  }

  /* ---------- bind everything ---------- */
  var pct1 = function (v) { return v.toFixed(2).replace(/\.?0+$/, "") + "%"; };
  bindRange("repay-amount", "repay-amount-out", gbp);
  bindRange("repay-rate", "repay-rate-out", pct1);
  bindRange("repay-term", "repay-term-out", function (v) { return String(v); });
  bindRange("borrow-inc1", "borrow-inc1-out", gbp);
  bindRange("borrow-inc2", "borrow-inc2-out", gbp);
  bindRange("sdlt-price", "sdlt-price-out", gbp);
  bindRange("btl-value", "btl-value-out", gbp);
  bindRange("btl-rent", "btl-rent-out", gbp);

  recalcAll();
})();
