+++
chapter = true
pre = "9."
title = " Lecture et écriture de fichiers textes (avec NumPy, Pandas)"
weight = 109
draft = true
+++

## à faire
- S8 Dict
- Les fichiers de données
- Semaine 11 
   - enlever Pandas, 
   - ajouter ici les éléments manquant - filtre
   - Ajouter (S9) exos de S8 comme Atelier S9 + NumPy load save
   - ajouter exos avec Dictionnaires dans S8
- Semaine 7 ajouter exos/Atelier Physique 
- S'assurer le le cours contient toutes les notions nécessaires

## Objectifs

**Partie 1: Avec NumPy**
* Lire des données à partir de fichiers `.txt` et `.csv` avec NumPy.
* Écrire des données dans des fichiers `.txt` et `.csv`.
* Manipuler les données lues sous forme de tableaux NumPy pour faire des calculs scientifiques.

**Partie 2: Avec Pandas
* Lire des fichiers `.csv` et `.txt` en utilisant pandas.
* Explorer rapidement le contenu des fichiers.
* Écrire des DataFrames pandas dans des fichiers `.csv` ou `.txt`.

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
3. Cliquez sur le lien pour télécharger le fichier de données (`.csv`): [temperatures.csv](./temperatures.csv)
   * Il contient un jeu de données météorologiques prévisibles pour Bâle (France).
4. Enregistrez les fichiers dans votre dossier **exercices** de la semaine en cours.
5. Ouvrez **Visual Studio Code**.
6. Dans VS Code, recherchez et ouvrez les fichiers `exercices_fichiers_np.ipynb` et `exercices_fichiers_pd.ipynb`
7. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
8. Vous pouvez commencer à faire les exercices.

## Exercices

### Exercice 1 (NumPy)

* À l'aide de NumPy, créez un fichier `vitesses.txt` avec les valeurs suivantes (4 valeurs par ligne, 3 lignes) :

```
5.2 6.1 5.8 6.0
5.5 6.2 6.1 6.3
5.9 6.0 5.7 6.1
```

* Lisez ce fichier avec NumPy.
* Calculez la moyenne de chaque colonne.
* Écrivez les moyennes dans un nouveau fichier `moyennes.txt`.

## Exercice 2 (NumPy)

* Lisez le fichier CSV `temperatures.csv` avec NumPy.
* Transformez les températures en degrés Kelvin.
* Sauvegardez le nouveau fichier en CSV.

## Exercice 3 (Pandas)

1. Téléchargez un fichier `students.csv` contenant les colonnes : `Nom,Âge,Note`.
2. Lisez-le dans un DataFrame `df_etudiants`.
3. Affichez les 3 premières lignes.
4. Affichez le résumé statistique des notes.

## Exercice 4 (Pandas)

1. Ajoutez une colonne `Mention` au DataFrame en fonction de la note :

   * `>= 70` → "Bien"
   * `>= 50` → "Passable"
   * `< 50` → "Échec"
2. Enregistrez le DataFrame dans un fichier `etudiants_mentions.csv`.

## Exercice 5 (Pandas)

1. Ouvrez un fichier `experiment.txt` séparé par des tabulations avec colonnes : `Température`, `Pression`, `Volume`.
2. Lisez-le dans un DataFrame.
3. Enregistrez-le sous `experiment_export.txt` en conservant les tabulations.

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

Parfait ! Voici une leçon complète sur la lecture et l’écriture de fichiers `.csv` et `.txt` avec **pandas**. Je vais structurer la leçon pour des étudiants en sciences de la nature débutants en Python, avec exemples et exercices.

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
df_txt = pd.read_csv("data.txt", sep="\t")

print(df_txt)
```

> Pour un fichier `.txt` avec un séparateur autre que la virgule, utilisez `sep`.

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


