+++
title = "Activité 8 - tableau périodique, molécule, données biologiques"
weight = 81
+++

## Sujet

**Thème : Structures de données (listes et dictionnaires)**
**Durée prévue :** 1 h 30 à 1 h 50
**Travail en équipe de 2 ou 3**

## Objectifs pédagogiques

* Savoir représenter des entités scientifiques sous forme de structures de données Python
* Utiliser les dictionnaires pour associer des clés et des valeurs significatives
* Accéder et modifier les éléments d’une structure
* Appliquer ces compétences à des situations authentiques en sciences

## Contexte

Les structures de données comme les **dictionnaires** et les **listes** sont très utiles pour représenter de l'information scientifique structurée. Cette activité propose trois mini-situations où vous devrez utiliser ces outils pour modéliser et manipuler des données pertinentes.

---

## Partie 1 – Mini-tableau périodique (Dictionnaire)

On souhaite représenter certains éléments du tableau périodique dans un dictionnaire Python. Chaque élément est représenté par son symbole, et on veut stocker son nom et sa masse atomique.

```python
elements = {
    "H": {"nom": "Hydrogène", "masse": 1.008},
    "O": {"nom": "Oxygène", "masse": 15.999},
    "C": {"nom": "Carbone", "masse": 12.011}
}
```

**Tâches**

* Ajouter un nouvel élément (`N` pour azote, masse 14.007)
* Afficher la masse atomique de l’oxygène
* Afficher tous les symboles et noms avec une boucle

---

## Partie 2 – Masse molaire d’une molécule (Listes et dictionnaire)

Une molécule est une liste d’atomes, et on veut calculer sa masse molaire à partir des masses de ses éléments.

```python
eau = ["H", "H", "O"]  # molécule d’eau
```

**Tâches**

* Utiliser le dictionnaire précédent pour calculer la masse molaire de la molécule d’eau
* Tester avec une autre molécule simple comme le dioxyde de carbone (`["C", "O", "O"]`)
* Ajouter une fonction `masse_molaire(molecule)` qui retourne la masse totale

---

## Partie 3 – Données biologiques (Liste de dictionnaires)

On veut représenter des observations d’un biologiste sous forme de structures Python. Chaque observation contient le nom d’une espèce, sa taille moyenne (cm) et son habitat.

```python
observations = [
    {"espèce": "Grenouille verte", "taille_cm": 9, "habitat": "Marais"},
    {"espèce": "Salamandre tachetée", "taille_cm": 15, "habitat": "Forêt"},
    {"espèce": "Triton du nord", "taille_cm": 10, "habitat": "Étang"}
]
```

**Tâches**

* Afficher les espèces vivant en forêt
* Calculer la taille moyenne de toutes les espèces
* Trier les observations par taille (optionnel)


## Résultat attendu

Un script bien structuré utilisant :

* au moins un dictionnaire imbriqué
* une ou deux fonctions simples
* des boucles pour le traitement des données

