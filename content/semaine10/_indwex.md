+++
chapter = true
pre = "<b>10.</b>"
title = " Traitement de fichiers textes (CSV)"
weight = 110
draft = false
+++


## Objectifs

* Lire un fichier csv contenant des données expérimentales
* Explorer les données
* Filtrer les résultats pour donnée ciblée.
* Comparer des valeurs selon une donnée

---


## Traitement de fichiers textes (.csv)

Les fichiers `.csv` (*Comma-Separated Values*) permettent de stocker des tableaux de données.

**Exemple de fichier `mesures.csv` :**

```
temps,temperature
0,22.5
5,24.1
10,26.3
15,28.0
```

### Lire et écrire des fichiers de données (.csv)

**Écrire (créer)** :

```python
with open("donnees.csv", "w") as f:
    f.write("Nom,Âge\n")
    f.write("Alice,20\n")
    f.write("Bob,22\n")
```

**Lire un fichier `.csv`**

```python
# Lecture du fichier CSV
import csv

with open("donnees.csv", "r") as f:
    contenu = f.read()
    print(contenu)
```

#### Pour des données **numériques**, on peut utiliser `numpy.savetxt()` et `numpy.loadtxt()`

```python
import numpy as np

# Sauvegarder un tableau
tableau = np.array([[1, 2], [3, 4]])
np.savetxt("tableau.csv", tableau, delimiter=",")

# Charger un tableau
donnees = np.loadtxt("tableau.csv", delimiter=",")
print(donnees)
```

---

## Traitement de fichiers .csv avec Pandas

### Importer la bibliothèque

```python
import pandas as pd
```

## Charger un fichier CSV

```python
df = pd.read_csv("solubilite.csv")
```

## Afficher les 10 premières lignes

```python
print(df.head())
```

## Afficher les noms des colonnes

```python
print(df.columns)
```

## Afficher toutes les mesures pour un seul composé

Exemple : tout ce qui concerne le **nitrate de potassium (KNO₃)**

```python
filtre = df["Composé"] == "KNO3"
print(df[filtre])
```

## Accéder à une colonne (ex. : Températures)

```python
print(df["Température"])
```

## Moyenne de solubilité pour un composé

```python
filtre = df["Composé"] == "NaCl"
moyenne = df[filtre]["Solubilité"].mean()
print(f"Moyenne de solubilité pour NaCl : {moyenne:.2f} g/100mL")
```

## Boucler sur les composés

```python
composes = df["Composé"].unique()
for compose in composes:
    moyenne = df[df["Composé"] == compose]["Solubilité"].mean()
    print(f"{compose} : {moyenne:.2f} g/100mL")
```

## Ajouter une colonne calculée

Exemple : ajouter une colonne indiquant si la solubilité est "haute" (> 80) ou "faible"

```python
df["Évaluation"] = df["Solubilité"] > 80
print(df)
```

---
{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* **Dictionnaires** :
```python
mon_dict = {"a": 5, "b": 10}
mon_dict["a"] 				# accéder à une valeur
for clé in mon_dict: 			# boucle sur les clés
mon_dict.get("clé", valeur_par_défaut) 	# accès sécurisé
mon_dict.keys(), .values() 		# itérations
```

* **Fichiers .csv  (sans Pandas)**: `open()`, `write()`, `read()`, `loadtxt()`, `savetxt()` 

* **Fichiers .csv  (avec Pandas)**:
```python
import pandas as pd
pd.read_csv("fichier.csv") 	# lecture de fichier
df.head() 			# aperçu des premières données
df["colonne"] 			# accès à une colonne
df.loc[3], df.iloc[3] 		# accès à une ligne
df.mean(), df["col"].std() 	# stats
df.dropna() 			# suppression des lignes incomplètes
df[df["col"] > seuil] 		# filtrage conditionnel
```
{{% /notice %}}

---


## Exercices à faire avant le cours

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_dict_fichiers.ipynb)


### Exercice 1 - Densités

Crée un dictionnaire `densites` qui contient la densité (en g/mL) de l’eau, de l’éthanol et du mercure :

```python
densites = {
    "eau": ...,
    "éthanol": ...,
    "mercure": ...
}
```

Puis :

1. Affiche la densité du mercure.
2. Ajoute la densité de l’huile (0.91 g/mL).
3. Affiche toutes les substances et leur densité.


### Exercice 2 – Chargement et exploration

[Fichier de données: solubilite.csv](./solubilite.csv)

1. Charge le fichier `solubilite.csv`.
2. Affiche les premières lignes.
3. Affiche les noms de colonnes.
4. Affiche toutes les températures pour le composé `"NaCl"`.


### Exercice 3 – Moyenne de solubilité

1. Calcule la moyenne de solubilité pour `"KNO3"`.
2. Fais de même pour `"NaCl"`.
3. Compare les deux valeurs avec des f-strings.


### Exercice 4 – Boucle sur les composés

1. Affiche la moyenne de solubilité pour chaque composé du fichier.
2. Indique pour chacun si elle est supérieure à 80 g/100mL.


### Exercice 5 – Ajout d’une colonne

1. Crée une colonne `Tendance` qui vaut `"Haute"` si la solubilité est > 80 et `"Faible"` sinon.
2. Affiche les 10 premières lignes du tableau mis à jour.


---

## À faire avant le prochain cours

1. Lire la matière sur [Les graphiques avancés et la regression linéaire](../semaine11/)
2. Faire les [exercices se trouvant à la fin de la leçon 11](../semaine11/#exercices-à-faire-avant-le-cours)


