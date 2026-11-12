# Atelier Cordeau : maquette de site de rénovation

Maquette de démonstration d'un site vitrine pour une entreprise **fictive** de rénovation intérieure à Bordeaux.

L'idée : une ligne de cordeau bleue sépare la pièce en chantier de la pièce livrée. Sur l'accueil, elle avance au défilement ; sur chaque fiche chantier, on la fait glisser.

## Voir le site
Ouvrir `index.html` dans un navigateur, ou servir le dossier :

```
python3 -m http.server 8000
```

## Pages
- `index.html` : accueil
- `echoppe-saint-genes.html`, `cuisine-chartrons.html`, `salle-de-bains-cauderan.html` : fiches chantier
- `contact.html` : formulaire (non relié)
- `mentions-legales.html` : mentions légales et données personnelles, avec les articles de loi et un bouton Imprimer / PDF ; `mentions-legales.pdf` en est la version PDF
- `404.html`

## Modifier
Tous les textes sont dans `sources/build.py`, puis `python3 sources/build.py`. Les photos se recadrent avec `sources/images.py`.

## À remplacer avant une vraie mise en ligne
Nom, coordonnées, chiffres, avis, informations légales (valeurs entre crochets ou marquées « fictif »), photos (Pexels, voir `PHOTOS.md`). Faire relire les mentions légales par un juriste.

Système graphique et concept : `DESIGN.md`.
