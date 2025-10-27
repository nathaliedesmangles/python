+++
pre = "<b>9.</b>"
title = " Manipulation de données dans un fichier (avec Pandas)"
weight = 209
draft = false
+++

<!--
## Exercice 1 (NumPy)

```python
import numpy as np

vitesses = np.array([
    [5.2, 6.1, 5.8, 6.0],
    [5.5, 6.2, 6.1, 6.3],
    [5.9, 6.0, 5.7, 6.1]
])

np.savetxt("vitesses.txt", vitesses, fmt="%.2f")

# Lire le fichier
donnees = np.loadtxt("vitesses.txt")

# Calcul des moyennes par colonne
moyennes = np.mean(donnees, axis=0)

# Sauvegarder le fichier des moyennes
np.savetxt("moyennes.txt", moyennes, fmt="%.2f")
```


## Exercice 2 (NumPy)

```python
import numpy as np

# 1. Lecture du fichier CSV (avec en-tête)

# On lit seulement la colonne numérique (températures)
# et on ignore la première ligne qui contient les titres.
temperatures_C = np.genfromtxt("temperatures.csv",
                               delimiter=",",
                               skip_header=1,
                               usecols=1)

print("Températures en °C :")
print(temperatures_C)

# 2. Conversion en Kelvin
# NumPy permet de faire l’opération sur tout le tableau d’un coup.
temperatures_K = temperatures_C + 273.15

print()
print("Températures converties en K :")
print(temperatures_K)

# 3. Enregistrement dans un nouveau fichier CSV
# On crée un fichier 'temperature_K.csv' avec 2 décimales.
np.savetxt("temperature_K.csv",
           temperatures_K,
           delimiter=",",
           fmt="%.2f",
           header="temperature_K",
           comments="")
```

-->

## Exercice 3 (Pandas)

```python
import pandas as pd

df_etudiants = pd.read_csv("etudiants.csv")
print(df_etudiants.head(3))
print(df_etudiants["Note"].describe())
```



## Exercice 4 (Pandas)

```python
import pandas as pd
import numpy as np

# 1. Lecture du fichier CSV contenant les étudiants
df_etudiants = pd.read_csv("etudiants.csv")

# Affichage du DataFrame original
print("Données originales")
print(df_etudiants)

# 2. Création de la colonne 'Mention' selon la note
df_etudiants["Mention"] = np.where(
    df_etudiants["Note"] >= 70, "Bien",
    np.where(df_etudiants["Note"] >= 50, "Passable", "Échec")
)

# Affichage du DataFrame mis à jour
print("Données avec mentions")
print(df_etudiants)

# 3. Sauvegarde du DataFrame dans un nouveau fichier CSV
df_etudiants.to_csv("etudiants_mentions.csv", index=False)
```

## Exercice 5 (Pandas)

```python

df = pd.read_csv("experiment.txt", sep="\t")
df.to_csv("experiment_export.txt", sep="\t", index=False)
print("Fichier 'experiment_export.txt' enregistré avec tabulations.")
```

## Exercice 6 (Pandas)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Lecture du fichier CSV
df = pd.read_csv("solubilite_sel.csv")

# Vérification des valeurs manquantes
print("Valeurs manquantes :")
print(df.isna())

# Nombre total de valeurs manquantes
print("Nombre total de NaN :", df.isna().sum().sum())

# Remplacement des NaN par la moyenne
moyenne = df['solubilite'].mean(skipna=True)
df['solubilite'] = df['solubilite'].fillna(moyenne)

# Vérification après remplacement
print("\nDonnées après traitement :")
print(df)

# Visualisation
plt.plot(df['temperature'], df['solubilite'], marker='o')
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100 mL)")
plt.title("Solubilité d’un sel en fonction de la température")
plt.show()
```

## Exercice 7 (Pandas)

```python
import pandas as pd

# Lecture du fichier CSV
plantes = pd.read_csv("plantes.csv")

# 1. Affiche la 5e ligne (index 4 car on commence à 0)
print("5e ligne complète :")
print(plantes.iloc[4])

# 2. Affiche uniquement la colonne de la hauteur
print()
print("Colonne Hauteur_cm :")
print(plantes.iloc[:, 1])  # colonne à l'index 1

# 3. Affiche les 3 premières lignes et les 2 premières colonnes
print()
print("3 premières plantes, 2 premières colonnes :")
print(plantes.iloc[0:3, 0:2])
```

## Exercice 8 (Pandas et NumPy)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lecture du fichier
solutions = pd.read_csv("solutions.csv")

# 1. Conversion en tableaux NumPy
T = solutions["Temp_C"].to_numpy()
C = solutions["Concentration_mol_L"].to_numpy()

# 2. Calcul de la moyenne et de l’écart-type
moyenne = np.mean(C)
ecart_type = np.std(C)

print("Concentration moyenne :", moyenne)
print("Écart-type :", ecart_type)

# 3. Graphique de concentration en fonction de la température
plt.plot(T, C, "o-", label="Données expérimentales")
plt.xlabel("Température (°C)")
plt.ylabel("Concentration (mol/L)")
plt.title("Variation de la concentration avec la température")
plt.legend()
plt.show()
```


## Exercice 9 (Pandas)

```python
import pandas as pd

# Lecture du fichier
mineraux = pd.read_csv("mineraux.csv")

# Liste vide pour stocker les catégories
categories = []

# 1-2. Parcours du DataFrame et classification
for index, ligne in mineraux.iterrows():
    if ligne["Densité"] < 3:
        categories.append("léger")
    else:
        categories.append("lourd")

# 3. Ajout d'une nouvelle colonne
mineraux["Catégorie"] = categories

# Affiche le tableau final
print(mineraux)
```

