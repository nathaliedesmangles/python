+++
chapter = true
pre = "<b>10.</b>"
title = " Graphiques SciPy et traitement de fichiers CSV avec Pandas"
weight = 110
draft = true
+++





\* Importer la bibliothèque NumPy

&nbsp;	\* Utiliser les fonctions de NumPy pour créer des tableaux (1D, 2D)

&nbsp;	\* Utiliser les fonctions mathématiques de NumPy pour obtenir des statistiques sur les données

\* Ajouter une droite sur un graphique (régression linéaire)

&nbsp;	\* Calculer une droite de régression (y = a·x + b)

&nbsp;	\* Extraire la pente, l’ordonnée à l’origine, le R², l’erreur-type et la p-valeur

&nbsp;	\* Évaluer la qualité de l’ajustement avec le coefficient de détermination



---



\## Importer la bibliothèque



Avant d’utiliser \*\*\*NumPy\*\*\*, il faut l’importer au début de votre script ou notebook :



```python

import numpy as np

```



---



\## 1. Créer un tableau NumPy (`np.array()`)



Un \*\*tableau NumPy\*\* est une structure efficace pour manipuler des séries de données numériques (ex : mesures, positions, températures…).



```python

\# Créer un tableau à partir d’une liste

mesures = np.array(\[3.2, 4.1, 2.9, 5.0])

print(mesures)

```



Résultat :



```

\[3.2 4.1 2.9 5. ]

```





\## 2. Fonctions mathématiques statistiques utiles



\### Somme



```python

np.sum(mesures)  # Total des valeurs

```



\### Moyenne



```python

np.mean(mesures)  # Moyenne des valeurs

```



\### Écart-type (standard deviation)



```python

np.std(mesures)  # Mesure de la dispersion des données

```



\### Tableau rempli d’une même valeur



```python

np.full(4, 0.5)  # Crée un tableau \[0.5, 0.5, 0.5, 0.5]

```



```python

np.zeros((2, 3))  # Crée un tableau de 2 lignes et 3 colonnes rempli de 0

```



```python

np.ones((3, 2))  # Crée un tableau de 3 lignes et 2 colonnes rempli de 1

```





\### Valeurs espacées régulièrement (utile pour les graphiques)



```python

np.linspace(0, 10, 5)  # Crée un tableau de 5 valeurs (saut de 5) : \[ 0.  2.5  5.  7.5 10. ]

```



```python

np.arange(0, 10, 2)  # Crée un tableau avec les nombres pairs de 0 à 10 exclu : \[0 2 4 6 8] 

```





\## 3. Opérations vectorielles (rapides et simples)



L’intérêt principal de NumPy : on peut faire des \*\*opérations sur tout un tableau en une seule ligne\*\*.



```python

x = np.array(\[1, 2, 3])

y = np.array(\[4, 5, 6])

```



\### Addition élément par élément :



```python

x + y    # \[5 7 9]

```



\### Soustraction :



```python

y - x    # \[3 3 3]

```



\### Multiplication par un scalaire :



```python

x \* 10   # \[10 20 30]

```



\### Division :



```python

y / 2    # \[2.  2.5 3. ]

```





\## Exemple complet :



```python

hauteurs = np.array(\[165, 172, 180, 158])

moy = np.mean(hauteurs)

ecart = np.std(hauteurs)

print("Moyenne :", moy)

print("Écart-type :", ecart)



\# Centrer les données

hauteurs\_centrees = hauteurs - moy

print("Hauteurs centrées :", hauteurs\_centrees)

```

\# \*\*Pause 5 minutes\*\*



!\[Pause](../pause.jpg?width=50vw)



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



