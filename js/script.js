// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {

  // ---------- Auto-inject navbar on every page (skip if page already has one) ----------
  if (!document.querySelector('.navbar')) {
    var currentPage = document.body.dataset.page || '';
    var nav = document.createElement('header');
    nav.className = 'navbar';
    nav.innerHTML = `
      <div class="nav-inner">
        <a href="index.html" class="brand">
          <span class="brand-mark"></span> UND GLIDE Lab
        </a>
        <nav class="nav-links">
          <a href="index.html" data-page="index">Home</a>
          <a href="research.html" data-page="research">Research</a>
          <a href="people.html" data-page="people">People</a>
          <a href="publications.html" data-page="publications">Publications</a>
          <a href="facilities.html" data-page="facilities">Facilities</a>
          <a href="funding.html" data-page="funding">Funding</a>
          <a href="outreach.html" data-page="outreach">Outreach</a>
          <button class="theme-toggle">🌙 Dark</button>
        </nav>
        <button class="nav-toggle">☰</button>
      </div>
    `;
    document.body.insertBefore(nav, document.body.firstChild);
    if (currentPage) {
      var activeLink = nav.querySelector('[data-page="' + currentPage + '"]');
      if (activeLink) activeLink.classList.add('active');
    }
  }

  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
  }
  // Dark mode
  var themeBtn = document.querySelector('.theme-toggle');
  var saved = localStorage.getItem('lab-theme');
  if (saved === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    if (themeBtn) themeBtn.textContent = '☀️ Light';
  }
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('lab-theme', 'light');
        themeBtn.textContent = '🌙 Dark';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('lab-theme', 'dark');
        themeBtn.textContent = '☀️ Light';
      }
    });
  }
  // Auto-inject footer on every page (skip if page already has one)
  if (!document.querySelector('footer')) {
    var footer = document.createElement('footer');
    footer.innerHTML = '<p class="copyright">© 2026 UND GLIDE Lab. All rights reserved.</p>';
    document.body.appendChild(footer);
  }
});
// Contact form (static demo - replace action with Formspree/Getform endpoint)
function handleContactSubmit(e) {
  e.preventDefault();
  alert('Thanks for reaching out! Replace this demo handler with a real form endpoint (e.g. Formspree) — see README.');
  e.target.reset();
}
