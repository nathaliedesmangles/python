+++
chapter = true
pre = "9."
title = " Manipulation de données dans un fichier (avec Pandas)"
weight = 109
draft = false
+++

## Objectif

1. Lire un fichier CSV contenant des données expérimentales.
2. Nettoyer et sauvegarder un nouveau fichier corrigé.
3. Manipuler un **DataFrame** Pandas (sélection, ajout, statistiques).
4. Transformer les colonnes en **tableaux NumPy** pour des calculs scientifiques.
5. Visualiser les données sous forme de **nuage de points**.

## Fichier .ipynb pour la démo en classe

[Fichier utilisé pour la démonstration](https://python-a25.netlify.app/blocnotes/demo_pandas.ipynb)

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

---

# Exercices

## Fichiers de départ à utiliser

[**Bloc-notes de départ - Pandas**](https://python-a25.netlify.app/blocnotes/exercices_fichiers_pd.ipynb)  

{{% notice style="accent" title="Exercices #1 et #2" %}}
Les exercices #1 et #2 utilisaient NumPy pour la lecture/écriture de fichiers et ils ont été retirés de la leçon.
{{% /notice %}}

### Exercice 3 (Pandas)

**Objectif :** lire un fichier CSV dans un DataFrame et explorer les données.

1. **Lire le fichier CSV `etudiants.csv`**
   * Utilisez `pd.read_csv("etudiants.csv")` pour créer un DataFrame `df_etudiants`.

2. **Afficher un aperçu des données**
   * `df_etudiants.head(3)` montre les 3 premières lignes. Utile pour vérifier que le fichier a été lu correctement.

3. **Résumé statistique**
   * `df_etudiants["Note"].describe()` fournit la moyenne, l’écart-type, le minimum, le maximum, etc. Permet de comprendre rapidement la distribution des notes.


**Résultats** :  
   **Pour df_etudiants.head(3)**
   ```
        Nom    Âge    Note
   0   Aurélie  20    85
   1   Claude   21    67
   2   Charlie  19    45
   ```
   **Pour df_etudiants["Note"].describe()**
   ```
   count    10.000000
   mean     66.200000
   std      15.061356
   min      45.000000
   25%      55.750000
   50%      65.500000
   75%      75.000000
   max      91.000000
   Name: Note, dtype: float64
   ```


### Exercice 4 (Pandas)

**Objectif :** créer une nouvelle colonne conditionnelle et sauvegarder le résultat.

1. **Dans le DataFrame **df_etudiants**, ajouter la colonne `Mention`**

   * Ajoutez une colonne **Mention** au DataFrame en fonction de la note, avec les conditions : 

     ```
     * note >= 70 → "Bien" 
     * note >= 50 → "Passable" 
     * note < 50 → "Échec"
     ```

   * Selon l’intervalle, attribuez la mention : "Bien", "Passable", "Échec".  
		* Utilisez 2 `np.where()` pour appliquer les conditions à tout le DataFrame.<br>[Rappel sur np.where()](http://localhost:1313/semaine8/#3-filtre-avec-npwhere)
		* Ex: `df_etudiants["Mention"] = np.where(Si_note_>=70, "Bien", np.where(si_note_>=50, "Passable", "Échec"))`
2. **Enregistrer le DataFrame**
   * Utilisez `df_etudiants.to_csv("etudiants_mentions.csv", index=False)` pour sauvegarder.
   * Vérifiez le fichier créé pour voir la nouvelle colonne.

**Résultats** :
```
Données originales
       Nom  Âge  Note
0  Aurélie   20    85
1   Claude   21    67
2  Charlie   19    45
3    David   22    72
4     Emma   20    58
5    Fiona   21    49
6   George   23    91
7   Hannah   20    76
8      Ian   22    64
9    Julia   19    55

Données avec mentions
       Nom  Âge  Note   Mention
0  Aurélie   20    85      Bien
1   Claude   21    67  Passable
2  Charlie   19    45     Échec
3    David   22    72      Bien
4     Emma   20    58  Passable
5    Fiona   21    49     Échec
6   George   23    91      Bien
7   Hannah   20    76      Bien
8      Ian   22    64  Passable
9    Julia   19    55  Passable
```

### Exercice 5 (Pandas)

**Objectif :** lire un fichier texte tabulé et le réexporter en conservant la structure.

1. **Lire le fichier `experience.txt`**
   * Utilisez `pd.read_csv("experience.txt", sep="\t")` pour indiquer que les colonnes sont séparées par des tabulations (`\t`).

2. **Vérifier les données**
   * Utilisez `df.head()` pour visualiser quelques lignes et vérifier que toutes les colonnes sont correctement lues.

3. **Réexporter le fichier**
   * Utilisez `df.to_csv("experience_export.txt", sep="\t", index=False)` pour sauvegarder en conservant les tabulations.
   * Vérifiez le fichier exporté pour vous assurer que la structure est respectée.

**Résultats** :
```
Fichier 'experience_export.txt' enregistré avec tabulations.
   Température  Pression  Volume
0         25.0      1.01    10.5
1         30.0      1.05    11.0
2         35.0      1.10    11.5
3         40.0      1.15    12.0
4         45.0      1.20    12.5
5         50.0      1.25    13.0
6         55.0      1.30    13.5
7         60.0      1.35    14.0
8         65.0      1.40    14.5
9         70.0      1.45    15.0
```


### Exercice 6 (Pandas)

Lors d’une expérience de chimie, on a mesuré la **solubilité d’un sel (en g/100 mL d’eau)** à différentes températures.
Certaines mesures ont été perdues pendant l’enregistrement, et apparaissent comme **valeurs manquantes** (`NaN`) dans le fichier.

Les données suivantes ont été enregistrées dans le fichier `solubilite_sel.csv` :

```csv
temperature,solubilite
0,32.0
10,34.1
20,NaN
30,37.5
40,38.8
50,NaN
60,42.0
```

1. **Lire** le fichier `solubilite_sel.csv` à l’aide de pandas et afficher son contenu.
2. **Vérifier la présence** de valeurs manquantes.  Utilisez `df.isna()` ou `df.isnull()` pour identifier les cellules vides.
3. **Compter** le nombre total de valeurs manquantes dans le tableau (`df.isna().sum().sum()`).
4. **Remplacer** les valeurs manquantes par la moyenne des autres valeurs mesurées. Utilisez  `df['colonne'].fillna(df['colonne'].mean())`  
5. **Afficher le nouveau tableau** et vérifier qu’il ne contient plus de valeurs manquantes.
6. **Tracer un graphique** (`plot()`) de la **solubilité** en fonction de la **température** pour visualiser le résultat.

**Résultats** :
```
Valeurs manquantes :
   temperature  solubilite
0        False       False
1        False       False
2        False        True
3        False       False
4        False       False
5        False        True
6        False       False
Nombre total de NaN : 2

Données après traitement :
   temperature  solubilite
0            0       32.00
1           10       34.10
2           20       36.88
3           30       37.50
4           40       38.80
5           50       36.88
6           60       42.00
```

![Solubilité vs température](./solubilite_temp.png?width=35vw)

### Exercice 7 (Pandas)

Cet exercice vous fait naviguer dans un tableau avant d’en extraire ou comparer des valeurs.

1. Lire le fichier `plantes.csv` contenant les colonnes `Nom`, `Hauteur_cm`, `Teneur_eau_%`.
2. Afficher la 5e ligne complète.
3. Afficher uniquement la colonne de la hauteur.
4. Afficher les 3 premières plantes et leurs deux premières colonnes.

**Résultats**:
```
5e ligne complète :
Nom             Bambou
Hauteur_cm         180
Teneur_eau_%        75
Name: 4, dtype: object

Colonne Hauteur_cm :
0     45
1     30
2     12
3     28
4    180
5     25
6     35
Name: Hauteur_cm, dtype: int64

3 premières plantes, 2 premières colonnes :
        Nom  Hauteur_cm
0   Fougère          45
1  Orchidée          30
2    Cactus          12
```

### Exercice 8 (Pandas et NumPy)

Cet exercice prépare à faire des analyses et régressions à partir de données réelles.

1. Avec **Pandas**, lire le fichier `solutions.csv` contenant des colonnes `Temp_C` et `Concentration_mol_L`.
2. Convertir ces deux colonnes en tableaux NumPy avec `.to_numpy()`.
3. Calculer la moyenne et l’écart-type de la concentration avec les fonctions appropriées de **NumPy** (pas Pandas).
4. Créer un graphique `Temp_C` vs `Concentration_mol_L` avec `plt.plot()`.

**Résultats**:
```
 Concentration moyenne : 0.1742857142857143
Écart-type : 0.05447335989982177
```
![Tempéraure vs Concentration](./temp_conc.png?width=35vw)


### Exercice 9 (Pandas)

Cet exercice aide à comprendre comment analyser chaque ligne d’un jeu de données et enrichir le tableau.

1. Lire le fichier `minéraux.csv` contenant les colonnes `Nom` et `Densité`.
2. Parcourir le DataFrame **ligne par ligne** avec `.iterrows()`.
3. Afficher `"léger"` si la densité < 3, sinon `"lourd"`. Utiliser `if-else`.
4. Ajouter une nouvelle colonne `Catégorie` contenant ces valeurs, puis affiche le tableau final.


**Résultats**:
```
        Nom  Densité Catégorie
0    Quartz     2.65     léger
1    Galène     7.50     lourd
2   Calcite     2.71     léger
3    Pyrite     5.02     lourd
4     Gypse     2.30     léger
5  Hématite     5.25     lourd
6      Mica     2.83     léger
```


---

# Cours

## Gestion de fichiers

### Lecture d’un fichier CSV avec `pandas.read_csv()`

Le format **CSV** (*Comma-Separated Values*) est couramment utilisé pour exporter des données depuis des logiciels comme Excel, Logger Pro ou Capstone.

Exemple :

```csv
x;v
0,00;0,00
0,02;		<-- Valeur manquante
0,04;0,60
0,06;0,82
0,08;0,96
0,10;1,05
0,12;1,18
0,14;1,26
0,16;		<-- Valeur manquante
0,18;1,42
0,20;1,50	
```

→ Ce fichier utilise **le point-virgule (;)** comme séparateur et **la virgule (,)** comme séparateur décimal (format canadien-français).

### Lecture du fichier avec Pandas

* Lorsqu'on lit un fichier *.csv* avec Pandas, le contenu est stocké dans une variable de type ***DataFrame***.
* Un ***DataFrame*** est un tableau de données à deux dimensions (colonnes et lignes).

```python
import pandas as pd

# Lecture du fichier avec le bon séparateur et la bonne convention décimale
df = pd.read_csv("donnees.csv", delimiter=";", decimal=",")
df
```

**Paramètres importants :**

* `delimiter=";"` → indique que les valeurs sont séparées par des points-virgules.
* `decimal=","` → indique que la virgule est utilisée pour les décimales.

```
	x	v
0	0.00	0.00
1	0.02	NaN	<-- Valeur manquante
2	0.04	0.60
3	0.06	0.82
4	0.08	0.96
5	0.10	1.05
6	0.12	1.18
7	0.14	1.26
8	0.16	NaN	<-- Valeur manquante
9	0.18	1.42
10	0.20	1.50
```

### Gestion des lignes contenant des valeurs manquantes avec `isna()` et `dropna()`

Quand on travaille avec des données expérimentales, il arrive qu’une mesure soit **absente** (oubliée, perdue, ou invalide).
Dans un tableau pandas, une valeur manquante est notée **`NaN`** (*Not a Number*).

**Utilisation de `.isna()`**

```python
df.isna()
```
```
	x	v
0	False	False
1	False	True	<-- Valeur manquante
2	False	False
3	False	False
4	False	False
5	False	False
6	False	False
7	False	False
8	False	True	<-- Valeur manquante
9	False	False
10	False	False
```


> On peut aussi utiliser la fonction `df.isnull()`. Au lieu de ***NaN*** elle renvoie un tableau de **valeurs booléennes** (`True` si la cellule est vide, `False` sinon) :


### Suppression de lignes contenant des valeurs manquantes avec `dropna()`

```python
df_corrige = df.dropna()
```

### Remplacement des valeurs manquantes avec `fillna()`

Au lieu de supprimer les lignes contenant des valeurs manquantes, on peut remplacer les valeurs manquantes par une valeur choisie (par exemple, la moyenne) :

```python
moyenne = df["v"].mean()
df["v"] = df["v"].fillna(moyenne)
```

> Ici, toutes les cases vides de la colonne `v` sont remplacées par la moyenne des valeurs existantes.

```
x,v
0.0,0.0
0.02,0.9766666666666666	<-- Moyenne
0.04,0.6
0.06,0.82
0.08,0.96
0.1,1.05
0.12,1.18
0.14,1.26
0.16,0.9766666666666666	<-- Moyenne
0.18,1.42
0.2,1.5
```


### Exportation d’un fichier nettoyé avec `to_csv()`

Une fois les données vérifiées et nettoyées, on peut les sauvegarder dans un nouveau fichier plus « propre » (ex. : avec des points pour les décimales).

Si on veut sauvegarder un fichier **corrigé** :

```python
# Exportation du fichier corrigé
df.to_csv("donnees_corrigees.csv", index=False)
```

* Les colonnes numériques sont automatiquement converties en ***float*** python (le point pour les décimales)
* `index=False` empêche Pandas d’ajouter une colonne de numéros de ligne.

**IMPORTANT** : Le fichier source **reste intact**, on ne modifie jamais le fichier original. C’est une bonne pratique de **ne jamais écraser le fichier original** pour conserver une trace des données brutes.


## Manipulation d'un DataFrame

### Sélection d’une colonne

```python
# Accès à une colonne
df["x"]	# Données de la colonne x
df["v"] # Données de la colonne v
```

On peut aussi accéder à **plusieurs colonnes** :

```python
df[["x", "v"]]	# Seulement les données des 2 colonnes
```

### Création de nouvelles colonnes

Exemple : calcul de l’étirement d’un ressort à partir de la position et de la position d’équilibre.

```python
x_eq = 0.125  # position d’équilibre du ressort
df["e"] = x_eq - df["x"]  # nouvelle colonne "e"
df["de"] = 0.002  # même incertitude pour toutes les mesures
```

### Affichage et statistiques de base

```python
# Afficher les 5 premières lignes
df.head()

# Afficher les 10 premières lignes
df.head(10)

# Afficher les 5 dernières lignes
df.tail()

# Afficher les 10 dernières lignes
df.tail(10)

# Informations sur les colonnes et le type de données
print(df.info())

# Obtenir un résumé statistique (Nombre de valeurs par colonne, moyenne, écart-type, etc.)
df.describe()
```

Résultat typique :

```
	x	v	E
count	11.000000	11.000000	11.000000
mean	0.100000	0.976667	0.138757
std	0.066332	0.414488	0.083847
min	0.000000	0.000000	0.000000
25%	0.050000	0.890000	0.099625
50%	0.100000	0.976667	0.119235
75%	0.150000	1.220000	0.186250
max	0.200000	1.500000	0.281250
```


## Conversion d'une colonne du DataFrame en tableaux NumPy avec `.to_numpy()`

Parfois, on veut faire des calculs mathématiques rapides sur une colonne (ex. : calcul d’énergie, moyenne, écart-type, etc.).
Pour cela, on peut convertir une colonne en **tableau NumPy**.

```python
import numpy as np

# Conversion d’une colonne en tableau NumPy
x = df["x"].to_numpy()
v = df["v"].to_numpy()

# Exemple de calcul
v_moy = np.mean(v)
v_moy
```

* Ensuite, on peut utiliser les fonctionnalités de NumPy sur les données (converties en tableaux).


## Visualisation : graphique en nuage de points avec `plt.scatter()`

Pour visualiser la relation entre deux grandeurs physiques (ex. position et vitesse) :

```python
import matplotlib.pyplot as plt

plt.scatter(df["x"], df["v"], color='blue', label="Données expérimentales")
plt.xlabel("Position x (m)")
plt.ylabel("Vitesse v (m/s)")
plt.title("Vitesse en fonction de la position")
plt.legend()
plt.show()
```

* Chaque point correspond à une mesure expérimentale.

![Nuage](./nuage.png?width=35vw)


## À retenir

| Étape                    | Fonction               | Objectif principal                               |
| ------------------------ | ---------------------- | ------------------------------------------------ |
| Lecture de fichier       | `read_csv()`           | Importer les données expérimentales              |
| Affichage du df          | `head()`, `tail()`     | Par défaut 5 lignes                              |
| Infos et statistiques    | `info()`, `describe()` | Noms, types et statistiques des colonnes         |
| Nettoyage et exportation | `to_csv()`             | Créer un fichier compatible avec Python          |
| Manipulation de colonnes | `DataFrame["col"]`     | Ajouter, modifier ou analyser les données        |
| Conversion en tableau    | `to_numpy()`           | Calculs scientifiques rapides                    |

| Étape                                               | Fonction             | Résultat           |
| --------------------------------------------------- | -------------------- | ------------------ |
| Vérifier si une valeur est manquante                | `isna()`             | True / False       |
| Compter le nombre de valeurs manquantes par colonne | `isna().sum()`       | nombre par colonne |
| Compter le total des valeurs manquantes             | `isna().sum().sum()` | total              |
| Remplacer les valeurs manquantes                    | `fillna()`           | Tableau sans NaN   |

---

# Atelier

1. Téléchargez les fichiers de départ (.ipynb):
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_fichiers.ipynb)
2. Téléchargez le fichier de données:[eau_riviere.csv](./eau_riviere.csv)
3. Déplacez-les dans votre dossier prévu pour de la semaine en cours.
4. Ouvrez votre dossier de travail programmation-sciences à partir de Visual Studio Code.
	* Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb, .txt, .csv).


## Exercice - Analyse de la qualité de l’eau d’une rivière

* Un groupe d’étudiants en sciences environnementales surveille la qualité de l’eau d’une rivière.  
* Les mesures (**température**, **pH**, **concentration en oxygène**, **turbidité**) ont été recueillies à différents points de la rivière.  
* Certaines données sont **manquantes** et doivent être traitées avant l’analyse.
* Afin de les aider dans l'analyse des données recueillies, ils vous demandent de :
	* Lire et écrire des fichiers .csv` avec **pandas**.
	* Nettoyer les valeurs manquantes.
	* Ajouter des colonnes dérivées (`Qualite`, `Alerte`).
	* Enregistrer les résultats nettoyés.
	* (optionnel) Visualiser graphiquement des données.

### PARTIE 1 — Lecture et nettoyage avec pandas

   * Lire le fichier `eau_riviere.csv` avec `pd.read_csv()`.
   * Détecter les valeurs manquantes avec `.isna()`.
   * Remplacer les manquantes par la moyenne de la colonne correspondante avec `.fillna()`.
   * Ajouter la colonne `Qualite` selon la concentration dans la colonne `Oxygene` (**Astuce**: Utilisez `np.where()`):

     * `Oxygene >= 8.0` → `"Bonne"`
     * `7.5 <= Oxygene < 8.0` → `"Moyenne"`
     * `Oxygene < 7.5` → `"Faible"`
   * Ajouter la colonne `Alerte` : Contenant `"Attention"` si `pH < 7.0`, sinon `"OK"`. **Astuce**: Utilisez `np.where()`.
   * Sauvegarder le DataFrame nettoyé dans un fichier `eau_riviere_nettoyee.csv`.


### PARTIE 2 — Visualisation graphique (optionnel)

* À partir du DataFrame Pandas, tracez 2 graphiques

**Graphique #1**

* Avec barre d'erreurs sur les valeurs d’oxygène par site, avec des barres d’erreur représentant ±0.2 mg/L d’incertitude.
* Ajoutez les titres et les étiquettes d’axes.
* Personnalisez les couleurs selon la qualité.

![Oxygène par site](./oxygene_sites.png?width=35vw)

**Graphique #2** -  Nuage de points des valeurs d’oxygène par site

![Oxygène par site](./oxygene_sites_nuage.png?width=35vw)


<!--
# Atelier

**Solution :**

```python
import pandas as pd

df = pd.read_csv("donnees_ressort.csv", delimiter=";", decimal=",")
print(df.head())
```
```python
x_eq = 0.125
df["e"] = x_eq - df["x"]
df.head()
```

```python
import numpy as np

v = df["v"].to_numpy()
v_moy = np.mean(v)
print("Vitesse moyenne =", v_moy, "m/s")
```


```python
import matplotlib.pyplot as plt

plt.scatter(df["x"], df["v"], color="purple")
plt.xlabel("Position x (m)")
plt.ylabel("Vitesse v (m/s)")
plt.title("Vitesse en fonction de la position")
plt.show()
```
```python
print(df.describe())
v_max = df["v"].max()
print("Vitesse maximale :", v_max, "m/s")
```


```python
df.to_csv("donnees_corrigees.csv", index=False)
```

## Exercice

1. Lecture et affichage d’un fichier CSV

Un fichier nommé `donnees_ressort.csv` contient les colonnes `x;v`.
Lis ce fichier dans un DataFrame Pandas et affiche les 5 premières lignes.

2. Ajout d’une colonne calculée

La position d’équilibre du ressort est `x_eq = 0.125 m`.
Ajoute une colonne `"e"` correspondant à l’étirement du ressort (`x_eq - x`).

3. Conversion d’une colonne en tableau NumPy

Transforme la colonne `"v"` en tableau NumPy, puis calcule sa moyenne.

4. Création d’un graphique

Trace la vitesse `v` en fonction de la position `x` sous forme de nuage de points.

5. Exploration statistique

Affiche les statistiques descriptives du DataFrame (`min`, `max`, `moyenne`, etc.) et identifie la plus grande vitesse mesurée.

6. Exportation d’un fichier corrigé

Enregistre le DataFrame (avec la nouvelle colonne `e`) sous le nom `donnees_corrigees.csv`.
-->
---

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **deuxième examen** (30%)

1. Lire la prochaine leçon : [11. Fonctions personnalisées](../semaine11/)
2. Faire les exercices de la [prochaine leçon](../semaine11/#exercices)

