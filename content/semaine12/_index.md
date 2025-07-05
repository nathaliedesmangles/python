+++
chapter = true
pre = "<b>12.</b>"
title = "Manipulation de tableaux avec Pandas"
weight = 112
+++


## Objectifs d'apprentissage

* Créer un tableau de données (`DataFrame`)
* Lire un fichier CSV
* Parcourir les lignes d’un tableau
* Faire des calculs sur les colonnes
* Ajouter une nouvelle colonne

---

## 1. Importer Pandas

Avant toute manipulation :

```python
import pandas as pd
```


## 2. Créer un DataFrame à la main

```python
data = {
    "Nom": ["Alice", "Bob", "Chloé"],
    "Note": [88, 72, 91]
}
df = pd.DataFrame(data)
```

On crée un tableau à partir d’un **dictionnaire** : chaque clé devient une **colonne**.


## 3. Lire un fichier CSV

```python
df = pd.read_csv("fichier.csv")
```

Le fichier doit être dans le même dossier, ou donner le chemin complet.


## 4. Parcourir un DataFrame

### Avec `.iterrows()` :

```python
for index, row in df.iterrows():
    print(row["Nom"], row["Note"])
```

On peut accéder à chaque **ligne** comme un dictionnaire (`row["Nom"]`).


## 5. Calculs sur une colonne

| But      | Syntaxe                                   |
| -------- | ----------------------------------------- |
| Moyenne  | `df["Note"].mean()`                       |
| Arrondir | `df["Note"].round(1)`                     |
| Trier    | `df.sort_values("Note", ascending=False)` |

### Exemple :

```python
moy = df["Note"].mean()
print("Moyenne :", moy)
```


## 6. Ajouter une nouvelle colonne

On peut **créer une colonne calculée** à partir des autres.

### Exemple :

```python
df["Note_sur_10"] = df["Note"] / 10
```

Cela ajoute une nouvelle colonne au tableau.


## Résumé minimal

| Action               | Syntaxe                        |
| -------------------- | ------------------------------ |
| Créer un DataFrame   | `pd.DataFrame({...})`          |
| Lire CSV             | `pd.read_csv("fichier.csv")`   |
| Parcourir les lignes | `for i, row in df.iterrows():` |
| Moyenne              | `df["col"].mean()`             |
| Arrondir             | `df["col"].round(1)`           |
| Trier                | `df.sort_values("col")`        |
| Ajouter une colonne  | `df["nouvelle"] = ...`         |

---

## Exercices guidés

### Exercice 1 – Lire et afficher

**Énoncé :**
Lis un fichier `donnees.csv` contenant les colonnes `Nom` et `Valeur`.
Affiche chaque nom et sa valeur.

**Solution :**

```python
import pandas as pd

df = pd.read_csv("donnees.csv")
for i, row in df.iterrows():
    print(row["Nom"], "→", row["Valeur"])
```

### Exercice 2 – Calculer une colonne normalisée

**Énoncé :**
À partir de la colonne `Valeur`, crée une colonne `Valeur_sur_100` qui est `Valeur / 100`.

**Solution :**

```python
df["Valeur_sur_100"] = df["Valeur"] / 100
```


### Exercice 3 – Trier et afficher

**Énoncé :**
Trie les données selon la colonne `Valeur` en ordre décroissant et affiche-les.

**Solution :**

```python
df = df.sort_values("Valeur", ascending=False)
print(df)
```
