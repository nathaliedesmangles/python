+++
chapter = true
pre = "<b>Semaine 9.</b>"
title = "Introduction à NumPy et Pandas"
weight = 90
+++
 

## Objectifs d’apprentissage

À la fin de cette leçon, vous devrez être capable de :

* Comprendre le rôle de **NumPy** pour le calcul scientifique rapide avec des tableaux.
* Utiliser **Pandas** pour manipuler des tableaux de données (DataFrame).
* Charger des données à partir d’un fichier CSV et faire des analyses simples.
* Appliquer des opérations mathématiques et statistiques de base.

---

## Pourquoi utiliser NumPy et Pandas?

Python est très puissant pour l’analyse de données scientifiques. Deux bibliothèques sont incontournables :

* **NumPy** (Numerical Python) : pour le calcul rapide sur des tableaux de données numériques.
* **Pandas** : pour organiser, filtrer et analyser des tableaux de données avec des étiquettes (colonnes/indices).

### Quand utiliser quoi?

* Tu veux faire des calculs rapides, des matrices, des moyennes, des sinusoïdes → NumPy
* Tu veux lire un fichier de données expérimentales, calculer une moyenne par groupe, trier ou filtrer → Pandas


## Introduction à NumPy

### Importation de la bibliothèque

```python
import numpy as np
```

### Création d’un tableau (array)

```python
a = np.array([1, 2, 3, 4])
print(a)
```

### Opérations mathématiques sur des tableaux

```python
b = a * 2           # Multiplie chaque élément par 2
c = np.sqrt(a)      # Racine carrée de chaque élément
```

### Quelques fonctions utiles

```python
np.mean(a)      # Moyenne
np.max(a)       # Maximum
np.min(a)       # Minimum
np.std(a)       # Écart-type
```

### Tableaux multidimensionnels

```python
matrice = np.array([[1, 2], [3, 4]])
print(matrice.shape)     # Affiche les dimensions (2 lignes, 2 colonnes)
```


## Introduction à Pandas

### Importation de la bibliothèque

```python
import pandas as pd
```

### Lecture d’un fichier CSV

```python
df = pd.read_csv("donnees.csv")
print(df.head())      # Affiche les 5 premières lignes
```

### Accès à une colonne

```python
df["Température"]
```

### Statistiques de base

```python
df.mean()
df["pH"].max()
```

### Filtrage des données

```python
df[df["Température"] > 25]     # Sélectionne les lignes où la température dépasse 25
```

### Moyenne par groupe

```python
df.groupby("Échantillon")["Concentration"].mean()
```


## Comparaison Pandas vs NumPy

| Tâche                      | NumPy | Pandas                           |
| -------------------------- | ----- | -------------------------------- |
| Calculs numériques rapides | ✅     | ❌ (moins rapide)                 |
| Données avec étiquettes    | ❌     | ✅ (DataFrame avec colonnes)      |
| Lecture de fichiers CSV    | ❌     | ✅                                |
| Visualisation rapide       | ❌     | ✅ (avec `.plot()` ou matplotlib) |


## Conclusion

NumPy est idéal pour les **tableaux numériques purs**. Pandas est parfait pour manipuler des **données tabulaires structurées** comme celles qu'on retrouve en laboratoire ou en recherche scientifique. Ces deux bibliothèques sont souvent utilisées ensemble.

