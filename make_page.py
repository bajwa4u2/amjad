# Amjad M. Chaudhry, Strategic Member: his room in the company's house (The Record).
# Rules from the founder (2 Oct 2026): no timeline, his own voice, no bank named
# (outside-activity care with his employer), and his role at Aura Platform =
# financial judgement, small-business introductions, institutions and banks,
# building and leading teams. No personal email or address.
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = ('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400'
         '&family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap')
SCRIPTS = 'https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu&family=Noto+Serif+Devanagari&display=swap'
CO = 'https://company.auraplatform.org'
URL = 'https://amjad.auraplatform.org/'
TITLE = 'Amjad M. Chaudhry | Strategic Member, Aura Platform LLC'
DESC = ('Amjad M. Chaudhry, Strategic Member of Aura Platform LLC: financial judgement, introductions to small '
        'businesses, banks and institutions, and building the teams that serve them.')

LD = {"@context": "https://schema.org", "@type": "ProfilePage", "@id": URL + "#profilepage", "url": URL,
      "mainEntity": {"@type": "Person", "@id": URL + "#person", "name": "Amjad M. Chaudhry", "jobTitle": "Strategic Member",
                     "description": "Michigan banker in business banking, commercial lending and branch leadership; Strategic Member of Aura Platform LLC.",
                     "address": {"@type": "PostalAddress", "addressRegion": "MI", "addressCountry": "US"},
                     "worksFor": {"@type": "Organization", "@id": CO + "/#organization", "name": "Aura Platform LLC", "url": CO + "/"},
                     "sameAs": ["https://www.linkedin.com/in/amjad-mchaudhry-1b90a844"],
                     "knowsLanguage": ["en", "pa", "ur", "hi"],
                     "knowsAbout": ["Business banking", "Commercial lending", "Credit and risk", "Team leadership", "Small business"]}}

def word(text, lang, d, gloss):
    return f'<span class="word" lang="{lang}" dir="{d}"><b>{text}</b><small lang="en" dir="ltr">{gloss}</small></span>'

body = f'''<section class="hero" id="presence"><div class="wrap split">
  <div>
    <div class="ey">Strategic Member · Aura Platform LLC</div>
    <h1 class="h1">Banking, business relationships and <em class="tl">financial judgement.</em></h1>
    <p class="lede">My career has been Michigan banking: business banking, commercial lending and leading bank branches and their teams. At Aura Platform I bring that judgement, and the relationships behind it, to the work alongside the founder.</p>
    <div class="btns"><a class="b1 tlbg" href="#with-aura">What I do at Aura Platform</a><a class="b2" href="#conversation">Write to me</a></div>
  </div>
  <figure class="portrait"><img src="assets/images/leadership/amjad.png" alt="Amjad M. Chaudhry" width="1200" height="1600"><figcaption><b>Amjad M. Chaudhry</b>Strategic Member, Aura Platform LLC · Michigan</figcaption></figure>
</div></section>

<section class="sec" id="with-aura"><div class="wrap">
  <div class="ey">At Aura Platform</div>
  <h2 class="h2">Four things I bring <em class="tl">to the company.</em></h2>
  <p class="swipe-hint" aria-hidden="true">Swipe →</p>
  <div class="carry four">
    <div class="cc">
      <div class="mini-stage s-col"><span class="ed"><b>Risk</b> · <b>Price</b> · <b>Capital</b><br><span>Does the decision hold?</span></span></div>
      <h3>Financial judgement.</h3>
      <p>Credit, risk and the money side of each decision: how we price, where capital goes, and whether the numbers hold.</p>
    </div>
    <div class="cc">
      <div class="mini-stage s-orc"><span class="path"><i class="d">Referred</i><i class="d">Introduced</i><i class="n">Customer</i></span></div>
      <h3>Small-business introductions.</h3>
      <p>Through the networks banking builds, attorneys, accountants and community leaders, I open doors to the small businesses <a href="{CO}/orchestrate">Orchestrate</a> serves.</p>
    </div>
    <div class="cc">
      <div class="mini-stage s-aura"><span class="bubble">Our branch, on the record</span><span class="bubble me">Official</span></div>
      <h3>Institutions and banks.</h3>
      <p>I approach banks, credit unions and community institutions, to answer on <a href="{CO}/aura">Aura</a> in their own name and to partner with us.</p>
    </div>
    <div class="cc">
      <div class="mini-stage s-co lead"><span class="path"><i class="d">Hire</i><i class="d">Coach</i><i class="n">Lead</i></span></div>
      <h3>Building and leading teams.</h3>
      <p>Years of hiring and coaching branch teams, carried into the team Aura Platform builds as it grows.</p>
    </div>
  </div>
</div></section>

<section class="sec" id="banking"><div class="wrap split">
  <div>
    <div class="ey">Where it comes from · Michigan banking</div>
    <h2 class="h2">The work behind <em class="tl">a financial relationship.</em></h2>
    <p class="lede">I have looked after small-business customers, made commercial and SBA loans, managed credit portfolios and written credit recommendations, and led branch teams to the standards regulated banking demands. Most of it began with a referral: an attorney, an accountant, someone in the community who trusted the relationship.</p>
  </div>
  <div class="stage s-co creds" data-name="The practice">
    <ul>
      <li><b>Business banking</b></li>
      <li><b>Commercial and SBA lending</b></li>
      <li><b>Credit and portfolio judgement</b></li>
      <li><b>Leading branch teams</b></li>
    </ul>
  </div>
</div></section>

<section class="sec" id="roots"><div class="wrap split">
  <div>
    <div class="ey">Where it comes from · Pakistan and Michigan</div>
    <h2 class="h2">Economics, <em class="tl">in two countries.</em></h2>
    <p class="lede">I studied business economics in Pakistan and again at Eastern Michigan University. I work in English, Punjabi, Urdu and Hindi, which matters in the communities and businesses I serve.</p>
  </div>
  <div class="stage s-co words four" data-name="Languages I work in" data-needs-scripts>{word('English', 'en', 'ltr', 'English')}{word('پنجابی', 'pa-Arab', 'rtl', 'Punjabi')}{word('اردو', 'ur', 'rtl', 'Urdu')}{word('हिन्दी', 'hi', 'ltr', 'Hindi')}</div>
</div></section>

<section class="hero convo2" id="conversation"><div class="wrap split" data-convo data-mailto="amjad@auraplatform.org" data-salute="Amjad">
  <div class="c-left">
    <div class="ey">Write to me</div>
    <h2 class="h1">Talk it through <em class="tone">with me.</em></h2>
    <div class="founder-line"><img src="assets/images/leadership/amjad.png" alt="" width="56" height="56"><p><b>I read every note myself</b> and reply personally.</p></div>
    <p class="origin" data-origin hidden></p>
    <div class="c-tabs" role="tablist" aria-label="Why are you writing?">
      <button type="button" role="tab" data-intent="business" aria-selected="false">A business question</button>
      <button type="button" role="tab" data-intent="product" aria-selected="false">A product for my business</button>
      <button type="button" role="tab" data-intent="institution" aria-selected="false">Our bank or institution</button>
      <button type="button" role="tab" data-intent="partnership" aria-selected="false">Partner</button>
      <button type="button" role="tab" data-intent="unsure" aria-selected="false">Something else</button>
    </div>
    <div class="c-direct" data-direct hidden></div>
  </div>
  <div class="stage s-letter" data-name="Your note">
    <form class="letter-card" data-letter novalidate>
      <div class="lh"><span><b>A personal note</b><small>Read by me, answered by me</small></span><span data-date></span></div>
      <div class="lto"><small>To</small> Amjad M. Chaudhry · Aura Platform LLC</div>
      <div class="lsubj"><small>About</small> <span data-subject>A conversation</span></div>
      <div class="lbody" data-body></div>
      <button type="button" class="lmore" data-more aria-expanded="false" aria-controls="c-detail">Bringing something specific? <u>Add the details.</u></button>
      <div class="ldetail" id="c-detail" data-detail hidden>
        <label><small>What I'm bringing</small><textarea name="bringing" rows="1" placeholder="The question, product or proposal, in a line or two"></textarea></label>
        <label><small>Why now</small><textarea name="pitch" rows="2" placeholder="What makes this the right moment"></textarea></label>
        <label><small>A good first outcome would be</small><textarea name="outcome" rows="1" placeholder="The first thing that would show it is working"></textarea></label>
      </div>
      <div class="lsign"><span>With regards,</span><input name="name" id="c-name" autocomplete="name" required placeholder="Your name" aria-label="Your name"></div>
      <div class="lact"><button class="b1 tonebg" type="submit">Open in my email ↗</button><a class="b2" href="https://auraplatform.org/i/aura-platform-llc/meet/let-s-connect" target="_blank" rel="noopener">Or choose a time to talk ↗</a></div>
      <div class="attr" data-status><i></i><span>Sent from your own email. The note stays yours.</span></div>
    </form>
  </div>
</div></section>'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="author" content="Amjad M. Chaudhry">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="profile"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{DESC}"><meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}assets/social/og-default.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{URL}assets/social/og-default.png">
<link rel="icon" href="favicon.ico"><link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}"><meta name="script-fonts" content="{SCRIPTS}">
<link rel="stylesheet" href="record.css"><link rel="stylesheet" href="member.css">
<script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>
</head>
<body class="record founder member">
<a class="skip-link" href="#main">Skip to content</a>
<header class="rh fh-head" role="banner">
  <div class="wrap">
    <a class="rh-brand" href="#presence" aria-label="Amjad M. Chaudhry"><img src="assets/images/leadership/amjad.png" alt="" width="28" height="28">Amjad M. Chaudhry</a>
    <nav class="rh-nav" aria-label="Primary">
      <a href="#with-aura">At Aura Platform</a><a href="#banking">Banking</a><a href="{CO}" rel="noopener">Aura Platform LLC ↗</a>
    </nav>
    <a class="rh-cta" href="#conversation">Write to me</a>
    <button class="rh-menu" type="button" aria-expanded="false" aria-controls="rh-panel"><span></span><b class="sr-only">Menu</b></button>
  </div>
  <nav class="rh-panel" id="rh-panel" aria-label="Mobile primary">
    <a href="#with-aura">At Aura Platform</a><a href="#banking">Banking</a><a href="#roots">Economics and languages</a><a href="{CO}" rel="noopener">Aura Platform LLC ↗</a><a href="#conversation">Write to me</a>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="founder-footer" role="contentinfo">
  <div class="ff-cols">
    <nav aria-label="This page"><b>This page</b><a href="#with-aura">At Aura Platform</a><a href="#banking">Banking</a><a href="#roots">Economics and languages</a><a href="#conversation">Write to me</a></nav>
    <nav aria-label="Products"><b>Products</b><a href="{CO}/orchestrate" rel="noopener">Orchestrate ↗</a><a href="{CO}/aura" rel="noopener">Aura ↗</a><a href="{CO}/colophon" rel="noopener">Colophon ↗</a></nav>
    <nav aria-label="Company"><b>Company</b><a href="{CO}" rel="noopener">Aura Platform LLC ↗</a><a href="{CO}/films" rel="noopener">Films ↗</a><a href="{CO}/get" rel="noopener">Get the apps ↗</a></nav>
  </div>
  <small>© 2026 Amjad M. Chaudhry</small>
</footer>
<script src="record.js" defer></script>
</body>
</html>
'''
with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('page written')
