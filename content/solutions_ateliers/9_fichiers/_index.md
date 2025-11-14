+++
pre = "<b>9.</b>"
title = " Lecture et écriture de fichiers de données"
weight = 309
draft = false
+++

```python
import numpy as np
import pandas as pd

# PARTIE 1 — Lecture et nettoyage avec pandas

# Lecture du fichier CSV "eau_riviere.csv"
df = pd.read_csv("eau_riviere.csv")

print()
print("Données initiales (pandas)")
print(df)

# Détection des valeurs manquantes
print()
print("Valeurs manquantes par colonne")
print(df.isna().sum())

# Remplacement des valeurs manquantes par la moyenne de la colonne
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["pH"] = df["pH"].fillna(df["pH"].mean())
df["Oxygene"] = df["Oxygene"].fillna(df["Oxygene"].mean())

# OU pour tout le DataFrame d’un coup
# df = df.fillna(df.mean(numeric_only=True))

print()
print("Données après remplissage des NaN")
print(df)


# Ajout de la colonne 'Qualite' selon la concentration en oxygène
# Règles :
# - Oxygène >= 8.0 → "Bonne"
# - 7.5 <= Oxygène < 8.0 → "Moyenne"
# - Oxygène < 7.5 → "Faible"

df["Qualite"] = np.where(
    df["Oxygene"] >= 8.0, "Bonne",
    np.where(
        (df["Oxygene"] >= 7.5) & (df["Oxygene"] < 8.0), "Moyenne",
        "Faible"
    )
)


# Ajout de la colonne 'Alerte' selon le pH
# Si pH < 7.0 → "Attention", sinon "OK"

df["Alerte"] = np.where(df["pH"] < 7.0, "Attention", "OK")

print()
print("Données finales avec colonnes dérivées")
print(df)


# Sauvegarde finale du fichier nettoyé
df.to_csv("eau_riviere_nettoyee.csv", index=False)
print()
print("Fichier 'eau_riviere_nettoyee.csv' sauvegardé avec succès.")



# PARTIE 2 — Visualisation graphique (Optionnel)

import matplotlib.pyplot as plt

# Graphique 1
erreur = 0.2
couleurs = df["Qualite"].map({"Bonne": "skyblue", "Moyenne": "gold", "Faible": "salmon"})

plt.bar(df["Site"], df["Oxygene"], yerr=erreur, capsize=5, color=couleurs)
plt.title("Concentration en oxygène dissous dans la rivière")
plt.xlabel("Site d'échantillonnage")
plt.ylabel("Oxygène (mg/L)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


# Graphique 2
plt.scatter(df["Site"], df["Oxygene"])
plt.title("Concentration en oxygène dissous dans la rivière")
plt.xlabel("Site d'échantillonnage")
plt.ylabel("Oxygène (mg/L)")
plt.grid()
plt.show()
```


---

## Que fait `.map()` en pandas ?

La méthode **`.map()`** permet de **remplacer les valeurs d’une série** selon un *dictionnaire de correspondance*.
Elle prend chaque valeur d’une colonne et la transforme selon les règles définies.

Exemple :

```python
couleurs = df["Qualite"].map({"Bonne": "skyblue",
                              "Moyenne": "gold",
                              "Faible": "salmon"})
```

Pour chaque ligne :

| Valeur dans `Qualite` | Devient                             |
| --------------------- | ----------------------------------- |
| `"Bonne"`             | `"skyblue"`                         |
| `"Moyenne"`           | `"gold"`                            |
| `"Faible"`            | `"salmon"`                          |
| autre chose           | `NaN` (car non prévue dans le dict) |

Utile pour :

* remplacer des valeurs textuelles par des étiquettes
* transformer des catégories en nombres
* assigner des couleurs pour un graphique (comme ici)



## Comment faire la même chose **sans `.map()`**

### 1. Avec une **boucle**

```python
couleurs = []

for q in df["Qualite"]:
    if q == "Bonne":
        couleurs.append("skyblue")
    elif q == "Moyenne":
        couleurs.append("gold")
    elif q == "Faible":
        couleurs.append("salmon")
    else:
        couleurs.append(None)   # équivalent de NaN
```


### 2. Avec **np.where()**

```python
import numpy as np

couleurs = np.where(df["Qualite"] == "Bonne", "skyblue",
            np.where(df["Qualite"] == "Moyenne", "gold",
            np.where(df["Qualite"] == "Faible", "salmon", None)))
```


### 3. Avec `replace()`

```python
couleurs = df["Qualite"].replace({
    "Bonne": "skyblue",
    "Moyenne": "gold",
    "Faible": "salmon"
})
```

**Avantage** : garde les autres valeurs intactes (pas transformées en NaN).



