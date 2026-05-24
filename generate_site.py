import os
import shutil

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# Clean existing site directory
if os.path.exists(BASE_DIR):
    shutil.rmtree(BASE_DIR)
os.makedirs(BASE_DIR, exist_ok=True)

# Copy static assets (images, fonts, etc.) from source to site
if os.path.exists("assets/images"):
    shutil.copytree("assets/images", os.path.join(BASE_DIR, "assets/images"), dirs_exist_ok=True)
if os.path.exists("assets/cv"):
    shutil.copytree("assets/cv", os.path.join(BASE_DIR, "assets/cv"), dirs_exist_ok=True)

def write(path, content):
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# CSS
css_content = """
:root {
  --color-bg: #faf9f6;
  --color-surface: #ffffff;
  --color-text: #171717;
  --color-text-muted: #6b7280;
  --color-accent-primary: #374151;
  --color-accent-secondary: #d1d5db;
  --color-border: rgba(0, 0, 0, 0.08);
  --color-overlay: rgba(0, 0, 0, 0.03);
  
  --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
}

:root[data-theme="dark"] {
  --color-bg: #1a1a1a;
  --color-surface: #262626;
  --color-text: #f3f4f6;
  --color-text-muted: #9ca3af;
  --color-accent-primary: #d1d5db;
  --color-accent-secondary: #4b5563;
  --color-border: rgba(255, 255, 255, 0.10);
  --color-overlay: rgba(255, 255, 255, 0.04);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-main);
  background-color: var(--color-bg);
  color: var(--color-text);
  line-height: 1.7;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
}

a { color: var(--color-accent-primary); text-decoration: none; transition: opacity 0.15s ease; }
a:hover { text-decoration: underline; }

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
  overflow-x: hidden;
}
@media (min-width: 480px) { .container { padding: 0 24px; } }
@media (min-width: 768px) { .container { padding: 0 48px; } }
@media (min-width: 1024px) { .container { padding: 0 80px; } }

/* Prevent horizontal overflow globally */
html, body { overflow-x: hidden; max-width: 100%; }

/* Typography */
h1 { font-size: 26px; font-weight: 500; line-height: 1.2; margin-top: 0; margin-bottom: 40px; display: flex; align-items: center; }
h1::before {
  content: '';
  display: block;
  width: 40px;
  height: 2px;
  background-color: #EAB308;
  margin-right: 16px;
  flex-shrink: 0;
}
h2 { font-size: 21px; font-weight: 500; line-height: 1.3; margin-top: 0; margin-bottom: 20px; }
h3 { font-size: 18px; font-weight: 500; line-height: 1.4; margin-top: 0; margin-bottom: 16px; }

@media(min-width: 768px) {
  h1 { font-size: 32px; }
  h2 { font-size: 24px; }
}
@media(min-width: 1024px) {
  h1 { font-size: 40px; }
  h2 { font-size: 28px; }
  h3 { font-size: 20px; }
}

/* Hero name: start at comfortable mobile size */
.text-hero-name { font-size: 28px; font-weight: 500; line-height: 1.15; margin-bottom: 24px; display: flex; align-items: center; flex-wrap: wrap; gap: 0; }
.text-hero-name::before {
  content: '';
  display: block;
  width: 36px;
  height: 2px;
  background-color: #EAB308;
  margin-right: 16px;
  flex-shrink: 0;
}
.text-hero-statement { font-size: 16px; font-weight: 400; line-height: 1.8; color: var(--color-text-muted); max-width: 680px; }
@media(min-width: 480px) {
  .text-hero-name { font-size: 32px; margin-bottom: 32px; }
  .text-hero-statement { font-size: 17px; }
}
@media(min-width: 768px) {
  .text-hero-name { font-size: 40px; margin-bottom: 40px; }
  .text-hero-statement { font-size: 19px; }
}
@media(min-width: 1024px) {
  .text-hero-name { font-size: 52px; margin-bottom: 48px; }
  .text-hero-statement { font-size: 22px; }
}

.section-title {
  font-size: 15px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.10em;
  color: var(--color-text);
  margin-top: 48px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
}
@media(min-width: 768px) {
  .section-title { font-size: 18px; margin-top: 72px; }
}
.section-title::before {
  content: '';
  display: block;
  width: 32px;
  height: 2px;
  background-color: #EAB308;
  margin-right: 16px;
  flex-shrink: 0;
}

.reading-width {
  max-width: 680px;
}

/* Section block: consistent readable text container */
.section-block {
  max-width: 680px;
}
.section-block p {
  margin-bottom: 20px;
  line-height: 1.8;
  font-size: 15px;
}
.section-block p:last-child { margin-bottom: 0; }

.body-lg { font-size: 18px; }
.text-muted { color: var(--color-text-muted); }
.text-micro { font-size: 11px; }

/* Layout / Spacing */
section { padding: 48px 0; }
@media(min-width: 768px) { section { padding: 72px 0; } }
@media(min-width: 1024px) { section { padding: 120px 0; } }

/* Header & Nav */
.site-header {
  padding: 24px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: transparent;
  transition: background-color 0.25s ease-out, box-shadow 0.25s ease-out;
  border-top: 3px solid #EAB308;
}
.site-header.is-sticky {
  background-color: var(--color-bg);
  box-shadow: 0 1px 0 var(--color-border);
}
.site-header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo { font-weight: 500; font-size: 18px; }

.main-nav { display: none; }
.lang-switcher { font-size: 12px; font-weight: 500; }
.lang-switcher a { color: var(--color-text-muted); text-decoration: none; padding: 4px; }
.lang-switcher a.active { color: var(--color-text); font-weight: 600; }

.theme-toggle {
  background: none; border: none; color: var(--color-text); font-size: 18px; cursor: pointer;
  margin-left: 16px; padding: 4px; display: flex; align-items: center; justify-content: center;
}

.menu-toggle, .menu-toggle-close {
  background: none; border: none; color: var(--color-text); font-size: 24px; cursor: pointer;
  display: block; padding: 8px; min-width: 44px; min-height: 44px;
  display: flex; align-items: center; justify-content: center;
}

@media(min-width: 1024px) {
  .main-nav {
    display: flex; gap: 24px; flex-wrap: wrap;
  }
  .main-nav a {
    color: var(--color-text); font-size: 14px; font-weight: 500; text-decoration: none;
  }
  .main-nav a:hover { color: var(--color-accent-primary); text-decoration: none; }
  .main-nav a.active { color: var(--color-accent-primary); }
  .menu-toggle { display: none; }
}

/* Mobile Nav Overlay */
.mobile-nav-overlay {
  display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: var(--color-bg); z-index: 200; padding: 24px;
  flex-direction: column;
}
.mobile-nav-overlay.is-open { display: flex; }
.mobile-nav-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; }
.mobile-nav-links { display: flex; flex-direction: column; gap: 24px; font-size: 24px; font-weight: 500; }
.mobile-nav-links a { color: var(--color-text); text-decoration: none; }

/* Grid */
.grid-3 { display: grid; grid-template-columns: 1fr; gap: 24px; }
.grid-4 { display: grid; grid-template-columns: 1fr; gap: 24px; }
.grid-5 { display: grid; grid-template-columns: 1fr; gap: 16px; }

@media(min-width: 480px) {
  .grid-5 { grid-template-columns: repeat(2, 1fr); }
}
@media(min-width: 768px) {
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
  .grid-4 { grid-template-columns: repeat(2, 1fr); gap: 24px; }
  .grid-5 { grid-template-columns: repeat(3, 1fr); }
}
@media(min-width: 1024px) {
  .grid-4 { grid-template-columns: repeat(4, 1fr); }
  .grid-5 { grid-template-columns: repeat(5, 1fr); }
}

/* Cards */
.card {
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 6px;
  overflow: hidden;
  transition: border-color 0.2s ease;
  display: block;
  color: inherit;
}
.card:hover {
  border-color: var(--color-accent-primary);
  text-decoration: none;
}
.card-img-placeholder {
  background-color: var(--color-border);
  aspect-ratio: 4/3;
  display: flex; align-items: center; justify-content: center;
  color: var(--color-text-muted); font-size: 14px;
}
.card-content { padding: 20px; }

.tag {
  display: inline-block;
  font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em;
  background-color: rgba(234,179,8,0.12); color: var(--color-accent-secondary);
  padding: 4px 10px; border-radius: 3px; margin-bottom: 12px;
}

/* Interest Cards */
.interest-card {
  padding: 0;
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 6px;
  overflow: hidden;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}
.interest-card:hover {
  transform: translateY(-4px);
  border-color: var(--color-accent-primary);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}
.interest-img {
  width: 100%;
  aspect-ratio: 1/1;
  background-color: #FFF;
  overflow: hidden;
  border-bottom: 1px solid var(--color-border);
}
.interest-img img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 20px;
  transition: transform 0.5s ease;
}
.interest-card:hover .interest-img img {
  transform: scale(1.05);
}
.interest-card-content {
  padding: 16px;
  flex-grow: 1;
}
.interest-card h3 { 
  font-size: 14px; 
  font-weight: 600; 
  margin-bottom: 6px; 
  text-transform: uppercase; 
  letter-spacing: 0.05em; 
  word-wrap: break-word;
  overflow-wrap: break-word;
  line-height: 1.4;
}
.interest-card p { font-size: 13px; color: var(--color-text-muted); line-height: 1.5; }

.process-step {
  padding: 32px 24px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
  background-color: var(--color-surface);
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.process-step:hover {
  transform: scale(1.05);
  border-color: #EAB308;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.06);
  position: relative;
  z-index: 10;
}
.process-step p { font-size: 14px; color: var(--color-text-muted); line-height: 1.65; margin: 0; }
.process-title {
  border: 1px solid var(--color-border);
  padding: 8px 16px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  text-transform: uppercase;
  border-radius: 2px;
  align-self: flex-start;
  margin-bottom: 8px;
}
/* Forms */
.form-group { margin-bottom: 24px; }
label { display: block; font-size: 13px; font-weight: 500; margin-bottom: 6px; }
input[type="text"], input[type="email"], textarea {
  width: 100%; padding: 12px 16px; font-size: 16px; font-family: inherit;
  background-color: var(--color-surface); color: var(--color-text);
  border: 1.5px solid var(--color-border); border-radius: 4px;
  transition: border-color 0.15s ease;
}
textarea { min-height: 120px; resize: vertical; }
input:focus, textarea:focus { border-color: var(--color-accent-primary); outline: none; }

.btn {
  display: inline-block; padding: 12px 24px; font-size: 14px; font-weight: 500;
  border-radius: 4px; cursor: pointer; transition: background-color 0.15s ease, transform 0.1s ease;
  text-decoration: none; text-align: center; border: none;
}
.btn-primary {
  background-color: var(--color-accent-primary); color: #FFF;
}
.btn-primary:hover { opacity: 0.9; text-decoration: none; color: #FFF; }
.btn-primary:active { transform: scale(0.98); }

.btn-secondary {
  background-color: transparent; border: 1.5px solid var(--color-accent-primary);
  color: var(--color-accent-primary);
}
.btn-secondary:hover { background-color: var(--color-overlay); text-decoration: none; }

/* Footer */
.site-footer {
  margin-top: 96px; padding: 48px 0;
  border-top: 1px solid var(--color-border);
}
.footer-content {
  display: flex; flex-direction: column; gap: 24px; align-items: center;
}
.footer-nav { display: flex; gap: 24px; }
.footer-nav a { color: var(--color-text-muted); font-size: 14px; }
.copyright { color: var(--color-text-muted); font-size: 12px; }

@media(min-width: 768px) {
  .footer-content { flex-direction: row; justify-content: space-between; }
}

/* CV Layout */
.cv-row {
  padding: 48px 0;
  border-bottom: 1px solid var(--color-border);
}
.cv-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}
.cv-label {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text);
}
.cv-content {
  font-size: 15px;
  line-height: 1.75;
  color: var(--color-text);
}
.cv-content strong { font-weight: 600; }
.cv-block { max-width: 760px; }

/* Architectural CV accents */
.cv-dot-list { list-style: none; padding: 0; margin: 0; }
.cv-dot-list li {
  position: relative;
  padding-left: 24px;
  margin-bottom: 12px;
}
.cv-dot-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 10px;
  width: 6px;
  height: 1px;
  background-color: #EAB308;
}
.cv-icon-wrap {
  color: #EAB308;
  opacity: 0.8;
}
.cv-icon-wrap svg { width: 16px; height: 16px; display: block; }

/* Project Cards */
.project-list { display: flex; flex-direction: column; gap: 0; max-width: 1000px; }
.project-card {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0;
  padding: 48px 0;
  border-bottom: 1px solid var(--color-border);
}
@media(min-width: 720px) {
  .project-card { grid-template-columns: 360px 1fr; gap: 48px; align-items: start; }
}
.project-img {
  background-color: var(--color-border);
  aspect-ratio: 4/3;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 24px;
}
@media(min-width: 720px) { .project-img { margin-bottom: 0; } }
.project-img img { width: 100%; height: 100%; object-fit: cover; display: block; }
.project-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}
.project-tag {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  padding: 6px 12px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
}
.project-title {
  font-size: 24px;
  font-weight: 500;
  margin-bottom: 16px;
  line-height: 1.3;
}
.project-desc {
  font-size: 15px;
  line-height: 1.75;
  color: var(--color-text-muted);
  margin-bottom: 16px;
}
.project-result {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text);
  padding-left: 12px;
  border-left: 2px solid #EAB308;
}
.mb-2 { margin-bottom: 8px; }
.mb-4 { margin-bottom: 16px; }
.mb-6 { margin-bottom: 24px; }
.mb-8 { margin-bottom: 32px; }
.mb-10 { margin-bottom: 40px; }
.mt-4 { margin-top: 16px; }
.mt-8 { margin-top: 32px; }
.flex { display: flex; }
.gap-4 { gap: 16px; }
.items-center { align-items: center; }
.hidden { display: none; }
"""

write("assets/css/style.css", css_content)

js_theme = """
// theme.js
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('theme-toggle');
  
  if (toggleBtn) {
    const updateIcon = () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      toggleBtn.textContent = isDark ? '☀' : '☾';
    };
    
    updateIcon();
    
    toggleBtn.addEventListener('click', () => {
      const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateIcon();
    });
  }
});
"""
write("assets/js/theme.js", js_theme)

js_nav = """
// nav.js
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const menuToggle = document.querySelector('.menu-toggle');
  const menuClose = document.querySelector('.menu-toggle-close');
  const overlay = document.querySelector('.mobile-nav-overlay');
  
  // Sticky header
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('is-sticky');
    } else {
      header.classList.remove('is-sticky');
    }
  });

  if (menuToggle && overlay && menuClose) {
    menuToggle.addEventListener('click', () => {
      overlay.classList.add('is-open');
    });
    menuClose.addEventListener('click', () => {
      overlay.classList.remove('is-open');
    });
  }
});
"""
write("assets/js/nav.js", js_nav)

write("assets/js/nav.js", js_nav)

# Language data
LANGS = {
    'sk': {
        'nav_home': 'Domov', 'nav_about': 'O mne', 'nav_projects': 'Projekty', 'nav_cv': 'CV', 'nav_contact': 'Kontakt',
        'nav_privacy': 'Ochrana údajov',
        'urls': {'home': '/', 'about': '/o-mne.html', 'projects': '/projekty/', 'cv': '/cv.html', 'contact': '/kontakt.html', 'privacy': '/ochrana-udajov.html'},
        'hero_stmt': 'Som stavebná inžinierka so zameraním na pozemné stavby, architektúru a BIM modelovanie rekonštrukcií. Venujem sa projektovej príprave s dôrazom na presnosť, prehľadný výstup a zmysluplné technické riešenia.',
        'sec_focus': 'Zameranie', 'sec_process': 'Ako pracujem', 'sec_projects': 'Projekty', 'sec_interests': 'Mimo práce', 'sec_contact': 'Ozvite sa',
        'intro_focus_1': 'V praxi sa venujem projekcii stavieb a BIM modelovaniu, najmä pri rekonštrukciách, kde je dôležité porozumieť existujúcemu stavu a citlivo naň nadviazať návrhom.',
        'intro_focus_2': 'Pracujem prioritne v prostredí Archicad a pri zdieľaní dokumentácie a koordinácii využívam aj platformu Dalux. Digitálny model vnímam ako pracovný nástroj pre presnejšie rozhodovanie a lepšiu spoluprácu.',
        'intro_focus_3': 'Záleží mi na tom, aby výsledok nebol len formálne správny, ale aj praktický, čitateľný a použiteľný v reálnom procese prípravy a realizácie stavby.',
        'step_1_title': 'Analýza', 'step_1_desc': 'Pochopenie existujúceho stavu — miesto, konštrukcia, kontext a obmedzenia.',
        'step_2_title': 'Návrh', 'step_2_desc': 'Vývoj koncepcie — funkčné, priestorové a konštrukčné rozhodnutia.',
        'step_3_title': 'BIM Model', 'step_3_desc': 'Tvorba digitálneho modelu — koordinácia, kontrola kolízií, vizualizácia.',
        'step_4_title': 'Dokumentácia', 'step_4_desc': 'Spracovanie projektovej dokumentácie — výkresy, rezy, detaily, špecifikácie.',
        'process_cta_text': 'Zaujíma vás výsledok mojej práce? Pozrite si kompletné portfólio s ukážkami realizácií, BIM modelov a technických riešení.',
        'process_cta_btn': 'Zobraziť projekty',
        'projects_intro': 'Vybrané projekty z oblasti rekonštrukcií a projektovej dokumentácie.',
        'projects_empty': 'Projekty pripravujem. Prvé prípadové štúdie pribudnú čoskoro.',
        'projects_all': 'Všetky projekty →',
        'meta_desc': 'Osobné portfólio Ing. Zuzany Vaškovej. Odborníčka na stavebné projektovanie, rekonštrukcie a BIM modelovanie v Archicade.',
        'meta_about': 'Spoznajte Ing. Zuzanu Vaškovú — stavebnú inžinierku so zameraním na BIM a rekonštrukcie.',
        'meta_projects': 'Prehľad projektov Ing. Zuzany Vaškovej. Ukážky BIM modelovania a technickej dokumentácie rekonštrukcií.',
        'meta_cv': 'Profesijný profil a životopis Ing. Zuzany Vaškovej. Skúsenosti v oblasti stavebníctva a architektúry.',
        'meta_contact': 'Kontaktujte Ing. Zuzanu Vaškovú pre spoluprácu na projektoch alebo odborné konzultácie v oblasti BIM.',
        'meta_privacy': 'Informácie o ochrane osobných údajov na stránke Ing. Zuzany Vaškovej.',
        'cards': [
            {'title':'Beh', 'desc':'Pohyb, pri ktorom si vyčistím hlavu a držím rytmus.', 'img': 'running.png', 'alt': 'Minimalistická ilustrácia bežiaceho muža - symbol vytrvalosti a rytmu'},
            {'title':'Lyžovanie', 'desc':'Dynamika, sústredenie a radosť z pohybu.', 'img': 'skiing.png', 'alt': 'Technická ilustrácia lyžiara na svahu s vrstevnicami hôr'},
            {'title':'Volejbal', 'desc':'Tímovosť, energia a prirodzený balans k práci.', 'img': 'volleyball.png', 'alt': 'Geometrický náčrt volejbalovej siete a lopty - symbol tímovej spolupráce'},
            {'title':'Fotografovanie', 'desc':'Všímavosť k detailu, svetlu a kompozícii.', 'img': 'photography.png', 'alt': 'Architektonický nákres fotoaparátu s dôrazom na technický detail'},
            {'title':'Jazyky a cestovanie', 'desc':'Spoznávanie nových krajín, kultúr a budovanie rozhľadu.', 'img': 'travel_v5.svg', 'alt': 'Grafická štúdia kufra, glóbusu a lietadla - symbol cestovania a rozhľadu'},
            {'title':'Turistika', 'desc':'Aktívny oddych v horách a objavovanie nových výhľadov.', 'img': 'hiking_v5.svg', 'alt': 'Lineárna ilustrácia hôr, kompasu a batohu - symbol aktívneho oddychu'}
        ],
        'projects_list': [
            {
                'title': 'Freising',
                'tags': ['BYTOVÝ DOM', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'freising.jpg',
                'desc': 'Spracovanie projektovej dokumentácie od pôvodného stavu, búracích prác až po nový stav a konštrukčné detaily, vrátane nastavenia parametrov projektu pre sw Nevaris a Bexel.',
                'result': '40 bytov v zrekonštruovanej pamiatkovo chránenej budove v Nemecku.'
            },
            {
                'title': 'Eversbuschstrasse',
                'tags': ['BYTOVÝ DOM', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'eversbuschstrasse.png',
                'desc': 'Spracovanie projektovej dokumentácie od pôvodného stavu, búracích prác až po nový stav a konštrukčné detaily, vrátane dokumentácie pre záhradu a okolie.',
                'result': 'Rekonštrukcia bytového komplexu v Nemecku — 900 m² obytnej plochy, 9 luxusných bytov, 5 bytov pre seniorov.'
            },
            {
                'title': 'Rodinný dom',
                'tags': ['RODINNÝ DOM', 'NOVOSTAVBA', 'ARCHICAD'],
                'img': 'rodinny_dom.jpg',
                'desc': 'Spracovanie návrhu, architektonickej štúdie a projektu pre stavebné povolenie.',
                'result': 'Moderný dvojpodlažný rodinný dom s plochou strechou, dreveným obkladom a integrovanou garážou.'
            },
            {
                'title': 'Eichstätt',
                'tags': ['BYTOVÝ DOM', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'eichstatt.jpg',
                'desc': 'Spracovanie projektovej dokumentácie od pôvodného stavu, búracích prác až po nový stav a konštrukčné detaily, vrátane nastavenia parametrov projektu pre sw Nevaris a Bexel.',
                'result': '44 bytov a 8 kancelárskych priestorov v zrekonštruovanej pamiatkovo chránenej budove v nemeckom meste Eichstätt.'
            },
            {
                'title': 'Královice',
                'tags': ['BYTOVÝ KOMPLEX', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'kralovice.jpg',
                'desc': 'Vypracovanie kompletnej projektovej dokumentácie hlavnej budovy zahŕňajúcej existujúci stav, búracie práce, navrhovaný stav a konštrukčné detaily, ako aj dokumentácie menších novostavieb a riešenia exteriéru záhrady.',
                'result': '8 mezonetových bytov so záhradkou a parkovacím miestom v pražskej časti Královice.'
            },
            {
                'title': 'RD Stropkov',
                'tags': ['RODINNÝ DOM', 'NOVOSTAVBA', 'ARCHICAD', 'LUMION'],
                'img': 'stropkov.jpg',
                'desc': 'Vytvorenie 3D modelu rodinného domu na základe výkresovej dokumentácie, návrh a vizualizácia exteriéru vrátane záhrady.',
                'result': 'Komplex 3 jednopodlažných rodinných domov s veľkou záhradou, bazénom a prístreškom.'
            },
            {
                'title': 'Prosiek',
                'tags': ['VÍKENDOVÁ CHATA', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'prosiek.jpg',
                'desc': 'Spracovanie projektovej dokumentácie a BIM modelu búracích prác aj nového stavu pre realizáciu stavby.',
                'result': 'Víkendová chata s vnútorným bazénom a vonkajšou saunou na Liptove.'
            },
            {
                'title': 'Wasserburger Landstraße',
                'tags': ['APARTMÁNOVÝ DOM', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'wasserburger.jpg',
                'desc': 'Vytvorenie BIM modelu existujúcej stavby po rekonštrukcii na účely kalkulácie rozpočtu stavby.',
                'result': '21 apartmánov v polyfunkčnej budove s obchodom na prízemí.'
            },
            {
                'title': 'Schnaitsee',
                'tags': ['BYTOVÝ KOMPLEX', 'REKONŠTRUKCIA', 'ARCHICAD'],
                'img': 'schnaitsee.jpg',
                'desc': 'Vytvorenie BIM modelu existujúcej stavby po rekonštrukcii na účely kalkulácie rozpočtu stavby.',
                'result': '13 bytov v bytovom komplexe s parkoviskom v typickej bavorskej dedine.'
            }
        ],
        'contact_intro': 'Ak vás moja práca oslovila alebo riešite projekt, pri ktorom by sa zišla presnosť, technické myslenie a cit pre návrh, pokojne sa mi ozvite.',
        'label_name': 'Meno', 'label_email': 'E-mail', 'label_msg': 'Správa', 'btn_send': 'Odoslať správu',
        'privacy_note': 'Odoslaním formulára súhlasíte so spracovaním údajov v rozsahu potrebnom na odpoveď na vašu správu.',
        'title_about': 'O mne', 'about_p1': 'Som stavebná projektantka so zameraním na rekonštrukcie, projektovú dokumentáciu a BIM modelovanie. Pracujem v oblasti, kde sa stretáva technická presnosť s návrhárskym myslením.',
        'about_p2': 'K rekonštrukciám ma priťahuje práca s tým, čo už existuje — pochopenie konštrukcie, kontextu a obmedzení pred tým, než sa začne navrhovať niečo nové.',
        'about_p3': 'BIM vnímam ako metodiku, nie len ako softvér. Digitálny model mi umožňuje overovať riešenia, koordinovať profesie a pracovať s vyššou presnosťou.',
        'about_p4': 'V práci si cením presnosť, zrozumiteľnosť a praktickosť. Dobrá dokumentácia nie je formalita — je to základ pre kvalitný výsledok na stavbe.',
        'about_p5': 'Mimo práce ma nabíjajú hory, šport a fotografovanie. Slovenské hory sú môj pravidelný cieľ.',
        'title_cv': 'Životopis', 'btn_download': 'Stiahnuť PDF',
        'cv_edu': 'Technická univerzita v Košiciach, Stavebná fakulta — Pozemné stavby a architektúra, bakalárske štúdium, ukončené štátnou skúškou 17. 6. 2021. Nadväzujúce štúdium v odbore Pozemné stavby v rokoch 2021 až 2023. Gymnázium Stropkov, ukončené maturitnou skúškou v roku 2017.', 'cv_exp': 'Stavebná inžinierka so zameraním na projekciu stavieb a BIM modelovanie rekonštrukcií. V praxi sa venujem projektovej príprave, digitálnemu spracovaniu stavieb a práci s technickou dokumentáciou, s dôrazom na presnosť, prehľadnosť a praktické využitie výstupov.', 'cv_sw': 'Archicad, Dalux, Allplan, Lumion, BIMx, Adobe Photoshop, Adobe Lightroom.',
        'cv_profile_title': 'Profil',
        'cv_education_title': 'Vzdelanie',
        'cv_education_list': [
            {
                'time': '2021 — 2023',
                'title': 'Technická univerzita v Košiciach',
                'subtitle': 'Stavebná fakulta',
                'desc': 'Nadväzujúce inžinierske štúdium v odbore <strong>Pozemné stavby</strong>. Dôraz na navrhovanie nosných konštrukcií, fyziku budov a pokročilú projektovú prípravu.'
            },
            {
                'time': '2017 — 2021',
                'title': 'Technická univerzita v Košiciach',
                'subtitle': 'Stavebná fakulta',
                'desc': 'Bakalárske štúdium v odbore <strong>Pozemné stavby a architektúra</strong>, úspešne ukončené štátnou skúškou 17. 6. 2021.'
            },
            {
                'time': '2013 — 2017',
                'title': 'Gymnázium Stropkov',
                'subtitle': 'Všeobecné stredoškolské vzdelanie',
                'desc': 'Ukončené maturitnou skúškou v roku 2017 so zameraním na prírodné vedy a technické základy.'
            }
        ],
        'cv_skills_title': 'Softvér & Zručnosti',
        'cv_skills_list': [
            {
                'name': 'Archicad',
                'role': 'Hlavný projekčný nástroj, pokročilé 3D BIM modelovanie a dokumentácia.',
                'level': 95,
                'icon': 'archicad'
            },
            {
                'name': 'Dalux',
                'role': 'CDE platforma, koordinácia, prezeranie BIM modelov priamo na stavbe.',
                'level': 85,
                'icon': 'dalux'
            },
            {
                'name': 'Allplan',
                'role': 'BIM modelovanie, vystužovanie, presné stavebné konštrukcie.',
                'level': 80,
                'icon': 'allplan'
            },
            {
                'name': 'Lumion',
                'role': 'Fotorealistické 3D vizualizácie architektúry a exteriérov.',
                'level': 85,
                'icon': 'lumion'
            },
            {
                'name': 'BIMx',
                'role': 'Prezentačné 3D modely a prechádzky, interaktívna koordinácia.',
                'level': 90,
                'icon': 'bimx'
            },
            {
                'name': 'Photoshop',
                'role': 'Postprodukcia výkresov, koláže, finálna úprava vizualizácií.',
                'level': 80,
                'icon': 'photoshop'
            },
            {
                'name': 'Lightroom',
                'role': 'Úprava a spracovanie fotografií, organizácia digitálneho portfólia.',
                'level': 75,
                'icon': 'lightroom'
            },
            {
                'name': 'Canva',
                'role': 'Tvorba grafických podkladov, prezentácií a vizuálnych materiálov na komunikáciu projektov.',
                'level': 85,
                'icon': 'canva'
            }
        ],
        'cv_sidebar_docs_title': 'Dokumenty',
        'cv_sidebar_format_label': 'Formát',
        'cv_sidebar_size_label': 'Veľkosť',
        'cv_sidebar_lang_label': 'Jazyk',
        'cv_sidebar_lang_val': 'Slovenský',
        'cv_sidebar_updated_label': 'Aktualizované',
        'cv_sidebar_updated_val': 'Máj 2026',
        'cv_sidebar_img_alt': 'Architektonický výkres rezidencie - BIM modelovanie rekonštrukcie',
        'title_contact': 'Kontakt', 'contact_page_intro': 'Ak riešite projekt, spoluprácu alebo sa chcete spojiť kvôli profesijnej príležitosti, budem rada, ak sa mi ozvete. Uprednostňujem vecnú a príjemnú komunikáciu s jasným zámerom.',
        'title_privacy': 'Ochrana osobných údajov', 'privacy_intro': 'Táto stránka vysvetľuje, aké osobné údaje zbierať pri návšteve webu vaskova.space a ako sú tieto údaje používané.',
        'privacy_content_full': '''
            <h2>Prevádzkovateľ</h2>
            <p>Prevádzkovateľom osobných údajov je Ing. Zuzana Vašková. Vaše údaje spracúvam v súlade s nariadením GDPR.</p>
            
            <h2>Rozsah a účel spracovania</h2>
            <p>Cez kontaktný formulár zbieram vaše meno a e-mailovú adresu výhradne za účelom odpovede na vašu otázku alebo dopyt. Tieto údaje neposkytujem tretím stranám a neukladám ich do žiadnej marketingovej databázy.</p>
            
            <h2>Súbory cookies</h2>
            <p>Tento web používa výhradne technické (nevyhnutné) súbory cookies, ktoré slúžia na správne fungovanie stránky (napr. zapamätanie si zvoleného farebného režimu alebo jazyka). Nepoužívam žiadne analytické ani reklamné cookies tretích strán.</p>
            
            <h2>Vaše práva</h2>
            <p>Máte právo kedykoľvek požiadať o informáciu o tom, aké údaje o vás spracúvam, požiadať o ich opravu alebo vymazanie. V prípade otázok ma kontaktujte na e-mailovej adrese uvedenej v sekcii Kontakt.</p>
        ''',
        '404_title': 'Stránka sa nenašla.', '404_back': 'Späť na úvod →'
    },
    'en': {
        'nav_home': 'Home', 'nav_about': 'About', 'nav_projects': 'Projects', 'nav_cv': 'CV', 'nav_contact': 'Contact',
        'nav_privacy': 'Privacy Policy',
        'urls': {'home': '/en/', 'about': '/en/about.html', 'projects': '/en/projects/', 'cv': '/en/cv.html', 'contact': '/en/contact.html', 'privacy': '/en/privacy-policy.html'},
        'hero_stmt': 'I am a civil engineer specializing in building construction, architecture, and BIM modeling of reconstructions. I focus on project preparation with an emphasis on accuracy, clear output, and meaningful technical solutions.',
        'sec_focus': 'Focus', 'sec_process': 'How I work', 'sec_projects': 'Projects', 'sec_interests': 'Outside work', 'sec_contact': 'Get in touch',
        'intro_focus_1': 'In practice, I focus on building design and BIM modeling, especially in reconstructions, where it is important to understand the existing condition and sensitively build upon it with a proposal.',
        'intro_focus_2': 'I work primarily in the Archicad environment and also use the Dalux platform for sharing documentation and coordination. I see the digital model as a working tool for more accurate decision-making and better collaboration.',
        'intro_focus_3': 'It is important to me that the result is not only formally correct but also practical, readable, and usable in the real process of project preparation and construction.',
        'step_1_title': 'Analysis', 'step_1_desc': 'Understanding the existing condition — site, construction, context, and constraints.',
        'step_2_title': 'Design', 'step_2_desc': 'Concept development — functional, spatial, and structural decisions.',
        'step_3_title': 'BIM Model', 'step_3_desc': 'Creating the digital model — coordination, collision check, visualization.',
        'step_4_title': 'Documentation', 'step_4_desc': 'Processing project documentation — drawings, sections, details, specifications.',
        'process_cta_text': 'Are you interested in the results of my work? View my complete portfolio of BIM models and technical solutions.',
        'process_cta_btn': 'View projects',
        'projects_intro': 'Selected projects in reconstruction and project documentation.',
        'projects_empty': 'Projects are being prepared. The first case studies will appear soon.',
        'projects_all': 'All projects →',
        'meta_desc': 'Personal portfolio of Ing. Zuzana Vašková. Specialist in civil engineering, reconstructions, and BIM modeling in Archicad.',
        'meta_about': 'Meet Ing. Zuzana Vašková — a civil engineer focused on BIM and reconstructions.',
        'meta_projects': 'Overview of projects by Ing. Zuzana Vašková. Showcase of BIM modeling and technical documentation for reconstructions.',
        'meta_cv': 'Professional profile and CV of Ing. Zuzana Vašková. Experience in civil engineering and architecture.',
        'meta_contact': 'Contact Ing. Zuzana Vašková for project collaboration or professional consulting in BIM.',
        'meta_privacy': 'Privacy policy information for the website of Ing. Zuzana Vašková.',
        'cards': [
            {'title':'Running', 'desc':'A way to clear my head and keep a steady rhythm.', 'img': 'running.png', 'alt': 'Minimalist illustration of a running person - symbol of endurance and rhythm'},
            {'title':'Skiing', 'desc':'Dynamics, focus, and the joy of movement.', 'img': 'skiing.png', 'alt': 'Technical illustration of a skier on a slope with mountain contour lines'},
            {'title':'Volleyball', 'desc':'Team spirit, energy, and a natural balance to work.', 'img': 'volleyball.png', 'alt': 'Geometric sketch of a volleyball net and ball - symbol of teamwork'},
            {'title':'Photography', 'desc':'Attention to detail, light, and composition.', 'img': 'photography.png', 'alt': 'Architectural drawing of a camera focusing on technical detail'},
            {'title':'Languages and Travel', 'desc':'Exploring new countries, cultures, and broadening horizons.', 'img': 'travel_v5.svg', 'alt': 'Graphic study of a suitcase, globe, and airplane - symbol of travel and perspective'},
            {'title':'Hiking', 'desc':'Active relaxation in the mountains and discovering new views.', 'img': 'hiking_v5.svg', 'alt': 'Linear illustration of mountains, compass, and backpack - symbol of active recreation'}
        ],
        'projects_list': [
            {
                'title': 'Freising',
                'tags': ['RESIDENTIAL BUILDING', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'freising.jpg',
                'desc': 'Processing of project documentation from the original state and demolition works to the new state and structural details, including setting project parameters for Nevaris and Bexel software.',
                'result': '40 apartments in a reconstructed heritage-protected building in Germany.'
            },
            {
                'title': 'Eversbuschstrasse',
                'tags': ['RESIDENTIAL BUILDING', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'eversbuschstrasse.png',
                'desc': 'Processing of project documentation from the original state and demolition works to the new state and structural details, including documentation for the garden and surroundings.',
                'result': 'Reconstruction of a residential complex in Germany — 900 m² of living space, 9 luxury apartments, 5 apartments for seniors.'
            },
            {
                'title': 'Family House',
                'tags': ['FAMILY HOUSE', 'NEW BUILD', 'ARCHICAD'],
                'img': 'rodinny_dom.jpg',
                'desc': 'Preparation of the design, architectural study, and project for a building permit.',
                'result': 'Modern two-story family house with a flat roof, wood cladding, and integrated garage.'
            },
            {
                'title': 'Eichstätt',
                'tags': ['RESIDENTIAL BUILDING', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'eichstatt.jpg',
                'desc': 'Processing of project documentation from the original state and demolition works to the new state and structural details, including setting project parameters for Nevaris and Bexel software.',
                'result': '44 apartments and 8 office spaces in a reconstructed heritage-protected building in the German town of Eichstätt.'
            },
            {
                'title': 'Královice',
                'tags': ['RESIDENTIAL COMPLEX', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'kralovice.jpg',
                'desc': 'Preparation of complete project documentation for the main building including existing state, demolition works, proposed state and structural details, as well as documentation for smaller new builds and garden exterior design.',
                'result': '8 maisonette apartments with a private garden and parking space in the Prague district of Královice.'
            },
            {
                'title': 'RD Stropkov',
                'tags': ['FAMILY HOUSE', 'NEW BUILD', 'ARCHICAD', 'LUMION'],
                'img': 'stropkov.jpg',
                'desc': 'Creation of a 3D model of a family house based on drawing documentation, design, and visualization of the exterior including the garden.',
                'result': 'A complex of 3 single-story family houses with a large garden, swimming pool, and carport.'
            },
            {
                'title': 'Prosiek',
                'tags': ['WEEKEND CABIN', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'prosiek.jpg',
                'desc': 'Processing of project documentation and BIM model of demolition works and new state for construction execution.',
                'result': 'A weekend cabin with an indoor swimming pool and an outdoor sauna in the Liptov region.'
            },
            {
                'title': 'Wasserburger Landstraße',
                'tags': ['APARTMENT BUILDING', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'wasserburger.jpg',
                'desc': 'Creation of a BIM model of the existing building after reconstruction for the purpose of construction budget calculation.',
                'result': '21 apartments in a mixed-use building with a shop on the ground floor.'
            },
            {
                'title': 'Schnaitsee',
                'tags': ['RESIDENTIAL COMPLEX', 'RECONSTRUCTION', 'ARCHICAD'],
                'img': 'schnaitsee.jpg',
                'desc': 'Creation of a BIM model of the existing building after reconstruction for the purpose of construction budget calculation.',
                'result': '13 apartments in a residential complex with a parking lot in a typical Bavarian village.'
            }
        ],
        'contact_intro': 'If my work speaks to you, or if you are dealing with a project that needs precision, technical thinking, and sensitivity to design, feel free to get in touch.',
        'label_name': 'Name', 'label_email': 'E-mail', 'label_msg': 'Message', 'btn_send': 'Send message',
        'privacy_note': 'By submitting the form, you agree to the processing of your data to the extent necessary to respond to your message.',
        'title_about': 'About me', 'about_p1': 'I am a structural designer specializing in reconstructions, project documentation, and BIM modeling. I work in a field where technical precision meets design thinking.',
        'about_p2': 'I am drawn to reconstructions because of the work with what already exists — understanding the structure, context, and constraints before proposing something new.',
        'about_p3': 'I see BIM as a methodology, not just software. The digital model allows me to verify solutions, coordinate trades, and work with higher accuracy.',
        'about_p4': 'In my work, I value precision, clarity, and practicality. Good documentation is not a formality — it is the foundation for a quality result on the construction site.',
        'about_p5': 'Outside of work, I recharge in the mountains, through sports, and photography. The Slovak mountains are my regular destination.',
        'title_cv': 'CV', 'btn_download': 'Download PDF',
        'cv_edu': 'Technical University of Košice, Faculty of Civil Engineering — Building Construction and Architecture, Bachelor studies, completed with state exam on June 17, 2021. Follow-up studies in the field of Building Construction from 2021 to 2023. Gymnasium Stropkov, completed with school-leaving exam in 2017.', 'cv_exp': 'Civil engineer focusing on building design and BIM modeling of reconstruction projects. In practice, I deal with project preparation, digital processing of buildings, and technical documentation, with an emphasis on accuracy, clarity, and practically usable outputs.', 'cv_sw': 'Archicad, Dalux, Allplan, Lumion, BIMx, Adobe Photoshop, Adobe Lightroom.',
        'cv_profile_title': 'Profile',
        'cv_education_title': 'Education',
        'cv_education_list': [
            {
                'time': '2021 — 2023',
                'title': 'Technical University of Košice',
                'subtitle': 'Faculty of Civil Engineering',
                'desc': 'Follow-up Master\'s studies in the field of <strong>Building Construction</strong>. Specialization in structural design, building physics, and advanced project preparation.'
            },
            {
                'time': '2017 — 2021',
                'title': 'Technical University of Košice',
                'subtitle': 'Faculty of Civil Engineering',
                'desc': 'Bachelor\'s studies in the field of <strong>Building Construction and Architecture</strong>, successfully completed with the state exam on June 17, 2021.'
            },
            {
                'time': '2013 — 2017',
                'title': 'Gymnázium Stropkov',
                'subtitle': 'General Secondary Education',
                'desc': 'Completed with the school-leaving exam in 2017, focusing on natural sciences and technical fundamentals.'
            }
        ],
        'cv_skills_title': 'Software & Skills',
        'cv_skills_list': [
            {
                'name': 'Archicad',
                'role': 'Main design and drafting tool, advanced 3D BIM modeling and documentation.',
                'level': 95,
                'icon': 'archicad'
            },
            {
                'name': 'Dalux',
                'role': 'CDE platform, coordination, viewing BIM models directly on-site.',
                'level': 85,
                'icon': 'dalux'
            },
            {
                'name': 'Allplan',
                'role': 'BIM modeling, reinforcement, precise building structures.',
                'level': 80,
                'icon': 'allplan'
            },
            {
                'name': 'Lumion',
                'role': 'Photorealistic 3D visualizations of architecture and exteriors.',
                'level': 85,
                'icon': 'lumion'
            },
            {
                'name': 'BIMx',
                'role': 'Presentation 3D models and walk-throughs, interactive coordination.',
                'level': 90,
                'icon': 'bimx'
            },
            {
                'name': 'Photoshop',
                'role': 'Drawing post-production, collages, final touch-ups of visualizations.',
                'level': 80,
                'icon': 'photoshop'
            },
            {
                'name': 'Lightroom',
                'role': 'Photo processing and editing, organization of digital portfolio.',
                'level': 75,
                'icon': 'lightroom'
            },
            {
                'name': 'Canva',
                'role': 'Creating graphic materials, presentations and visual assets for project communication.',
                'level': 85,
                'icon': 'canva'
            }
        ],
        'cv_sidebar_docs_title': 'Documents',
        'cv_sidebar_format_label': 'Format',
        'cv_sidebar_size_label': 'Size',
        'cv_sidebar_lang_label': 'Language',
        'cv_sidebar_lang_val': 'English',
        'cv_sidebar_updated_label': 'Updated',
        'cv_sidebar_updated_val': 'May 2026',
        'cv_sidebar_img_alt': 'Architectural drawing of residence - BIM reconstruction modeling',
        'title_contact': 'Contact', 'contact_page_intro': 'If you are planning a project, a collaboration, or want to connect for a professional opportunity, I would be happy to hear from you. I value clear and pleasant communication with a specific intent.',
        'title_privacy': 'Privacy Policy', 'privacy_intro': 'This page explains what personal data is collected when visiting the website vaskova.space and how this data is used.',
        'privacy_content_full': '''
            <h2>Operator</h2>
            <p>The personal data operator is Ing. Zuzana Vašková. Your data is processed in accordance with the GDPR regulation.</p>
            
            <h2>Scope and Purpose of Processing</h2>
            <p>Through the contact form, I collect your name and e-mail address exclusively for the purpose of responding to your question or inquiry. I do not provide this data to third parties and do not store it in any marketing database.</p>
            
            <h2>Cookies</h2>
            <p>This website uses exclusively technical (strictly necessary) cookies, which serve for the proper functioning of the page (e.g., remembering the chosen color mode or language). I do not use any analytical or advertising cookies from third parties.</p>
            
            <h2>Your Rights</h2>
            <p>You have the right at any time to request information about what data I process about you, to request its correction or deletion. In case of questions, please contact me at the e-mail address provided in the Contact section.</p>
        ''',
        '404_title': 'Page not found.', '404_back': 'Back to home →'
    },
    'de': {
        'nav_home': 'Startseite', 'nav_about': 'Über mich', 'nav_projects': 'Projekte', 'nav_cv': 'Lebenslauf', 'nav_contact': 'Kontakt',
        'nav_privacy': 'Datenschutz',
        'urls': {'home': '/de/', 'about': '/de/ueber-mich.html', 'projects': '/de/projekte/', 'cv': '/de/cv.html', 'contact': '/de/kontakt.html', 'privacy': '/de/datenschutz.html'},
        'hero_stmt': 'Ich bin Bauingenieurin mit Schwerpunkt Hochbau, Architektur und BIM-Modellierung von Sanierungen. Ich widme mich der Projektvorbereitung mit Fokus auf Präzision, klare Ergebnisse und sinnvolle technische Lösungen.',
        'sec_focus': 'Schwerpunkt', 'sec_process': 'Wie ich arbeite', 'sec_projects': 'Projekte', 'sec_interests': 'Abseits der Arbeit', 'sec_contact': 'Kontakt aufnehmen',
        'intro_focus_1': 'In der Praxis konzentriere ich mich auf Gebäudeplanung und BIM-Modellierung, insbesondere bei Sanierungen, wo es wichtig ist, den Bestand zu verstehen und sensibel mit einem Entwurf darauf aufzubauen.',
        'intro_focus_2': 'Ich arbeite primär in der Archicad-Umgebung und nutze auch die Dalux-Plattform für den Dokumentenaustausch und die Koordination. Das digitale Modell sehe ich als Werkzeug für präzisere Entscheidungen und bessere Zusammenarbeit.',
        'intro_focus_3': 'Es ist mir wichtig, dass das Ergebnis nicht nur formal richtig ist, sondern auch praktisch, lesbar und im realen Prozess der Projektvorbereitung und Ausführung nutzbar ist.',
        'step_1_title': 'Analyse', 'step_1_desc': 'Bestandserfassung — Ort, Konstruktion, Kontext und Einschränkungen.',
        'step_2_title': 'Entwurf', 'step_2_desc': 'Konzeptentwicklung — funktionale, räumliche und konstruktive Entscheidungen.',
        'step_3_title': 'BIM-Modell', 'step_3_desc': 'Erstellung des digitalen Modells — Koordination, Kollisionsprüfung, Visualisierung.',
        'step_4_title': 'Dokumentation', 'step_4_desc': 'Erstellung der Projektdokumentation — Pläne, Schnitte, Details, Spezifikationen.',
        'process_cta_text': 'Interessieren Sie sich für die Ergebnisse meiner Arbeit? Sehen Sie sich mein vollständiges Portfolio an BIM-Modellen und technischen Lösungen an.',
        'process_cta_btn': 'Projekte ansehen',
        'projects_intro': 'Ausgewählte Projekte aus den Bereichen Sanierung und Projektdokumentation.',
        'projects_empty': 'Projekte werden vorbereitet. Die ersten Fallstudien folgen in Kürze.',
        'projects_all': 'Alle Projekte →',
        'meta_desc': 'Persönliches Portfolio von Ing. Zuzana Vašková. Expertin für Bauplanung, Sanierung und BIM-Modellierung in Archicad.',
        'meta_about': 'Lernen Sie Ing. Zuzana Vašková kennen — Bauingenieurin mit Fokus auf BIM and Sanierung.',
        'meta_projects': 'Projektübersicht von Ing. Zuzana Vašková. Beispiele für BIM-Modellierung und technische Dokumentation von Sanierungen.',
        'meta_cv': 'Berufliches Profil und Lebenslauf von Ing. Zuzana Vašková. Erfahrung im Bauwesen und Architektur.',
        'meta_contact': 'Kontaktieren Sie Ing. Zuzana Vašková für Projektzusammenarbeit oder Fachberatung im Bereich BIM.',
        'meta_privacy': 'Datenschutzerklärung für die Website von Ing. Zuzana Vašková.',
        'cards': [
            {'title':'Laufen', 'desc':'Eine Art, den Kopf freizubekommen und den eigenen Rhythmus zu halten.', 'img': 'running.png', 'alt': 'Minimalistische Illustration einer laufenden Person - Symbol für Ausdauer und Rhythmus'},
            {'title':'Skifahren', 'desc':'Dynamik, Konzentration und Freude an der Bewegung.', 'img': 'skiing.png', 'alt': 'Technische Illustration eines Skifahrers am Hang mit Höhenlinien der Berge'},
            {'title':'Volleyball', 'desc':'Teamgeist, Energie and ein natürlicher Ausgleich zur Arbeit.', 'img': 'volleyball.png', 'alt': 'Geometrische Skizze eines Volleyballnetzes und Balls - Symbol für Teamarbeit'},
            {'title':'Fotografie', 'desc':'Aufmerksamkeit für Detail, Licht und Komposition.', 'img': 'photography.png', 'alt': 'Architektonische Zeichnung einer Kamera mit Fokus auf technisches Detail'},
            {'title':'Sprachen und Reisen', 'desc':'Neue Länder und Kulturen entdecken und den Horizont erweitern.', 'img': 'travel_v5.svg', 'alt': 'Grafische Studie eines Koffers, Globus und Flugzeugs - Symbol für Reisen und Horizont'},
            {'title':'Wandern', 'desc':'Aktive Erholung in den Bergen und Entdecken neuer Ausblicke.', 'img': 'hiking_v5.svg', 'alt': 'Lineare Illustration von Bergen, Kompass und Rucksack - Symbol für aktive Erholung'}
        ],
        'projects_list': [
            {
                'title': 'Freising',
                'tags': ['WOHNGEBÄUDE', 'SANIERUNG', 'ARCHICAD'],
                'img': 'freising.jpg',
                'desc': 'Bearbeitung der Projektdokumentation vom Bestand und Abbrucharbeiten bis hin zum neuen Zustand und Konstruktionsdetails, einschließlich der Festlegung von Projektparametern für die Software Nevaris und Bexel.',
                'result': '40 Wohnungen in einem sanierten denkmalgeschützten Gebäude in Deutschland.'
            },
            {
                'title': 'Eversbuschstrasse',
                'tags': ['WOHNGEBÄUDE', 'SANIERUNG', 'ARCHICAD'],
                'img': 'eversbuschstrasse.png',
                'desc': 'Bearbeitung der Projektdokumentation vom Bestand und Abbrucharbeiten bis hin zum neuen Zustand und Konstruktionsdetails, einschließlich der Dokumentation für Garten und Umgebung.',
                'result': 'Sanierung einer Wohnanlage in Deutschland — 900 m² Wohnfläche, 9 Luxuswohnungen, 5 Seniorenwohnungen.'
            },
            {
                'title': 'Einfamilienhaus',
                'tags': ['EINFAMILIENHAUS', 'NEUBAU', 'ARCHICAD'],
                'img': 'rodinny_dom.jpg',
                'desc': 'Ausarbeitung von Entwurf, architektonischer Studie und Projekt für die Baugenehmigung.',
                'result': 'Modernes zweistöckiges Einfamilienhaus mit Flachdach, Holzverkleidung und integrierter Garage.'
            },
            {
                'title': 'Eichstätt',
                'tags': ['WOHNGEBÄUDE', 'SANIERUNG', 'ARCHICAD'],
                'img': 'eichstatt.jpg',
                'desc': 'Bearbeitung der Projektdokumentation vom Bestand und Abbrucharbeiten bis hin zum neuen Zustand und Konstruktionsdetails, einschließlich der Festlegung von Projektparametern für die Software Nevaris und Bexel.',
                'result': '44 Wohnungen und 8 Büroräume in einem sanierten denkmalgeschützten Gebäude in der deutschen Stadt Eichstätt.'
            },
            {
                'title': 'Královice',
                'tags': ['WOHNANLAGE', 'SANIERUNG', 'ARCHICAD'],
                'img': 'kralovice.jpg',
                'desc': 'Erstellung der vollständigen Projektdokumentation für das Hauptgebäude, einschließlich des Bestands, der Abbrucharbeiten, des geplanten Zustands und der Konstruktionsdetails, sowie der Dokumentation für kleinere Neubauten und die Gestaltung des Gartenbereichs.',
                'result': '8 Maisonette-Wohnungen mit Eigengarten und Stellplatz im Prager Stadtteil Královice.'
            },
            {
                'title': 'RD Stropkov',
                'tags': ['EINFAMILIENHAUS', 'NEUBAU', 'ARCHICAD', 'LUMION'],
                'img': 'stropkov.jpg',
                'desc': 'Erstellung eines 3D-Modells eines Einfamilienhauses auf der Grundlage von Zeichnungsunterlagen, Entwurf und Visualisierung des Außenbereichs einschließlich des Gartens.',
                'result': 'Ein Komplex aus 3 eingeschossigen Einfamilienhäusern mit großem Garten, Pool und Carport.'
            },
            {
                'title': 'Prosiek',
                'tags': ['WOCHENENDHAUS', 'SANIERUNG', 'ARCHICAD'],
                'img': 'prosiek.jpg',
                'desc': 'Bearbeitung der Projektdokumentation und des BIM-Modells der Abbrucharbeiten und des neuen Zustands für die Bauausführung.',
                'result': 'Ein Wochenendhaus mit Innenpool und Außensauna in der Region Liptov.'
            },
            {
                'title': 'Wasserburger Landstraße',
                'tags': ['APARTMENTHAUS', 'SANIERUNG', 'ARCHICAD'],
                'img': 'wasserburger.jpg',
                'desc': 'Erstellung eines BIM-Modells des bestehenden Gebäudes nach der Sanierung zum Zweck der Baukalkulation.',
                'result': '21 Apartments in einem Wohn- und Geschäftshaus mit Ladenlokal im Erdgeschoss.'
            },
            {
                'title': 'Schnaitsee',
                'tags': ['WOHNANLAGE', 'SANIERUNG', 'ARCHICAD'],
                'img': 'schnaitsee.jpg',
                'desc': 'Erstellung eines BIM-Modells des bestehenden Gebäudes nach der Sanierung zum Zweck der Baukalkulation.',
                'result': '13 Wohnungen in einer Wohnanlage mit Parkplatz in einem typischen bayerischen Dorf.'
            }
        ],
        'contact_intro': 'Wenn Sie meine Arbeit anspricht oder ein Projekt betreuen, bei dem Präzision, technisches Denken und gestalterisches Feingefühl gefragt sind, können Sie sich gern bei mir melden.',
        'label_name': 'Name', 'label_email': 'E-Mail', 'label_msg': 'Nachricht', 'btn_send': 'Nachricht senden',
        'privacy_note': 'Mit dem Absenden des Formulars stimmen Sie der Verarbeitung Ihrer Daten in dem Umfang zu, der für die Beantwortung Ihrer Nachricht erforderlich ist.',
        'title_about': 'Über mich', 'about_p1': 'Ich bin Bauplanerin mit den Schwerpunkten Sanierung, Projektdokumentation und BIM-Modellierung. Ich arbeite in einem Bereich, in dem technische Präzision auf gestalterisches Denken trifft.',
        'about_p2': 'Sanierungen reizen mich wegen der Arbeit mit dem Bestehenden — dem Verständnis der Struktur, des Kontextes und der Rahmenbedingungen, bevor etwas Neues vorgeschlagen wird.',
        'about_p3': 'Ich sehe BIM als Methodik, nicht nur als Software. Das digitale Modell ermöglicht es mir, Lösungen zu überprüfen, Gewerke zu koordinieren und mit höherer Genauigkeit zu arbeiten.',
        'about_p4': 'Bei meiner Arbeit lege ich Wert auf Präzision, Klarheit und Praktikabilität. Eine gute Dokumentation ist keine Formalität — sie ist die Grundlage für ein qualitatives Ergebnis auf der Baustelle.',
        'about_p5': 'Abseits der Arbeit tanke ich Kraft in den Bergen, beim Sport und beim Fotografieren. Die slowakischen Berge sind mein regelmäßiges Ziel.',
        'title_cv': 'Lebenslauf', 'btn_download': 'PDF herunterladen',
        'cv_edu': 'Technische Universität Košice, Fakultät für Bauingenieurwesen — Hochbau und Architektur, Bachelorstudium, abgeschlossen mit Staatsprüfung am 17. Juni 2021. Weiterführendes Studium im Bereich Hochbau von 2021 bis 2023. Gymnasium Stropkov, abgeschlossen mit Reifeprüfung im Jahr 2017.', 'cv_exp': 'Bauingenieurin mit Schwerpunkt auf Gebäudeplanung und BIM-Modellierung von Rekonstruktionsprojekten. In der Praxis beschäftige ich mich mit Projektvorbereitung, digitaler Gebäudebearbeitung und technischer Dokumentation, mit Fokus auf Präzision, Klarheit und praktisch nutzbare Ergebnisse.', 'cv_sw': 'Archicad, Dalux, Allplan, Lumion, BIMx, Adobe Photoshop, Adobe Lightroom.',
        'cv_profile_title': 'Profil',
        'cv_education_title': 'Ausbildung',
        'cv_education_list': [
            {
                'time': '2021 — 2023',
                'title': 'Technische Universität Košice',
                'subtitle': 'Fakultät für Bauingenieurwesen',
                'desc': 'Weiterführendes Masterstudium im Bereich <strong>Hochbau</strong>. Schwerpunkt auf Tragwerksplanung, Bauphysik und fortgeschrittene Projektvorbereitung.'
            },
            {
                'time': '2017 — 2021',
                'title': 'Technische Universität Košice',
                'subtitle': 'Fakultät für Bauingenieurwesen',
                'desc': 'Bachelorstudium im Bereich <strong>Hochbau und Architektur</strong>, erfolgreich abgeschlossen mit der Staatsprüfung am 17. Juni 2021.'
            },
            {
                'time': '2013 — 2017',
                'title': 'Gymnázium Stropkov',
                'subtitle': 'Allgemeine Sekundarstufe II',
                'desc': 'Abgeschlossen mit der Reifeprüfung im Jahr 2017, mit Schwerpunkt auf Naturwissenschaften und technische Grundlagen.'
            }
        ],
        'cv_skills_title': 'Software & Kenntnisse',
        'cv_skills_list': [
            {
                'name': 'Archicad',
                'role': 'Hauptplanungswerkzeug, fortgeschrittene 3D BIM-Modellierung und Dokumentation.',
                'level': 95,
                'icon': 'archicad'
            },
            {
                'name': 'Dalux',
                'role': 'CDE-Plattform, Koordination, direkte Anzeige von BIM-Modellen auf der Baustelle.',
                'level': 85,
                'icon': 'dalux'
            },
            {
                'name': 'Allplan',
                'role': 'BIM-Modellierung, Bewehrung, präzise Baukonstruktionen.',
                'level': 80,
                'icon': 'allplan'
            },
            {
                'name': 'Lumion',
                'role': 'Fotorealistische 3D-Visualisierungen von Architektur und Außenräumen.',
                'level': 85,
                'icon': 'lumion'
            },
            {
                'name': 'BIMx',
                'role': 'Präsentation von 3D-Modellen und virtuelle Begehungen, interaktive Koordination.',
                'level': 90,
                'icon': 'bimx'
            },
            {
                'name': 'Photoshop',
                'role': 'Nachbearbeitung von Zeichnungen, Collagen, finaler Feinschliff von Visualisierungen.',
                'level': 80,
                'icon': 'photoshop'
            },
            {
                'name': 'Lightroom',
                'role': 'Bildverarbeitung und -bearbeitung, Organisation des digitalen Portfolios.',
                'level': 75,
                'icon': 'lightroom'
            },
            {
                'name': 'Canva',
                'role': 'Erstellung von Grafikmaterialien, Präsentationen und visuellen Inhalten zur Projektkommunikation.',
                'level': 85,
                'icon': 'canva'
            }
        ],
        'cv_sidebar_docs_title': 'Dokumente',
        'cv_sidebar_format_label': 'Format',
        'cv_sidebar_size_label': 'Größe',
        'cv_sidebar_lang_label': 'Sprache',
        'cv_sidebar_lang_val': 'Deutsch',
        'cv_sidebar_updated_label': 'Aktualisiert',
        'cv_sidebar_updated_val': 'Mai 2026',
        'cv_sidebar_img_alt': 'Architektonische Zeichnung der Residenz - BIM-Rekonstruktionsmodellierung',
        'title_contact': 'Kontakt', 'contact_page_intro': 'Wenn Sie ein Projekt planen, eine Zusammenarbeit in Betracht ziehen oder mich wegen einer beruflichen Gelegenheit kontaktieren möchten, freue ich mich über Ihre Nachricht. Ich schätze klare und angenehme Kommunikation mit einem konkreten Anliegen.',
        'title_privacy': 'Datenschutzerklärung', 'privacy_intro': 'Diese Seite erklärt, welche personenbezogenen Daten bei einem Besuch der Website vaskova.space erhoben werden und wie sie verwendet werden.',
        'privacy_content_full': '''
            <h2>Verantwortlicher</h2>
            <p>Verantwortlich für die Verarbeitung personenbezogener Daten ist Ing. Zuzana Vašková. Ihre Daten werden im Einklang mit der DSGVO verarbeitet.</p>
            
            <h2>Umfang und Zweck der Verarbeitung</h2>
            <p>Über das Kontaktformular erhebe ich Ihren Namen und Ihre E-Mail-Adresse ausschließlich zum Zweck der Beantwortung Ihrer Anfrage. Diese Daten werden nicht an Dritte weitergegeben und in keiner Marketing-Datenbank gespeichert.</p>
            
            <h2>Cookies</h2>
            <p>Diese Website verwendet ausschließlich technische (zwingend erforderliche) Cookies, die dem ordnungsgemäßen Funktionieren der Seite dienen (z. B. Speichern des gewählten Farbmodus oder der Sprache). Ich verwende keine Analyse- oder Werbe-Cookies von Drittanbietern.</p>
            
            <h2>Ihre Rechte</h2>
            <p>Sie haben jederzeit das Recht, Auskunft über die von mir über Sie verarbeiteten Daten zu verlangen, deren Berichtigung oder Löschung zu fordern. Bei Fragen kontaktieren Sie mich bitte unter der im Abschnitt Kontakt angegebenen E-Mail-Adresse.</p>
        ''',
        '404_title': 'Seite nicht gefunden.', '404_back': 'Zurück zur Startseite →'
    }
}

def get_file_path(url):
    clean = url.strip("/")
    if url.endswith("/"):
        return clean + "/index.html" if clean else "index.html"
    return clean

def get_asset_prefix(url):
    clean = url.strip("/")
    depth = clean.count("/")
    if url.endswith("/") and clean:
        depth += 1
    if depth == 0:
        return "./"
    return "../" * depth

def render_layout(lang, title, url, content, page_key='home', meta_description=None):
    d = LANGS[lang]
    asset_prefix = get_asset_prefix(url)
    final_meta = meta_description if meta_description else d['meta_desc']
    
    sk_link = asset_prefix + get_file_path(LANGS['sk']['urls'].get(page_key, '/'))
    en_link = asset_prefix + get_file_path(LANGS['en']['urls'].get(page_key, '/en/'))
    de_link = asset_prefix + get_file_path(LANGS['de']['urls'].get(page_key, '/de/'))
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Ing. Zuzana Vašková</title>
    <meta name="description" content="{final_meta}">
    <link rel="stylesheet" href="{asset_prefix}assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
    <script>
        const storedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', storedTheme);
    </script>
</head>
<body>
    <header class="site-header">
        <div class="container">
            <div class="logo">Ing. Zuzana Vašková</div>
            <nav class="main-nav">
                <a href="{asset_prefix + get_file_path(d['urls']['home'])}">{d['nav_home']}</a>
                <a href="{asset_prefix + get_file_path(d['urls']['about'])}">{d['nav_about']}</a>
                <a href="{asset_prefix + get_file_path(d['urls']['projects'])}">{d['nav_projects']}</a>
                <a href="{asset_prefix + get_file_path(d['urls']['cv'])}">{d['nav_cv']}</a>
                <a href="{asset_prefix + get_file_path(d['urls']['contact'])}">{d['nav_contact']}</a>
            </nav>
            <div style="display: flex; align-items: center;">
                <div class="lang-switcher">
                    <a href="{sk_link}" {"class='active'" if lang=='sk' else ""}>SK</a> | 
                    <a href="{en_link}" {"class='active'" if lang=='en' else ""}>EN</a> | 
                    <a href="{de_link}" {"class='active'" if lang=='de' else ""}>DE</a>
                </div>
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle Theme"></button>
            </div>
            <button class="menu-toggle" aria-label="Menu">☰</button>
        </div>
    </header>

    <div class="mobile-nav-overlay">
        <div class="mobile-nav-header">
            <div class="logo">Ing. Zuzana Vašková</div>
            <button class="menu-toggle-close" aria-label="Close Menu">✕</button>
        </div>
        <nav class="mobile-nav-links">
            <a href="{asset_prefix + get_file_path(d['urls']['home'])}">{d['nav_home']}</a>
            <a href="{asset_prefix + get_file_path(d['urls']['about'])}">{d['nav_about']}</a>
            <a href="{asset_prefix + get_file_path(d['urls']['projects'])}">{d['nav_projects']}</a>
            <a href="{asset_prefix + get_file_path(d['urls']['cv'])}">{d['nav_cv']}</a>
            <a href="{asset_prefix + get_file_path(d['urls']['contact'])}">{d['nav_contact']}</a>
        </nav>
        <div class="lang-switcher mt-8">
            <a href="{sk_link}" {"class='active'" if lang=='sk' else ""}>SK</a> | 
            <a href="{en_link}" {"class='active'" if lang=='en' else ""}>EN</a> | 
            <a href="{de_link}" {"class='active'" if lang=='de' else ""}>DE</a>
        </div>
    </div>

    <main>
{content}
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <nav class="footer-nav">
                <a href="{asset_prefix + get_file_path(d['urls']['privacy'])}">{d['nav_privacy']}</a>
            </nav>
            <div class="copyright">© 2026 Ing. Zuzana Vašková</div>
            <div class="lang-switcher">
                <a href="{sk_link}" {"class='active'" if lang=='sk' else ""}>SK</a> | 
                <a href="{en_link}" {"class='active'" if lang=='en' else ""}>EN</a> | 
                <a href="{de_link}" {"class='active'" if lang=='de' else ""}>DE</a>
            </div>
        </div>
    </footer>

    <script src="{asset_prefix}assets/js/theme.js"></script>
    <script src="{asset_prefix}assets/js/nav.js"></script>
</body>
</html>'''
    return html

# Generate Pages
for lang, d in LANGS.items():
    asset_p = get_asset_prefix(d['urls']['home'])
    
    # Interests HTML
    interests_html = f'<div class="grid-3" style="gap: 24px;">' + "".join([
        f'''<div class="interest-card">
            <div class="interest-img">
                <img src="{asset_p}assets/images/interests/{c['img']}" alt="{c['alt']}" loading="lazy">
            </div>
            <div class="interest-card-content">
                <h3>{c["title"]}</h3>
                <p>{c["desc"]}</p>
            </div>
        </div>''' for c in d['cards']
    ]) + '</div>'
    def get_projects_html(asset_prefix):
        html = ""
        if 'projects_list' in d:
            for p in d['projects_list']:
                tags_html = "".join([f'<span class="project-tag">{t}</span>' for t in p['tags']])
                html += f'''
                <div class="project-card">
                    <div class="project-img">
                        <img src="{asset_prefix}assets/images/projects/{p['img']}" alt="{p['title']}" loading="lazy">
                    </div>
                    <div>
                        <div class="project-meta">
                            {tags_html}
                        </div>
                        <h3 class="project-title">{p['title']}</h3>
                        <p class="project-desc">{p['desc']}</p>
                        <div class="project-result" style="border-left-width: 3px; padding-left: 16px;">
                            {p['result']}
                        </div>
                    </div>
                </div>
                '''
        else:
            html = f'''
            <div style="padding: 96px 0; border: 1px dashed var(--color-border); border-radius: 4px; text-align: center; color: var(--color-text-muted);">
                {d['projects_empty']}
            </div>
            '''
        return html


    home_content = f'''
        <section id="hero" class="container" style="padding-top: 80px; padding-bottom: 48px;">
            <div class="reading-width">
                <h1 class="text-hero-name" style="margin-bottom: 32px;">Ing. Zuzana Vašková</h1>
                <div class="project-result" style="border-left-width: 4px; padding-left: 24px;">
                    <p class="text-hero-statement" style="font-size: 20px; line-height: 1.6; color: var(--color-text);">{d['hero_stmt']}</p>
                </div>
            </div>
        </section>

        <section class="container" style="padding-bottom: 48px;">
            <h2 class="mb-12" style="display: flex; align-items: center; text-transform: uppercase; letter-spacing: 0.1em; font-size: 16px;"><span style="display: inline-block; width: 32px; height: 2px; background-color: #EAB308; margin-right: 16px;"></span>{d['sec_process']}</h2>
            <div class="grid-4">
                <div class="process-step">
                    <div class="process-title">{d['step_1_title']}</div>
                    <p>{d['step_1_desc']}</p>
                </div>
                <div class="process-step">
                    <div class="process-title">{d['step_2_title']}</div>
                    <p>{d['step_2_desc']}</p>
                </div>
                <div class="process-step">
                    <div class="process-title">{d['step_3_title']}</div>
                    <p>{d['step_3_desc']}</p>
                </div>
                <div class="process-step">
                    <div class="process-title">{d['step_4_title']}</div>
                    <p>{d['step_4_desc']}</p>
                </div>
            </div>
            <div class="project-result" style="border-left-width: 4px; padding-left: 24px; margin-top: 48px; max-width: 760px;">
                <p style="font-size: 18px; line-height: 1.6; color: var(--color-text); margin-bottom: 24px; font-weight: 500;">
                    {d['process_cta_text']}
                </p>
                <a href="{asset_p + get_file_path(d['urls']['projects'])}" class="btn btn-primary" style="display: inline-block;">{d['process_cta_btn']} →</a>
            </div>
        </section>


        <section class="container" style="padding-top: 48px; padding-bottom: 96px;">
            <h2 class="mb-8">{d['sec_contact']}</h2>
            <div class="reading-width">
                <p class="mb-8">{d['contact_intro']}</p>
                <a href="{asset_p + get_file_path(d['urls']['contact'])}" class="btn btn-primary">{d['nav_contact']} →</a>
            </div>
        </section>
    '''
    write(get_file_path(d['urls']['home']), render_layout(lang, d['nav_home'], d['urls']['home'], home_content, 'home', d['meta_desc']))

    # 2. About
    icon_bio = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
    icon_heart = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
    
    about_content = f'''
        <section class="container" style="padding-top: 64px;">
            <h1 class="mb-8">{d['title_about']}</h1>
            
            <div class="cv-block">
                <div class="cv-row">
                    <div class="cv-header">
                        <div class="cv-icon-wrap" style="color: #EAB308;">{icon_bio}</div>
                        <div class="cv-label">{d['title_about']}</div>
                    </div>
                    <div class="cv-content">
                        <div class="project-result" style="color: var(--color-text); font-weight: 400; font-size: 15px; border-left-width: 3px;">
                            <p class="mb-4">{d['about_p1']}</p>
                            <p class="mb-4">{d['about_p2']}</p>
                            <p class="mb-4">{d['about_p3']}</p>
                            <p>{d['about_p4']}</p>
                        </div>
                    </div>
                </div>

                <div class="cv-row">
                    <div class="cv-header">
                        <div class="cv-icon-wrap" style="color: #EAB308;">{icon_heart}</div>
                        <div class="cv-label">{d['sec_interests']}</div>
                    </div>
                    <div class="cv-content">
                        {interests_html}
                    </div>
                </div>
            </div>
        </section>
    '''
    write(get_file_path(d['urls']['about']), render_layout(lang, d['title_about'], d['urls']['about'], about_content, 'about', d['meta_about']))


    projects_content = f'''
        <section class="container" style="padding-top: 64px; padding-bottom: 96px;">
            <h1 class="mb-8">{d['sec_projects']}</h1>
            
            <div class="reading-width">
                <p class="mb-12">{d['projects_intro']}</p>
            </div>
            
            <div class="project-list">
                {get_projects_html(get_asset_prefix(d['urls']['projects']))}
            </div>
        </section>
    '''
    write(get_file_path(d['urls']['projects']), render_layout(lang, d['sec_projects'], d['urls']['projects'], projects_content, 'projects', d['meta_projects']))

    # 4. CV
    cv_prefix = get_asset_prefix(d['urls']['cv'])
    svg_icons = {
        'archicad': '<svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>',
        'dalux': '<svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
        'allplan': '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line></svg>',
        'lumion': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="3"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></svg>',
        'bimx': '<svg viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>',
        'photoshop': '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>',
        'lightroom': '<svg viewBox="0 0 24 24"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>',
        'canva': '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="3"></rect><circle cx="8.5" cy="12" r="2"></circle><path d="M15 9v6"></path><path d="M18 9v6"></path><path d="M15 12h3"></path></svg>'
    }

    edu_html = ""
    for item in d['cv_education_list']:
        edu_html += f'''
                            <div class="cv-timeline-item">
                                <div class="cv-timeline-dot"></div>
                                <div class="cv-timeline-time">{item['time']}</div>
                                <h3 class="cv-timeline-title">{item['title']}</h3>
                                <div class="cv-timeline-subtitle">{item['subtitle']}</div>
                                <p class="cv-timeline-desc">
                                    {item['desc']}
                                </p>
                            </div>'''

    skills_html = ""
    for skill in d['cv_skills_list']:
        icon_svg = svg_icons.get(skill['icon'], '')
        skills_html += f'''
                            <div class="software-card">
                                <div class="software-card-header">
                                    <div class="software-icon">
                                        {icon_svg}
                                    </div>
                                    <div class="software-name">{skill['name']}</div>
                                </div>
                                <p class="software-role">{skill['role']}</p>
                                <div class="software-level">
                                    <div class="software-level-bar" style="width: {skill['level']}%;"></div>
                                </div>
                            </div>'''

    cv_content = f'''
        <style>
            /* Scoped style for the CV page */
            .cv-middle-grid {{
                display: grid;
                grid-template-columns: 1fr;
                gap: 40px;
            }}

            @media (min-width: 1024px) {{
                .cv-middle-grid {{
                    grid-template-columns: 1fr 360px;
                    gap: 56px;
                    align-items: start;
                }}
            }}

            .cv-sidebar {{
                position: sticky;
                top: 100px;
            }}

            .cv-card-visual {{
                background-color: var(--color-surface);
                border: 1px solid var(--color-border);
                border-radius: 8px;
                overflow: hidden;
                transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s ease, box-shadow 0.3s ease;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
                margin-bottom: 24px;
            }}

            .cv-card-visual:hover {{
                border-color: #EAB308;
                box-shadow: 0 16px 40px rgba(234, 179, 8, 0.12);
                transform: translateY(-6px);
            }}

            .cv-visual-img {{
                width: 100%;
                aspect-ratio: 1/1;
                object-fit: cover;
                display: block;
                border-bottom: 1px solid var(--color-border);
            }}

            .cv-sidebar-info {{
                padding: 24px;
            }}

            .cv-sidebar-title {{
                font-size: 14px;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                margin-bottom: 12px;
                color: var(--color-text);
                display: flex;
                align-items: center;
                gap: 8px;
            }}

            .cv-sidebar-meta {{
                font-size: 13.5px;
                color: var(--color-text-muted);
                line-height: 1.7;
                margin-bottom: 24px;
            }}

            .cv-sidebar-meta div {{
                display: flex;
                justify-content: space-between;
                border-bottom: 1px dashed var(--color-border);
                padding: 6px 0;
            }}

            .cv-sidebar-meta div:last-child {{
                border-bottom: none;
            }}

            .cv-sidebar-meta strong {{
                color: var(--color-text);
                font-weight: 500;
            }}

            /* Sections styling */
            .cv-section {{
                display: flex;
                flex-direction: column;
                gap: 24px;
            }}

            .cv-section-title {{
                font-size: 16px;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                color: var(--color-text);
                display: flex;
                align-items: center;
                margin-bottom: 8px;
            }}

            .cv-section-title::before {{
                content: '';
                display: inline-block;
                width: 24px;
                height: 2px;
                background-color: #EAB308;
                margin-right: 12px;
                flex-shrink: 0;
            }}

            /* Timeline */
            .cv-timeline {{
                position: relative;
                padding-left: 28px;
                border-left: 1.5px solid var(--color-border);
                margin-left: 8px;
                display: flex;
                flex-direction: column;
                gap: 40px;
            }}

            .cv-timeline-item {{
                position: relative;
                transition: transform 0.2s ease;
            }}

            .cv-timeline-item:hover {{
                transform: translateX(4px);
            }}

            .cv-timeline-dot {{
                position: absolute;
                left: -35px;
                top: 5px;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background-color: var(--color-bg);
                border: 2.5px solid #EAB308;
                transition: background-color 0.25s ease, box-shadow 0.25s ease;
            }}

            .cv-timeline-item:hover .cv-timeline-dot {{
                background-color: #EAB308;
                box-shadow: 0 0 0 4px rgba(234, 179, 8, 0.2);
            }}

            .cv-timeline-time {{
                font-size: 13px;
                font-weight: 600;
                color: #EAB308;
                margin-bottom: 4px;
                letter-spacing: 0.05em;
            }}

            .cv-timeline-title {{
                font-size: 17px;
                font-weight: 500;
                color: var(--color-text);
                margin-bottom: 4px;
                line-height: 1.4;
            }}

            .cv-timeline-subtitle {{
                font-size: 14px;
                font-weight: 400;
                color: var(--color-text-muted);
                margin-bottom: 8px;
            }}

            .cv-timeline-desc {{
                font-size: 14.5px;
                line-height: 1.7;
                color: var(--color-text-muted);
            }}

            /* Software grid */
            .software-grid {{
                display: grid;
                grid-template-columns: 1fr;
                gap: 16px;
            }}

            @media (min-width: 480px) {{
                .software-grid {{
                    grid-template-columns: repeat(2, 1fr);
                }}
            }}

            @media (min-width: 768px) {{
                .software-grid {{
                    grid-template-columns: repeat(3, 1fr);
                }}
            }}

            @media (min-width: 1200px) {{
                .software-grid {{
                    grid-template-columns: repeat(4, 1fr);
                }}
            }}

            .software-card {{
                background-color: var(--color-surface);
                border: 1px solid var(--color-border);
                border-radius: 6px;
                padding: 20px;
                display: flex;
                flex-direction: column;
                gap: 12px;
                transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.25s ease, box-shadow 0.25s ease;
            }}

            .software-card:hover {{
                transform: translateY(-4px);
                border-color: #EAB308;
                box-shadow: 0 10px 24px rgba(0, 0, 0, 0.04);
            }}

            .software-card-header {{
                display: flex;
                align-items: center;
                gap: 10px;
            }}

            .software-icon {{
                width: 32px;
                height: 32px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #EAB308;
                background-color: rgba(234, 179, 8, 0.06);
                border-radius: 4px;
                flex-shrink: 0;
                transition: background-color 0.2s ease;
            }}

            .software-card:hover .software-icon {{
                background-color: rgba(234, 179, 8, 0.12);
            }}

            .software-icon svg {{
                width: 20px;
                height: 20px;
                stroke: currentColor;
                stroke-width: 1.8;
                fill: none;
            }}

            .software-name {{
                font-size: 15px;
                font-weight: 500;
                color: var(--color-text);
            }}

            .software-role {{
                font-size: 13px;
                color: var(--color-text-muted);
                line-height: 1.45;
                min-height: 36px;
            }}

            .software-level {{
                margin-top: auto;
                height: 3px;
                background-color: var(--color-border);
                border-radius: 1.5px;
                overflow: hidden;
                position: relative;
            }}

            .software-level-bar {{
                height: 100%;
                background-color: #EAB308;
                border-radius: 1.5px;
                transition: width 1.2s ease-out;
            }}
        </style>

        <section class="container" style="padding-top: 64px; padding-bottom: 64px; display: flex; flex-direction: column; gap: 56px;">
            <h1 class="mb-4">{d['title_cv']}</h1>
            
            <!-- Profil Section (Full width) -->
            <section class="cv-section" style="padding: 0;">
                <h2 class="cv-section-title">{d['cv_profile_title']}</h2>
                <div class="project-result" style="border-left-width: 4px; padding-left: 20px;">
                    <p class="cv-profile-text" style="font-size: 15.5px; line-height: 1.8;">
                        {d['cv_exp']}
                    </p>
                </div>
            </section>

            <!-- Middle Section: Vzdelanie (Left) & Sidebar (Right) -->
            <div class="cv-middle-grid">
                
                <!-- Vzdelanie Section -->
                <section class="cv-section" style="padding: 0;">
                    <h2 class="cv-section-title">{d['cv_education_title']}</h2>
                    <div class="cv-timeline">
                        {edu_html}
                    </div>
                </section>

                <!-- Sidebar (Downloads) -->
                <aside class="cv-sidebar">
                    <div class="cv-card-visual">
                        <img src="{cv_prefix}assets/images/cv_architectural_graphic.png" alt="{d['cv_sidebar_img_alt']}" class="cv-visual-img" loading="lazy">
                        <div class="cv-sidebar-info">
                            <h3 class="cv-sidebar-title">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; color:#EAB308;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                {d['cv_sidebar_docs_title']}
                            </h3>
                            <div class="cv-sidebar-meta">
                                <div><span>{d['cv_sidebar_format_label']}:</span> <strong>PDF (A4)</strong></div>
                                <div><span>{d['cv_sidebar_size_label']}:</span> <strong>~120 kB</strong></div>
                                <div><span>{d['cv_sidebar_lang_label']}:</span> <strong>{d['cv_sidebar_lang_val']}</strong></div>
                                <div><span>{d['cv_sidebar_updated_label']}:</span> <strong>{d['cv_sidebar_updated_val']}</strong></div>
                            </div>
                            <a href="{cv_prefix}assets/cv/cv-{lang}.pdf" class="btn btn-primary" style="display: block; width: 100%; text-align: center;" target="_blank">{d['btn_download']}</a>
                        </div>
                    </div>
                </aside>

            </div>

            <!-- Software Section (Full width) -->
            <section class="cv-section" style="padding: 0;">
                <h2 class="cv-section-title">{d['cv_skills_title']}</h2>
                <div class="software-grid">
                    {skills_html}
                </div>
            </section>

        </section>
    '''
    write(get_file_path(d['urls']['cv']), render_layout(lang, d['title_cv'], d['urls']['cv'], cv_content, 'cv', d['meta_cv']))

    contact_content = f'''
        <section class="container" style="padding-top: 64px;">
            <h1 class="mb-8">{d['title_contact']}</h1>
            
            <div class="reading-width">
                <p class="mb-8">{d['contact_page_intro']}</p>
                
                <form action="/api/contact" method="POST" style="max-width: 500px;">
                    <div class="form-group">
                        <label for="name">{d['label_name']}</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">{d['label_email']}</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">{d['label_msg']}</label>
                        <textarea id="message" name="message" required></textarea>
                    </div>
                    <input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">
                    
                    <div class="cf-turnstile mb-6" data-sitekey="0x4AAAAAADT3OfjmkyZFgTnh"></div>
                    
                    <button type="submit" class="btn btn-primary mb-4">{d['btn_send']}</button>
                    <p class="text-micro text-muted"><a href="{get_asset_prefix(d['urls']['contact']) + get_file_path(d['urls']['privacy'])}" class="text-muted">{d['privacy_note']}</a></p>
                </form>
            </div>
        </section>
    '''
    write(get_file_path(d['urls']['contact']), render_layout(lang, d['title_contact'], d['urls']['contact'], contact_content, 'contact', d['meta_contact']))

    privacy_content = f'''
        <section class="container" style="padding-top: 64px;">
            <h1 class="mb-8">{d['title_privacy']}</h1>
            
            <div class="reading-width privacy-page">
                <p class="mb-8">{d['privacy_intro']}</p>
                <div class="project-result" style="border-left-width: 3px; padding-left: 32px; font-size: 15px; color: var(--color-text-muted);">
                    {d['privacy_content_full']}
                </div>
            </div>
        </section>
    '''
    write(get_file_path(d['urls']['privacy']), render_layout(lang, d['title_privacy'], d['urls']['privacy'], privacy_content, 'privacy', d['meta_privacy']))

    p404_content = f'''
        <section class="container" style="padding-top: 64px; text-align: left;">
            <h1 class="mb-8">{d['404_title']}</h1>
            <a href="{get_asset_prefix('/404.html') + get_file_path(d['urls']['home'])}" class="btn btn-primary mt-4">{d['404_back']}</a>
        </section>
    '''
    write(f"{lang}/404.html" if lang != 'sk' else "404.html", render_layout(lang, '404', f"/{lang}/404.html" if lang != 'sk' else "/404.html", p404_content))

print("Site generation complete.")
