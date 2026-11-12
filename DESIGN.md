# Atelier Cordeau : maquette de site de rénovation

## Brief
- **Sujet :** Atelier Cordeau, entreprise **fictive** de rénovation intérieure à Bordeaux (échoppes, appartements anciens, cuisines, salles de bains). Maquette de démonstration pour artisans du bâtiment.
- **Public :** propriétaires bordelais qui préparent des travaux, souvent dans l'ancien.
- **Rôle du site :** obtenir une demande de visite (formulaire ou appel).
- **Langue :** français. **Stack :** HTML/CSS/JS statique (comme les autres maquettes du projet), GSAP + ScrollTrigger + Lenis hébergés localement. Pages générées par `sources/build.py`.

## Trois concepts
| Territoire | Idée | Signature | Ancre | Orig. | Fit | Faisab. | Portab. |
|---|---|---|---|---|---|---|---|
| Matière du métier | **Le cordeau** : la ligne bleue claquée sur le mur avant de couper sépare le chantier de la pièce livrée | La ligne claque, vibre puis se pose ; elle sépare « chantier » et « livré » | Les rénovateurs tracent au cordeau bleu avant toute dépose | 4 | 5 | 4 | 2 |
| Lieu | La pierre blonde des échoppes bordelaises, le site comme une façade | Une façade qui se ravale au scroll | Bordeaux, l'échoppe | 3 | 4 | 3 | 3 |
| Méthode | Le carnet de chantier, chaque page est un vendredi de chantier | Les pages se tournent semaine après semaine | Le point photo hebdomadaire | 3 | 4 | 3 | 3 |

**Choix : le cordeau.** C'est le geste qui précède toute rénovation, et il fournit à la fois l'outil de comparaison avant/après et le langage graphique du site.

## Concept Card
```
Idée :        On trace la ligne, puis on rénove : une ligne de cordeau bleue sépare le chantier de la pièce finie.
Métaphore :   le marquage de chantier (cordeau à poudre bleue, crayon de charpentier, ruban de masquage, cotes)
Signature :   la ligne de cordeau qui claque et vibre au-dessus de deux photos ; au scroll (accueil) ou au doigt (réalisations) elle balaie le chantier pour révéler la pièce livrée
Émotion :     la netteté d'un geste de pro, la promesse d'un avant/après
Verbe :       « claquer comme un cordeau » : arrivée nette, petite vibration amortie, puis immobile
Capture :     la pièce en chantier à gauche, la pièce bleue au parquet en chevrons à droite, la ligne bleue entre les deux
```

## Système
- **Palette :** enduit `#ECEAE4` (fond), graphite `#17181A` (encre), gris ciment `#5B5A55` (texte secondaire), joint `#CBC6BB` (filets), cordeau `#1E46D8` (accent, poudre bleue), ruban `#E6D69C` (étiquettes façon ruban de masquage). Fond sombre : graphite, accent `#8FA8FF`.
- **Typo :** Archivo variable (axe largeur) : titres en largeur 68, graisse 700, approche négative ; texte en largeur 100. IBM Plex Mono 400/500 pour les cotes, étiquettes et métadonnées. Polices auto-hébergées (OFL).
- **Grille :** 12 colonnes, gouttière 20 px, marges `clamp(16px, 4vw, 56px)`. Les titres s'alignent sur la colonne 1, les textes courants démarrent colonne 7 sur desktop.
- **Forme :** angles droits partout (rayon 0), sauf la poignée de la ligne (cercle).
- **Mouvement :** une famille d'easing (`expo.out` pour les entrées, `back.out(1.6)` réservé au claquement). Durées : petits éléments 0,35 s, grands 0,9 s. Une seule horloge : `gsap.ticker`.
- **Interactions :** liens primaires = trait bleu qui claque de gauche à droite ; boutons = remplissage bleu qui balaie de gauche à droite ; lignes de réalisations = la ligne de cordeau de la vignette balaie jusqu'au livré.
- **Idle :** la ligne de cordeau garde une vibration très faible au repos (amplitude ~1 px, lente), à l'arrêt hors écran et en mouvement réduit.

## Composition
```
ACCUEIL
[bandeau maquette]
[logo ............................. nav · Demander une visite]
[  PHOTO CHANTIER   |cordeau|   PHOTO LIVRÉE              ]  ← épinglé, scroll = la ligne balaie
[  H1 en bas à gauche, sur voile ]       [ruban: Livré, sem. 11]
---------------------------------------------------------------
[ Manifeste en grand (8 col) ]      [photo crayon/mètre, décalée]
--------------------------- ligne qui claque -------------------
[ Index des réalisations : lignes pleine largeur, vignette avant/après à droite ]
---------------------------------------------------------------
[ titre collant + photo pose ] | [ 6 métiers, lignes avec cotes ]
---------------------------------------------------------------
[ MÉTHODE fond graphite : une ligne horizontale, 4 repères ]
---------------------------------------------------------------
[ Avis (exemple) grande citation décalée ]
---------------------------------------------------------------
[ Contact : grand appel, téléphone, communes desservies ]
[ pied de page ]
```

## Test de banalité
- Un modèle générique aurait fait un hero centré « Rénovez votre intérieur » sur une photo de salon + 3 cartes de services. Remplacé par l'avant/après coupé par la ligne de cordeau.
- Palette générique beige + terracotta évitée : enduit gris clair + bleu de cordeau.
- Les numéros 01-04 ne servent qu'à la méthode, qui est une vraie séquence.
