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



# Exercices

## Fichiers de départ à utiliser

1. Cliquez sur le lien pour télécharger les fichiers.  
[Bloc-notes de départ - NumPy](https://python-a25.netlify.app/blocnotes/exercices_fichiers_np.ipynb)  
[Bloc-notes de départ - Pandas](https://python-a25.netlify.app/blocnotes/exercices_fichiers_pd.ipynb)  
3. Télécharger le fichier de données (`.csv`): [temperatures.csv](./temperatures.csv)
   * Il contient un jeu de données météorologiques prévisibles pour Bâle (France).
4. Téléchargez le fichier de données (`.csv`): [etudiants.csv](./etudiants.csv)
   * Il contenant 3 colonnes : `Nom,Âge,Note`.
5. Cliquer sur le lien du fichier de données (`.txt`): [experience.txt](./experience.txt). Une fois ouvert, faites un clic-droit et choisir ***Enregistrer sous*** pour enregistrer le fichier dans votre dossier **exercices**.
6. Enregistrez les fichiers dans votre dossier **exercices** de la semaine en cours **(au même endroit que votre fichier .ipynb)**.
7. Ouvrez **Visual Studio Code**.
8. Dans VS Code, recherchez et ouvrez les fichiers `exercices_fichiers_np.ipynb` et `exercices_fichiers_pd.ipynb`.
9. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
10. Vous pouvez commencer à faire les exercices.

## Exercices

### Exercice 1 (NumPy)

**Objectif :** À l'aide de NumPy, créez un fichier `vitesses.txt` avec les valeurs suivantes (4 valeurs par ligne, 3 lignes) :
```
5.2 6.1 5.8 6.0
5.5 6.2 6.1 6.3
5.9 6.0 5.7 6.1
```

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
   * Vérifiez le séparateur utilisé dans le fichier (généralement `,`) et utilisez `delimiter=","` dans `np.genfromtxt()`.

2. **Conversion en Kelvin**
   * Pour convertir des degrés Celsius en Kelvin, ajoutez 273.15 à toutes les valeurs du tableau.
   * NumPy permet d’effectuer cette opération sur tout le tableau en une seule instruction.

3. **Enregistrer les données converties**
   * Utilisez `np.savetxt()` avec `delimiter=","` pour créer un **nouveau** fichier CSV (ex: `temperature_K.csv`).
   * Choisissez un format de nombres lisible (`fmt="%.2f"` par exemple).
   * Vérifier le contenu du fichier `temperature_K.csv` (données en K).

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
   	* [**Rappel sur np.where()**](http://localhost:1313/semaine8/#3-filtre-avec-npwhere)

2. **Enregistrer le DataFrame**
   * Utilisez `df_etudiants.to_csv("etudiants_mentions.csv", index=False)` pour sauvegarder.
   * Vérifiez le fichier créé pour voir la nouvelle colonne.

**Résultats** :
```
Données originales
       Nom  Âge  Note
0    Alice   20    85
1      Bob   21    67
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
0    Alice   20    85      Bien
1      Bob   21    67  Passable
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


