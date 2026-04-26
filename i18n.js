(function () {
  const KEY = "portfolio.lang";
  const supported = ["en", "no"];
  const fallback = "en";

  function getLang() {
    const stored = localStorage.getItem(KEY);
    if (stored && supported.includes(stored)) return stored;
    const nav = (navigator.language || "en").slice(0, 2).toLowerCase();
    return nav === "no" || nav === "nb" || nav === "nn" ? "no" : "en";
  }

  function applyLang(lang) {
    document.documentElement.lang = lang === "no" ? "nb" : "en";
    document.querySelectorAll("[data-en]").forEach((el) => {
      const text = el.dataset[lang] || el.dataset[fallback];
      if (text != null) el.textContent = text;
    });
    document.querySelectorAll("[data-en-html]").forEach((el) => {
      const html = el.dataset[lang + "Html"] || el.dataset[fallback + "Html"];
      if (html != null) el.innerHTML = html;
    });
    document.querySelectorAll(".lang-switch button").forEach((btn) => {
      btn.classList.toggle("is-active", btn.dataset.lang === lang);
      btn.setAttribute("aria-pressed", btn.dataset.lang === lang ? "true" : "false");
    });
  }

  function setLang(lang) {
    if (!supported.includes(lang)) lang = fallback;
    localStorage.setItem(KEY, lang);
    applyLang(lang);
  }

  document.addEventListener("DOMContentLoaded", function () {
    applyLang(getLang());
    document.querySelectorAll(".lang-switch button").forEach((btn) => {
      btn.addEventListener("click", () => setLang(btn.dataset.lang));
    });
  });
})();
