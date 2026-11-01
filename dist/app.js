const themeButton = document.querySelector('.theme-toggle');
function updateThemeButton() {
  const dark = document.documentElement.dataset.theme === 'dark';
  themeButton.setAttribute('aria-pressed', String(dark));
  themeButton.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} mode`);
  themeButton.querySelector('use').setAttribute('href', dark ? '#sun' : '#moon');
  document.querySelector('meta[name="theme-color"]').content = dark ? '#111823' : '#FAF8F3';
}
updateThemeButton();
themeButton.addEventListener('click', () => {
  const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = theme;
  try { localStorage.setItem('baseline-theme', theme); } catch (e) {}
  updateThemeButton();
});
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if ('IntersectionObserver' in window && !reducedMotion.matches) {
  document.documentElement.classList.add('motion-ready');
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
  }), { threshold: 0.07 });
  document.querySelectorAll('.reveal').forEach(section => observer.observe(section));
}
const carousel = document.querySelector('.carousel');
const previous = document.querySelector('.carousel-prev');
const next = document.querySelector('.carousel-next');
function updateCarousel() {
  previous.disabled = carousel.scrollLeft < 2;
  next.disabled = carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 2;
}
function moveCarousel(direction) {
  const distance = carousel.querySelector('figure').getBoundingClientRect().width + parseFloat(getComputedStyle(carousel).gap);
  carousel.scrollBy({left: direction * distance, behavior: reducedMotion.matches ? 'instant' : 'smooth'});
}
previous.addEventListener('click', () => moveCarousel(-1));
next.addEventListener('click', () => moveCarousel(1));
carousel.addEventListener('scroll', updateCarousel, {passive: true});
carousel.addEventListener('keydown', event => {
  if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
    event.preventDefault(); moveCarousel(event.key === 'ArrowRight' ? 1 : -1);
  }
});
new ResizeObserver(updateCarousel).observe(carousel);
updateCarousel();
