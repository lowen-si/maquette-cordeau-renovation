#!/usr/bin/env python3
"""Génère les pages HTML de la maquette Atelier Cordeau.

Usage : python3 sources/build.py   (depuis le dossier du site)
Tout le contenu est dans ce fichier : coordonnées, réalisations, métiers, textes.
"""
import json, os
from html import escape

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SITE_URL = 'https://www.atelier-cordeau.example'  # à remplacer par le vrai domaine

BIZ = {
    'name': 'Atelier Cordeau',
    'tagline': 'Rénovation intérieure à Bordeaux',
    'phone': '05 56 00 00 00', 'phone_href': '+33556000000',
    'email': 'bonjour@atelier-cordeau.example',
    'street': '14 rue des Menuts', 'zip': '33000', 'city': 'Bordeaux',
    'hours': 'Du lundi au vendredi, 8 h à 18 h',
    'communes': ['Bordeaux', 'Talence', 'Bègles', 'Le Bouscat', 'Caudéran', 'Mérignac', 'Pessac', 'Floirac', 'Cenon', 'Bruges', 'Eysines', 'Villenave-d’Ornon'],
}

def img(name, alt, cls='', sizes='100vw', eager=False, pos=None):
    a = f' class="{cls}"' if cls else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    st = f' style="object-position:{pos}"' if pos else ''
    return (f'<img{a} src="assets/img/{name}-1800.webp" srcset="assets/img/{name}-900.webp 900w, assets/img/{name}-1800.webp 1800w" '
            f'sizes="{sizes}" width="1800" height="1200" alt="{escape(alt)}" decoding="async"{load}{st}>')

PROJECTS = [
    {
        'slug': 'echoppe-saint-genes', 'title': 'Une échoppe rendue à la lumière', 'short': 'Échoppe, Saint-Genès',
        'commune': 'Bordeaux, Saint-Genès', 'surface': '68 m²', 'duree': '11 semaines', 'budget': '74 000 € TTC',
        'lots': ['Curage', 'Plâtrerie', 'Électricité', 'Parquet en chevrons', 'Peinture'],
        'before': ('echoppe-chantier', 'La pièce de vie pendant le curage : sol à nu, bétonnière, radiateurs déposés, porte-fenêtre d’origine'),
        'after': ('echoppe-livree', 'La même pièce livrée : murs bleu profond, parquet en chevrons clair, grande baie sur le jardin'),
        'detail': ('echoppe-detail', 'Plinthe moulurée et parquet en pin clair au pied d’un encadrement de porte'),
        'besoin': 'Une échoppe double des années 1920, cloisonnée en quatre petites pièces sombres. Les propriétaires voulaient une seule pièce de vie ouverte sur le jardin, sans perdre le caractère de la maison.',
        'reponse': 'Relevé complet et plan coté en première semaine. On a déposé deux cloisons non porteuses, repris les enduits à la chaux sur les murs en pierre, refait l’électricité aux normes et posé un parquet massif en chevrons, recoupé à la main contre chaque mur.',
        'resultat': 'Une pièce de 41 m² traversante, une baie élargie côté jardin et un bleu profond choisi sur trois échantillons peints sur place. Livrée avec une semaine d’avance sur le planning.',
        'pos_before': '50% 50%', 'pos_after': '45% 50%',
    },
    {
        'slug': 'cuisine-chartrons', 'title': 'Une cuisine refaite autour d’une fenêtre', 'short': 'Cuisine, Chartrons',
        'commune': 'Bordeaux, Chartrons', 'surface': '14 m²', 'duree': '6 semaines', 'budget': '31 000 € TTC',
        'lots': ['Cloisons', 'Plomberie', 'Faïence', 'Pose de cuisine', 'Peinture'],
        'before': ('cuisine-chantier', 'Cloisons en plaques de plâtre sur ossature métallique, deux escabeaux et des gaines au sol'),
        'after': ('cuisine-livree', 'Cuisine en U blanche, plan de travail en bois, crédence en carreaux gris, fenêtre au centre'),
        'detail': ('batons-rompus', 'Gros plan d’un parquet à bâtons rompus en chêne'),
        'besoin': 'Un appartement au deuxième étage d’un immeuble en pierre. La cuisine était fermée, mal éclairée, avec une plomberie qui datait des années 1970.',
        'reponse': 'Nouvelle cloison sur ossature métallique pour gagner un mètre linéaire, réseau d’eau refait en multicouche, crédence en carreaux métro posés à joints fins, cuisine en U implantée pour que l’évier soit face à la fenêtre.',
        'resultat': 'Un plan de travail de 4,20 m, tout le rangement en hauteur et une seule fenêtre qui éclaire désormais toute la pièce.',
        'pos_before': '40% 50%', 'pos_after': '50% 50%',
    },
    {
        'slug': 'salle-de-bains-cauderan', 'title': 'Une salle de bains reprise jusqu’à l’ossature', 'short': 'Salle de bains, Caudéran',
        'commune': 'Bordeaux, Caudéran', 'surface': '9 m²', 'duree': '5 semaines', 'budget': '23 500 € TTC',
        'lots': ['Dépose', 'Ossature bois', 'Étanchéité', 'Carrelage', 'Sanitaires'],
        'before': ('sdb-chantier', 'Cloisons déposées jusqu’à l’ossature en bois, porte d’origine, sol à nu'),
        'after': ('sdb-livree', 'Salle de bains claire : douche vitrée, baignoire îlot, marbre clair et fenêtre sur la verdure'),
        'detail': ('pose-parquet', 'Mains d’un artisan qui ajustent une lame de parquet au maillet'),
        'besoin': 'Une maison des années 1930 dont la salle de bains avait subi une fuite ancienne. Le plancher et une partie des cloisons étaient à reprendre avant toute finition.',
        'reponse': 'Dépose complète jusqu’à l’ossature, remplacement des montants abîmés, étanchéité sous carrelage sur toute la zone de douche, puis faïence grand format posée au laser.',
        'resultat': 'Une douche à l’italienne et une baignoire îlot dans 9 m², une ventilation refaite et une garantie décennale sur l’étanchéité.',
        'pos_before': '50% 50%', 'pos_after': '50% 50%',
    },
]

METIERS = [
    ('Curage et dépose', 'On vide la pièce jusqu’à ce qui est sain : cloisons, sols, réseaux. Les gravats sont triés et évacués en déchèterie pro.', 'Bennes et évacuation comprises'),
    ('Plâtrerie et isolation', 'Cloisons sur ossature, doublages isolants, faux plafonds et enduits à la chaux sur les murs en pierre.', 'Plaque, chaux, fibre de bois'),
    ('Sols et parquets', 'Parquet massif posé collé ou cloué, chevrons et bâtons rompus recoupés sur place, ponçage et vitrification.', 'Chêne, pin, carreaux de ciment'),
    ('Cuisines et salles de bains', 'Plomberie, étanchéité, faïence et pose de meubles, avec un seul interlocuteur pour tous les corps de métier.', 'Douche à l’italienne, cuisine sur mesure'),
    ('Électricité', 'Mise aux normes NF C 15-100, éclairage, prises et tableau, avec attestation Consuel quand elle est nécessaire.', 'Partenaire électricien qualifié'),
    ('Peinture et finitions', 'Préparation des supports, deux couches minimum, échantillons peints sur vos murs avant de choisir la teinte.', 'Peintures à faible émission'),
]

METHODE = [
    ('Visite et relevé', 'On passe chez vous sous 8 jours ouvrés. On mesure tout, on photographie, on écoute ce que vous voulez changer.', 'Gratuit, environ 1 h'),
    ('Plan coté et devis', 'Vous recevez un plan coté de l’existant et du projet, et un devis détaillé lot par lot, sans ligne « divers ».', 'Sous 10 jours'),
    ('Chantier', 'Un chef de chantier unique. Chaque vendredi, un point photo par message et le planning de la semaine suivante.', 'Point chaque vendredi'),
    ('Réception', 'On fait le tour de la pièce ensemble, on note les réserves et on les lève avant de vous rendre les clés.', 'Garantie décennale'),
]

# --------------------------------------------------------------------------- layout

HEAD_JS = "<script>(function(h){h.classList.add('js');var r=matchMedia('(prefers-reduced-motion: reduce)').matches;if(!r){h.classList.add('intro-pending');setTimeout(function(){h.classList.remove('intro-pending')},2500);try{if(sessionStorage.getItem('cordeau-nav')){h.classList.add('is-arriving');sessionStorage.removeItem('cordeau-nav')}}catch(e){}}})(document.documentElement);</script>"

def nav_link(href, label, current):
    cur = ' aria-current="page"' if current == href else ''
    return f'<li><a class="link-trait" href="{href}"{cur}>{label}</a></li>'

def page(*, path, title, description, body, current='', body_class='', jsonld=None, og_image='echoppe-livree'):
    canonical = SITE_URL + '/' + ('' if path == 'index.html' else path)
    nav = ''.join([
        nav_link('index.html#realisations', 'Réalisations', current),
        nav_link('index.html#metiers', 'Métiers', current),
        nav_link('index.html#methode', 'Méthode', current),
        nav_link('contact.html', 'Contact', current),
    ])
    ld = ''
    if jsonld:
        ld = '<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + '</script>'
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{BIZ['name']}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:image" content="{SITE_URL}/assets/img/{og_image}-1800.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ECEAE4">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css">
{HEAD_JS}
{ld}
</head>
<body class="{body_class}">
<a class="skip" href="#contenu">Aller au contenu</a>
<aside class="demo-bar" aria-label="Avertissement maquette"><p>Maquette de démonstration. Atelier Cordeau est une entreprise fictive : chantiers, chiffres et avis sont des exemples, photos Pexels.</p></aside>
<header class="site-header" data-header>
  <a class="brand" href="index.html" aria-label="{BIZ['name']}, accueil">
    <svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true"><rect x="1" y="1" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"/><path d="M16 1v30" stroke="var(--cordeau)" stroke-width="3"/></svg>
    <span class="brand-name">Atelier Cordeau</span>
  </a>
  <nav class="site-nav" aria-label="Navigation principale">
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu" data-nav-toggle><span class="nav-toggle-label">Menu</span><span class="nav-toggle-bars" aria-hidden="true"></span></button>
    <ul id="menu" class="nav-list" data-nav-list>{nav}</ul>
  </nav>
  <a class="btn btn-small header-cta" href="contact.html"><span>Demander une visite</span></a>
</header>
<main id="contenu" tabindex="-1">
{body}
</main>
{footer()}
<div class="curtain" aria-hidden="true"><span class="curtain-line"></span></div>
<nav class="mobile-bar" aria-label="Contact rapide"><a href="tel:{BIZ['phone_href']}">Appeler</a><a href="contact.html">Demander une visite</a></nav>
<script src="assets/vendor/gsap.min.js" defer></script>
<script src="assets/vendor/ScrollTrigger.min.js" defer></script>
<script src="assets/vendor/lenis.min.js" defer></script>
<script src="assets/site.js" defer></script>
</body>
</html>
'''

def footer():
    communes = ', '.join(BIZ['communes'])
    return f'''<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <p class="footer-name">Atelier Cordeau</p>
      <p>Rénovation intérieure, échoppes et appartements anciens.<br>{BIZ['street']}, {BIZ['zip']} {BIZ['city']}</p>
    </div>
    <div>
      <p class="label">Nous joindre</p>
      <p><a class="link-utility" href="tel:{BIZ['phone_href']}">{BIZ['phone']}</a><br><a class="link-utility" href="mailto:{BIZ['email']}">{BIZ['email']}</a><br>{BIZ['hours']}</p>
    </div>
    <div>
      <p class="label">Communes desservies</p>
      <p>{communes}</p>
    </div>
    <div>
      <p class="label">Le site</p>
      <ul class="footer-links">
        <li><a class="link-utility" href="index.html#realisations">Réalisations</a></li>
        <li><a class="link-utility" href="contact.html">Contact</a></li>
        <li><a class="link-utility" href="mentions-legales.html">Mentions légales et données personnelles</a></li>
      </ul>
    </div>
  </div>
  <p class="footer-note">Maquette de démonstration. Garantie décennale, assureur et numéros d’immatriculation à compléter avec les informations réelles.</p>
</footer>'''

def cordeau_stage(before, after, *, labels=('Chantier', 'Livré'), cls='', eager=False, interactive=True, start=0.5, pos=('50% 50%', '50% 50%'), sizes='100vw', range_label='Position de la ligne entre chantier et pièce livrée', variant='', rigid=False):
    rng = ''
    if interactive:
        rng = f'<input class="cordeau-range" type="range" min="0" max="100" value="{int(start*100)}" aria-label="{range_label}" data-cordeau-range>'
    va = (f' data-variant="{variant}"' if variant else '') + (' data-rigid' if rigid else '')
    return f'''<div class="cordeau {cls}" data-cordeau data-start="{start}"{va}>
  <figure class="cordeau-layer cordeau-before">{img(before[0], before[1], sizes=sizes, eager=eager, pos=pos[0])}<span class="tape tape-before" aria-hidden="true">{labels[0]}</span></figure>
  <figure class="cordeau-layer cordeau-after" data-cordeau-after>{img(after[0], after[1], sizes=sizes, eager=eager, pos=pos[1])}<span class="tape tape-after" aria-hidden="true">{labels[1]}</span></figure>
  <svg class="cordeau-svg" aria-hidden="true" data-cordeau-svg><path class="cordeau-dust" d="" /><path class="cordeau-halo" d="" /><path class="cordeau-path" d="" /><path class="cordeau-ticks" d="" /><path class="cordeau-ticks2" d="" /></svg>
  <span class="cordeau-handle" aria-hidden="true" data-cordeau-handle></span>
  {rng}
</div>'''

def snap_line(cls=''):
    return f'<div class="snap-line {cls}" data-snap-line aria-hidden="true"><svg preserveAspectRatio="none"><path d=""/></svg></div>'

LOCAL_BUSINESS = {
    '@context': 'https://schema.org', '@type': 'HomeAndConstructionBusiness',
    'name': BIZ['name'], 'description': 'Rénovation intérieure à Bordeaux : échoppes, appartements anciens, cuisines et salles de bains.',
    'url': SITE_URL + '/', 'telephone': '+33 5 56 00 00 00', 'email': BIZ['email'],
    'address': {'@type': 'PostalAddress', 'streetAddress': BIZ['street'], 'postalCode': BIZ['zip'], 'addressLocality': BIZ['city'], 'addressCountry': 'FR'},
    'areaServed': BIZ['communes'], 'openingHours': 'Mo-Fr 08:00-18:00', 'image': SITE_URL + '/assets/img/echoppe-livree-1800.webp',
}

# --------------------------------------------------------------------------- pages

def home():
    hero_p = PROJECTS[0]
    rows = []
    for p in PROJECTS:
        lots = ' · '.join(p['lots'][:3])
        rows.append(f'''<li class="work-row">
  <a class="work-link" href="{p['slug']}.html">
    <span class="work-meta mono">{p['commune']}<span aria-hidden="true"> · </span>{p['surface']}<span aria-hidden="true"> · </span>{p['duree']}</span>
    <span class="work-title">{p['title']}</span>
    <span class="work-lots mono">{lots}</span>
    <span class="work-thumb" aria-hidden="true">
      <span class="work-thumb-before">{img(p['before'][0], '', sizes='(min-width: 900px) 30vw, 90vw')}</span>
      <span class="work-thumb-after">{img(p['after'][0], '', sizes='(min-width: 900px) 30vw, 90vw')}</span>
      <span class="work-thumb-line"></span>
    </span>
    <span class="work-cta mono">Voir le chantier</span>
  </a>
</li>''')
    metiers = ''.join(f'''<li class="metier">
  <h3 class="metier-title">{t}</h3>
  <p>{d}</p>
  <p class="metier-cote mono">{c}</p>
</li>''' for t, d, c in METIERS)
    methode = ''.join(f'''<li class="step" style="--i:{i}">
  <span class="step-tick" aria-hidden="true"></span>
  <p class="step-num mono">Étape {i+1}</p>
  <h3 class="step-title">{t}</h3>
  <p>{d}</p>
  <p class="step-note mono">{n}</p>
</li>''' for i, (t, d, n) in enumerate(METHODE))
    communes = ''.join(f'<li>{c}</li>' for c in BIZ['communes'])
    body = f'''
<section class="hero" aria-labelledby="hero-title" data-hero>
  <div class="hero-pin" data-hero-pin>
    {cordeau_stage(hero_p['before'], hero_p['after'], labels=('Chantier · semaine 2', 'Livré · semaine 11'), cls='cordeau-hero', eager=True, interactive=False, start=0.56, pos=(hero_p['pos_before'], '50% 62%'), sizes='100vw')}
    <div class="hero-scrim" aria-hidden="true"></div>
    <div class="hero-copy">
      <h1 id="hero-title" class="hero-title"><span class="line"><span>On trace la ligne.</span></span><span class="line"><span>Puis on rénove.</span></span></h1>
      <p class="hero-sub">Atelier Cordeau rénove les échoppes et les appartements anciens de Bordeaux, du curage à la dernière couche de peinture.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html"><span>Demander une visite gratuite</span></a>
        <a class="link-trait link-light" href="{hero_p['slug']}.html">Voir cette échoppe</a>
      </div>
    </div>
    <p class="hero-scroll mono" aria-hidden="true" data-hero-hint>Faites défiler : la ligne avance</p>
  </div>
</section>

<section class="manifeste" aria-labelledby="manifeste-title">
  <div class="manifeste-text">
    <h2 id="manifeste-title" class="display-l">On ne casse rien avant d’avoir tracé.</h2>
    <div class="manifeste-body">
      <p>Chaque chantier commence par un relevé et un plan coté. Puis on claque un cordeau bleu sur le mur, là où passera la nouvelle cloison, la crédence ou le bord du parquet. Tout le monde voit la même ligne : vous, le plombier, l’électricien et nous.</p>
      <p>C’est ce trait qui permet de tenir un devis sans ligne « divers » et un planning qui ne glisse pas.</p>
    </div>
  </div>
  <figure class="manifeste-figure">
    {img('trait', 'Un crayon trace un repère contre un mètre ruban posé sur une planche', sizes='(min-width: 900px) 34vw, 90vw')}
    <figcaption class="mono">Repère au crayon avant la coupe</figcaption>
  </figure>
  <dl class="chiffres">
    <div><dt class="mono">Chantiers livrés depuis 2014</dt><dd>140</dd></div>
    <div><dt class="mono">Visite et relevé</dt><dd>Gratuits</dd></div>
    <div><dt class="mono">Interlocuteur par chantier</dt><dd>1 seul</dd></div>
  </dl>
</section>

{snap_line()}

<section class="work" id="realisations" aria-labelledby="work-title">
  <div class="section-head">
    <h2 id="work-title" class="display-l">Trois chantiers récents</h2>
    <p class="section-aside">Chaque fiche montre la pièce pendant les travaux puis à la livraison, avec la surface, la durée et le budget réel.</p>
  </div>
  <ol class="work-list">{''.join(rows)}</ol>
</section>

<section class="metiers" id="metiers" aria-labelledby="metiers-title">
  <div class="metiers-side">
    <div class="metiers-sticky">
      <h2 id="metiers-title" class="display-l">Tous les corps de métier, un seul chef de chantier</h2>
      <figure class="metiers-figure">
        {img('pose-parquet', 'Un artisan ajuste une lame de parquet au maillet', sizes='(min-width: 900px) 40vw, 90vw')}
      </figure>
    </div>
  </div>
  <ul class="metiers-list">{metiers}</ul>
</section>

<section class="methode" id="methode" aria-labelledby="methode-title">
  <div class="section-head">
    <h2 id="methode-title" class="display-l">Quatre étapes, du premier rendez-vous aux clés</h2>
    <p class="section-aside">Vous savez toujours où en est le chantier et ce qui se passe la semaine suivante.</p>
  </div>
  <div class="methode-track">
    {snap_line('snap-line-dark')}
    <ol class="steps">{methode}</ol>
  </div>
</section>

<section class="avis" aria-labelledby="avis-title">
  <h2 id="avis-title" class="visually-hidden">Avis client</h2>
  <figure class="avis-figure">
    <blockquote><p>« Le plan coté nous a servi pendant tout le chantier. Quand on a hésité sur la place de la cuisine, ils ont claqué une nouvelle ligne au mur et on a décidé en cinq minutes. »</p></blockquote>
    <figcaption class="mono">Claire et Mathieu, échoppe à Saint-Genès <span class="tag-exemple">Avis d’exemple</span></figcaption>
  </figure>
</section>

<section class="contact-band" aria-labelledby="contact-title">
  <div class="contact-band-main">
    <h2 id="contact-title" class="display-xl">Montrez-nous la pièce.</h2>
    <p>On vient la mesurer gratuitement, sous 8 jours ouvrés, partout dans Bordeaux et à 25 km autour.</p>
    <div class="hero-actions">
      <a class="btn" href="contact.html"><span>Demander une visite</span></a>
      <a class="link-trait" href="tel:{BIZ['phone_href']}">{BIZ['phone']}</a>
    </div>
  </div>
  <div class="contact-band-zone">
    <p class="label">Communes desservies</p>
    <ul class="communes mono">{communes}</ul>
  </div>
</section>
'''
    return page(path='index.html', title='Atelier Cordeau, rénovation intérieure à Bordeaux',
                description='Rénovation d’échoppes et d’appartements anciens à Bordeaux : curage, plâtrerie, parquet, cuisines et salles de bains. Visite et plan coté gratuits.',
                body=body, body_class='page-home', jsonld=LOCAL_BUSINESS)

def project_page(i):
    p = PROJECTS[i]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    lots = ''.join(f'<li>{l}</li>' for l in p['lots'])
    body = f'''
<article class="case">
  <header class="case-head">
    <p class="crumbs mono"><a class="link-utility" href="index.html#realisations">Réalisations</a> <span aria-hidden="true">/</span> {p['short']}</p>
    <h1 class="display-xl case-title">{p['title']}</h1>
    <dl class="fiche">
      <div><dt class="mono">Commune</dt><dd>{p['commune']}</dd></div>
      <div><dt class="mono">Surface</dt><dd>{p['surface']}</dd></div>
      <div><dt class="mono">Durée</dt><dd>{p['duree']}</dd></div>
      <div><dt class="mono">Budget</dt><dd>{p['budget']}</dd></div>
    </dl>
  </header>
  <div class="case-stage">
    {cordeau_stage(p['before'], p['after'], labels=('Chantier', 'Livré'), cls='cordeau-case', eager=True, start=0.5, pos=(p['pos_before'], p['pos_after']))}
    <p class="case-hint mono" aria-hidden="true"><span class="hint-pointer">Passez la souris sur la photo : la ligne suit</span><span class="hint-touch">Glissez le doigt sur la photo</span></p>
  </div>
  <div class="case-body">
    <section class="case-block" aria-labelledby="b1"><h2 id="b1" class="case-h">Le besoin</h2><p>{p['besoin']}</p></section>
    <section class="case-block" aria-labelledby="b2"><h2 id="b2" class="case-h">Notre réponse</h2><p>{p['reponse']}</p></section>
    <section class="case-block" aria-labelledby="b3"><h2 id="b3" class="case-h">Le résultat</h2><p>{p['resultat']}</p></section>
    <aside class="case-lots" aria-label="Lots réalisés"><p class="label">Lots réalisés</p><ul class="mono">{lots}</ul></aside>
  </div>
  <figure class="case-detail">
    {img(p['detail'][0], p['detail'][1], sizes='(min-width: 900px) 58vw, 100vw')}
    <figcaption class="mono">Photo d’illustration (Pexels), à remplacer par une photo du chantier</figcaption>
  </figure>
  <nav class="next" aria-label="Chantier suivant">
    <a class="next-link" href="{nxt['slug']}.html">
      <span class="label">Chantier suivant</span>
      <span class="next-title">{nxt['title']}</span>
      <span class="next-thumb" aria-hidden="true">
        <span class="work-thumb-before">{img(nxt['before'][0], '', sizes='40vw')}</span>
        <span class="work-thumb-after">{img(nxt['after'][0], '', sizes='40vw')}</span>
        <span class="work-thumb-line"></span>
      </span>
    </a>
  </nav>
</article>
'''
    ld = {'@context': 'https://schema.org', '@type': 'CreativeWork', 'name': p['title'], 'about': p['commune'],
          'creator': {'@type': 'HomeAndConstructionBusiness', 'name': BIZ['name']}}
    return page(path=p['slug'] + '.html', title=f"{p['title']} · Atelier Cordeau",
                description=f"{p['short']} : {p['surface']} rénovés en {p['duree']}. {p['besoin'][:110]}…",
                body=body, body_class='page-case', jsonld=ld, current='index.html#realisations', og_image=p['after'][0])

def contact():
    opts = ''.join(f'<option>{t}</option>' for t in ['Rénovation complète', 'Cuisine', 'Salle de bains', 'Parquet et sols', 'Plâtrerie, isolation', 'Autre'])
    body = f'''
<section class="contact-page" aria-labelledby="contact-h1">
  <div class="contact-intro">
    <h1 id="contact-h1" class="display-xl">Parlons de votre pièce.</h1>
    <p>Dites-nous ce que vous voulez changer. On vous rappelle sous 48 h pour fixer une visite, gratuite et sans engagement.</p>
    <dl class="contact-infos">
      <div><dt class="mono">Téléphone</dt><dd><a class="link-trait" href="tel:{BIZ['phone_href']}">{BIZ['phone']}</a></dd></div>
      <div><dt class="mono">E-mail</dt><dd><a class="link-trait" href="mailto:{BIZ['email']}">{BIZ['email']}</a></dd></div>
      <div><dt class="mono">Atelier</dt><dd>{BIZ['street']}, {BIZ['zip']} {BIZ['city']}</dd></div>
      <div><dt class="mono">Horaires</dt><dd>{BIZ['hours']}</dd></div>
    </dl>
  </div>
  <form class="form" data-form novalidate>
    <div class="field"><label for="f-nom">Nom</label><input id="f-nom" name="nom" autocomplete="name" required></div>
    <div class="field"><label for="f-tel">Téléphone</label><input id="f-tel" name="tel" type="tel" autocomplete="tel" required></div>
    <div class="field"><label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="f-commune">Commune</label><input id="f-commune" name="commune" autocomplete="address-level2"></div>
    <div class="field field-wide"><label for="f-type">Type de travaux</label><select id="f-type" name="type">{opts}</select></div>
    <div class="field field-wide"><label for="f-msg">Votre projet</label><textarea id="f-msg" name="message" rows="5" placeholder="La pièce, ce qui ne va pas, ce que vous imaginez"></textarea></div>
    <div class="field field-wide field-check"><input id="f-rgpd" name="rgpd" type="checkbox" required><label for="f-rgpd">J’accepte qu’Atelier Cordeau utilise ces informations pour me recontacter. Détails dans <a href="mentions-legales.html#donnees">mentions légales et données personnelles</a>.</label></div>
    <div class="field-wide form-foot">
      <button class="btn" type="submit"><span>Envoyer la demande</span></button>
      <p class="form-status mono" role="status" data-form-status></p>
    </div>
  </form>
</section>
'''
    return page(path='contact.html', title='Contact et visite gratuite · Atelier Cordeau',
                description='Demandez une visite gratuite pour votre rénovation à Bordeaux. Rappel sous 48 h, relevé et plan coté offerts.',
                body=body, body_class='page-contact', current='contact.html', jsonld=LOCAL_BUSINESS)

PHOTOS = [
    ('Accueil et échoppe, chantier', 'Francesco Ungaro', 'https://www.pexels.com/photo/interior-of-a-room-under-renovation-15798784/'),
    ('Accueil et échoppe, livré', 'Max Vakhtbovych', 'https://www.pexels.com/photo/an-empty-room-with-blue-walls-7587859/'),
    ('Échoppe, détail', 'Lisa Anna', 'https://www.pexels.com/photo/parquet-in-a-minimalist-apartment-19866428/'),
    ('Cuisine, chantier', 'Rene Terp', 'https://www.pexels.com/photo/house-renovation-3990359/'),
    ('Cuisine, livrée', 'Max Vakhtbovych', 'https://www.pexels.com/photo/interior-of-contemporary-kitchen-in-pastel-colors-6580220/'),
    ('Cuisine, détail', 'Magda Ehlers', 'https://www.pexels.com/photo/pattern-on-a-hardwood-flooring-15066939/'),
    ('Salle de bains, chantier', 'Monica Silvestre', 'https://www.pexels.com/photo/renovations-in-a-house-4756489/'),
    ('Salle de bains, livrée', 'Spencer Lee Eiseman', 'https://www.pexels.com/photo/interior-design-of-bathroom-15369789/'),
    ('Accueil, crayon et mètre', 'Ono Kosuki', 'https://www.pexels.com/photo/man-making-marks-on-wooden-plank-with-measurement-tape-5973909/'),
    ('Métiers et salle de bains, pose de parquet', 'Kelly', 'https://www.pexels.com/photo/crop-man-installing-laminate-flooring-4263067/'),
]

def legal():
    B = BIZ
    adr = f"{B['street']}, {B['zip']} {B['city']}"
    mail = f'<a href="mailto:{B["email"]}">{B["email"]}</a>'
    def dl(rows):
        return '<dl class="ml-dl">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows) + '</dl>'
    def table(head, rows):
        th = ''.join(f'<th scope="col">{h}</th>' for h in head)
        tr = ''.join('<tr>' + ''.join((f'<th scope="row">{c}</th>' if i == 0 else f'<td>{c}</td>') for i, c in enumerate(r)) + '</tr>' for r in rows)
        return f'<div class="ml-table-wrap" tabindex="0" role="region" aria-label="Tableau : {head[0]}"><table class="ml-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
    secs = []
    def sec(sid, title, textes, body):
        secs.append((sid, title))
        n = len(secs)
        return f'''<section class="ml-sec" id="{sid}" aria-labelledby="{sid}-t">
  <h2 id="{sid}-t"><span class="ml-n mono">{n:02d}</span> {title}</h2>
  <p class="ml-base"><span class="mono">Textes</span> {textes}</p>
  {body}
</section>'''
    S = []
    S.append(sec('editeur', 'Éditeur du site',
        'article 1-1 de la loi n° 2004-575 du 21 juin 2004 pour la confiance dans l’économie numérique (LCEN), dans sa rédaction issue de la loi n° 2024-449 du 21 mai 2024 (SREN) ; article 19 de la LCEN ; articles L111-1, R111-1 et R111-2 du Code de la consommation ; article R123-237 du Code de commerce ; article 21 de la loi n° 96-603 du 5 juillet 1996.',
        f'''<p>Toute entreprise qui édite un site doit dire qui elle est, comment la joindre et sous quels numéros elle est immatriculée. Le site {SITE_URL.replace('https://','')} est édité par :</p>
{dl([
  ('Dénomination sociale', 'Atelier Cordeau'),
  ('Forme juridique', 'Société à responsabilité limitée (SARL)'),
  ('Capital social', '10 000 € (fictif)'),
  ('Siège social', adr),
  ('Immatriculation', 'Registre national des entreprises (RNE), activité artisanale ; RCS Bordeaux 000 000 000 (fictif)'),
  ('SIRET du siège', '000 000 000 00000 (fictif)'),
  ('Code APE', '43.39Z, autres travaux de finition (fictif, à vérifier sur l’avis de situation Insee)'),
  ('TVA intracommunautaire', 'FR00 000000000 (fictif)'),
  ('Téléphone', f'{B["phone"]} (fictif), appel non surtaxé'),
  ('E-mail', mail),
  ('Directeur de la publication', '[Prénom Nom], gérant'),
])}
<p>Le directeur de la publication est responsable des contenus publiés sur le site. C’est ici le représentant légal de la société.</p>'''))
    S.append(sec('hebergeur', 'Hébergeur',
        'article 1-1 de la LCEN.',
        f'''<p>L’hébergeur stocke le site et le rend accessible sur internet. Ses coordonnées doivent figurer ici pour qu’on puisse le joindre directement, par exemple pour signaler un contenu illicite.</p>
{dl([('Société', '[Raison sociale de l’hébergeur]'), ('Adresse', '[Adresse postale complète]'), ('Téléphone', '[Numéro de téléphone]'), ('Localisation des serveurs', '[Pays, de préférence dans l’Union européenne]')])}'''))
    S.append(sec('qualification', 'Qualification professionnelle et assurances',
        'article 16 de la loi n° 96-603 du 5 juillet 1996 et décret n° 98-246 du 2 avril 1998 (qualification professionnelle) ; articles L241-1 et L243-2 du Code des assurances (assurance décennale) ; article L242-1 du Code des assurances (dommages-ouvrage) ; article R111-2 du Code de la consommation ; article 1er de la loi n° 75-1334 du 31 décembre 1975 (sous-traitance).',
        f'''<p>Les travaux du bâtiment sont des activités réglementées : ils doivent être réalisés par une personne qualifiée, ou sous son contrôle effectif et permanent. La qualification s’obtient par un diplôme du métier (au minimum un CAP ou un BEP) ou par trois ans d’expérience professionnelle.</p>
{dl([
  ('Personne qualifiée', '[Prénom Nom], titulaire du [diplôme, par exemple BP plâtrier-plaquiste]'),
  ('Signe de qualité RGE', '[Qualibat RGE], certificat n° [numéro], valable jusqu’au [date], pour [isolation des murs par l’intérieur, etc.]'),
  ('Assurance décennale', '[Nom de l’assureur], [adresse], contrat n° [numéro]'),
  ('Responsabilité civile professionnelle', '[Nom de l’assureur], contrat n° [numéro]'),
  ('Couverture géographique', 'France métropolitaine'),
])}
<p>L’assurance décennale est obligatoire pour tous les travaux de construction et de rénovation qui touchent au bâti. Le nom de l’assureur, ses coordonnées et la couverture géographique figurent aussi sur chacun de nos devis et chacune de nos factures (article L243-2 du Code des assurances).</p>
<p><strong>Électricité et plomberie.</strong> Certains lots peuvent être confiés à des artisans partenaires qualifiés. Dans ce cas, le devis indique le lot sous-traité et le nom de l’entreprise. Atelier Cordeau reste votre seul interlocuteur et répond de l’ensemble des travaux.</p>
<p><strong>Assurance dommages-ouvrage.</strong> Pour des travaux importants qui touchent à la structure, la loi demande au propriétaire de souscrire lui-même une assurance dommages-ouvrage avant l’ouverture du chantier. Nous vous signalons au devis quand elle est nécessaire.</p>'''))
    S.append(sec('prix', 'Prix, devis et TVA',
        'articles L112-1 et L112-3 du Code de la consommation ; arrêté du 24 janvier 2017 relatif à la publicité des prix des prestations de dépannage, de réparation et d’entretien dans le secteur du bâtiment et de l’équipement de la maison ; article L541-21-2-3 du Code de l’environnement et article D541-385-2 du même code (déchets de chantier) ; articles 278-0 bis A et 279-0 bis du Code général des impôts.',
        f'''<p>Les prix des réalisations présentées sur ce site sont donnés à titre d’exemple. Chaque chantier fait l’objet d’un devis.</p>
{dl([
  ('Visite, relevé et plan coté', 'Gratuits et sans engagement'),
  ('Taux horaire (petits travaux et reprises)', '52 € TTC (TVA 10 % incluse) (fictif)'),
  ('Frais de déplacement', 'Offerts dans Bordeaux et à 25 km autour'),
  ('Majorations', 'Aucune : nous n’intervenons pas le soir, le week-end ni en urgence'),
])}
<p><strong>Devis.</strong> Avant tout chantier, vous recevez un devis écrit, gratuit et détaillé lot par lot : nature et quantité de chaque prestation, prix unitaires, main-d’œuvre, durée de validité de l’offre, date de début et durée prévisionnelle des travaux, modalités de paiement. Aucun travail n’est commencé sans devis signé.</p>
<p><strong>Déchets de chantier.</strong> Comme la loi l’impose, le devis précise la quantité estimée de déchets produits, la façon dont ils seront triés et collectés, l’installation où ils seront déposés et le coût de cette gestion.</p>
<p><strong>TVA.</strong> Les prix affichés sont toutes taxes comprises. Le taux réduit de 10 % s’applique aux travaux d’amélioration et d’entretien d’un logement achevé depuis plus de deux ans, et le taux de 5,5 % aux travaux de rénovation énergétique, sur attestation du client. À défaut, le taux de 20 % s’applique.</p>'''))
    S.append(sec('contrat', 'Informations avant contrat et signature',
        'articles L111-1, L221-5, L221-8, L221-9 et L221-10 du Code de la consommation.',
        '''<p>Avant que vous ne vous engagiez, nous vous informons de façon lisible des caractéristiques des travaux, de leur prix total, du délai d’exécution, de notre identité et de nos coordonnées, des garanties légales, de l’existence et des modalités du droit de rétractation et de la possibilité de recourir à un médiateur.</p>
<p>Quand le contrat est signé chez vous, vous recevez un exemplaire papier daté et signé, ou, si vous l’acceptez, sur un autre support durable, accompagné du formulaire de rétractation. Aucun paiement ne peut vous être demandé pendant les 7 jours qui suivent cette signature. Quand le contrat est conclu à distance (téléphone, e-mail), nous vous envoyons une confirmation écrite au plus tard avant le début des travaux.</p>'''))
    S.append(sec('retractation', 'Droit de rétractation',
        'articles L221-18, L221-20, L221-21, L221-24, L221-25, L221-28 et R221-1 (formulaire type en annexe) du Code de la consommation.',
        f'''<p><strong>Le principe.</strong> Quand un contrat est conclu chez vous ou à distance, vous disposez de 14 jours à compter de sa signature pour changer d’avis, sans avoir à vous justifier ni à payer de pénalité. Si nous avons oublié de vous informer de ce droit, le délai est prolongé de 12 mois.</p>
<p><strong>Si les travaux commencent avant la fin du délai.</strong> Vous pouvez nous demander par écrit de commencer plus tôt. Vous restez libre de vous rétracter, mais vous payez alors la part des travaux déjà réalisée, en proportion du prix total.</p>
<p><strong>Quand ce droit ne s’applique pas.</strong> Un contrat signé à l’atelier, à votre initiative, n’ouvre pas droit à rétractation. Le droit ne s’applique pas non plus aux travaux entièrement terminés avant la fin du délai, quand vous avez demandé leur démarrage anticipé et reconnu perdre ce droit.</p>
<p><strong>Comment se rétracter.</strong> Envoyez-nous, avant la fin du délai, une déclaration sans ambiguïté, par lettre au {adr} ou par e-mail à {mail}. Vous pouvez utiliser le modèle ci-dessous. Nous vous remboursons les sommes versées au plus tard 14 jours après réception de votre décision, par le même moyen de paiement.</p>
<div class="ml-form" role="group" aria-label="Formulaire de rétractation">
  <p class="ml-form-t">Formulaire de rétractation</p>
  <p>À l’attention d’Atelier Cordeau, {adr}, {B["email"]} :</p>
  <p>Je vous notifie par la présente ma rétractation du contrat portant sur la prestation de services ci-dessous :</p>
  <p class="ml-line">Description des travaux :</p>
  <p class="ml-line">Commandé le :</p>
  <p class="ml-line">Nom du client :</p>
  <p class="ml-line">Adresse du client :</p>
  <p class="ml-line">Date et signature (uniquement en cas de notification sur papier) :</p>
</div>'''))
    S.append(sec('paiement', 'Acompte et paiement',
        'article L112-6 et D112-3 du Code monétaire et financier ; article L221-10 du Code de la consommation ; articles L441-9 et L441-10 du Code de commerce (clients professionnels).',
        '''<p>Un acompte de 30 % au plus est demandé à la signature du devis, après le délai de 7 jours prévu pour les contrats signés à domicile. Le solde est échelonné selon l’avancement indiqué au devis, et la dernière part est payée après la signature du procès-verbal de réception.</p>
<p>Nous acceptons le virement, la carte bancaire et le chèque. La loi limite le paiement en espèces à 1 000 €.</p>
<p><strong>Clients professionnels.</strong> En cas de retard de paiement, des pénalités égales à trois fois le taux d’intérêt légal sont dues de plein droit, ainsi qu’une indemnité forfaitaire de 40 € pour frais de recouvrement. Ces pénalités ne s’appliquent pas aux particuliers.</p>'''))
    S.append(sec('garanties', 'Réception des travaux et garanties légales',
        'articles 1792, 1792-2, 1792-3, 1792-4-1 et 1792-6 du Code civil ; articles 1641 à 1649 du Code civil ; articles L217-3 à L217-20 du Code de la consommation.',
        table(['Garantie', 'Durée', 'Ce qu’elle couvre'], [
            ('Parfait achèvement', '1 an après la réception', 'Tous les défauts signalés à la réception ou dans l’année qui suit, quelle que soit leur importance.'),
            ('Bon fonctionnement (biennale)', '2 ans après la réception', 'Les équipements qu’on peut retirer sans abîmer le bâti : portes intérieures, volets, robinetterie, radiateurs.'),
            ('Décennale', '10 ans après la réception', 'Les dommages qui compromettent la solidité de l’ouvrage ou le rendent impropre à son usage, par exemple un défaut d’étanchéité de douche qui abîme le plancher.'),
            ('Conformité', '2 ans après la livraison', 'Les matériaux et équipements que nous vous vendons, s’ils ne correspondent pas au devis ou présentent un défaut.'),
            ('Vices cachés', '2 ans après la découverte du vice', 'Les défauts cachés qui rendent un matériau ou un équipement impropre à son usage.'),
        ]) + '''<p><strong>La réception.</strong> À la fin du chantier, nous faisons le tour des pièces ensemble et signons un procès-verbal de réception, avec ou sans réserves. C’est cette date qui fait courir les garanties. Les réserves notées sont levées dans le délai convenu sur le procès-verbal.</p>
<p>Pour faire jouer une garantie, écrivez-nous en décrivant le problème, avec une photo si possible. Nous venons constater le désordre sous 15 jours. Ces garanties s’appliquent sans supplément de prix et ne peuvent pas être écartées par le contrat.</p>'''))
    S.append(sec('mediation', 'Réclamations et médiation de la consommation',
        'articles L611-1, L612-1, L616-1 et R616-1 du Code de la consommation.',
        f'''<p>Pour toute réclamation, écrivez-nous d’abord à {mail} ou au {adr}. Nous vous répondons sous 15 jours.</p>
<p>Si le désaccord persiste, vous pouvez saisir gratuitement le médiateur de la consommation dont nous relevons, au plus tard un an après votre réclamation écrite. Le médiateur est indépendant : il propose une solution que chacun reste libre d’accepter ou de refuser.</p>
{dl([('Médiateur', '[Nom du médiateur de la consommation]'), ('Adresse', '[Adresse postale]'), ('Site internet', '[Adresse du site, avec le formulaire de saisine]')])}'''))
    S.append(sec('avis', 'Avis clients',
        'article L111-7-2 et articles D111-16 à D111-19 du Code de la consommation.',
        '''<p>Un site qui publie des avis de clients doit dire s’ils sont vérifiés et, si oui, comment.</p>
<ul class="ml-list">
  <li><strong>Origine :</strong> les avis affichés sont recueillis par e-mail après la réception des travaux.</li>
  <li><strong>Contrôle :</strong> [les avis sont / ne sont pas] vérifiés. La vérification consiste à [rapprocher chaque avis d’un procès-verbal de réception].</li>
  <li><strong>Sélection :</strong> [préciser si tous les avis sont publiés, ou selon quels critères].</li>
  <li><strong>Contrepartie :</strong> aucun avis n’est rémunéré ni récompensé.</li>
</ul>
<p>Sur cette maquette, l’avis affiché sur la page d’accueil est un exemple rédigé pour la démonstration.</p>'''))
    photos = table(['Emplacement', 'Photographe', 'Source'], [(w, a, f'<a href="{u}">Pexels</a>') for w, a, u in PHOTOS])
    S.append(sec('propriete', 'Propriété intellectuelle et crédits photos',
        'articles L111-1, L122-4 et L335-2 du Code de la propriété intellectuelle.',
        f'''<p>Les textes, le logo, la charte graphique et la mise en page de ce site appartiennent à Atelier Cordeau. Les reproduire ou les réutiliser sans autorisation écrite constitue une contrefaçon.</p>
<p><strong>Photos.</strong> Les photos viennent de Pexels et sont utilisées selon la <a href="https://www.pexels.com/license/">licence Pexels</a>, qui autorise l’usage commercial. Aucune ne représente l’entreprise, ses salariés ou ses chantiers : ce sont des illustrations à remplacer par des photos réelles.</p>
{photos}
<p><strong>Polices de caractères.</strong> Archivo et IBM Plex Mono, distribuées sous licence libre SIL Open Font License 1.1.</p>'''))
    S.append(sec('responsabilite', 'Liens et responsabilité',
        'article 1240 du Code civil ; article 6 de la LCEN.',
        '''<p>Les informations de ce site sont données à titre indicatif ; seuls le devis signé et la facture font foi. Nous les mettons à jour régulièrement, mais une erreur ou un retard de mise à jour reste possible : signalez-le-nous et nous le corrigerons.</p>
<p>Les liens vers d’autres sites (Pexels, CNIL, Bloctel, médiateur) sont fournis pour votre information. Nous ne contrôlons pas leur contenu et n’en sommes pas responsables.</p>'''))
    S.append(sec('donnees', 'Données personnelles',
        'règlement (UE) 2016/679 du 27 avril 2016 (RGPD), notamment ses articles 5, 6, 12 à 22, 28, 32, 37, 44 à 49 et 77 ; loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés, notamment son article 85 ; articles L223-1 et L223-2 du Code de la consommation.',
        f'''<h3>Qui est responsable de vos données</h3>
<p>Atelier Cordeau, {adr}, {mail}, représentée par son gérant. Au vu de sa taille et de son activité, l’entreprise n’est pas tenue de désigner un délégué à la protection des données (article 37 du RGPD) ; le gérant est votre interlocuteur pour toute question.</p>
<h3>Ce que nous collectons, pourquoi, et combien de temps</h3>
<p>Nous ne collectons que ce qui sert à vous répondre et à réaliser les travaux. Dans le formulaire de contact, seuls le nom, le téléphone et votre accord sont obligatoires.</p>
{table(['Données', 'Pourquoi', 'Base légale (art. 6 RGPD)', 'Conservation'], [
  ('Nom, téléphone, e-mail, commune, type de travaux', 'Vous rappeler et organiser la visite', 'Mesures précontractuelles à votre demande (6.1.b)', '3 ans après le dernier contact sans suite'),
  ('Description du projet', 'Préparer la visite et le devis', 'Mesures précontractuelles (6.1.b)', '3 ans, ou durée du contrat si les travaux sont réalisés'),
  ('Devis signé, adresse du chantier, plans cotés, photos du chantier', 'Réaliser les travaux et assurer les garanties', 'Exécution du contrat (6.1.b)', '10 ans après la réception, durée de la garantie décennale'),
  ('Factures et pièces comptables', 'Tenir la comptabilité', 'Obligation légale (6.1.c), article L123-22 du Code de commerce', '10 ans'),
  ('Photos du chantier publiées sur le site', 'Montrer nos réalisations', 'Votre consentement écrit (6.1.a), retirable à tout moment', 'Jusqu’au retrait de votre accord'),
])}
<h3>Qui peut voir vos données</h3>
<p>Seuls le gérant, les chefs de chantier et la personne chargée de l’administratif y ont accès, ainsi que nos prestataires techniques : l’hébergeur du site, [l’outil d’envoi du formulaire] et [le logiciel de devis et de facturation]. Ils agissent uniquement sur nos instructions, dans le cadre d’un contrat conforme à l’article 28 du RGPD. Les artisans partenaires d’un lot reçoivent l’adresse du chantier et vos coordonnées, et rien d’autre. Notre expert-comptable et notre assureur peuvent y accéder quand c’est nécessaire. Vos données ne sont jamais vendues, louées ni utilisées pour de la publicité.</p>
<h3>Où elles sont stockées et comment elles sont protégées</h3>
<p>Vos données sont hébergées dans l’Union européenne. Si un prestataire devait les traiter hors de l’Union, ce transfert serait encadré par l’une des garanties prévues aux articles 44 à 49 du RGPD. Le site est servi en HTTPS, les accès à nos outils sont protégés par mot de passe et réservés aux personnes qui en ont besoin, et les dossiers papier sont rangés sous clé à l’atelier (article 32 du RGPD).</p>
<h3>Vos droits</h3>
<ul class="ml-list">
  <li><strong>Accès :</strong> savoir quelles données nous avons sur vous et en obtenir une copie (article 15).</li>
  <li><strong>Rectification :</strong> faire corriger des données inexactes ou incomplètes (article 16).</li>
  <li><strong>Effacement :</strong> faire supprimer vos données quand elles ne sont plus nécessaires, sauf celles que la loi nous oblige à garder, comme les factures (article 17).</li>
  <li><strong>Limitation :</strong> demander que vos données soient conservées sans être utilisées, le temps de vérifier une contestation (article 18).</li>
  <li><strong>Portabilité :</strong> récupérer les données que vous nous avez fournies dans un format lisible par machine (article 20).</li>
  <li><strong>Opposition :</strong> vous opposer à un traitement fondé sur notre intérêt légitime (article 21).</li>
  <li><strong>Retrait du consentement :</strong> retirer à tout moment votre accord, par exemple pour la publication des photos de votre chantier (article 7).</li>
  <li><strong>Directives après décès :</strong> indiquer ce que doivent devenir vos données après votre décès (article 85 de la loi Informatique et Libertés).</li>
</ul>
<p>Pour exercer ces droits, écrivez à {mail} ou au {adr}. Nous répondons dans un délai d’un mois, prolongeable de deux mois si la demande est complexe ; nous vous prévenons alors. Nous pouvons vous demander de justifier de votre identité en cas de doute raisonnable.</p>
<p>Si vous estimez que vos droits ne sont pas respectés, vous pouvez adresser une réclamation à la Commission nationale de l’informatique et des libertés (CNIL), 3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07, ou sur <a href="https://www.cnil.fr/fr/plaintes">cnil.fr</a> (article 77 du RGPD).</p>
<h3>Démarchage téléphonique</h3>
<p>Si vous ne souhaitez pas être démarché par téléphone, vous pouvez vous inscrire gratuitement sur la liste d’opposition <a href="https://www.bloctel.gouv.fr">Bloctel</a>. Nous n’utilisons votre numéro que pour répondre à votre demande et ne vous démarchons jamais.</p>'''))
    S.append(sec('cookies', 'Cookies et traceurs',
        'article 82 de la loi n° 78-17 du 6 janvier 1978 ; délibérations de la CNIL n° 2020-091 (lignes directrices) et n° 2020-092 (recommandation) du 17 septembre 2020.',
        '''<p>Un cookie est un petit fichier déposé sur votre appareil. Hors cookies strictement nécessaires, la loi impose de recueillir votre accord avant d’en déposer, et de vous laisser refuser aussi facilement qu’accepter.</p>
<p>Ce site ne dépose aucun cookie et n’utilise aucun outil de mesure d’audience ni de publicité : c’est pourquoi aucun bandeau ne vous demande votre accord. Il garde seulement, le temps de votre visite, une information technique dans la mémoire de votre navigateur (« sessionStorage ») pour l’animation entre les pages ; elle n’est transmise à personne et disparaît à la fermeture de l’onglet.</p>
<p>Les polices de caractères et les scripts sont hébergés sur le même serveur que le site. Aucune ressource n’est chargée depuis un service tiers : votre adresse IP n’est transmise qu’à notre hébergeur.</p>
<p>Si un outil de mesure d’audience ou une carte interactive est ajouté plus tard, un bandeau de consentement sera mis en place et cette section indiquera chaque outil, sa finalité et sa durée de conservation (13 mois au plus pour les traceurs).</p>'''))
    S.append(sec('accessibilite', 'Accessibilité',
        'article 47 de la loi n° 2005-102 du 11 février 2005, modifié par l’ordonnance n° 2023-859 du 6 septembre 2023 (transposition de la directive (UE) 2019/882).',
        '''<p>Avec moins de 10 salariés et un chiffre d’affaires inférieur à 2 millions d’euros, Atelier Cordeau est une microentreprise : elle n’est pas soumise à l’obligation de déclaration d’accessibilité. Le site est tout de même conçu pour se naviguer au clavier, rester lisible en grand format, respecter le réglage « réduire les animations » de votre appareil et fonctionner avec les lecteurs d’écran. Si une page vous pose problème, écrivez-nous : nous vous transmettrons l’information autrement.</p>'''))
    S.append(sec('droit', 'Droit applicable et litiges',
        'article R631-3 du Code de la consommation ; articles 42 et 46 du Code de procédure civile.',
        '''<p>Ce site et les contrats conclus avec Atelier Cordeau sont soumis au droit français. En cas de litige, après une tentative de solution amiable ou une médiation, un consommateur peut saisir, à son choix, le tribunal du lieu où il demeurait au moment de la signature du contrat, celui du lieu des travaux ou celui du siège de l’entreprise.</p>'''))
    toc = ''.join(f'<li><a class="link-utility" href="#{sid}"><span class="mono">{i+1:02d}</span> {t}</a></li>' for i, (sid, t) in enumerate(secs))
    actions = '<button class="btn" type="button" data-print><span>Imprimer / PDF</span></button>'
    body = f'''
<article class="ml">
  <header class="ml-head">
    <p class="crumbs mono">Informations légales</p>
    <h1 class="display-xl">Mentions légales et données personnelles</h1>
    <p class="ml-lead">Qui édite ce site, à quelles conditions nous intervenons chez vous, et ce que nous faisons des informations que vous nous confiez. Chaque partie indique les textes de loi sur lesquels elle repose.</p>
    <p class="ml-meta mono">Dernière mise à jour : 12 novembre 2026 · Version 1.0</p>
    <div class="ml-actions">{actions}<a class="link-trait" href="mentions-legales.pdf">Ouvrir la version PDF</a></div>
    <p class="ml-hint mono">Dans la fenêtre d’impression, choisissez « Enregistrer au format PDF » pour garder une copie.</p>
    <p class="ml-note">Maquette. Atelier Cordeau est une entreprise fictive. Les valeurs entre crochets et celles marquées « fictif » sont à remplacer par celles du client, et le texte doit être relu par un juriste avant la mise en ligne.</p>
  </header>
  <div class="ml-layout">
    <nav class="ml-toc" aria-label="Sommaire"><p class="label">Sommaire</p><ol>{toc}</ol></nav>
    <div class="ml-body">
      <p class="print-only ml-print-src mono">Atelier Cordeau · {adr} · {B["phone"]} · {B["email"]}</p>
      {''.join(S)}
      <div class="ml-end">{actions}<a class="link-trait" href="#contenu">Revenir en haut</a></div>
    </div>
  </div>
</article>
'''
    return page(path='mentions-legales.html', title='Mentions légales et données personnelles · Atelier Cordeau',
                description='Éditeur, assurances, devis, rétractation, garanties, médiation, données personnelles et cookies du site Atelier Cordeau, avec les textes de loi.',
                body=body, body_class='page-legal')

def notfound():
    body = f'''
<section class="nf" aria-labelledby="nf-title">
  <p class="mono nf-code">Erreur 404</p>
  <h1 id="nf-title" class="display-xl">Ce mur n’existe pas encore.</h1>
  {snap_line('snap-line-nf')}
  <p>La page que vous cherchez a été déplacée ou n’a jamais été tracée.</p>
  <div class="hero-actions"><a class="btn" href="index.html"><span>Retour à l’accueil</span></a><a class="link-trait" href="index.html#realisations">Voir les réalisations</a></div>
</section>
'''
    return page(path='404.html', title='Page introuvable · Atelier Cordeau', description='Cette page n’existe pas.', body=body, body_class='page-404')


VARIANTES = [
    ('cordeau', 'A. Le cordeau (actuel)', 'Ligne bleue de poudre de craie, poignée ronde. Elle vibre quand on la lâche, comme un cordeau qu’on claque sur un mur.', False),
    ('ruban', 'B. Le ruban de masquage', 'Une bande de ruban beige posée verticalement, comme celle qu’on colle avant de peindre. Les mots « chantier » et « livré » sont écrits dessus au feutre.', True),
    ('metre', 'C. Le mètre ruban', 'Un mètre jaune gradué tous les centimètres, avec son boîtier comme poignée. Évoque la prise de mesures du relevé.', True),
    ('laser', 'D. Le niveau laser', 'Un trait rouge fin et lumineux, avec le petit boîtier du laser posé en bas de l’image. Très précis, très technique.', True),
    ('crayon', 'E. Le trait de crayon et la cote', 'Un trait de crayon de charpentier, et au centre une étiquette de cote « Chantier | Livré » comme sur un plan.', False),
    ('joint', 'F. Le joint ouvert', 'Une simple fente couleur enduit qui coupe l’image en deux, et deux chevrons au centre. La version la plus sobre.', True),
]

def variantes():
    p = PROJECTS[0]
    cards = []
    for i, (v, t, d, rigid) in enumerate(VARIANTES):
        cards.append(f'''<section class="var-card" aria-labelledby="v-{v}">
  <div class="var-text"><h2 id="v-{v}" class="var-title">{t}</h2><p>{d}</p></div>
  {cordeau_stage(p['before'], p['after'], labels=('Chantier', 'Livré'), cls='cordeau-var', start=0.5, pos=(p['pos_before'], p['pos_after']), sizes='(min-width: 900px) 66vw, 100vw', variant=v, rigid=rigid, range_label=f'{t} : position de la barre')}
</section>''')
    body = f'''
<section class="var-page" aria-labelledby="var-h1">
  <p class="crumbs mono">Page de travail, non publiée dans le menu</p>
  <h1 id="var-h1" class="display-xl">Six barres pour le avant/après</h1>
  <p class="var-lead">Passez la souris sur chaque photo (ou glissez le doigt, ou utilisez les flèches du clavier) pour comparer. Toutes utilisent les mêmes photos de l’échoppe.</p>
  {''.join(cards)}
</section>
'''
    return page(path='variantes-barre.html', title='Variantes de la barre avant/après · Atelier Cordeau',
                description='Page de travail : six designs pour la barre de comparaison chantier / livré.', body=body, body_class='page-var')

def write(name, html):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    write('index.html', home())
    for i, p in enumerate(PROJECTS):
        write(p['slug'] + '.html', project_page(i))
    write('contact.html', contact())
    write('mentions-legales.html', legal())
    write('404.html', notfound())
    write('variantes-barre.html', variantes().replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"', 1))
    urls = ['', 'contact.html', 'mentions-legales.html'] + [p['slug'] + '.html' for p in PROJECTS]
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          ''.join(f'  <url><loc>{SITE_URL}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n')
    print('pages générées')
