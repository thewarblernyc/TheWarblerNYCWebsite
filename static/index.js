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
