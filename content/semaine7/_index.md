+++
chapter = true
pre = "7."
title = " Tableaux numpy et droite de régression"
weight = 107
draft = false
+++


## Objectifs

* Créer des tableaux de données à une ou deux dimensions.
* Calculer des **moyennes** et **écarts types**.
* Gérer des données **expérimentales incomplètes** (`np.nan`).
* Comparer des résultats entre éléments ou conditions.
* Filtrer des données selon des conditions.
* Tracer un graphique à barres muni d'une barre d'erreur avec `matplotlib`.
* Tracer une droite de régression et interpréter la pente, l’ordonnée à l’origine et le coefficient de détermination R²
* Établir une relation entre deux données

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

## Filtrage de données

1. Créer un tableau et afficher uniquement certaines valeurs selon une condition

```python
array = np.array([2, 5, 7, 1, 8, 3])
masque = array > 5	# Masquage : valeurs supérieures à 5
print(f"Masque booléen : {masque}
valeurs_filtrées = array[masque]
print(f"Valeurs supérieures à 5 : {valeurs_filtrées}")
```
**Sortie attendue :**

```
Masque booléen : [False False  True False  True False]
Valeurs supérieures à 5 : [7 8]
```

2. Comptage conditionnel avec `np.sum`

Compter combien de valeurs respectent un seuil donné.

```python
array = np.array([3, 7, 4, 6, 2, 9, 5])
seuil = 5
nb_valeurs = np.sum(array > seuil)	# Comptage des valeurs > 5
print(f"Nombre de valeurs supérieures à {seuil} : {nb_valeurs}")
```

**Sortie attendue :**
```
Nombre de valeurs supérieures à 5 : 3
```

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


## Tracer un graphique à barres avec barre d'erreurs

### Importer la bibliothèque

```python
import matplotlib.pyplot as plt
```

### Graphique à barres

**Exemple de base :**

```python
noms = ["A", "B", "C"]
valeurs = [4, 7, 5]

plt.bar(noms, valeurs)
plt.title("Résultats")
plt.xticks(rotation=0)
plt.legend(["Score"])
plt.show()
```

| Fonction        | Rôle                                |
| --------------- | ----------------------------------- |
| `plt.bar(x, y)` | Crée des barres                     |
| `plt.xticks()`  | Contrôle les étiquettes sur l’axe x |


### Graphique avec barres d’erreur

**Exemple :**

```python
x = [1, 2, 3]
y = [10, 12, 9]
erreurs = [0.5, 0.3, 0.6]

plt.errorbar(x, y, yerr=erreurs, fmt="o", label="Mesures")
plt.title("Mesures avec incertitude")
plt.legend()
plt.grid(True)
plt.show()
```

| Argument  | Signification                    |
| --------- | -------------------------------- |
| `yerr`    | barres d’erreur verticales       |
| `xerr`    | (optionnel) erreurs horizontales |
| `fmt="o"` | style des points                 |


## Tracer une droite de régression

**Rappel** : L'équation d'une droite est `y = a·x + b`

### Exemple

```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2.1, 4.2, 6.1, 8.0])

# Droite de régression : y = a·x + b

a, b = np.polyfit(x, y, 1)
y_reg = a * x + b

plt.plot(x, y, "o", label="Données")
plt.plot(x, y_reg, "-", label=f"y = {a:.2f}x + {b:.2f}")
plt.legend()
plt.grid(True)
plt.show()
```

## Affichage propre

| Fonction             | Effet                                            |
| -------------------- | ------------------------------------------------ |
| `plt.tight_layout()` | Ajuste l'espacement pour éviter le chevauchement 



## Résumé minimal

| Tâche                | Fonction                           |
| -------------------- | ---------------------------------- |
| Graphique à barres   | `plt.bar()`                        |
| Barres d’erreur      | `plt.errorbar()`                   |
| Droite de régression | `np.polyfit()`, `plt.plot()`       |
| Affichage final      | `plt.show()`, `plt.tight_layout()` |


---

## Exercices

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_numpy.ipynb)

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
4. Trace la droite de régression linéaire pour le graphique (`plot()`) de la pression en fonction de la hauteur.

---

## Atelier

## Exercice : Analyse d’une expérience sur l’effet de la lumière sur la croissance des plantes

Une équipe de recherche a mesuré la hauteur (en cm) de jeunes plantes après 10 jours de croissance dans trois conditions lumineuses différentes :

* lumière naturelle,
* lumière LED blanche,
* lumière LED rouge.

Pour chaque condition, 5 plantes ont été mesurées. Certaines données sont manquantes, car une ou deux plantes n’ont pas survécu. Les données brutes sont les suivantes :

| Condition   | Plante 1 | Plante 2 | Plante 3 | Plante 4 | Plante 5 |
| ----------- | -------- | -------- | -------- | -------- | -------- |
| Naturelle   | 12.5     | 13.1     | 12.9     | 13.0     | 12.8     |
| LED blanche | 11.2     | 11.6     | np.nan   | 11.5     | 11.3     |
| LED rouge   | 10.4     | 10.1     | 10.2     | np.nan   | np.nan   |


Écris un programme Python qui :

1. **Représente les données sous forme d’un tableau 2D** (à l’aide de `numpy`).
2. **Calcule la moyenne et l’écart-type** de la hauteur des plantes pour chaque condition, en **ignorant les valeurs manquantes**.
3. **Compare les hauteurs moyennes** entre les conditions (affiche par exemple la condition ayant la croissance moyenne la plus élevée).
4. **Affiche un résumé clair**, par exemple :
   ```
   Moyenne (Naturelle) = 12.86 cm, écart-type = 0.22 cm
   Moyenne (LED blanche) = ...
   ...
   Condition avec la plus grande croissance moyenne : Naturelle
   ```
5. Affiche le graphique montrant la croissance moyenne par type de lumière, avec **barres d’erreur** représentant l’écart-type.

### Aide

* Utilise `numpy.array()` pour construire le tableau.
* Utilise `np.nanmean()` et `np.nanstd()` pour les calculs.
* Tu peux créer une liste `conditions = ["Naturelle", "LED blanche", "LED rouge"]` pour faciliter l'affichage.
* Utilise `np.arrange()`, `plt.bar()` et `plt.plt.xticks()` pour construire le graphique.

---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [8. Dictionnaires](../semaine8/)
2. Faire les exercices de la [prochaine leçon :](../semaine8/#exercices)