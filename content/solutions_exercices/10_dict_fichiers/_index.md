+++
pre = "<b>10.</b>"
title = " Dictionnaires et traitement de fichiers CSV"
weight = 210
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

# 3. Afficher les noms de colonnes
print(df.columns)

# 4. Afficher toutes les températures pour le composé "NaCl"
nacl_temp = df[df["Composé"] == "NaCl"]["Température (°C)"]
print("Températures pour NaCl :")
print(nacl_temp)
```


## Exercice 3 – Moyenne de solubilité

```python
# 1. Moyenne pour KNO3
moy_kno3 = df[df["Composé"] == "KNO3"]["Solubilité (g/100 mL)"].mean()

# 2. Moyenne pour NaCl
moy_nacl = df[df["Composé"] == "NaCl"]["Solubilité (g/100 mL)"].mean()

# 3. Comparaison avec f-strings
print(f"Moyenne de solubilité - KNO3 : {moy_kno3:.2f} g/100 mL")
print(f"Moyenne de solubilité - NaCl : {moy_nacl:.2f} g/100 mL")
```


## Exercice 4 – Boucle sur les composés

```python
# 1. Moyenne pour chaque composé
composés = df["Composé"].unique()

for c in composés:
    moy = df[df["Composé"] == c]["Solubilité (g/100 mL)"].mean()
    
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
df["Tendance"] = df["Solubilité (g/100 mL)"].apply(lambda s: "Haute" if s > 80 else "Faible")

# 2. Affichage des 10 premières lignes
print(df.head(10))
```



