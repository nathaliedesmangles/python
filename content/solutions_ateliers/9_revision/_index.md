+++
pre = "<b>9.</b>"
title = " Révision"
weight = 309
+++


## Atelier - Étude de la photosynthèse et de la température chez les plantes

### Étape 1 – Lecture et nettoyage des données

```python
import pandas as pd
import numpy as np

# Lecture du fichier CSV
df = pd.read_csv("photosynthese.csv")

# Affichage des 5 premières lignes
print(df.head())

# Nettoyage : suppression des lignes avec valeurs manquantes
df_clean = df.dropna(subset=["Température", "Taux"])

# Conversion en tableaux NumPy
temperature = df_clean["Température"].to_numpy()
taux = df_clean["Taux"].to_numpy()
```

---

### Étape 2 – Analyse par espèce (dictionnaire)

```python
# Création d’un dictionnaire contenant les taux par espèce
donnees_par_espece = {}

for espece in df_clean["Espèce"].unique():
    valeurs = df_clean[df_clean["Espèce"] == espece]["Taux"].to_list()
    donnees_par_espece[espece] = valeurs

# Calcul des statistiques
resume = {}

for espece, liste in donnees_par_espece.items():
    tableau = np.array(liste)
    resume[espece] = {
        "moyenne": np.mean(tableau),
        "ecart_type": np.std(tableau),
        "n": len(tableau)
    }

# Affichage des résultats
for espece, infos in resume.items():
    print(f"{espece} → Moyenne = {infos['moyenne']:.2f}, Écart-type = {infos['ecart_type']:.2f}, N = {infos['n']}")
```

---

### Étape 3 – Analyse graphique (nuage + régression)

```python
import matplotlib.pyplot as plt
from scipy.stats import linregress

plt.figure(figsize=(8, 6))

# Tracé pour chaque espèce
for espece in df_clean["Espèce"].unique():
    sous_df = df_clean[df_clean["Espèce"] == espece]
    x = sous_df["Température"]
    y = sous_df["Taux"]

    # Nuage de points
    plt.scatter(x, y, label=espece)

    # Régression
    slope, intercept, *_ = linregress(x, y)
    x_range = np.linspace(x.min(), x.max(), 100)
    y_fit = slope * x_range + intercept
    plt.plot(x_range, y_fit, linestyle="--")

plt.title("Taux de photosynthèse selon la température")
plt.xlabel("Température (°C)")
plt.ylabel("Taux (μmol CO₂/m²/s)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Sauvegarde
plt.savefig("photosynthese_plot.png")
plt.show()
```

![Photosynthèse-régression](../../semaine9/photosynthese_regression.png?width=45vw)

---

### Étape 4 – Recherche par capteur

```python
nom_capteur = input("Entrez le nom du capteur (ex: capteur-01) : ")

# Recherche dans les données
selection = df_clean[df_clean["Capteur"] == nom_capteur]

if not selection.empty:
    print(selection[["Date", "Température", "Taux", "Espèce"]])
else:
    print("Aucune donnée pour ce capteur.")
```

---

### Étape 5 – Exploration temporelle

```python
# Calcul du taux moyen par date
moyennes_par_date = df_clean.groupby("Date")["Taux"].mean()

print(moyennes_par_date)

# Courbe
moyennes_par_date.plot(marker='o', title="Taux moyen par date")
plt.xlabel("Date")
plt.ylabel("Taux moyen (μmol CO₂/m²/s)")
plt.grid(True)
plt.tight_layout()
plt.show()
```