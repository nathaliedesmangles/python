+++
chapter = true
pre = "<b>9.</b>"
title = " Tableaux NumPy"
weight = 109
draft = false
+++
 

## Objectifs

À la fin de cette leçon, vous devrez être capable de :

* Créer des tableaux de données à une ou deux dimensions.
* Calculer des **moyennes** et **écarts types**.
* Gérer des données **expérimentales incomplètes** (`np.nan`).
* Comparer des résultats entre éléments ou conditions.

---

<!--
## 1. Importer la bibliothèque

```python
import numpy as np
```


## 2. Créer un tableau de données (`array`)

**Tableau 1D**

```python
sol = np.array([32.0, 35.5, 37.2])
print(f"Solubilités mesurées : {sol}")
```

**Tableau 2D**

* Un **tableau numpy** multidimentionnel c'est un **tableau numpy** qui contient **une liste de listes**.

```python
matrice = np.array([[1, 2], [3, 4]])
print(matrice.shape)     # Affiche les dimensions (2 lignes, 2 colonnes)
```


## 3. Calculer la moyenne

```python
moy = np.mean(sol)
print(f"Moyenne : {moy:.2f} g/100mL")
```


## 4. Calculer l’écart type

```python
ecart = np.std(sol)
print(f"Écart type : {ecart:.2f}")
```


## 5. Ignorer des valeurs manquantes (`np.nan`)

Parfois, une mesure a été oubliée ou mal prise. On utilise `np.nan` pour représenter une valeur manquante :

```python
sol = np.array([32.0, np.nan, 37.2])
moy = np.nanmean(sol)
print(f"Moyenne (sans valeur manquante) : {moy:.2f} g/100mL")
```


## 6. Comparer plusieurs substances

```python
sol_A = np.array([35.0, 36.5, 38.0])
sol_B = np.array([15.0, 16.0, 15.5])

moy_A = np.mean(sol_A)
moy_B = np.mean(sol_B)

print(f"Solubilité moyenne A : {moy_A:.2f}")
print(f"Solubilité moyenne B : {moy_B:.2f}")
```


## 7. Interprétation conditionnelle

```python
if moy_A > moy_B:
    print(f"Le composé A est plus soluble que le composé B.")
else:
    print(f"Le composé B est plus soluble ou équivalent à A.")
```

---

## Exercices pratiques

### Exercice 1 – Moyenne et écart type

1. Crée un tableau avec les valeurs `[20.0, 22.5, 21.0, 23.5]`.
2. Calcule et affiche la moyenne et l’écart type avec des f-strings.


### Exercice 2 – Données incomplètes

1. Crée un tableau : `[18.0, np.nan, 19.5, 20.0]`.
2. Calcule la moyenne **en ignorant** la valeur manquante.
3. Affiche un message si la moyenne est supérieure à 19.


### Exercice 3 – Comparaison de deux composés

1. Crée deux tableaux :

   * A : `[40.0, 41.5, 42.0]`
   * B : `[35.0, 36.0, 36.5]`
2. Calcule les moyennes.
3. Affiche lequel a la solubilité la plus élevée.



===========================




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
-->

### Exercices à faire avant le cours

## À faire avant le prochain cours

1. Lire la matière sur [Traitement de fichiers CSV (Pandas) et graphiques (SciPy)](../semaine10/)
2. Faire les [exercices se trouvant à la fin de la leçon 10](../semaine10/#exercices-à-faire-avant-le-cours)

