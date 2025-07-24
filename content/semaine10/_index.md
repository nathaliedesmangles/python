+++
chapter = true
pre = "<b>10.</b>"
title = " Traitement de fichiers CSV avec Pandas et graphiques SciPy "
weight = 110
draft = false
+++


## Objectifs

* Lire un tableau contenant des données expérimentales
* Explorer les données
* Filtrer les résultats pour donnée ciblée.
* Comparer des valeurs selon une donnée
* Utiliser `linregress()` de `scipy.stats` pour la régression linéaire.
* Interpréter la pente, l’ordonnée à l’origine et le coefficient de détermination R²
* Établir une relation entre deux données
* Interpréter les résultats pour répondre à une question scientifique

---





---

# Leçon : Régression linéaire simple avec `scipy`

## Objectifs

* Calculer une droite de régression (y = a·x + b)
* Extraire la pente, l’ordonnée à l’origine, le R², l’erreur-type et la p-valeur
* Évaluer la qualité de l’ajustement avec le coefficient de détermination

---

## 1. Importation de la fonction

```python
from scipy.stats import linregress
```

---

## 2. Données

On part de deux listes (ou tableaux) de valeurs numériques :

```python
x = [1, 2, 3, 4, 5]       # Variable indépendante
y = [2.1, 4.0, 5.9, 8.2, 10.1]  # Variable dépendante
```

---

## 3. Régression linéaire

### Commande :

```python
resultats = linregress(x, y)
```

La fonction retourne un objet contenant :

| Élément     | Signification                |
| ----------- | ---------------------------- |
| `slope`     | pente (a)                    |
| `intercept` | ordonnée à l’origine (b)     |
| `rvalue`    | coefficient de corrélation   |
| `pvalue`    | test statistique de validité |
| `stderr`    | erreur-type sur la pente     |

### Exemple :

```python
from scipy.stats import linregress

x = [1, 2, 3, 4]
y = [2.0, 4.1, 6.0, 7.9]

res = linregress(x, y)

print("Pente :", res.slope)
print("Ordonnée à l’origine :", res.intercept)
print("r :", res.rvalue)
print("R² :", res.rvalue**2)
print("Erreur-type :", res.stderr)
print("p-valeur :", res.pvalue)
```

---

## 4. Équation de la droite

L’équation ajustée est :

```
y = slope * x + intercept
```

Tu peux l’utiliser pour tracer la droite ou prédire des valeurs.

---

## 5. Évaluer la concordance (qualité de l’ajustement)

### Coefficient de détermination :

```python
R2 = res.rvalue ** 2
```

* R² proche de **1** → très bon ajustement
* R² proche de **0** → pas de relation linéaire

---

## Résumé minimal

| Tâche                  | Syntaxe                              |
| ---------------------- | ------------------------------------ |
| Importer               | `from scipy.stats import linregress` |
| Calculer la régression | `res = linregress(x, y)`             |
| Obtenir la pente       | `res.slope`                          |
| Obtenir l’intercept    | `res.intercept`                      |
| Obtenir R²             | `res.rvalue ** 2`                    |
| Obtenir l’erreur-type  | `res.stderr`                         |
| Obtenir la p-valeur    | `res.pvalue`                         |

---

## Exercice guidé

### Exercice – Ajuster une droite

**Énoncé :**
Pour `x = [0, 1, 2, 3]` et `y = [1, 2.2, 3.9, 6.0]` :

* Calcule la régression linéaire
* Affiche l’équation de la droite (y = ax + b)
* Affiche R²

**Solution :**

```python
from scipy.stats import linregress

x = [0, 1, 2, 3]
y = [1, 2.2, 3.9, 6.0]

res = linregress(x, y)

print(f"Équation : y = {res.slope:.2f}x + {res.intercept:.2f}")
print(f"R² = {res.rvalue**2:.4f}")
```


=======================================
<!--
## 1. Importer la bibliothèque

```python
import pandas as pd
```

---

## 2. Charger un fichier CSV

```python
df = pd.read_csv("solubilite.csv")
```

Ce fichier contient des données expérimentales : pour chaque composé, on indique la **température** et la **quantité dissoute** dans l’eau.

---

## 3. Afficher les premières lignes

```python
print(df.head())
```

---

## 4. Afficher les noms de colonnes

```python
print(df.columns)
```

---

## 5. Afficher toutes les mesures pour un seul composé

Exemple : tout ce qui concerne le **nitrate de potassium (KNO₃)**

```python
filtre = df["Composé"] == "KNO3"
print(df[filtre])
```

---

## 6. Accéder à une colonne (ex. : températures)

```python
print(df["Température"])
```

---

## 7. Moyenne de solubilité pour un composé

```python
filtre = df["Composé"] == "NaCl"
moyenne = df[filtre]["Solubilité"].mean()
print(f"Moyenne de solubilité pour NaCl : {moyenne:.2f} g/100mL")
```

---

## 8. Boucler sur les composés

```python
composes = df["Composé"].unique()
for compose in composes:
    moyenne = df[df["Composé"] == compose]["Solubilité"].mean()
    print(f"{compose} : {moyenne:.2f} g/100mL")
```

---

## 9. Ajouter une colonne calculée

Exemple : ajouter une colonne indiquant si la solubilité est "haute" (> 80) ou "faible"

```python
df["Évaluation"] = df["Solubilité"] > 80
print(df)
```

---

## 1. Importation des bibliothèques

```python
import numpy as np
from scipy import stats
```

---

## 2. Données de solubilité

Supposons qu’on mesure la solubilité (en g/100g d’eau) d’un sel à différentes températures (en °C) :

```python
temperature = np.array([0, 10, 20, 30, 40, 50])
solubilite = np.array([14, 18, 23, 28, 35, 42])
```

---

## 3. Régression linéaire

```python
resultat = stats.linregress(temperature, solubilite)
```

---

## 4. Affichage des résultats

```python
print(f"Pente : {resultat.slope:.2f} g/°C")
print(f"Ordonnée à l’origine : {resultat.intercept:.2f} g à 0°C")
print(f"R² : {resultat.rvalue**2:.4f}")
print(f"Valeur de p : {resultat.pvalue:.4f}")
```

---

## 5. Interprétation scientifique

```python
if resultat.rvalue**2 > 0.9:
    print(f"La température influence fortement la solubilité.")
elif resultat.rvalue**2 > 0.5:
    print(f"La température influence modérément la solubilité.")
else:
    print(f"La solubilité ne semble pas fortement liée à la température.")
```

---

## Exercices pratiques Pandas

### Exercice 1 – Chargement et exploration

1. Charge le fichier `solubilite.csv`.
2. Affiche les premières lignes.
3. Affiche les noms de colonnes.
4. Affiche toutes les températures pour le composé `"NaCl"`.


### Exercice 2 – Moyenne de solubilité

1. Calcule la moyenne de solubilité pour `"KNO3"`.
2. Fais de même pour `"NaCl"`.
3. Compare les deux valeurs avec des f-strings.


### Exercice 3 – Boucle sur les composés

1. Affiche la moyenne de solubilité pour chaque composé du fichier.
2. Indique pour chacun si elle est supérieure à 80 g/100mL.


### Exercice 4 – Ajout d’une colonne

1. Crée une colonne `Tendance` qui vaut `"Haute"` si la solubilité est > 80 et `"Faible"` sinon.
2. Affiche les 10 premières lignes du tableau mis à jour.


## Exercices pratiques Scipy

### 🔹 Exercice 1 – Sulfate de cuivre

1. Températures : `[0, 10, 20, 30, 40, 50]`
2. Solubilité (g/100g eau) : `[23, 27, 32, 37, 44, 51]`
3. Calcule la régression linéaire.
4. Affiche les résultats et une conclusion scientifique.

---

### 🔹 Exercice 2 – Comparaison de deux sels

1. Sel A :

   * Température : `[0, 20, 40, 60]`
   * Solubilité : `[15, 21, 30, 38]`

2. Sel B :

   * Température : `[0, 20, 40, 60]`
   * Solubilité : `[30, 32, 33, 33.5]`

3. Pour chaque sel :

   * Effectue la régression
   * Affiche pente, intercept, R²
   * Déduis quel sel est le plus influencé par la température

---

### 🔹 Exercice 3 – Prévision

1. Utilise les données de l’exemple principal
2. Calcule la solubilité prévue à 60 °C avec la formule :

```python
valeur_predite = resultat.slope * 60 + resultat.intercept
print(f"Solubilité prévue à 60 °C : {valeur_predite:.2f} g/100g d’eau")
```
---

==========================================

\## Régression linéaire simple avec SciPy



\## 1. Importation de la fonction



```python

from scipy.stats import linregress

```



\## 2. Données



On part de deux listes (ou tableaux) de valeurs numériques :



```python

x = \[1, 2, 3, 4, 5]       # Variable indépendante

y = \[2.1, 4.0, 5.9, 8.2, 10.1]  # Variable dépendante

```



\## 3. Régression linéaire



\### Code :



```python

resultats = linregress(x, y)

```



La fonction retourne les informations suivantes :



| Élément     | Signification                |

| ----------- | ---------------------------- |

| `slope`     | pente (a)                    |

| `intercept` | ordonnée à l’origine (b)     |

| `rvalue`    | coefficient de corrélation   |

| `pvalue`    | test statistique de validité |

| `stderr`    | erreur-type sur la pente     |



\### Exemple :



```python

from scipy.stats import linregress



x = \[1, 2, 3, 4]

y = \[2.0, 4.1, 6.0, 7.9]



res = linregress(x, y)



print("Pente :", res.slope)

print("Ordonnée à l’origine :", res.intercept)

print("r :", res.rvalue)

print("R² :", res.rvalue\*\*2)

print("Erreur-type :", res.stderr)

print("p-valeur :", res.pvalue)

```





\## 4. Équation de la droite



L’équation ajustée est :



```

y = slope \* x + intercept

```



On peut l’utiliser pour tracer la droite ou prédire des valeurs.





\## 5. Évaluer la concordance (qualité de l’ajustement)



\### Coefficient de détermination :



```python

R2 = res.rvalue \*\* 2

```



\* R² proche de \*\*1\*\* → très bon ajustement

\* R² proche de \*\*0\*\* → pas de relation linéaire




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


\## Résumé minimal



| Tâche                  | Syntaxe                              |

| ---------------------- | ------------------------------------ |

| Importer               | `from scipy.stats import linregress` |

| Calculer la régression | `res = linregress(x, y)`             |

| Obtenir la pente       | `res.slope`                          |

| Obtenir l’intercept    | `res.intercept`                      |

| Obtenir R²             | `res.rvalue \*\* 2`                    |

| Obtenir l’erreur-type  | `res.stderr`                         |

| Obtenir la p-valeur    | `res.pvalue`                         |





\## Exercice guidé



\### 🔧 Exercice – Ajuster une droite



\*\*Énoncé :\*\*

Pour `x = \[0, 1, 2, 3]` et `y = \[1, 2.2, 3.9, 6.0]` :



\* Calcule la régression linéaire

\* Affiche l’équation de la droite (y = ax + b)

\* Affiche R²



\*\*Solution :\*\*



```python

from scipy.stats import linregress



x = \[0, 1, 2, 3]

y = \[1, 2.2, 3.9, 6.0]



res = linregress(x, y)



print(f"Équation : y = {res.slope:.2f}x + {res.intercept:.2f}")

print(f"R² = {res.rvalue\*\*2:.4f}")

```





---



\# 🧪 Python scientifique – NumPy avec exercices guidés



---



\## 📦 1. Importer NumPy



```python

import numpy as np

```



---



\## 🔢 2. Créer un tableau NumPy



\### 📘 Exemple :



```python

mesures = np.array(\[3.2, 4.1, 2.9, 5.0])

print(mesures)

```



\### 🧪 Exercice 1 :



Crée un tableau nommé `temperatures` contenant les valeurs :

`\[21.1, 19.5, 22.3, 20.7, 23.0]`

et affiche-le.



```python

\# Ton code ici

```



---



\## 🧮 3. Fonctions mathématiques



\### 📘 Exemple :



```python

np.mean(mesures)   # Moyenne

np.std(mesures)    # Écart-type

np.full(4, 0.5)    # \[0.5, 0.5, 0.5, 0.5]

np.linspace(0, 10, 5)  # \[0.  2.5  5.  7.5 10.]

```



\### 🧪 Exercice 2 :



Utilise le tableau `temperatures` pour :



\* Calculer la moyenne

\* Calculer l’écart-type



```python

\# Ton code ici

```



---



\### 🧪 Exercice 3 :



Crée un tableau nommé `barres\_d\_erreur` rempli de `0.5`, de même longueur que `temperatures`.



```python

\# Ton code ici

```



---



\### 🧪 Exercice 4 :



Crée un tableau de 6 valeurs également espacées entre 0 et 100, nommé `x\_positions`.



```python

\# Ton code ici

```



---



\## ➗ 4. Opérations vectorielles



\### 📘 Exemple :



```python

x = np.array(\[1, 2, 3])

y = np.array(\[4, 5, 6])



x + y     # \[5 7 9]

x \* 2     # \[2 4 6]

y / 2     # \[2.  2.5 3. ]

```



\### 🧪 Exercice 5 :



Crée un tableau `decalage = temperatures - 20`.

Que signifie ce tableau ?



```python

\# Ton code ici

```



---



\### 🧪 Exercice 6 :



Multiplie chaque valeur de `temperatures` par 1.8 et ajoute 32 pour obtenir la température en Fahrenheit.



```python

\# Ton code ici

```



---



\### 🧪 Exercice 7 (révision libre) :



Crée deux tableaux NumPy : `a = \[1, 3, 5, 7]` et `b = \[2, 4, 6, 8]`

Fais les opérations suivantes :



\* Addition

\* Soustraction

\* Multiplication par un scalaire



```python

\# Ton code ici

```

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

-->

### Exercices à faire avant le cours

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **troisième et dernier examen** (20%)

1. Lire la description du [Projet final](../semaine12/)
2. Prendre connaissance de la [Grille de correction](../semaine12/grille/)
3. S'approprier des [Notions à savoir pour réussir le projet](../semaine12/competences_reussite/)


