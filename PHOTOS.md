# Photos libres de droits : maquette Atelier Cordeau

Toutes les photos viennent de **Pexels** (licence : https://www.pexels.com/license/). Usage commercial autorisé, attribution non obligatoire ; le site crédite quand même chaque photographe (page Mentions légales). Noms relevés sur la page Pexels de chaque photo le 12 novembre 2026. Aucune photo ne montre de visage.

Les paires « chantier / livré » montrent **deux pièces différentes** : ce sont des illustrations. Pour un vrai client, il faut ses propres photos avant/après, prises du même point de vue (idéalement au même cadrage, pour que la ligne de cordeau coupe vraiment la même pièce).

| Emplacement | Fichier | Ce qu'on voit | Photographe | Lien |
|---|---|---|---|---|
| Accueil + échoppe, chantier | echoppe-chantier | Pièce en curage, bétonnière, porte-fenêtre | Francesco Ungaro | https://www.pexels.com/photo/interior-of-a-room-under-renovation-15798784/ |
| Accueil + échoppe, livré | echoppe-livree | Murs bleus, parquet en chevrons, baie | Max Vakhtbovych | https://www.pexels.com/photo/an-empty-room-with-blue-walls-7587859/ |
| Échoppe, détail | echoppe-detail | Plinthe moulurée, parquet pin | Lisa Anna | https://www.pexels.com/photo/parquet-in-a-minimalist-apartment-19866428/ |
| Cuisine, chantier | cuisine-chantier | Cloisons sur ossature, escabeaux | Rene Terp | https://www.pexels.com/photo/house-renovation-3990359/ |
| Cuisine, livrée | cuisine-livree | Cuisine en U blanche | Max Vakhtbovych | https://www.pexels.com/photo/interior-of-contemporary-kitchen-in-pastel-colors-6580220/ |
| Cuisine, détail | batons-rompus | Parquet à bâtons rompus | Magda Ehlers | https://www.pexels.com/photo/pattern-on-a-hardwood-flooring-15066939/ |
| Salle de bains, chantier | sdb-chantier | Cloisons ouvertes jusqu'à l'ossature | Monica Silvestre | https://www.pexels.com/photo/renovations-in-a-house-4756489/ |
| Salle de bains, livrée | sdb-livree | Douche vitrée, baignoire îlot | Spencer Lee Eiseman | https://www.pexels.com/photo/interior-design-of-bathroom-15369789/ |
| Accueil, manifeste | trait | Crayon et mètre ruban sur une planche | Ono Kosuki | https://www.pexels.com/photo/man-making-marks-on-wooden-plank-with-measurement-tape-5973909/ |
| Métiers + salle de bains, détail | pose-parquet | Pose de parquet au maillet | Kelly | https://www.pexels.com/photo/crop-man-installing-laminate-flooring-4263067/ |

Originaux dans `sources/originaux/`, versions web (WebP 900 et 1800 px) générées par `sources/images.py`.

## Pages
- `index.html` : accueil (avant/après épinglé, manifeste, réalisations, métiers, méthode, avis, contact)
- `echoppe-saint-genes.html`, `cuisine-chartrons.html`, `salle-de-bains-cauderan.html` : fiches chantier avec comparateur à glisser
- `contact.html` (formulaire non relié), `mentions-legales.html` (mentions légales et données personnelles sur une même page, articles de loi, bouton Imprimer / PDF, crédits photos) et `mentions-legales.pdf` (la même page en PDF A4), `404.html`

Tout le contenu se modifie dans `sources/build.py`, puis `python3 sources/build.py`.
