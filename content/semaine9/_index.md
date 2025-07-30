+++
chapter = true
pre = "9."
title = " Révision ou rattrapage"
weight = 109
draft = false
+++
 
***AJOUTER GRAPHIQUE***

> **RAPPEL**: Semaine prochaine c'est le **deuxième examen** (25%)

## Objectifs

* Utiliser des **listes de listes** et des **listes de dictionnaires**.
* Parcourir des structures **imbriquées** avec des boucles `for` imbriquées.
* Réutiliser les connaissances sur listes, dictionnaires, et tableaux NumPy.
* Appliquer des **conditions** lors des parcours.
* Tracer des graphiques 

---


**Nom du fichier** : `revisions_eval2.ipynb`

## Exercice 1 – Liste de listes

# 1. Crée une grille 3x3 contenant les nombres de 1 à 9 (sous forme de liste de listes).
# 2. Affiche la valeur au centre.
# 3. Affiche tous les nombres un par un avec deux boucles for.

grille = [
    ...
]


## Exercice 2 – Liste de dictionnaires
# On t’a donné les données suivantes :

```
mesures = [
    {"id": "E1", "temp": 21.3, "pression": 101.5},
    {"id": "E2", "temp": 23.0, "pression": 100.8},
    {"id": "E3", "temp": 20.8, "pression": 102.0}
]
```

# 1. Affiche le nom de chaque échantillon et sa température.
# 2. Affiche uniquement les échantillons dont la température est supérieure à 22 °C.

---

## Exercice 3 – NumPy 2D
# Crée un tableau NumPy 2D à partir de cette grille :

```
import numpy as np

tableau = np.array(grille)
```
# 1. Affiche la moyenne de chaque ligne (utilise une boucle).
# 2. Affiche tous les éléments supérieurs à 5.

---

### Corrigé

Nom du fichier : `4_revisions_boucles_corrige.ipynb`

```python
# Exercice 1
grille = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grille[1][1])  # Centre = 5

for ligne in grille:
    for valeur in ligne:
        print(valeur)

# Exercice 2
mesures = [
    {"id": "E1", "temp": 21.3, "pression": 101.5},
    {"id": "E2", "temp": 23.0, "pression": 100.8},
    {"id": "E3", "temp": 20.8, "pression": 102.0}
]

for echantillon in mesures:
    print(f"{echantillon['id']} : {echantillon['temp']} °C")

for echantillon in mesures:
    if echantillon["temp"] > 22:
        print(f"{echantillon['id']} est chaud (>22 °C)")

# Exercice 3
import numpy as np

tableau = np.array(grille)

for ligne in tableau:
    print(np.mean(ligne))

print(tableau[tableau > 5])
```