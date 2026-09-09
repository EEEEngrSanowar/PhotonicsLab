# UND GLIDE Lab Website

Static website for the **Guided Light Integration, Design, and Experimentation (GLIDE) Lab** at the University of North Dakota, led by Dr. M. Jobayer Hossain.

🌐 **Live site:** [glidephotonics.org](https://glidephotonics.org)

---

## Overview

The GLIDE Lab works on photonic integrated circuits for computing, sensing, and communication — with active research in silicon photonics, photonic neuromorphic computing, reservoir computing, quantum photonics, LiDAR, and signal manipulation.

This repository hosts the source for the lab's public website, built with plain HTML, CSS, and JavaScript and served through GitHub Pages.

---

## Site Structure

    PhotonicsLab/
    ├── index.html              # Home — hero, about, image slider, latest news, contact
    ├── research.html           # Research areas with figures and related publications
    ├── people.html             # PI, graduate students, and alumni
    ├── publications.html       # Journal, conference, and preprint list
    ├── facilities.html         # Software, lab equipment, and fabrication
    ├── funding.html            # Grants and awards
    ├── news.html               # Full news feed
    ├── outreach.html           # Lab outings and gallery
    │
    ├── css/
    │   └── style.css           # Global styles (colors, layout, typography)
    │
    ├── js/
    │   └── script.js           # Auto-injects navbar + footer, handles dark mode & mobile menu
    │
    ├── Images/
    │   ├── Index Page/         # Home page slider photos
    │   ├── People Page/        # Member headshots
    │   ├── Research Page/      # Figures for each research area
    │   └── Outreach Page/      # Gallery photos
    │
    ├── glide-logo2.png         # Lab logo (used in navbar and footer)
    ├── CNAME                   # Custom domain (glidephotonics.org)
    ├── build_site.py           # Optional build/helper script
    └── README.md

---

## How It Works

**Navbar and footer are injected via JavaScript.** Every HTML page loads `js/script.js`, which:

- Injects a consistent navbar (with active-link highlighting based on the page's `data-page` attribute on `<body>`)
- Injects the footer with the copyright line
- Handles the mobile menu toggle and light/dark theme switcher

This means **editing the menu or footer is a one-line change in `js/script.js`** — no need to touch every HTML file.

To highlight the active menu item, each page's `<body>` tag carries its page name:

    <body data-page="research">

---

## Making Changes

### Adding a news item

Edit both:

1. `news.html` — full feed
2. `index.html` — Latest News section on the home page (top 4 items only)

### Adding a publication

Edit `publications.html`. Follow the existing format:

    <div class="pub-item">
      <h4>Paper Title</h4>
      <p class="authors">Author list</p>
      <p class="venue">Venue, Year</p>
    </div>

### Adding a new person

Edit `people.html` under the appropriate section (Principal Investigator, Graduate Students, or Alumni). Photos live in `Images/People Page/`.

### Adding a research area

Edit `research.html`. Copy an existing `<div class="research-area">` block, update the title, description, image paths (in `Images/Research Page/`), and related publications list. Also add the section to the "Quick jump nav" at the top.

### Changing the menu

Edit the `nav.innerHTML` template inside `js/script.js`. The change propagates to every page automatically.

### Changing site-wide colors or typography

Edit the CSS variables in the `:root` block at the top of `css/style.css`. The primary color (`--primary`) is UND Kelly Green (`#009A44`).

---

## Deployment

The site deploys automatically to GitHub Pages from the `main` branch. Any commit to `main` is live at [glidephotonics.org](https://glidephotonics.org) within a minute.

---

## Contact

**Dr. M. Jobayer Hossain**  
Assistant Professor, School of Electrical Engineering & Computer Science  
University of North Dakota  
📧 jobayer.hossain@UND.edu  
📞 701.777.6270

---

*Website designed and developed by [Md Sanowar Hossain](https://eeeengrsanowar.github.io/MdSanowarHossain/) (PhD Student at UND).*
