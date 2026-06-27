# Photonic Intelligence Laboratory — Website

A clean, modern, responsive static website for a university photonics/neuromorphic
computing research lab. No build tools required — plain HTML/CSS/JS, ready for
GitHub Pages.

## Structure

```
photonic-lab/
├── index.html
├── research.html
├── people.html
├── publications.html
├── projects.html
├── news.html
├── join.html
├── contact.html
├── css/style.css
├── js/script.js
└── images/   (put photos/logo here)
```

## Features

- Fully responsive (mobile nav menu)
- Dark / light mode toggle (saved in localStorage)
- Research / People / Publications / Projects / News / Join Us / Contact pages
- Card-based layout, easy to extend
- No dependencies, no Jekyll, no build step — works the moment you upload it

## Deploy to GitHub Pages (free hosting)

1. Create a new GitHub repository, e.g. `photonic-lab`.
2. Upload all files in this folder to the repo (keep the folder structure).
3. Go to **Settings → Pages** in your repo.
4. Under "Build and deployment", set **Source: Deploy from a branch**,
   branch: `main`, folder: `/ (root)`. Click **Save**.
5. After a minute, your site will be live at:
   `https://<your-username>.github.io/photonic-lab/`

   (If the repo is named `<your-username>.github.io`, the site will be at
   the root of that URL instead.)

## Customizing content

- **Text/colors:** edit the HTML files directly, or change the CSS variables
  at the top of `css/style.css` (`--primary`, `--accent`, `--bg`, etc.).
- **Adding a person:** copy a `.person` block in `people.html`.
- **Adding a publication:** copy a `.pub-item` block in `publications.html`.
- **Adding news:** copy a `.list-item` block in `news.html` or `index.html`.
- **Logo/photos:** drop image files into `images/`, then replace the
  `.brand-mark` / `.avatar` divs with `<img src="images/yourfile.jpg">`.

## Contact form

The contact form in `contact.html` currently shows a demo alert (see
`js/script.js`, `handleContactSubmit`). To make it actually send email without
a backend server, sign up for a free service like
[Formspree](https://formspree.io) or [Getform](https://getform.io), then
replace the `<form onsubmit="handleContactSubmit(event)">` tag with:

```html
<form action="https://formspree.io/f/your-form-id" method="POST">
```

and remove the `onsubmit` handler.

## Regenerating the site (optional)

`build_site.py` (not needed for deployment) was used to generate the HTML
pages from shared header/footer templates. If you want to add a new page
with the same nav/footer, you can adapt that script instead of editing every
HTML file by hand.
