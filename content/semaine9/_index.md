+++
chapter = true
pre = "9."
title = " Révision ou rattrapage"
weight = 109
draft = false
+++

## 1. Exercices simples

### Exercice 1 – Solubilité d’un sel

Un technicien a mesuré la **solubilité (en g/100 mL)** d’un sel à différentes températures. Une des valeurs est manquante.

```python
import numpy as np
sol = np.array([32.0, 35.5, np.nan, 37.2, 39.0])
```

1. Affiche toutes les solubilités mesurées.
2. Calcule la **moyenne** des valeurs disponibles (ignore la valeur manquante).
3. Calcule l’**écart type** des valeurs disponibles.
4. Interprète : La solubilité semble-t-elle augmenter de façon régulière ? Explique brièvement.

---

### Exercice 2 – Températures journalières

Un biologiste a mesuré la température **le matin, à midi et en fin d’après-midi** pendant 7 jours consécutifs.

```python
temperatures = np.array([
    [12.1, 17.3, 14.2],
    [11.8, 16.9, 13.9],
    [13.0, 18.1, 15.0],
    [12.5, 17.5, 14.7],
    [np.nan, 16.0, 14.0],
    [13.2, 18.0, 15.2],
    [12.0, 17.0, 14.5]
])
```

1. Quelle est la **forme** du tableau (`shape`) ?
2. Calcule la **moyenne quotidienne** (pour chaque jour).
3. Calcule la **moyenne du matin** (colonne 0), en ignorant la valeur manquante.
4. Que peut-on conclure sur la stabilité des températures matinales ?

---

### Exercice 3 – Analyse d’ADN

Deux échantillons d’ADN ont été analysés. On a mesuré l’intensité d’un marqueur génétique à 5 loci.

```python
ech1 = np.array([3.2, 2.8, 4.1, 3.9, 2.5])
ech2 = np.array([2.9, 3.0, 4.2, 4.0, 2.7])
```

1. Calcule le **profil combiné** des deux échantillons (somme des valeurs).
2. Calcule la **différence point par point** entre les deux échantillons (éch2 - éch1).
3. Calcule la **moyenne** et l’**écart type** de chaque échantillon.
4. En te basant sur l’écart type, lequel des deux échantillons est le plus homogène ?

---

### Exercice 4 – Pression dans un cylindre

On mesure la pression (en kPa) dans un cylindre rempli d’un gaz à différentes hauteurs.

```python
hauteur = np.linspace(0, 50, 6)  # [0, 10, 20, 30, 40, 50]
pression = np.array([101.3, 100.0, 98.7, 97.5, 96.2, 95.0])
```

1. Affiche les hauteurs et les pressions correspondantes.
2. Calcule la **variation de pression** entre chaque tranche de 10 cm.
3. Calcule la **moyenne de la pression** dans le cylindre.
4. Que peut-on dire de l’évolution de la pression avec la hauteur ?

---

### Exercice 5 – Croissance d’une plante

Une plante pousse de façon régulière : **2 cm par jour**. Elle mesure 5 cm au jour 0.

1. Crée un tableau représentant la **taille quotidienne de la plante** pendant 10 jours (sans engrais).
2. Simule l’effet d’un **engrais** qui augmente la croissance de **1 cm par jour**.
3. Calcule la **moyenne** de la taille de la plante **avec et sans engrais**.
4. Quel est l’effet de l’engrais en moyenne ? Justifie à l’aide des résultats.

---

## 2. Atelier

### Étude de la photosynthèse et de la température chez les plantes

Cet atelier permet de :

* manipuler des **fichiers CSV** avec `pandas` et `numpy`,
* utiliser des **listes**, **chaînes**, **tableaux NumPy** et **dictionnaires**,
* produire des **graphiques professionnels** avec `matplotlib`,
* réaliser une **analyse scientifique complète** d’un jeu de données réel ou simulé,
* réviser toutes les structures de contrôle (boucles, conditions, fonctions).

### Concepts révisés

| Compétence Python                     |
| ------------------------------------- |
| Listes, chaînes, boucles, conditions  |
| Dictionnaires                         |
| Tableaux NumPy et fonctions `np.*`    |
| Manipulation de fichiers `.csv`       |
| Visualisation avec matplotlib         |
| Régression linéaire                   |
| Fonctions personnalisées (facultatif) |

### Notebook de départ

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_photosynthese_etudiant.ipynb)

---

### Contexte scientifique

Un groupe de biologistes a mené une expérience pour étudier l'effet de la **température** sur l’**efficacité de la photosynthèse** chez plusieurs espèces végétales.

Ils ont récolté les données suivantes :

* Température (°C),
* Taux de photosynthèse (μmol CO₂/m²/s),
* Espèce (nom),
* Nom du capteur utilisé (chaîne de caractères),
* Date de la mesure.

Les données sont stockées dans le fichier `.csv` disponible ici : [photosynthese.csv](./photosynthese.csv), dont voici un aperçu :

| Température | Taux | Espèce      | Capteur    | Date       |
| ----------- | ---- | ----------- | ---------- | ---------- |
| 22.5        | 18.2 | Arabidopsis | capteur-01 | 2023-06-01 |
| 24.1        | 19.3 | Arabidopsis | capteur-02 | 2023-06-01 |
| 28.0        | 20.5 | Maïs        | capteur-03 | 2023-06-02 |
| ...         | ...  | ...         | ...        | ...        |

---

### Instructions

#### Étape 1 – Lecture et nettoyage des données

1. Charger le fichier CSV avec **`pandas`**.
2. Vérifier la présence de données manquantes (`NaN`) et les nettoyer si nécessaire.
3. Transformer les colonnes **Température** et **Taux** en tableaux **NumPy**.

#### Étape 2 – Analyse par espèce (listes et dictionnaires)

1. Créer un dictionnaire dont les clés sont les noms des **espèces**, et les valeurs sont des **listes de taux de photosynthèse**.
2. Calculer pour chaque espèce :

   * la moyenne,
   * l’écart-type,
   * le nombre de mesures.

> Vous pouvez stocker ces résultats dans un second dictionnaire (`résumé[espèce] = {...}`).

#### Étape 3 – Analyse graphique

1. Tracer un **nuage de points** température vs taux pour chaque espèce (couleurs différentes).
2. Ajouter une **droite de régression linéaire** pour chaque espèce.
3. Sauvegarder le graphique en PNG.

#### Étape 4 – Recherche par capteur (chaînes et conditions)

1. Demander à l’utilisateur le nom d’un capteur (`input()`).
2. Afficher toutes les mesures associées à ce capteur :

   * date, température, taux, espèce.

#### Étape 5 – Exploration temporelle (tri et regroupement)

1. Trier les données par **date**.
2. Pour chaque date, calculer le **taux moyen global**.
3. Afficher une **courbe de tendance** (date vs taux moyen).