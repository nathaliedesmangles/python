+++
chapter = true
pre = "9."
title = " Lecture et écriture de fichiers textes (avec NumPy et Pandas)"
weight = 109
draft = false
+++


## Objectifs

**Partie 1: Avec NumPy**
* Lire des données à partir de fichiers `.txt` et `.csv` avec NumPy.
* Écrire des données dans des fichiers `.txt` et `.csv`.
* Manipuler les données lues sous forme de tableaux NumPy pour faire des calculs scientifiques.

**Partie 2: Avec Pandas**
* Lire des fichiers `.csv` et `.txt` en utilisant pandas.
* Explorer rapidement le contenu des fichiers.
* Écrire des DataFrames pandas dans des fichiers `.csv` ou `.txt`.
* Manipuler les données lues sous forme de DataFrames Pandas pour faire des calculs scientifiques.

## Fichier .ipynb pour la démo en classe

[Fichier utilisé pour la démonstration](https://python-a25.netlify.app/blocnotes/demo_fichiers.ipynb)

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}



# Exercices

## Fichiers de départ à utiliser

1. Cliquez sur les liens pour télécharger les fichiers (`.ipynb`, `.csv` et `.txt`).  
[**Bloc-notes de départ - NumPy**](https://python-a25.netlify.app/blocnotes/exercices_fichiers_np.ipynb)  
[**Bloc-notes de départ - Pandas**](https://python-a25.netlify.app/blocnotes/exercices_fichiers_pd.ipynb)  
**Fichiers de données** :   
	* [**temperatures.csv**](./temperatures.csv) : données météorologiques prévisibles pour Bâle (France).<br>
	* [**etudiants.csv**](./etudiants.csv) : 3 colonnes : `Nom,Âge,Note`.<br>
	* [**solubilite_sel.csv**](./solubilite_sel.csv) : 2 colonnes : `temperature,solubilite`.<br>
	* [**plantes.csv**](./plantes.csv) : 3 colonnes : `Nom,Hauteur_cm,Teneur_eau_%`.<br>
	* [**solutions.csv**](./solutions.csv) : 2 colonnes : `Temp_C,Concentration_mol_L`.<br>
	* [**mineraux.csv**](./mineraux.csv) : 2 colonnes : `Nom,Densité`.<br>
	* [**experience.txt**](./experience.txt). Une fois ouvert, faites un clic-droit et choisir ***Enregistrer sous*** pour enregistrer le fichier dans votre dossier **exercices**.
2. Enregistrez les fichiers dans votre dossier **exercices** de la semaine en cours **(au même endroit que votre fichier .ipynb)**.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez les fichiers `exercices_fichiers_np.ipynb` et `exercices_fichiers_pd.ipynb`.
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.

## Exercices

### Exercice 1 (NumPy)

**Objectif :** À l'aide de NumPy, créez un fichier `vitesses.txt` avec les valeurs suivantes (4 valeurs par ligne, 3 lignes) :
```
5.2 6.1 5.8 6.0
5.5 6.2 6.1 6.3
5.9 6.0 5.7 6.1
```

1. **Créer le tableau de données**
   * Utilisez **une liste de 3 listes** pour stocker les vitesses.
     ``` 
     [
       [5.2, 6.1, 5.8, 6.0],
       [5.5, 6.2, 6.1, 6.3],
       [5.9, 6.0, 5.7, 6.1]
     ]
     ```
   * Utilisez `np.array()` pour créer un tableau 2D contenant les vitesses.

2. **Enregistrer le tableau dans un fichier**
   * Utilisez `np.savetxt("nom_fichier.ext", tableau_numpy, format)` pour écrire le tableau dans un fichier `vitesses.txt`.  
		* Pour appliquer le format des nombres, par exemple pour 2 décimales, remplacez ***format*** par `fmt="%.2f"`.

3. **Lire le fichier avec NumPy**
   * Utilisez `np.loadtxt()` pour lire les données à partir du fichier créé précédemment.
   * Affichez les données lues et vérifiez que le tableau lu a bien la même forme que le tableau original.
   ```
   [[5.2 6.1 5.8 6. ]
    [5.5 6.2 6.1 6.3]
    [5.9 6.  5.7 6.1]]
   ```

4. **Calculer la moyenne de chaque colonne**
   * Utilisez `np.mean(..., axis=0)` pour obtenir les moyennes colonne par colonne.

5. **Enregistrer les moyennes dans un nouveau fichier**
   * Utilisez `np.savetxt()` pour écrire les moyennes dans un fichier nommé `moyennes.txt`.
   * Vérifiez le contenu du fichier après écriture. Vous devriez voir ceci : 
   ```
   5.53
   6.10
   5.87
   6.13
   ```

**Résultats** :
```
Moyennes enregistrées : [5.53333333 6.1        5.86666667 6.13333333]
```

### Exercice 2 (NumPy)

**Objectif :** lire un fichier CSV (`temperatures.csv`), manipuler les données et sauvegarder les résultats.

1. **Lire le fichier CSV `temperatures.csv`**
   * Vérifiez le séparateur utilisé dans le fichier (généralement `,`) et utilisez `delimiter=","`, `skip_heade=1` et `usecols=1` dans `np.genfromtxt()`.

2. **Conversion en Kelvin**
   * Pour convertir des degrés Celsius en Kelvin, ajoutez 273.15 à toutes les valeurs du tableau.
     * **Astuces** : NumPy permet d’effectuer cette opération sur tout le tableau en une seule instruction (sans boucle).

3. **Enregistrer les données converties**
   * Utilisez `np.savetxt()` avec `delimiter=","` pour créer un **nouveau** fichier CSV (ex: `temperature_K.csv`).
   * Choisissez un format de nombres lisible (`fmt="%.2f"` par exemple).
   * Vérifier le contenu du fichier `temperature_K.csv` (données en K). Vous devriez voir ceci (partiel):
   
   ![Températures en K](./tempK_csv.png?width=15vw&height=25vw)

**Résultats** :
```
Températures en °C :
[2.31 2.37 2.43 ... 1.92 1.96 1.68]

Températures converties en K :
[275.46 275.52 275.58 ... 275.07 275.11 274.83]
```

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

1. Lire un fichier `solutions.csv` contenant des colonnes `Temp_C` et `Concentration_mol_L`.
2. Convertir ces deux colonnes en tableaux NumPy.
3. Calculer la moyenne et l’écart-type de la concentration.
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
2. Parcourir le DataFrame avec `.iterrows()`.
3. Afficher `"léger"` si la densité < 3, sinon `"lourd"`.
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

## Pourquoi lire et écrire des fichiers ?

En sciences, on ne travaille pas toujours avec des données générées dans le programme.
Souvent, les données proviennent :

* d’expériences mesurées,
* de fichiers partagés par d’autres chercheurs,
* de simulations précédentes.

Pour traiter ces données en Python, les bibliothèques `NumPy` et `Pandas` fournissent des fonctions rapides pour **lire** et **écrire** des tableaux numériques.


## 1. Lecture et écriture avec NumPy

### Lecture de fichiers

#### Fichiers texte simples (`.txt`)

Supposons que nous avons un fichier `mesures.txt` contenant des valeurs de température (sans en-tête) :

```
20.1 21.3 19.8 22.0
21.0 22.2 20.5 23.1
```

Lecture en NumPy :

```python
import numpy as np

# Lecture du fichier
donnees = np.loadtxt("mesures.txt")

print(donnees)
print(type(donnees))
```

**Explications :**

* `np.loadtxt()` lit un fichier texte et retourne un tableau NumPy.
* Par défaut, les colonnes sont séparées par des espaces.
* `donnees` est un tableau NumPy 2D (lignes × colonnes).


#### Fichiers CSV (`.csv`)

Un fichier CSV (*Comma-Separated Values*) contient des données tabulaires séparées par des virgules (ou parfois par un autre séparateur).

Si les données sont séparées par des virgules :

```
20.1,21.3,19.8,22.0
21.0,22.2,20.5,23.1
```

On peut lire le fichier avec :

```python
donnees = np.loadtxt("mesures.csv", delimiter=",")
print(donnees)
```

**Remarque :**
`delimiter=","` indique que les colonnes sont séparées par des virgules.


### Option 1 : Utiliser `np.genfromtxt()` (plus robuste)

Si ton fichier contient :

* une **première ligne d’en-têtes**,
* des **valeurs manquantes**,
* ou des **colonnes non numériques** (comme des dates),

alors `np.loadtxt()` échouera.
Dans ce cas, on utilise `np.genfromtxt()`.

Exemple :

```
timestamp,temperature
2021-01-01 00:00:00,20.1
2021-01-01 01:00:00,21.3
2021-01-01 02:00:00,19.8
```

Lecture uniquement de la colonne numérique :

```python
import numpy as np

# Lecture en sautant la première ligne et en lisant la 2e colonne
temperatures = np.genfromtxt("temperatures.csv", delimiter=",", skip_header=1, usecols=1)

# Conversion en Kelvin
temperatures_K = temperatures + 273.15

# Sauvegarde dans un nouveau fichier
np.savetxt("temperatures_kelvin.csv", temperatures_K, delimiter=",", fmt="%.2f")
print("Fichier 'temperatures_kelvin.csv' enregistré.")
```

**Explications :**

* `skip_header=1` : ignore la première ligne contenant les titres.
* `usecols=1` : lit seulement la colonne d’indice 1 (ici, les températures).
* `np.genfromtxt()` : accepte les fichiers mixtes (texte + nombres) et les valeurs manquantes.


#### Exemple avancé avec plusieurs types de données

Si on veut **conserver les dates** et les températures :

```python
data = np.genfromtxt("temperatures.csv", delimiter=",", dtype=None, encoding=None, names=True)

dates = data['timestamp']
temperatures = data['temperature']
temperatures_K = temperatures + 273.15

# Combine dates et températures converties
output = np.column_stack((dates, temperatures_K))
np.savetxt("temperatures_kelvin.csv", output, fmt="%s,%.2f", delimiter=",", header="timestamp,temperature_K", comments="")
```


### Écriture de fichiers

#### Fichiers texte (`.txt` ou `.csv`)

Pour écrire un tableau NumPy dans un fichier texte :

```python
import numpy as np

donnees = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt("resultats.txt", donnees)
```

* Chaque ligne du tableau devient une ligne dans le fichier.
* Par défaut, les valeurs sont séparées par un espace.

Pour un séparateur différent :

```python
np.savetxt("resultats.csv", donnees, delimiter=",")
```

**Format et précision des nombres** :

```python
np.savetxt("resultats.csv", donnees, delimiter=",", fmt="%.2f")
```

* `%.2f` : deux chiffres après la virgule.


## Conclusion

`NumPy` permet de lire et d’écrire facilement des données scientifiques :

| Tâche           | Fonction          | Usage typique                                     |
| --------------- | ----------------- | ------------------------------------------------- |
| Lecture simple  | `np.loadtxt()`    | fichiers purement numériques                      |
| Lecture robuste | `np.genfromtxt()` | fichiers avec texte, en-têtes, valeurs manquantes |
| Écriture        | `np.savetxt()`    | export en `.txt` ou `.csv`                        |

---

## Introduction à pandas


* Pandas est conçu pour manipuler des tableaux hétérogènes (colonnes de types différents).
* C’est l’outil de référence pour les fichiers de données expérimentales complexes (ex. : plusieurs variables, unités, dates).
* Pandas simplifie la lecture et l’écriture de fichiers de données.

## Importation de la bibliothèque

```python
import pandas as pd
```

## Lecture d’un fichier CSV avec Pandas

### Exemple de fichier `data.csv`

```text
Nom,Âge,Poids
Alice,20,55
Bob,22,70
Charlie,19,65
```

### Lecture avec pandas

```python
import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("data.csv")

# Afficher le DataFrame
print(df)
```

**Résultat**
```
      Nom  Âge  Poids
0    Alice   20     55
1      Bob   22     70
2  Charlie   19     65
```

> `read_csv()` lit le fichier et crée un DataFrame.


### Options utiles de `read_csv`

| Option        | Description                                         |
| ------------- | --------------------------------------------------- |
| `sep=";"`     | Séparateur différent de la virgule                  |
| `header=None` | Pas de ligne d’en-tête dans le fichier              |
| `names=[...]` | Nommer les colonnes si le fichier n’a pas d’en-tête |
| `index_col=0` | Utiliser une colonne comme index du DataFrame       |


## Lecture d’un fichier texte (`.txt`)

Les fichiers `.txt` peuvent contenir des données séparées par un espace, une tabulation, ou un autre caractère.

### Exemple de fichier `data.txt` (séparateur tabulation)

```text
Nom    Âge    Poids
Alice  20     55
Bob    22     70
Charlie 19    65
```

### Lecture avec pandas

```python
# Lire le fichier texte avec tabulation comme séparateur
df_txt = pd.read_csv("data.txt", sep="\t")	# \t = tabulation

print(df_txt)
```

> Pour un fichier `.txt` avec un séparateur autre que la virgule, utilisez `sep`. 
> Dans le code précédent `sep="\t"`, signifie que le séparateur est la tabulation (touche `tab` du clavier)


## Exploration rapide des données avec Pandas

Une fois le fichier lu, on peut explorer les données :

```python
# Afficher les 5 premières lignes
print(df.head())

# Afficher les 5 dernières lignes
print(df.tail())

# Résumé statistique pour les colonnes numériques
print(df.describe())

# Informations sur les colonnes et le type de données
print(df.info())
```


## Écriture d’un DataFrame dans un fichier

Vous pouvez enregistrer vos données modifiées dans un nouveau fichier CSV ou TXT :

```python
# Écriture dans un CSV
df.to_csv("data_export.csv", index=False)  # index=False pour ne pas enregistrer les index

# Écriture dans un TXT avec tabulation
df.to_csv("data_export.txt", sep="\t", index=False)
```

> `to_csv()` peut aussi utiliser `sep=";"` pour un séparateur point-virgule, ou d’autres séparateurs selon vos besoins.


## Conclusion pour la lecture et l'écriture de fichiers avec Pandas

* `pd.read_csv()` lit les fichiers CSV et TXT avec des séparateurs personnalisés.
* `df.to_csv()` permet d’enregistrer les DataFrames dans des fichiers.
* pandas facilite l’exploration rapide des données avec `head()`, `tail()`, `describe()` et `info()`.


## Gestion des valeurs manquantes avec Pandas

Quand on travaille avec des données expérimentales, il arrive qu’une mesure soit **absente** (oubliée, perdue, ou invalide).
Dans un tableau pandas, une valeur manquante est notée **`NaN`** (Not a Number).

### 1. Détecter les valeurs manquantes : `pd.isna()` ou `pd.isnull()`

Ces deux fonctions font **exactement la même chose**. On peut utiliser l’une ou l’autre.


```python
import pandas as pd

# Données expérimentale (dictionnaire)
data = {
         'temp': [0, 10, 20, 30], 
         'solubilite': [32.0, 34.1, , 37.5]
       }
# Dictionnaire converti en dataframe
df = pd.DataFrame(data)
print(df)
```

| temp | solubilite |
| ---- | ---------- |
| 0    | 32.0       |
| 10   | 34.1       |
| 20   | **NaN**        |
| 30   | 37.5       |

#### Utilisation de `.isna()`

```python
df.isna()
```

#### Utilisation de `.isnull()`
```python
df.isnull()
```

> Résultat identique à `df.isna()`, renvoie un tableau de **valeurs booléennes** (`True` si la cellule est vide, `False` sinon) :

| temp  | solubilite |
| ----- | ---------- |
| False | False      |
| False | False      |
| False | **True**       |
| False | False      |

{{% notice style="Cyan" title="Information" %}}
Pour le reste des exemples, on utilisera `isna()`, mais on pourrait aussi le faire avec `.isnull()`.
{{% /notice %}}

### 2. Compter les valeurs manquantes : `df.isna().sum()`

```python
df.isna().sum()
```

> donne le **nombre de valeurs manquantes par colonne et le type (ici `int64`)** :

```
temp          0
solubilite    1
dtype: int64
```

**Astuce** : Pour savoir le **nombre total** de valeurs manquantes dans tout le tableau :

```python
df.isna().sum().sum()	# Résultat : 1
```


### 3. Remplacer les valeurs manquantes : `fillna()`

Si on veut **remplir** les valeurs manquantes par une valeur choisie (par exemple, la moyenne), on peut utiliser :

```python
moyenne = df['solubilite'].mean()
df['solubilite'] = df['solubilite'].fillna(moyenne)
```

> Ici, toutes les cases vides de la colonne `solubilite` sont remplacées par la moyenne des valeurs existantes.


## Résumé pour la gestion des valeurs manquantes

| Objectif                                            | Fonction                | Exemple             | Résultat           |
| --------------------------------------------------- | ----------------------- | ------------------- | ------------------ |
| Vérifier si une valeur est manquante                | `pd.isna()`             | `df.isna()`         | True / False       |
| Idem (synonyme)                                     | `pd.isnull()`           | `df.isnull()`       | True / False       |
| Compter le nombre de valeurs manquantes par colonne | `df.isna().sum()`       | —                   | nombre par colonne |
| Compter le total des valeurs manquantes             | `df.isna().sum().sum()` | —                   | total              |
| Remplacer les valeurs manquantes                    | `fillna()`              | `df.fillna(valeur)` | Tableau sans NaN   |


## Sélection de données dans un DataFrame avec `iloc`

* `iloc` permet de **sélectionner des **lignes** ou des **colonnes** selon leur position (index numérique)** plutôt que leur nom.
* C’est pratique quand on ne connaît pas les noms des colonnes ou qu’on veut simplement accéder à une portion du tableau.

	* `df.iloc[0]` → première ligne
	* `df.iloc[:, 1]` → toute la 2ᵉ colonne
	* `df.iloc[2:5, 0:2]` → lignes 2 à 4 et colonnes 0 et 1

**Exemple** :
```python
import pandas as pd

data = {
    "Espèce": ["Truite", "Saumon", "Perchaude", "Brochet"],
    "Longueur_cm": [35, 52, 27, 61],
    "Masse_g": [450, 1500, 320, 2200]
}

poissons = pd.DataFrame(data)

# Affiche la 2e ligne (index 1)
print(poissons.iloc[1])

# Affiche la première colonne
print(poissons.iloc[:, 0])

# Affiche les 2 premières lignes et colonnes
print(poissons.iloc[0:2, 0:2])
```

## Conversion d'une colonne ou n DataFrame en tableau NumPy avec `.to_numpy()`

* `.to_numpy()` transforme une **colonne ou un DataFrame en tableau NumPy**, ce qui permet d’utiliser les fonctions mathématiques rapides de NumPy (`mean`, `std`, `polyfit`, etc.).

**Exemple** :

```python
import pandas as pd
import numpy as np

data = {
    "Température_C": [15, 18, 20, 23],
    "Taux_croissance": [1.2, 1.8, 2.3, 2.9]
}
plantes = pd.DataFrame(data)

# Convertir en tableau NumPy
t = plantes["Température_C"].to_numpy()
r = plantes["Taux_croissance"].to_numpy()

# Calculs avec NumPy
moyenne = np.mean(r)
print("Croissance moyenne :", moyenne)
```


## Parcourir les lignes d'un DataFrame avec `.iterrows()`

* `.iterrows()` permet de **parcourir chaque ligne d’un DataFrame** dans une boucle `for`. 
* C’est utile pour faire des vérifications ou des calculs ligne par ligne.
* Chaque itération retourne :
	* l’**index de la ligne**
	* la **ligne elle-même** (comme une mini-série Pandas)

**Exemple** : 

```python
import pandas as pd

data = {
    "Échantillon": ["A", "B", "C"],
    "pH": [6.5, 7.2, 8.1]
}
eau = pd.DataFrame(data)

for index, ligne in eau.iterrows():
    if ligne["pH"] > 7:
        print(f"Échantillon {ligne['Échantillon']} : basique")
    else:
        print(f"Échantillon {ligne['Échantillon']} : acide ou neutre")
```

---

# Atelier

1. Téléchargez les fichiers de départ (.ipynb):
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_fichiers.ipynb)
2. Téléchargez les fichiers de données:[eau.txt](./eau.txt) et [eau_riviere.csv](./eau_riviere.csv)
3. Déplacez-les dans votre dossier prévu pour de la semaine en cours.
4. Ouvrez votre dossier de travail programmation-sciences à partir de Visual Studio Code.
	* Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb, .txt, .csv).


## Exercice - Analyse de la qualité de l’eau d’une rivière

* Un groupe d’étudiants en sciences environnementales surveille la qualité de l’eau d’une rivière.  
* Les mesures (**température**, **pH**, **concentration en oxygène**, **turbidité**) ont été recueillies à différents points de la rivière.  
* Certaines données sont **manquantes** et doivent être traitées avant l’analyse.
* Afin de les aider dans l'analyse des données recueillies, ils vous demandent de :
	* Lire et écrire des fichiers `.txt` et `.csv` avec **NumPy** et **pandas**.
	* Nettoyer les valeurs manquantes.
	* Ajouter des colonnes dérivées (`Qualite`, `Alerte`).
	* Enregistrer les résultats nettoyés.
	* (optionnel) Visualiser graphiquement des données. 

### Quelques rappels pédagogiques rapides

* `np.loadtxt()` convient pour les fichiers **purement numériques** et sans en-têtes.
* `np.genfromtxt()` est plus tolérant (en-têtes, missing).
* `pandas.read_csv()` lit automatiquement les en-têtes et conserve les types.
* `df.isna().sum()` permet d’identifier où se trouvent les valeurs manquantes.
* `df.fillna(...)` remplace les NaN.
* `np.where()` permettent d’ajouter des colonnes conditionnelles de façon vectorisée (rapide).


### PARTIE 1 — Lecture et écriture avec NumPy

   * Lire le fichier `eau.txt` sachant qu'il ne contient que des valeurs numériques sans en-têtes, délimitées par un espace.
   * Calculer la moyenne de chaque **colonne** avec `np.mean()` ou `np.nanmean()`.
   * Sauvegarder les moyennes avec le format `fmt="%.2f"` dans un fichier texte `moyennes_eau.txt`. 

### PARTIE 2 — Lecture et nettoyage avec pandas

   * Lire le fichier `eau_riviere.csv` avec `pd.read_csv()`.
   * Détecter les valeurs manquantes avec `.isna()`.
   * Remplacer les manquantes par la moyenne de la colonne correspondante avec `.fillna()`.
   * Ajouter la colonne `Qualite` selon la oncentration dans la colonne `Oxygene` (**Astuce**: Utilisez `np.where()`):

     * `Oxygene >= 8.0` → `"Bonne"`
     * `7.5 <= Oxygene < 8.0` → `"Moyenne"`
     * `Oxygene < 7.5` → `"Faible"`
   * Ajouter la colonne `Alerte` : Contenant `"Attention"` si `pH < 7.0`, sinon `"OK"`. **Astuce**: Utilisez `np.where()`.
   * Sauvegarder le DataFrame nettoyé dans un fichier `eau_riviere_nettoyee.csv`.


### PARTIE 3 — Visualisation graphique (optionnel)

* À partir du DataFrame Pandas, tracez un graphique en barres des valeurs d’oxygène par site, avec des barres d’erreur représentant ±0.2 mg/L d’incertitude.
* Ajoutez les titres et les étiquettes d’axes.
* Personnalisez les couleurs selon la qualité.

![Oxygène par site](./oxygene_sites.png?width=35vw)

---

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **deuxième examen** (30%)

1. Lire la prochaine leçon : [11. Fonctions personnalisées](../semaine11/)
2. Faire les exercices de la [prochaine leçon](../semaine11/#exercices)



