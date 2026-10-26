"""Builds the Cut & Convert static pages into the site repo.
Usage: python3 build.py <repo_dir>
"""
import sys, pathlib

REPO = pathlib.Path(sys.argv[1])
HERE = pathlib.Path(__file__).parent
MARQUEE = (HERE / "marquee.html").read_text().replace('src="logos/', 'src="/logos/')

NAV = [
    ("/local/", "Local Business", "local"),
    ("/ecommerce/", "Ecommerce", "ecommerce"),
    ("/youtube-creative/", "YouTube Creative", "youtube"),
    ("/about/", "About", "about"),
]

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">
</head>
<body>
"""

LOGO = '<a class="logo" href="/" aria-label="Cut &amp; Convert home"><span>Cut</span><span class="amp">&amp;</span><span>Convert</span></a>'

def header(active):
    links = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if key == active else ""}>{label}</a>'
        for h, label, key in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap">
    {LOGO}
    <nav class="nav" aria-label="Main">
{links}
      <a class="btn btn-ink" href="#contact">Book a free audit</a>
    </nav>
  </div>
</header>
"""

def cta(title, sub, subject):
    return f"""
  <section class="section" id="contact">
    <div class="wrap">
      <div class="cta-box">
        <div>
          <h2>{title}</h2>
          <p>{sub}</p>
        </div>
        <a class="btn btn-ink" href="#contact">Book a free audit</a>
      </div>
    </div>
  </section>
"""

FOOTER = f"""
<footer class="site-footer">
  <div class="wrap">
    {LOGO}
    <nav class="footer-nav" aria-label="Footer">
      <a href="/local/">Local Business</a>
      <a href="/ecommerce/">Ecommerce</a>
      <a href="/youtube-creative/">YouTube Creative</a>
      <a href="/about/">About</a>
    </nav>
    <span>Google Ads &amp; YouTube Ads · San Diego, CA</span>
  </div>
</footer>
"""

SERVICE = {"local": "local", "ecommerce": "ecommerce", "youtube": "youtube"}

def page(path, title, desc, active, body, scripts=""):
    html = head(title, desc) + header(active) + "\n<main>\n" + body + "\n</main>\n" + FOOTER + scripts + "\n</body>\n</html>\n"
    svc = SERVICE.get(active)
    html = html.replace('href="#contact"', f'href="/contact/?service={svc}"' if svc else 'href="/contact/"')
    out = REPO / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out)

for name in ["home", "local", "ecommerce", "youtube", "about", "contact", "thanks"]:
    mod = {}
    exec((HERE / f"{name}.py").read_text(), {"MARQUEE": MARQUEE, "cta": cta}, mod)
    page(mod["PATH"], mod["TITLE"], mod["DESC"], mod["ACTIVE"], mod["BODY"], mod.get("SCRIPTS", ""))
