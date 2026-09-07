// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {
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
