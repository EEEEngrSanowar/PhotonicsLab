
## Features

- Fully responsive (mobile nav menu)
- Dark / light mode toggle (saved in localStorage)
- UND-branded green color palette (`#009A44`)
- Research / People / Publications / Projects / News / Join Us / Contact pages
- Alumni section on the People page
- Card-based layout, easy to extend
- No dependencies, no Jekyll, no build step — works the moment you upload it

## Live Site

`https://eeeengrsanowar.github.io/PhotonicsLab/`

## Deploy to GitHub Pages (free hosting)

1. Create a new GitHub repository, e.g. `PhotonicsLab`.
2. Upload all files in this folder to the repo (keep the folder structure).
3. Go to **Settings → Pages** in your repo.
4. Under "Build and deployment", set **Source: Deploy from a branch**,
   branch: `main`, folder: `/ (root)`. Click **Save**.
5. After a minute, your site will be live at:
   `https://<your-username>.github.io/<repo-name>/`
   (If the repo is named `<your-username>.github.io`, the site will be at
   the root of that URL instead.)

## Customizing content

- **Text/colors:** edit the HTML files directly, or change the CSS variables
  at the top of `css/style.css` (`--primary`, `--accent`, `--bg`, etc.).
  Current palette uses UND Kelly Green `#009A44`.
- **Adding a person:** copy a `.person` block in `people.html`.
- **Adding a publication:** copy a `.pub-item` block in `publications.html`.
- **Adding news:** copy a `.list-item` block in `news.html` or `index.html`.
- **Team photos:** drop `.jpg` files into `Picture/` folder using the naming
  convention `firstname.jpg` (e.g. `sanowar.jpg`). Square photos work best
  (400×400 recommended) — they render as circular avatars.

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

## Contact

**Dr. M. Jobayer Hossain** — jobayer.hossain@UND.edu
GLIDE Lab, Leonard Hall Room 42
School of Electrical Engineering & Computer Science
University of North Dakota, Grand Forks, ND 58202

---

Website designed & developed by **Md Sanowar Hossain** (PhD Student, UND).
