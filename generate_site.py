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
        </section>

        <section class="container" style="padding-top: 48px; padding-bottom: 96px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 48px;">
                <h2 style="margin:0;">{d['sec_projects']}</h2>
                <a href="{asset_p + get_file_path(d['urls']['projects'])}" class="text-muted" style="font-size: 14px; font-weight: 500;">{d['projects_all']}</a>
            </div>
            <div class="project-list">
                {get_projects_html(asset_p)}
            </div>
        </section>


        <section class="container">
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
                            <p class="mb-4">{d['about_p4']}</p>
                            <p>{d['about_p5']}</p>
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
            <h1 class="mb-8" style="display: flex; align-items: center;"><span style="display: inline-block; width: 48px; height: 2px; background-color: #EAB308; margin-right: 24px;"></span>{d['sec_projects']}</h1>
            
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
    tools_html = "".join([f'<span class="project-tag" style="margin: 4px 4px 4px 0;">{t.strip()}</span>' for t in d['cv_sw'].split(',')])
    cv_content = f'''
        <section class="container" style="padding-top: 64px;">
            <h1 class="mb-8">{d['title_cv']}</h1>
            
            <div class="cv-block">
                <div class="cv-row">
                    <div class="cv-header"><div class="cv-label">Profil</div></div>
                    <div class="cv-content">{d['cv_exp']}</div>
                </div>
                <div class="cv-row">
                    <div class="cv-header"><div class="cv-label">Vzdelanie</div></div>
                    <div class="cv-content">{d['cv_edu']}</div>
                </div>
                <div class="cv-row" style="border-bottom: none;">
                    <div class="cv-header"><div class="cv-label">Software</div></div>
                    <div class="cv-content">
                        <div class="project-result" style="border-left-width: 3px; padding-bottom: 2px;">
                            {tools_html}
                        </div>
                    </div>
                </div>
            </div>

            <div style="padding-top: 56px;">
                <a href="{asset_p}assets/cv/cv-{lang}.pdf" class="btn btn-primary" target="_blank">{d['btn_download']}</a>
            </div>
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
                    
                    <div class="cf-turnstile mb-6" data-sitekey="0x4AAAAAAABBBBBCCCCCDDDD"></div>
                    
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
