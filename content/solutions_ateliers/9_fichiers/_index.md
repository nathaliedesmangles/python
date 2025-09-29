+++
pre = "<b>9.</b>"
title = " Lecture et écriture de fichiers de données"
weight = 309
draft = true
+++

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Étape 1 - Lecture
df = pd.read_csv("croissance_algues.csv")

# Vérifier les NaN
print(df.isna().sum())
df = df.dropna()

# Conversion NumPy
temperatures = df["Température"].to_numpy()
taux = df["Taux"].to_numpy()

# Étape 2 - Analyse par espèce
donnees_par_espece = {}

for _, ligne in df.iterrows():
    espece = ligne["Espèce"]
    taux_val = ligne["Taux"]
    if espece not in donnees_par_espece:
        donnees_par_espece[espece] = []
    donnees_par_espece[espece].append(taux_val)

resume = {}
for espece, valeurs in donnees_par_espece.items():
    valeurs_np = np.array(valeurs)
    resume[espece] = {
        "nb": len(valeurs),
        "moyenne": np.mean(valeurs_np),
        "ecart_type": np.std(valeurs_np)
    }

print("Résumé par espèce :")
for espece, stats in resume.items():
    print(f"{espece} -> {stats}")

# Étape 3 - Graphique
plt.figure(figsize=(8,6))

especes = df["Espèce"].unique()
for espece in especes:
    sous_df = df[df["Espèce"] == espece]
    x = sous_df["Température"].to_numpy()
    y = sous_df["Taux"].to_numpy()
    plt.scatter(x, y, label=f"{espece} (données)")

    # Régression linéaire
    coeffs = np.polyfit(x, y, deg=1)
    y_pred = np.polyval(coeffs, x)
    plt.plot(x, y_pred, linestyle="--", label=f"{espece} (régression)")

plt.title("Taux de croissance vs Température")
plt.xlabel("Température (°C)")
plt.ylabel("Taux de croissance (mm/jour)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("croissance_regression.png")
plt.show()

# Étape 4 - Recherche capteur
nom_capteur = input("Entrez le nom du capteur : ")
filtre = df[df["Capteur"] == nom_capteur]

if filtre.empty:
    print("Aucune donnée pour ce capteur.")
else:
    print("Mesures associées :")
    for _, ligne in filtre.iterrows():
        print(f"{ligne['Date']} | {ligne['Espèce']} | {ligne['Température']} °C | {ligne['Taux']} mm/jour")
```


