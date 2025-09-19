+++
pre = "<b>8.</b>"
title = " Dictionnaires et fichiers texte"
weight = 208
draft = false
+++


## Exercice 1 – Densités

```python
# Création du dictionnaire
densites = {
    "eau": 1.0,
    "éthanol": 0.789,
    "mercure": 13.6
}

# 1. Affiche la densité du mercure
print(f"Densité du mercure : {densites['mercure']} g/mL")

# 2. Ajout de la densité de l'huile
densites["huile"] = 0.91

# 3. Affiche toutes les substances et leur densité
for substance, densite in densites.items():
    print(f"{substance} : {densite} g/mL")
```


## Exercice 2 – Chargement et exploration

```python
import pandas as pd

# 1. Charger le fichier
df = pd.read_csv("solubilite.csv")

# 2. Afficher les premières lignes
print(df.head())
print(df.head(10))

# 3. Afficher les noms de colonnes
print(df.columns)

# 4. Afficher toutes les températures pour le composé "NaCl"
nacl_temp = df[df["Composé"] == "NaCl"]["Température"]
print("Températures pour NaCl :")
print(nacl_temp)
```


## Exercice 3 – Moyenne de solubilité

```python
# 1. Moyenne pour KNO3
moy_kno3 = df[df["Composé"] == "KNO3"]["Solubilité"].mean()

# 2. Moyenne pour NaCl
moy_nacl = df[df["Composé"] == "NaCl"]["Solubilité"].mean()

# 3. Comparaison avec f-strings
print(f"Moyenne de solubilité - KNO3 : {moy_kno3:.2f} g/100 mL")
print(f"Moyenne de solubilité - NaCl : {moy_nacl:.2f} g/100 mL")
```


## Exercice 4 – Boucle sur les composés

```python
# 1. Moyenne pour chaque composé
composés = df["Composé"].unique()

for c in composés:
    moy = df[df["Composé"] == c]["Solubilité"].mean()
    
    # 2. Vérifier si > 80
    if moy > 80:
        etat = "supérieure à 80"
    else:
        etat = "inférieure ou égale à 80"
        
    print(f"{c} : {moy:.2f} g/100 mL ({etat})")
```


## Exercice 5 – Ajout d’une colonne

```python
# 1. Création de la colonne "Tendance"

# Avec np.where
import numpy as np

df["Tendance"] = np.where(df["Solubilité"] > 80, "Haute", "Faible")

# 2. Affichage des 10 premières lignes
print(df.head(10))
```

### Avec df.loc

```python
# 1. Création de la colonne "Tendance"
df["Tendance"] = "Faible"
df.loc[df["Solubilité"] > 80, "Tendance"] = "Haute"

# 2. Affichage des 10 premières lignes
print(df.head(10))
```
