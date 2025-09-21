+++
chapter = true
pre = "8."
title = " Dictionnaires et fichiers texte (csv)"
weight = 108
draft = true
+++
 

## Objectifs

* Créer un dictionnaire simple pour représenter des données associatives (ex. : atome → masse atomique)
* Manipuler des données dans un dictionnaire (accès, ajout, modification, parcours).
* Lire un fichier csv contenant des données expérimentales
* Explorer les données.
* Filtrer les résultats pour une donnée ciblée.
* Comparer des valeurs selon une donnée.

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

---

# Exercices

## Fichiers de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier `.ipynb`:
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_dict_fichiers.ipynb)
2. Cliquez sur le lien pour télécharger le fichier de données (`.csv`): [solubilite.csv](./solubilite.csv)
   * Ce fichier de données sera utilisé dans les exercices #2 à #5.
3. Enregistrez le fichier dans votre dossier **exercices** de la semaine en cours.
4. Ouvrez **Visual Studio Code**.
5. Dans VS Code, recherchez et ouvrez le fichier `exercices_dict_fichiers.ipynb`
6. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
7. Vous pouvez commencer à faire les exercices.


## Exercice 1 – Densités

On veut représenter la densité (en g/mL) de différentes substances à l’aide d’un **dictionnaire**.

1. **Créez** un dictionnaire nommé `densites` qui contient les valeurs suivantes :

   * eau : 1.0
   * éthanol : 0.79
   * mercure : 13.6

   Exemple de structure attendue :

   ```python
   densites = {
       "eau": 1.0,
       "éthanol": 0.79,
       "mercure": 13.6
   }
   ```

2. **Affichez** uniquement la densité du mercure. *(Indice : utilise la clé `"mercure"` dans le dictionnaire.)*
3. **Ajoutez** une nouvelle entrée au dictionnaire pour l’huile, avec une densité de `0.91`. *(Indice : utilise la clé `"huile"` dans le dictionnaire.)*
4. **Affichez** ensuite toutes les substances et leur densité à l’aide d’une boucle `for` et de `densites.items()`.

**Résultats attendus** :
```
Densité du mercure : 13.6 g/mL
eau : 1.0 g/mL
éthanol : 0.789 g/mL
mercure : 13.6 g/mL
huile : 0.91 g/mL
```

{{% notice style="orange" title="Rappel" %}}
* Si l'importation de `pandas` est faite qu'une seule fois, au début de l'exercice #2, utilisez **Exécuter tout** pour éviter l'erreur *`NameError: name 'pd' is not defined`*.
{{% /notice %}}


## Exercice 2 – Chargement et exploration de données

1. **Charger le fichier CSV**
   * Utilisez la fonction `pd.read_csv("solubilite.csv")` pour importer les données dans un DataFrame nommé `df`.

2. **Explorer rapidement les données**
   * Affichez les **5 premières lignes** du DataFrame avec la méthode `.head()`.
   * Affichez les **10 premières lignes** du DataFrame avec la méthode `.head(10)`.

3. **Identifier la structure du tableau**
   * Affichez la liste des **noms de colonnes** avec l’attribut `.columns`.

4. **Filtrer les données pour un composé précis**
   * Sélectionnez toutes les **températures** correspondant au composé `"NaCl"`.
   * **Indice** : commence par isoler les lignes où la colonne `"Composé"` vaut `"NaCl"`, puis affiche uniquement la colonne `"Température"`.


**Résultats attendus** :
```
2. Exploration - 5 et 10 premières lignes
Composé  Température  Solubilité
0    NaCl            0        35.7
1    NaCl           20        36.0
2    NaCl           40        36.5
3    NaCl           60        37.0
4    NaCl           80        37.2
  Composé  Température  Solubilité
0    NaCl            0        35.7
1    NaCl           20        36.0
2    NaCl           40        36.5
3    NaCl           60        37.0
4    NaCl           80        37.2
5    KNO3            0        13.3
6    KNO3           20        31.6
7    KNO3           40        63.9
8    KNO3           60        85.5
9    KNO3           80       110.0

3. Colonnes
Index(['Composé', 'Température', 'Solubilité'], dtype='object')

4. Températures de NaCl
Températures pour NaCl :
0     0
1    20
2    40
3    60
4    80
Name: Température, dtype: int64
```


## Exercice 3 – Moyenne de solubilité

On dispose de données expérimentales de solubilité (en g/100 mL d’eau) pour différents sels à différentes températures.

1. Sélectionne uniquement les valeurs de solubilité correspondant au sel **`"KNO3"`**. *Utilise df[df["Compose"] == "KNO3"*
2. Calcule la moyenne de ces valeurs à l’aide de `mean()`. Utilise le résultat de la question `1.` avec un filtre sur la colonne "Solubilité".
3. Répète la même opération pour le sel **`"NaCl"`**.
4. Affiche un message contenant les deux moyennes.

**Résultats attendus** :
```
Moyenne de solubilité - KNO3 : 60.86 g/100 mL
Moyenne de solubilité - NaCl : 36.48 g/100 mL
```


## Exercice 4 – Boucle sur les composés

1. Calculez la **moyenne de solubilité** de chaque composé à partir des valeurs disponibles.
   * Utilisez `.unique()` pour pouvoir cibler tous les composé présents.
   ***Astuce** : pense à utiliser une boucle pour traiter chaque composé du fichier.*
2. Affichez le nom du composé suivi de sa moyenne de solubilité. Utilisez `.mean()`.
3. Indiquez également si cette moyenne est **supérieure à 80 g/100 mL** ou non.
   *Utilisez `if/else` pour traiter le cas.

**Résultats attendus** :
```
NaCl : 36.48 g/100 mL (inférieure ou égale à 80 g/100 mL)
KNO3 : 60.86 g/100 mL (inférieure ou égale à 80 g/100 mL)
CaCl2 : 84.50 g/100 mL (supérieure à 80 g/100 mL)
C12H22O11 : 253.64 g/100 mL (supérieure à 80 g/100 mL)
```

## Exercice 5 – Ajout d’une colonne

1. Crée une colonne `Tendance` qui vaut `"Haute"` si la solubilité est > 80 et `"Faible"` sinon.
   * Utilise `np.where(condition, valeur_si_vrai, valauer_si_faux)`. 
2. Affiche les 10 premières lignes du tableau mis à jour avec `.head(10)`.

**Résultats attendus** :
```
Composé  Température  Solubilité Tendance
0    NaCl            0        35.7   Faible
1    NaCl           20        36.0   Faible
2    NaCl           40        36.5   Faible
3    NaCl           60        37.0   Faible
4    NaCl           80        37.2   Faible
5    KNO3            0        13.3   Faible
6    KNO3           20        31.6   Faible
7    KNO3           40        63.9   Faible
8    KNO3           60        85.5    Haute
9    KNO3           80       110.0    Haute
```
3. Refaites l'exercice, mais en utilisant `df.loc` au lieu de `np.where()` et assurez vous que les deux résultats sont les mêmes.

---

# Cours

## Qu’est-ce qu’un dictionnaire?

Un **dictionnaire** est une structure de données qui associe des **clés** à des **valeurs**.
Il permet de stocker des informations organisées, un peu comme un mini-fichier Excel, mais avec des étiquettes personnalisées au lieu d’indices numériques.

Les dictionnaires sont utiles pour :

* Associer des symboles d’éléments à des valeurs (masse molaire, charge, état).
* Regrouper des résultats par échantillon (ex. température par lieu).
* Associer des noms de gènes à leur expression.
* etc.

**Syntaxe de base** :

```python
mon_dictionnaire = {
    "clé1": valeur1,
    "clé2": valeur2
}
```

{{% notice style="accent" title="Attention à la casse et aux accents dans les clés" %}}
* Lorsque vous utilisez les **clés d’un dictionnaire**, il faut respecter exactement l’écriture définie :
   * La **casse** (majuscules/minuscules) et les **lettres accentuées** comptent :
     * `"Nom"` et `"nom"` sont considérés comme **deux clés différentes** dans un dictionnaire.
     * `"Prénom"` et `"Prenom"` ne désignent **pas la même clés** dans un dictionnaire.
* Si vous obtenez une erreur du type `KeyError`, vérifiez l’orthographe, la casse et les accents du nom utilisé.
{{% /notice %}}


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
```python
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[2], line 7
      1 masses_molaires = {
      2     "H": 1.008,
      3     "O": 15.999,
      4     "C": 12.011
      5 }
----> 7 print(masses_molaires["Fe"])

KeyError: 'Fe'
```

## Ajouter ou modifier une valeur

### Ajouter une donnée

**Exemple**: L'azote
```python
masses_molaires["N"] = 14.007
```

### Modifier une valeur

**Exemple**: Le carbone
```python
masses_molaires["C"] = 12.01  # Correction
```

## Vérifier si une clé est présente avec *if* et *in*

```python
if "H" in masses_molaires:
    print("L’hydrogène est dans le dictionnaire.")
```

## Parcourir un dictionnaire à l'aide de *for*

### Via les clés

**Par défaut**, la boucle `for` parcours les clés (**Elles sont l'équivalent des indices dans les tableaux**)

```python
for element in masses_molaires:
    print(element)
```
**Résultat**:
```
H
O
C
N
```

### Via les valeurs avec .values()

* Pour parcourir les valeurs il faut le préciser à l'aide de `dictionnaire.values()`.

```python
for valeur in masses_molaires.values():
    print(valeur)
```

**Résultat** :
```
1.008
15.999
12.01
14.007
```

* `.values()` permet d’obtenir **uniquement les valeurs** du dictionnaire, sans les clés.
* **Utile quand on veut faire un calcul avec les valeurs**, comme une moyenne ou une somme.


### Via les paires clé-valeur :

* Pour avoir **les deux** (la clé **ET** la valeur associée) il faut préciser **deux variables** dans la boucle `for`.

**Exemple** (variables `element` et `masse`) :
```python
for element, masse in masses_molaires.items():
    print(f"{element} → {masse}")
```

**Résultat** :
```
H → 1.008
O → 15.999
C → 12.01
N → 14.007
```

* `.items()` permet d’obtenir les couples **clé-valeur** sous forme de paires (appelées aussi tuples en Python).
* Utile quand on veut à la fois le **nom (clé)** et la **valeur associée** pour un affichage ou un traitement.

## Supprimer une entrée du dictionnaire avec del

```python
del masses_molaires["H"]
```

**Résultat si on affiche le dictionnaire après la suppression**
```
{'O': 15.999, 'C': 12.01, 'N': 14.007}
```
---

## Traitement de fichiers texte (.csv) avec Pandas

Les fichiers `.csv` (*Comma-Separated Values*) permettent de stocker des tableaux de données.

**Exemple de fichier `mesures.csv` :**

```
temps,temperature
0,22.5
5,24.1
10,26.3
15,28.0
```
<!--
### Lire et écrire des fichiers de données (.csv)

**Écrire (créer)** :

Voici comment procéder:

* `with open("donnees.csv", "w") as f` : On ouvre (ou crée) un fichier nommé `donnees.csv` en mode écriture (`"w"`), prêt à y écrire du texte.
* `f.write("Nom,Âge\n")` : On écrit l'en-tête (les noms de colonnes) dans le fichier.
* `f.write("Alice,20\n")` : On écrit la première ligne de données.
* `f.write("Bob,22\n")` : On écrit la deuxième ligne de données.

Le code complet:
```python
with open("donnees.csv", "w") as f:
    f.write("Nom,Âge\n")
    f.write("Alice,20\n")
    f.write("Bob,22\n")
```

**Lire un fichier `.csv`**

Voici comment procéder :

* `import csv` : On importe le module `csv`, utile pour lire des fichiers CSV.
* `with open("donnees.csv", "r") as f` : On ouvre le fichier `donnees.csv` en mode lecture (`"r"`).
* `contenu = f.read()` : On lit tout le contenu du fichier et on le met dans la variable `contenu`.
* `print(contenu)` : On affiche le contenu du fichier à l’écran.


```python
# Lecture du fichier CSV
import csv

with open("donnees.csv", "r") as f:
    contenu = f.read()
    print(contenu)
```

**Pour des données **numériques**, on peut utiliser `numpy.savetxt()` et `numpy.loadtxt()`**

```python
import numpy as np

# Sauvegarder un tableau
tableau = np.array([[1, 2], [3, 4]])
np.savetxt("tableau.csv", tableau, delimiter=",")

# Charger un tableau
donnees = np.loadtxt("tableau.csv", delimiter=",")
print(donnees)
```
-->


### Importer la bibliothèque

```python
import pandas as pd
```

* On utilisera l'alias `pd` pour accéder aux fonctionnalités de Pandas.

## Charger un fichier CSV

```python
df = pd.read_csv("solubilite.csv")
```

* Le contenu du fichier est stocké dans une variable de type `DataFrame` représentée par `df`.


## Afficher les 5 premières lignes d'un dataframe

**NB** : `df.head()` affichera **par défaut** les **5** premières lignes du dataframe. 
* Pour afficher un autre nombre de lignes, il faut l'indiquer dans les `()`.

```python
print(df.head())	# 5 premières lignes
print(df.head(10))	# 10 premières lignes
```

### Exemple d'affichage pour *df.head()*

```
   Sel          Température               Solubilité
0  NaCl                  20                     35.7
1  NaCl                  40                     36.5
2  NaCl                  60                     37.3
3  KNO3                  20                     31.6
4  KNO3                  40                     63.9
```


## Afficher les noms des colonnes

```python
print(df.columns)
```

**Résultat** :
```
Index(['Sel', 'Température', 'Solubilité'], dtype='object')
```

{{% notice style="accent" title="Attention à la casse et aux accents dans les noms de colonnes" %}}
* Lorsque vous utilisez les **noms de colonnes dans un dataframe**, il faut respecter exactement l’écriture définie :
   * La **casse** (majuscules/minuscules) et les **lettres accentuées** comptent :
     * `"Sel"` et `"sel"` sont considérés comme **deux colonnes différentes** dans un dataframe.
     * `"Solubilité"` et `"Solubilite"` ne désignent **pas la même colonne** dans un dataframe.
* Si vous obtenez une erreur du type `KeyError`, vérifiez l’orthographe, la casse et les accents du nom utilisé.
{{% /notice %}}

## Afficher toutes les mesures pour un seul composé

**Exemple** : tout ce qui concerne le **nitrate de potassium (KNO₃)**

```python
filtre = df["Sel"] == "KNO3"
print(df[filtre])
```
* Le filtre sélectionne les **lignes où le composé est exactement "KNO3"**.

### Exemple d'affichage

```
      Sel       Température               Solubilité
3    KNO3                20                     31.6
4    KNO3                40                     63.9
5    KNO3                60                     85.5
```

## Accéder à une colonne (ex. : Température)

* Afficher toutes les valeurs de la colonne **Température** du tableau de données.

```python
print(df["Température"])
```
**Résultat** :
```
0      0
1     20
2     40
3     60
4     80
5      0
6     20
7     40
8     60
9     80
10     0
11    20
12    40
13    60
14    80
15     0
16    20
17    40
18    60
19    80
Name: Température, dtype: int64
```


## Moyenne de solubilité pour un composé

```python
filtre = df["Composé"] == "NaCl"
moyenne = df[filtre]["Solubilité"].mean()
print(f"Moyenne de solubilité pour NaCl : {moyenne:.2f} g/100mL")
```

**Explication** : 

* `filtre = df[""] Composé == "NaCl"` : On crée un filtre pour ne garder que les lignes où le sel est **NaCl**.
* `moyenne = df[filtre]["Solubilité"].mean()` : On calcule la **moyenne** des valeurs de solubilité pour **NaCl** seulement.

**Résultat** :
```
Moyenne de solubilité pour NaCl : 36.48 g/100mL
```


## Boucler sur les composés

```python
composes = df["Composé"].unique()
for compose in composes:
    moyenne = df[df["Composé"] == compose]["Solubilité"].mean()
    print(f"{compose} : {moyenne:.2f} g/100mL")
```

**Explication** :

* `composes = df["Composé"].unique()` : On récupère la liste des différents sels présents dans la colonne **Composé**.
* `for compose in composes:` : Pour chaque composé dans cette liste, on calcule la moyenne de la solubilité.

**Résultat** :
```
NaCl : 36.48 g/100mL
KNO3 : 60.86 g/100mL
CaCl2 : 84.50 g/100mL
C12H22O11 : 253.64 g/100mL
```

## Ajouter une colonne calculée

**Exemple** : ajouter une colonne indiquant si la solubilité est **supérieure à 80 "True" ou non "False"**.

La colonne **Évaluation** aura la valeur `True` si la solubilité est supérieure à 80, `False` sinon.

```python
df["Évaluation"] = df["Solubilité"] > 80
print(df)
```

**Résultat** :
```
Composé  Température  Solubilité  Évaluation
0        NaCl            0        35.7       False
1        NaCl           20        36.0       False
2        NaCl           40        36.5       False
3        NaCl           60        37.0       False
4        NaCl           80        37.2       False
5        KNO3            0        13.3       False
6        KNO3           20        31.6       False
7        KNO3           40        63.9       False
8        KNO3           60        85.5        True
9        KNO3           80       110.0        True
10      CaCl2            0        59.5       False
11      CaCl2           20        74.5       False
12      CaCl2           40        83.5        True
13      CaCl2           60        95.0        True
14      CaCl2           80       110.0        True
15  C12H22O11            0       179.2        True
16  C12H22O11           20       204.0        True
17  C12H22O11           40       238.0        True
18  C12H22O11           60       287.0        True
19  C12H22O11           80       360.0        True
```

---

# Atelier

1. Téléchargez le fichier de départ (`.ipynb`): [Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_dict_fichiers.ipynb)
2. Téléchargez le fichier de données (`.csv`): [cristallisation.csv](./cristallisation.csv)
3. Déplacez-le dans votre dossier prévu pour **l'atelier de la semaine 8**.
4. Ouvrez votre dossier de travail `programmation-sciences` **à partir de Visual Studio Code**.
   * Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb).

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
