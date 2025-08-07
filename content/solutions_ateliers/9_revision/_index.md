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
import matplotlib.pyplot as plt

especes = df["espece"].unique()

for espece in especes:
    sous_df = df[df["espece"] == espece]
    plt.plot(sous_df["temperature"], sous_df["taux_photosynthese"], marker='o', label=f"Espèce {espece}")

plt.xlabel("Température (°C)")
plt.ylabel("Taux de photosynthèse (µmol CO₂/m²/s)")
plt.title("Taux de photosynthèse selon la température")
plt.legend()
plt.grid()
plt.show()
```

### Étape 3 — Trouver la température optimale par espèce

```python
for espece in especes:
    sous_df = df[df["espece"] == espece]
    idx_max = sous_df["taux_photosynthese"].idxmax()
    temp_opt = sous_df.loc[idx_max, "temperature"]
    print(f"Température optimale pour l'espèce {espece} : {temp_opt} °C")
```

### Étape 4 — Calculer la pente moyenne entre 15 °C et 25 °C

Cela donne une idée de la **sensibilité** de la photosynthèse à l’augmentation de température entre 15 °C et 25 °C.

```python
for espece in especes:
    sous_df = df[(df["espece"] == espece) & (df["temperature"].isin([15, 25]))]
    t1, t2 = sous_df["temperature"].values
    p1, p2 = sous_df["taux_photosynthese"].values
    pente = (p2 - p1) / (t2 - t1)
    print(f"Pente moyenne 15-25 °C pour espèce {espece} : {pente:.2f} µmol CO₂/m²/s/°C")
```


### Étape 5 — Ajuster une régression linéaire simple avec NumPy (sans SciPy)

```python
import numpy as np

for espece in especes:
    sous_df = df[df["espece"] == espece]
    x = sous_df["temperature"].values
    y = sous_df["taux_photosynthese"].values
    
    # Ajustement linéaire
    a, b = np.polyfit(x, y, deg=1)
    print(f"Espèce {espece} : y = {a:.2f}x + {b:.2f}")
    
    # Tracé
    plt.plot(x, y, 'o', label=f"Espèce {espece}")
    plt.plot(x, a*x + b, '--', label=f"Régression {espece}")

plt.xlabel("Température (°C)")
plt.ylabel("Taux de photosynthèse (µmol CO₂/m²/s)")
plt.title("Régression linéaire (approximation)")
plt.legend()
plt.grid()
plt.show()
```

### Interprétation

* L'espèce **A** atteint un maximum à **25 °C**, puis son efficacité décroît.
* L'espèce **B** est plus tolérante à la chaleur et performe encore à 35 °C.
* L'espèce **C** a un taux plus faible, mais réagit de façon similaire à A.


