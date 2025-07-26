+++
chapter = true
pre = "<b>9.</b>"
title = " Tableaux NumPy"
weight = 109
draft = false
+++
 

## Objectifs

* Créer des tableaux de données à une ou deux dimensions.
* Calculer des **moyennes** et **écarts types**.
* Gérer des données **expérimentales incomplètes** (`np.nan`).
* Comparer des résultats entre éléments ou conditions.

---

## Importer la bibliothèque

```python
import numpy as np
```


## Créer un tableau de données (`array`)

### Tableau 1D

```python
sol = np.array([32.0, 35.5, 37.2])
print(f"Solubilités mesurées : {sol}")
```

### Tableau 2D

* Un **tableau numpy** multidimentionnel c'est un **tableau numpy** qui contient **une liste de listes**.

```python
matrice = np.array([[1, 2], [3, 4]])
print(matrice.shape)     # Affiche les dimensions (2 lignes, 2 colonnes)
```

## Créer des tableaux remplis d’une même valeur

### Rempli de 0

```python
np.zeros((2, 3))  # Crée un tableau de 2 lignes et 3 colonnes rempli de 0
```

### Rempli de 1

```python
np.ones((3, 2))  # Crée un tableau de 3 lignes et 2 colonnes rempli de 1
```

### Rempli d'une autre valeur

```python
np.full(4, 0.5)  # Crée un tableau [0.5, 0.5, 0.5, 0.5]
```

### Rempli de valeurs espacées régulièrement (utile pour les graphiques)

```python
np.linspace(0, 10, 5)  # Crée un tableau : [ 0.  2.5  5.  7.5 10. ]
```

## Fonctions statistiques

### Calculer la moyenne des données

```python
moy = np.mean(sol)
print(f"Moyenne : {moy:.2f} g/100mL")
```


### Calculer l’écart type des données

```python
ecart = np.std(sol)
print(f"Écart type : {ecart:.2f}")
```

## Opérations vectorielles (rapides et simples)

L’intérêt principal de NumPy : on peut faire des **opérations sur tout un tableau en une seule ligne**.

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
```

### Addition élément par élément

```python
x + y    # [5 7 9]
```

### Soustraction élément par élément

```python
y - x    # [3 3 3]
```

### Multiplication par un scalaire

```python
x * 10   # [10 20 30]
```

### Division par un scalaire

```python
y / 2    # [2.  2.5 3. ]
```

## Ignorer des valeurs manquantes (`np.nan`)

Parfois, une mesure a été oubliée ou mal prise. On utilise `np.nan` pour représenter une valeur manquante :

```python
sol = np.array([32.0, np.nan, 37.2])
moy = np.nanmean(sol)
print(f"Moyenne (sans valeur manquante) : {moy:.2f} g/100mL")
```

La fonction `np.nanmean()` calcule **la moyenne des éléments en ignorant les valeurs `NaN`** (`Not a Number`), qui représentent généralement des données manquantes ou invalides.

{{% notice style="cyan" title="Notez" %}}
Sans `nanmean`, la fonction `np.mean(sol)` retournerait `nan` car une seule valeur `nan` dans la liste contamine le résultat.
{{% /notice %}}

---

{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* `import numpy as np` pour utiliser NumPy.
* `np.array()` crée un tableau de données.
* `np.zeros()`, `np.ones()`, `np.full()` créent des tableaux remplis.
* `np.linspace()` génère des valeurs espacées régulièrement.
* `np.mean()` calcule la moyenne.
* `np.std()` calcule l’écart type.
* `np.nanmean()` ignore les données manquantes.
* Les opérations (`+`, `-`, `*`, `/`) s’appliquent à tout le tableau.
{{% /notice %}}

---

## Exercices à faire avant le cours

[Bloc-notes de départ](./exercices_numpy.ipynb)

### Exercice 1 – Solubilité d’un sel

Une solution a été testée à différentes températures. Voici les résultats (en g/100 mL) :

```python
import numpy as np

sol = np.array([32.0, 35.5, np.nan, 37.2, 39.0])
```

1. Affiche les valeurs de solubilité.
2. Calcule et affiche la moyenne **en ignorant la valeur manquante**.
3. Calcule et affiche l’écart type.


### Exercice 2 – Températures journalières

Un thermomètre enregistre la température trois fois par jour pendant 7 jours :

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

1. Quelle est la forme (shape) du tableau ?
2. Calcule la **moyenne journalière** pour chaque jour.
3. Calcule la **température moyenne du matin** (1re colonne), en ignorant les données manquantes.


### Exercice 3 – Analyse d’ADN

Un test mesure l’intensité de 5 fragments ADN (valeurs arbitraires) pour deux échantillons :

```python
ech1 = np.array([3.2, 2.8, 4.1, 3.9, 2.5])
ech2 = np.array([2.9, 3.0, 4.2, 4.0, 2.7])
```

1. Additionne les deux tableaux pour obtenir un profil combiné.
2. Calcule la différence entre les deux échantillons.
3. Calcule la moyenne et l’écart type pour chacun des deux.


### Exercice 4 – Pressions dans un cylindre

On mesure la pression (en kPa) à différentes hauteurs (en cm) dans un cylindre :

```python
hauteur = np.linspace(0, 50, 6)  # [0, 10, 20, 30, 40, 50]
pression = np.array([101.3, 100.0, 98.7, 97.5, 96.2, 95.0])
```

1. Affiche les hauteurs et les pressions.
2. Calcule la variation de pression par tranche de 10 cm.
3. Calcule la moyenne de pression.


### Exercice 5 – Croissance d’une plante (modélisation simplifiée)

Une plante pousse selon ce modèle : sa taille augmente de 2 cm par jour.

1. Crée un tableau NumPy qui contient la taille de la plante pendant 10 jours, en partant de 5 cm.
2. Ajoute 1 cm supplémentaire à chaque valeur pour simuler un apport d’engrais.
3. Calcule la moyenne de croissance avec et sans engrais.

---

## À faire avant le prochain cours

1. Lire la matière sur [Traitement de fichiers CSV (Pandas) et graphiques](../semaine10/)
2. Faire les [exercices se trouvant à la fin de la leçon 10](../semaine10/#exercices-à-faire-avant-le-cours)

