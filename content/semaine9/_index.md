+++
chapter = true
pre = "<b>9.</b>"
title = " Tableaux NumPy"
weight = 109
draft = true
+++
 

## Objectifs

À la fin de cette leçon, vous devrez être capable de :

* Utiliser les fonctions de NumPy pour créer des tableaux (1D, 2D)
* Utiliser les fonctions mathématiques de NumPy pour obtenir des statistiques sur les données


---


## Importer la bibliothèque

Avant d’utiliser NumPy, il faut l’importer au début de votre bloc-notes :

```python
import numpy as np
```

## Créer un tableau NumPy (`np.array()`)

Un **tableau NumPy** est une structure efficace pour manipuler des séries de données numériques (ex : mesures, positions, températures…).

```python
# Créer un tableau à partir d’une liste
mesures = np.array([3.2, 4.1, 2.9, 5.0])
print(mesures)
```

Résultat :

```
[3.2 4.1 2.9 5. ]
```


## Fonctions mathématiques utiles

### Moyenne

```python
np.mean(mesures)  # Moyenne des valeurs
```

### Écart-type (standard deviation)

```python
np.std(mesures)  # Mesure de la dispersion des données
```

### Tableau rempli d’une même valeur

**Que des 0**

```python
np.zeros((2, 3))  # Crée un tableau de 2 lignes et 3 colonnes rempli de 0
```

**Que des 1**

```python
np.ones((3, 2))  # Crée un tableau de 3 lignes et 2 colonnes rempli de 1
```

**Une autre valeur**

```python
np.full(4, 0.5)  # Crée un tableau [0.5, 0.5, 0.5, 0.5]
```

### Valeurs espacées régulièrement (utile pour les graphiques)

```python
np.linspace(0, 10, 5)  # Crée un tableau : [ 0.  2.5  5.  7.5 10. ]
```


## Opérations vectorielles (rapides et simples)

L’intérêt principal de NumPy : on peut faire des **opérations sur tout un tableau en une seule ligne**.

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
```

### Addition élément par élément :

```python
x + y    # [5 7 9]
```

### Soustraction :

```python
y - x    # [3 3 3]
```

### Multiplication par un scalaire :

```python
x * 10   # [10 20 30]
```

### Division :

```python
y / 2    # [2.  2.5 3. ]
```

## Exemple complet :

```python
hauteurs = np.array([165, 172, 180, 158])
moy = np.mean(hauteurs)
maxium = np.max(hauteurs)     
minimum = np.min(hauteurs)       
ecart = np.std(hauteurs)
print(f"Moyenne : {moy}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Écart-type :{ecart}")

# Centrer les données
hauteurs_centrees = hauteurs - moy
print(f"Hauteurs centrées : {hauteurs_centrees}")
```

## Tableaux multidimensionnels

* Un **tableau numpy** multidimentionnel c'est un **tableau numpy** qui contient **une liste de listes**.

```python
matrice = np.array([[1, 2], [3, 4]])
print(matrice.shape)     # Affiche les dimensions (2 lignes, 2 colonnes)
```


