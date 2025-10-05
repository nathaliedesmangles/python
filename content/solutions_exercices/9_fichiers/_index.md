+++
pre = "<b>9.</b>"
title = " Lecture et écriture de fichiers de données"
weight = 209
draft = true
+++


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
print("Moyennes enregistrées :", moyennes)
```


## Exercice 2 (NumPy)

```python
import numpy as np

# Lecture du fichier CSV (températures en °C)
temperatures = np.loadtxt("temperatures.csv", delimiter=",")

# Conversion en Kelvin
temperatures_K = temperatures + 273.15

# Sauvegarde en CSV
np.savetxt("temperatures_kelvin.csv", temperatures_K, delimiter=",", fmt="%.2f")
print("Fichier 'temperatures_kelvin.csv' enregistré.")
```

## Exercice 3 (Pandas)

```python
import pandas as pd

df_etudiants = pd.read_csv("students.csv")
print(df_etudiants.head(3))
print(df_etudiants["Note"].describe())
```


## Exercice 4 (Pandas)

```python
import numpy as np

conditions = [
    df_etudiants["Note"] >= 70,
    (df_etudiants["Note"] >= 50) & (df_etudiants["Note"] < 70),
    df_etudiants["Note"] < 50
]
mentions = ["Bien", "Passable", "Échec"]

df_etudiants["Mention"] = np.select(conditions, mentions)
df_etudiants.to_csv("etudiants_mentions.csv", index=False)
print("Fichier 'etudiants_mentions.csv' enregistré.")
```

## Exercice 5 (Pandas)

```python

df = pd.read_csv("experiment.txt", sep="\t")
df.to_csv("experiment_export.txt", sep="\t", index=False)
print("Fichier 'experiment_export.txt' enregistré avec tabulations.")
```
