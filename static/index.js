const swup = new Swup({
  plugins: [
    new SwupOverlayTheme({
      color: "#2B2C3A",

    }),
  ],
});

swup.on("animationInStart", () => {
  document.documentElement.scrollTop = 0;
  document.getElementById('nav-toggle').checked = false;
});

swup.on("pageView", () => {
  (function () {
    var i,
      e,
      d = document,
      s = "script";
    i = d.createElement("script");
    i.async = 1;
    i.src =
      "https://cdn.curator.io/published/6b6062cf-6084-4cff-b779-b3169e306108.js";
    e = d.getElementsByTagName(s)[0];
    e.parentNode.insertBefore(i, e);
  })();
})