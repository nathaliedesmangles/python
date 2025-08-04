+++
chapter = true
pre = "8."
title = " Dictionnaires et fichier textes (csv)"
weight = 108
draft = false
+++
 

## Objectifs

* Créer un dictionnaire simple pour représenter des données associatives (ex. : atome → masse atomique)
* Manipuler des données dans un dictionnaire (accès, ajout, modification, parcours).
* Lire un fichier csv contenant des données expérimentales
* Explorer les données
* Filtrer les résultats pour donnée ciblée.
* Comparer des valeurs selon une donnée


## Qu’est-ce qu’un dictionnaire?

Un **dictionnaire** est une structure de données qui associe des **clés** à des **valeurs**.
Il permet de stocker des informations organisées, un peu comme un mini-fichier Excel, mais avec des étiquettes personnalisées au lieu d’indices numériques.

**Syntaxe de base** :

```python
mon_dictionnaire = {
    "clé1": valeur1,
    "clé2": valeur2
}
```

## Utilisation fréquente en sciences

Les dictionnaires sont utiles pour :

* Associer des symboles d’éléments à des valeurs (masse molaire, charge, état)
* Regrouper des résultats par échantillon (ex. température par lieu)
* Associer des noms de gènes à leur expression

### Exemple

Un dictionnaire contenant les masses molaires de quelques éléments :

```python
masses_molaires = {
    "H": 1.008,
    "O": 15.999,
    "C": 12.011
}
```

## Accéder à une valeur avec une clé

```python
print(masses_molaires["O"])  # Affiche : 15.999
```

> Si la clé n’existe pas, Python déclenche une erreur `KeyError`.

## Ajouter ou modifier une valeur

### Ajouter

```python
masses_molaires["N"] = 14.007
```

### Modifier

```python
masses_molaires["C"] = 12.01  # Correction
```

## Vérifier si une clé est présente

```python
if "H" in masses_molaires:
    print("L’hydrogène est dans le dictionnaire.")
```

## Parcourir un dictionnaire

### Via les clés

```python
for element in masses_molaires:
    print(element)
```

### Via les valeurs

```python
for valeur in masses_molaires.values():
    print(valeur)
```

* `.values()` permet d’obtenir **uniquement les valeurs** du dictionnaire, sans les clés.
* **Utile quand on veut faire un calcul avec les valeurs**, comme une moyenne ou une somme.

```python
for valeur in densites.values():
    print(valeur)
```


### Via les paires clé-valeur :

```python
for element, masse in masses_molaires.items():
    print(f"{element} → {masse}")
```

* `.items()` permet d’obtenir les couples **clé-valeur** sous forme de paires (appelées aussi tuples en Python).
* Utile quand on veut à la fois le **nom (clé)** et la **valeur associée** pour un affichage ou un traitement.

## Supprimer une entrée

```python
del masses_molaires["H"]
```

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

## Exercices

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_dict_fichiers.ipynb)

[Fichier à utiliser: solubilite.csv](./solubilite.csv)

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

## Atelier

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_dict_fichiers.ipynb)

[Fichier à utiliser: cristallisation.csv](./cristallisation.csv)

## Exercice

On a réalisé des expériences pour mesurer la température de cristallisation de différentes substances dans plusieurs conditions (pression normale, pression élevée, en solution aqueuse, etc.).

Les données sont enregistrées dans le fichier CSV.

Contenu :

```csv
substance,condition,temp_cristallisation
NaCl,pression_normale,801
NaCl,en_solution,800
H2O,pression_normale,0
H2O,pression_elevee,-1
Fe,pression_normale,1538
Fe,en_solution,1530
```

### Instructions

1. **Lire le fichier CSV** `cristallisation.csv` et stocker les données sous forme de dictionnaire ayant la structure suivante :

```python
{
    "NaCl": {"pression_normale": 801, "en_solution": 800},
    "H2O": {"pression_normale": 0, "pression_elevee": -1},
    "Fe": {"pression_normale": 1538, "en_solution": 1530}
}
```

2. **Afficher** les températures de cristallisation pour chaque substance dans chaque condition avec une phrase comme :

```text
NaCl cristallise à 801°C sous pression normale.
NaCl cristallise à 800°C en solution.
...
```

3. **Ajouter** une nouvelle mesure : supposons qu’on a obtenu une température de cristallisation de `-5°C` pour `H2O` dans une nouvelle condition `en_solution`. Ajoutez cette donnée au dictionnaire.

4. **Vérifiez** si la substance `"Cu"` est présente dans le dictionnaire. Si elle ne l’est pas, affichez : `"Cu n'est pas présent dans les données."`

5. **Filtrer** et afficher toutes les substances ayant une température de cristallisation inférieure à `100°C` dans au moins une condition.

6. **Comparer** les températures de cristallisation d’une même substance selon les conditions expérimentales et afficher la différence maximale observée pour chaque substance, par exemple :

```text
Pour H2O, l’écart maximal est de 5°C entre deux conditions.
```

---

## À faire avant le prochain cours

> Semaine prochaine est une révision

1. Lire la prochaine leçon : [9. Révision](../semaine9/)
2. Faire les exercices de la [prochaine leçon :](../semaine9/#exercices)
