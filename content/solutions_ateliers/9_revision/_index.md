+++
pre = "<b>9.</b>"
title = " Révision"
weight = 309
+++

```python
### Étape 1 — Charger les données
import pandas as pd

df = pd.read_csv("photosynthese.csv")
print(df.head())
```

### Étape 2 — Visualiser les courbes

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("photosynthese.csv")

# Étape 1 : Calcul des moyennes et écarts types
groupes = df.groupby(["Espèce", "Température"])["Taux"]
stats = groupes.agg(["mean", "std"]).reset_index()

# Étape 2 : Création du graphique avec barres d'erreur
especes = stats["Espèce"].unique()
plt.figure(figsize=(10, 6))

for espece in especes:
    sous_df = stats[stats["Espèce"] == espece]
    x = sous_df["Température"]
    y = sous_df["mean"]
    yerr = sous_df["std"]
    plt.errorbar(x, y, yerr=yerr, label=espece, capsize=5, marker='o', linestyle='--')

plt.title("Taux de photosynthèse en fonction de la température")
plt.xlabel("Température (°C)")
plt.ylabel("Taux de photosynthèse (µmol CO₂/m²/s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graphique_photosynthese.png")
plt.show()

# Étape 3 : Calcul de la pente entre 15 °C et 25 °C pour chaque espèce
pentes = {}
for espece in especes:
    sous_df = df[(df["Espèce"] == espece) & (df["Température"].isin([15, 25]))]
    moyennes = sous_df.groupby("Température")["Taux"].mean()

    if len(moyennes) == 2:
        t1, t2 = moyennes.index
        p1, p2 = moyennes.values
        pente = (p2 - p1) / (t2 - t1)
        pentes[espece] = pente
    else:
        print(f"Données insuffisantes pour l'espèce '{espece}' pour calculer la pente.")

# Étape 4 : Identifier l’espèce avec la plus grande pente
if pentes:
    espece_max = max(pentes, key=pentes.get)
    pente_max = pentes[espece_max]

    # Étape 5 : Conclusion
    print(f"\nEspèce avec la plus forte augmentation du taux de photosynthèse entre 15°C et 25°C : {espece_max}")
    print(f"Pente moyenne observée : {pente_max:.2f} µmol CO₂/m²/s/°C")
else:
    print("Aucune espèce avec données suffisantes pour comparer 15°C à 25°C.")
```


