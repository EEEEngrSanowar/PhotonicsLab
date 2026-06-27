import os

OUT = "/home/claude/photonic-lab"

NAV = """<header class="navbar">
  <div class="nav-inner">
    <a href="index.html" class="brand">
      <span class="brand-mark"></span> Photonic Intelligence Lab
    </a>
    <nav class="nav-links">
      <a href="index.html" data-page="index">Home</a>
      <a href="research.html" data-page="research">Research</a>
      <a href="people.html" data-page="people">People</a>
      <a href="publications.html" data-page="publications">Publications</a>
      <a href="projects.html" data-page="projects">Projects</a>
      <a href="news.html" data-page="news">News</a>
      <a href="join.html" data-page="join">Join Us</a>
      <a href="contact.html" data-page="contact">Contact</a>
      <button class="theme-toggle">🌙 Dark</button>
    </nav>
    <button class="nav-toggle">☰</button>
  </div>
</header>
"""

FOOTER = """<footer>
  <div class="brand" style="justify-content:center;color:#fff;">
    <span class="brand-mark"></span> Photonic Intelligence Laboratory
  </div>
  <div class="footer-links">
    <a href="https://github.com/" target="_blank">GitHub</a>
    <a href="https://scholar.google.com/" target="_blank">Google Scholar</a>
    <a href="https://linkedin.com/" target="_blank">LinkedIn</a>
    <a href="mailto:lab@example.edu">Email</a>
  </div>
  <p>Department of Electrical Engineering · North Dakota State University</p>
  <p class="copyright">© 2026 Photonic Intelligence Laboratory. All rights reserved.</p>
</footer>
"""

def page(title, desc, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Photonic Intelligence Laboratory</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{NAV}
{body}
{FOOTER}
<script src="js/script.js"></script>
<script>
document.querySelector('[data-page="{active}"]').classList.add('active');
</script>
</body>
</html>
"""

pages = {}

# ---------------- INDEX ----------------
pages["index.html"] = page(
    "Home", "Integrated Photonics Lab — silicon photonics, neuromorphic computing, and AI hardware research.",
    "index",
    """
<section class="hero">
  <div class="container">
    <h1>Integrated Photonics Lab</h1>
    <p>Advancing silicon photonics, neuromorphic computing, and AI hardware for next-generation intelligent systems.</p>
    <div class="btn-row">
      <a href="research.html" class="btn btn-primary">Explore Our Research</a>
      <a href="publications.html" class="btn btn-outline">View Publications</a>
      <a href="join.html" class="btn btn-outline">Join Our Lab</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Research Areas</h2>
    <p class="section-sub">We work at the intersection of photonics, computing, and machine learning.</p>
    <div class="grid">
      <div class="card">
        <div class="icon"></div>
        <h3>Silicon Photonics</h3>
        <p>Design of integrated photonic devices for communication, sensing, and computing.</p>
      </div>
      <div class="card">
        <div class="icon"></div>
        <h3>Photonic Integrated Circuits</h3>
        <p>Large-scale PIC design using silicon, silicon nitride, and heterogeneous integration.</p>
      </div>
      <div class="card">
        <div class="icon"></div>
        <h3>Neuromorphic Computing</h3>
        <p>Brain-inspired computing architectures built from optical devices.</p>
      </div>
      <div class="card">
        <div class="icon"></div>
        <h3>Optical Reservoir Computing</h3>
        <p>High-speed physical information processing for speech recognition and time-series prediction.</p>
      </div>
      <div class="card">
        <div class="icon"></div>
        <h3>Machine Learning for Photonics</h3>
        <p>Inverse design, optimization, and data-driven photonic system development.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 class="section-title">Latest News</h2>
    <div class="list-item"><span class="date">JUNE 2026</span><p>Lab website launched.</p></div>
    <div class="list-item"><span class="date">JUNE 2026</span><p>Looking for motivated PhD and MS students — see Join Us.</p></div>
    <div class="list-item"><span class="date">MAY 2026</span><p>New research direction launched on photonic reservoir computing for spoken digit recognition.</p></div>
    <div style="text-align:center; margin-top:24px;">
      <a href="news.html" class="btn btn-primary" style="background:var(--primary); color:#fff;">All News</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Featured Publications</h2>
    <div class="pub-item">
      <h4>Integrated Optical Reservoir Computing for Speech Recognition</h4>
      <p class="venue">In preparation — 2026</p>
    </div>
    <div class="pub-item">
      <h4>Role of Delay-Times in Delay-Based Photonic Reservoir Computing (study notes)</h4>
      <p class="venue">Reference: Hülser et al., Optical Materials Express, 2022</p>
    </div>
  </div>
</section>
"""
)

# ---------------- RESEARCH ----------------
pages["research.html"] = page(
    "Research", "Research areas of the Integrated Photonics Lab.",
    "research",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>Research</h1><p>Interdisciplinary work spanning photonics, neuromorphic systems, and machine learning.</p></div>
</section>

<section class="section">
  <div class="container">
    <div class="grid">
      <div class="card">
        <h3>Silicon Photonics</h3>
        <p>Integrated photonic devices fabricated using CMOS-compatible processes.</p>
        <span class="tag">Waveguides</span><span class="tag">Ring Resonators</span><span class="tag">Grating Couplers</span><span class="tag">MZI Devices</span>
      </div>
      <div class="card">
        <h3>Neuromorphic Photonics</h3>
        <p>Photonic systems inspired by biological neural networks.</p>
        <span class="tag">Optical Neural Networks</span><span class="tag">Spiking Photonics</span><span class="tag">Analog Optical Computing</span>
      </div>
      <div class="card">
        <h3>Optical Reservoir Computing</h3>
        <p>Physical computing using nonlinear, delay-based optical systems.</p>
        <span class="tag">Speech Recognition</span><span class="tag">Time-Series Prediction</span><span class="tag">RF Signal Processing</span>
      </div>
      <div class="card">
        <h3>Integrated AI Hardware</h3>
        <p>Energy-efficient hardware accelerators built on photonic integrated circuits.</p>
      </div>
      <div class="card">
        <h3>Machine Learning for Photonics</h3>
        <p>AI-assisted photonic device optimization.</p>
        <span class="tag">Inverse Design</span><span class="tag">Bayesian Optimization</span><span class="tag">Neural Networks</span>
      </div>
    </div>
  </div>
</section>
"""
)

# ---------------- PEOPLE ----------------
pages["people.html"] = page(
    "People", "Meet the members of the Integrated Photonics Lab.",
    "people",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>People</h1><p>Our principal investigator and graduate researchers.</p></div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Principal Investigator</h2>
    <div class="grid" style="max-width:340px;margin:0 auto 60px;">
      <div class="person">
        <div class="avatar"></div>
        <h3>Dr. M. Jobayer Hossain</h3>
        <p class="role">Assistant Professor, School of Electrical Engineering & Computer Science (SEECS)</p>
        <p>Research interests: Photonic Integrated Circuits (PICs), Reconfigurable PICs, Quantum PICs, Optical Interconnects, AI Accelerators, Photonic Neuromorphic Computing, Space & Satellite Technologies.</p>
      </div>
    </div>

    <h2 class="section-title">Graduate Students</h2>
    <div class="grid">
      <div class="person">
        <div class="avatar"></div>
        <h3>Md Sanowar Hossain</h3>
        <p class="role">PhD Student</p>
        <p>Reservoir Computing · Neuromorphic Photonics · Silicon Photonics · Machine Learning</p>
      </div>
      <div class="person" style="opacity:0.6;">
        <div class="avatar"></div>
        <h3>Open Position</h3>
        <p class="role">PhD / MS Student</p>
        <p>We are recruiting — see the Join Us page.</p>
      </div>
    </div>
  </div>
</section>
"""
)

# ---------------- PUBLICATIONS ----------------
pages["publications.html"] = page(
    "Publications", "Publications from the Integrated Photonics Lab.",
    "publications",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>Publications</h1><p>Journal articles, conference papers, and preprints.</p></div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">2026</h2>
    <div class="pub-item">
      <h4>Integrated Optical Reservoir Computing for Speech Recognition</h4>
      <p class="venue">In preparation</p>
      <div class="pub-links"><a href="#">PDF</a><a href="#">DOI</a><a href="#">BibTeX</a></div>
    </div>
    <div class="pub-item">
      <h4>Silicon Photonic Neural Networks</h4>
      <p class="venue">Target venue: OFC 2026</p>
      <div class="pub-links"><a href="#">PDF</a><a href="#">BibTeX</a></div>
    </div>
    <div class="pub-item">
      <h4>Integrated Neuromorphic Photonic Computing</h4>
      <p class="venue">Target venue: CLEO</p>
      <div class="pub-links"><a href="#">PDF</a></div>
    </div>
  </div>
</section>
"""
)

# ---------------- PROJECTS ----------------
pages["projects.html"] = page(
    "Projects", "Active research projects in the Integrated Photonics Lab.",
    "projects",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>Projects</h1><p>Current and ongoing research initiatives.</p></div>
</section>

<section class="section">
  <div class="container">
    <div class="grid">
      <div class="card">
        <h3>Optical Reservoir Computing Platform</h3>
        <p>Time-multiplexed, delay-based photonic reservoir computing for spoken digit recognition.</p>
        <span class="tag">Status: Active</span><span class="tag">Funding: Pending</span>
      </div>
      <div class="card">
        <h3>Photonic Neural Network Accelerator</h3>
        <p>Hardware-efficient optical neural network architectures.</p>
        <span class="tag">Status: Active</span>
      </div>
      <div class="card">
        <h3>Silicon Photonic AI Chips</h3>
        <p>Integrated chip-scale designs for AI inference acceleration.</p>
        <span class="tag">Status: Ongoing</span>
      </div>
    </div>
  </div>
</section>
"""
)

# ---------------- NEWS ----------------
pages["news.html"] = page(
    "News", "Latest news from the Integrated Photonics Lab.",
    "news",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>News</h1><p>Lab announcements and updates.</p></div>
</section>

<section class="section">
  <div class="container">
    <div class="list-item"><span class="date">JUNE 2026</span><p>Lab website launched.</p></div>
    <div class="list-item"><span class="date">JUNE 2026</span><p>Sanowar joined the lab as a PhD student.</p></div>
    <div class="list-item"><span class="date">MAY 2026</span><p>New paper accepted for OFC 2026.</p></div>
    <div class="list-item"><span class="date">APRIL 2026</span><p>Lab officially launched.</p></div>
  </div>
</section>
"""
)

# ---------------- JOIN ----------------
pages["join.html"] = page(
    "Join Us", "Open positions in the Integrated Photonics Lab.",
    "join",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>Join Us</h1><p>We are recruiting motivated PhD and MS students.</p></div>
</section>

<section class="section">
  <div class="container">
    <p style="max-width:680px;margin:0 auto 32px;text-align:center;">
      We welcome applications from students interested in silicon photonics, AI hardware, optical computing,
      neuromorphic computing, and machine learning. Please email the lab with the following:
    </p>
    <div class="grid" style="max-width:680px;margin:0 auto;">
      <div class="card"><h3>CV</h3><p>Your most recent curriculum vitae.</p></div>
      <div class="card"><h3>Transcript</h3><p>Unofficial transcript is acceptable for initial review.</p></div>
      <div class="card"><h3>Research Interests</h3><p>A short statement on your background and interests.</p></div>
    </div>
    <div style="text-align:center;margin-top:32px;">
      <a href="contact.html" class="btn btn-primary" style="background:var(--primary);color:#fff;">Contact the Lab</a>
    </div>
  </div>
</section>
"""
)

# ---------------- CONTACT ----------------
pages["contact.html"] = page(
    "Contact", "Contact the Integrated Photonics Lab.",
    "contact",
    """
<section class="hero" style="padding:70px 24px;">
  <div class="container"><h1>Contact</h1><p>School of Electrical Engineering & Computer Science, University of North Dakota.</p></div>
</section>

<section class="section">
  <div class="container">
    <div class="grid" style="grid-template-columns: 1fr 1fr; align-items:start;">
      <div>
        <h3 style="color:var(--primary);margin-bottom:12px;">Address</h3>
        <p>Integrated Photonics Lab<br>
        School of Electrical Engineering & Computer Science<br>
        Leonard Hall, Room No. 42<br>
        University of North Dakota<br>
        81 Cornell St Stop 8153<br>
        Grand Forks, ND 58202-8153, USA</p>
        <h3 style="color:var(--primary);margin:20px 0 12px;">Email</h3>
        <p><a href="mailto:lab@example.edu" style="color:var(--accent);">lab@example.edu</a></p>
      </div>
      <div class="form-box">
        <form onsubmit="handleContactSubmit(event)">
          <label>Name</label>
          <input type="text" required>
          <label>Email</label>
          <input type="email" required>
          <label>Message</label>
          <textarea rows="4" required></textarea>
          <button type="submit" class="btn btn-primary" style="background:var(--primary);color:#fff;border:none;cursor:pointer;">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""
)

for fname, content in pages.items():
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated:", list(pages.keys()))
