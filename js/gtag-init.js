/* Agnes Mortgage — Google Analytics 4 + Consent Mode v2
 *
 * Loaded early in <head> on every page (the reference is injected by
 * build-sitemap.js, so future ABB posts get it automatically).
 *
 * analytics_storage is DENIED by default. It is granted only when the
 * visitor presses Accept on the cookie banner (handled in scripts.js),
 * and that choice is remembered in localStorage('am-consent'). Until
 * then GA4 runs in cookieless Consent Mode — no analytics cookies set.
 */
(function () {
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;

  gtag("js", new Date());

  /* Default: everything that needs consent is denied up front. */
  gtag("consent", "default", {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied",
    functionality_storage: "granted",
    security_storage: "granted",
    wait_for_update: 500
  });

  /* Re-apply a previously saved acceptance before gtag.js finishes loading,
     so returning visitors who already accepted are measured immediately. */
  try {
    if (localStorage.getItem("am-consent") === "granted") {
      gtag("consent", "update", { analytics_storage: "granted" });
    }
  } catch (e) {}

  gtag("config", "G-ZR0EYLMEFF", { anonymize_ip: true });

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=G-ZR0EYLMEFF";
  document.head.appendChild(s);
})();
