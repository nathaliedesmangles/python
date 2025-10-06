+++
chapter = true
pre = "9."
title = " Lecture et écriture de fichiers textes (avec NumPy ou Pandas)"
weight = 109
draft = true
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

## Fichier .ipynb pour la démo en classe

[Fichier utilisé pour la démonstration](https://python-a25.netlify.app/blocnotes/demo_fichiers.ipynb)

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}


Téléchargez un fichier students.csv contenant les colonnes : Nom,Âge,Note.

# Exercices

## Fichiers de départ à utiliser

1. Cliquez sur le lien pour télécharger les fichiers.  
[Bloc-notes de départ - NumPy](https://python-a25.netlify.app/blocnotes/exercices_fichiers_np.ipynb)  
[Bloc-notes de départ - Pandas](https://python-a25.netlify.app/blocnotes/exercices_fichiers_pd.ipynb)  
3. Cliquez sur le lien pour télécharger le fichier de données (`.csv`): [temperatures.csv](./temperatures.csv)
   * Il contient un jeu de données météorologiques prévisibles pour Bâle (France).
4. Cliquez sur le lien pour télécharger le fichier de données (`.txt`): [experience.txt](./experience.txt)

5. Enregistrez les fichiers dans votre dossier **exercices** de la semaine en cours **(au même endroit que votre fichier .ipynb)**.
6. Ouvrez **Visual Studio Code**.
7. Dans VS Code, recherchez et ouvrez les fichiers `exercices_fichiers_np.ipynb` et `exercices_fichiers_pd.ipynb`.
8. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
9. Vous pouvez commencer à faire les exercices.

## Exercices

### Exercice 1 (NumPy)

**Objectif :** À l'aide de NumPy, créez un fichier `vitesses.txt` avec les valeurs suivantes (4 valeurs par ligne, 3 lignes) :
```
5.2 6.1 5.8 6.0
5.5 6.2 6.1 6.3
5.9 6.0 5.7 6.1
```

**Étapes** :

1. **Créer le tableau de données**
   * Utilisez `np.array()` pour créer un tableau 2D contenant les vitesses.
   * Chaque ligne du tableau correspond à une ligne dans le fichier texte.

2. **Enregistrer le tableau dans un fichier**
   * Utilisez `np.savetxt()` pour écrire le tableau dans un fichier `vitesses.txt`.
   * Vérifiez le format des nombres (par exemple `fmt="%.2f"` pour 2 décimales).

3. **Lire le fichier avec NumPy**
   * Utilisez `np.loadtxt()` pour lire les données à partir du fichier créé.
   * Vérifiez que le tableau lu a bien la même forme que le tableau original.

4. **Calculer la moyenne de chaque colonne**
   * Utilisez `np.mean(..., axis=0)` pour obtenir les moyennes colonne par colonne.

5. **Enregistrer les moyennes dans un nouveau fichier**
   * Utilisez `np.savetxt()` pour écrire les moyennes dans `moyennes.txt`.
   * Vérifiez le contenu du fichier après écriture.

**Résultats** :
```
Moyennes enregistrées : [5.53333333 6.1        5.86666667 6.13333333]
```

### Exercice 2 (NumPy)

**Objectif :** lire un fichier CSV (`temperatures.csv`), manipuler les données et sauvegarder les résultats.

1. **Lire le fichier CSV `temperatures.csv`**
   * Vérifiez le séparateur utilisé dans le fichier (généralement `,`) et utilisez `delimiter=","` dans `np.loadtxt()`.

2. **Conversion en Kelvin**
   * Pour convertir des degrés Celsius en Kelvin, ajoutez 273.15 à toutes les valeurs du tableau.
   * NumPy permet d’effectuer cette opération sur tout le tableau en une seule instruction.

3. **Enregistrer les données converties**
   * Utilisez `np.savetxt()` avec `delimiter=","` pour créer un **nouveau** fichier CSV (ex: `temperature_K.csv`).
   * Choisissez un format de nombres lisible (`fmt="%.2f"` par exemple).

**Résultats** :
```
```

### Exercice 3 (Pandas)

**Objectif :** lire un fichier CSV dans un DataFrame et explorer les données.

1. **Lire le fichier CSV `etudiants.csv`**
   * Utilisez `pd.read_csv("etudiants.csv")` pour créer un DataFrame `df_etudiants`.

2. **Afficher un aperçu des données**
   * `df_etudiants.head(3)` montre les 3 premières lignes.
   * Utile pour vérifier que le fichier a été lu correctement.

3. **Résumé statistique**
   * `df_etudiants["Note"].describe()` fournit la moyenne, l’écart-type, le minimum, le maximum, etc.
   * Permet de comprendre rapidement la distribution des notes.

**Résultats** :
```
Nom  Âge  Note
0    Alice   20    85
1      Bob   21    67
2  Charlie   19    45
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

   * Examinez la valeur de chaque note.
   * Selon l’intervalle, attribuez la mention : "Bien", "Passable", "Échec".
   * Vous pouvez utiliser `np.where()` pour appliquer les conditions à tout le DataFrame.

2. **Enregistrer le DataFrame**
   * Utilisez `df_etudiants.to_csv("etudiants_mentions.csv", index=False)` pour sauvegarder.
   * Vérifiez le fichier créé pour voir la nouvelle colonne.

**Résultats** :
```python
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
---

# Cours

## Pourquoi lire et écrire des fichiers ?

En sciences, on ne travaille pas toujours avec des données générées dans le programme.
Souvent, les données proviennent :

* d’expériences mesurées,
* de fichiers partagés par d’autres chercheurs,
* de simulations précédentes.

Pour traiter ces données en Python, les bibliothèques `NumPy` et `Pandas` fournissent des fonctions rapides pour lire et écrire des tableaux.

## 1. Avec NumPy

### Lecture de fichiers

#### 1. Fichiers texte simples (`.txt`)

Supposons que nous avons un fichier `mesures.txt` contenant des valeurs de température (sans en-tête :

```
20.1 21.3 19.8 22.0
21.0 22.2 20.5 23.1
```

Pour lire ce fichier en NumPy :

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
* `donnees` est maintenant un tableau NumPy 2D.

#### 2. Fichiers CSV (`.csv`)

Si les données sont séparées par des virgules (format CSV) :

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

* `delimiter=","` indique que les colonnes sont séparées par des virgules.

Si le fichier contient une première ligne avec des titres de colonnes :

```
Temp1,Temp2,Temp3,Temp4
20.1,21.3,19.8,22.0
21.0,22.2,20.5,23.1
```

On peut utiliser `np.genfromtxt` :

```python
donnees = np.genfromtxt("mesures.csv", delimiter=",", skip_header=1)
print(donnees)
```

* `skip_header=1` ignore la première ligne.
* `np.genfromtxt` est plus robuste si le fichier contient des valeurs manquantes.


## Écriture de fichiers

### 1. Fichiers texte (`.txt` ou `.csv`)

Pour écrire un tableau NumPy dans un fichier texte :

```python
import numpy as np

donnees = np.array([[1, 2, 3], [4, 5, 6]])

np.savetxt("resultats.txt", donnees)
```

* Chaque ligne du tableau devient une ligne dans le fichier.
* Par défaut, les valeurs sont séparées par un espace.

Pour utiliser un autre séparateur, par exemple une virgule :

```python
np.savetxt("resultats.csv", donnees, delimiter=",")
```

**Format et précision des nombres**

Vous pouvez choisir le format des nombres :

```python
np.savetxt("resultats.csv", donnees, delimiter=",", fmt="%.2f")
```

* `%.2f` signifie deux chiffres après la virgule.


## Conclusion pour NumPy

NumPy permet de manipuler rapidement des fichiers de données scientifiques :

* Lecture simple : `np.loadtxt`
* Lecture robuste avec en-têtes ou valeurs manquantes : `np.genfromtxt`
* Écriture : `np.savetxt` avec choix du séparateur et de la précision

---

## Introduction à pandas

* **pandas** est une bibliothèque Python puissante pour la manipulation et l’analyse de données.
* Les données sont stockées dans des **DataFrames**, qui ressemblent à des tableaux Excel : lignes × colonnes.
* pandas simplifie la lecture et l’écriture de fichiers de données.

## Importation de la bibliothèque

```python
import pandas as pd
```

## Lecture d’un fichier CSV avec Pandas

Un fichier CSV (Comma-Separated Values) contient des données tabulaires séparées par des virgules (ou parfois par un autre séparateur).

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


## Conclusion pour Pandas

* `pd.read_csv()` lit les fichiers CSV et TXT avec des séparateurs personnalisés.
* `df.to_csv()` permet d’enregistrer les DataFrames dans des fichiers.
* pandas facilite l’exploration rapide des données avec `head()`, `tail()`, `describe()` et `info()`.


