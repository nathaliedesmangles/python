+++
title = "Atelier 6"
weight = 106
draft = false
+++


## Objectifs

* Comprendre et manipuler des **listes simples** et **listes imbriquées**
* Appliquer les manipulations de listes sur les **chaînes de caractères**
* Dessiner des formes triangulaires à l'aide de la boucle `for`.
* Utiliser **matplotlib** pour tracer, **embellir** et **enregistrer** un graphique simple

---

## Exercice 

Une station météorologique t’a envoyé un fichier `.csv` nommé **`temperatures.csv`**, contenant les relevés bruts de températures (en °C) prises 3 fois par jour (matin, midi, soir) pendant 7 jours.

Tu disposes de la variable suivante :

```python
donnees = [
    "12.3, 16.8, 14.0",  # jour 1 : matin, midi, soir
    "11.5, 18.2, 15.4",
    "10.8, 17.6, 14.9",
    "13.0, 19.1, 16.3",
    "14.1, 20.2, 18.5",
    "12.9, 18.7, 16.2",
    "11.7, 17.8, 15.0"
]
```

#### Étapes à suivre :

1. **Extraction et nettoyage des données**

   * Transforme chaque chaîne de la liste `donnees` en une **liste de 3 nombres flottants**.
   * Obtiens ainsi une **liste imbriquée** `temperatures`, contenant 7 sous-listes (une par jour).

2. **Calculs sur les données**

   * Calcule la température moyenne de chaque jour, et stocke les résultats dans une **nouvelle liste** `moyennes_journalières`.
   * Trouve la température **maximale** de toute la semaine et **quel jour** elle a eu lieu.
   * Calcule la température **moyenne générale** sur l’ensemble de la semaine (toutes les valeurs confondues).

3. **Visualisation avec matplotlib**

   * Crée une figure avec :

     * l’axe X : jours (1 à 7)
     * l’axe Y : température moyenne journalière
   * Ajoute un **titre** et des **étiquettes d’axes**
   * Ajoute une **grille** et une **courbe** bleue avec marqueurs ronds (`'o'`)
   * **Sauvegarde** le graphique sous le nom `graphique_temperature.png`


4. **Exploration des chaînes de caractères**

   * Affiche le nombre de jours où la température du midi a dépassé **18°C**
   * Utilise la fonction `split()` pour isoler les températures de midi dans chaque chaîne.

---

### Exemple d’affichage attendu (partiel) :

```
Liste des températures (liste imbriquée) :
[[12.3, 16.8, 14.0], [11.5, 18.2, 15.4], ..., [11.7, 17.8, 15.0]]

Températures moyennes par jour :
[14.37, 15.03, 14.43, ..., 14.83]

Température maximale : 20.2°C (Jour 5)

Température moyenne de la semaine : 15.01°C

Nombre de jours où la température de midi a dépassé 18°C : 2
```

---

### Boîte à outils

* `float()` pour convertir un texte en nombre
* `split(',')` pour découper une chaîne
* `append()` pour ajouter dans une liste
* `sum()` et `len()` pour les moyennes
* `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.grid()`, `plt.savefig()`


## Exercice 2 – Motif croissant simple

* Écrire un programme qui affiche :
```
1
12
123
```

* Utiliser deux boucles `for` imbriquées.
* Ne pas utiliser de conditions (`if`).
* Aucun `input()` n’est requis.
* Le résultat doit s’afficher exactement comme ci-dessus.


## Exercice 3 – Motif croissant inversé (triangle renversé)

* Écrire un programme qui affiche :
```
123
12
1
```

* Utiliser une boucle `for` pour afficher un motif décroissant.
* Ne pas utiliser de conditions (`if`).
* Aucun `input()` n’est requis.
* Le résultat doit s’afficher exactement comme ci-dessus.


## Exercice 4 – Triangle inversé symétrique d’étoiles

* Écrire un programme qui affiche :
```
*****
 ***
  *
```

* Le motif doit être centré.
* Le nombre d’étoiles par ligne suit la suite : 5, 3, 1 (soit `(2 x i) – 1`).
* Utilise des boucles pour gérer les espaces et les étoiles.
* Ne pas utiliser de conditions (`if`).
* Aucun `input()` n’est requis.