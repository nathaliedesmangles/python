+++
pre = "<b>7.</b>"
title = " Tableaux NumPy et droite de régression"
weight = 307
+++


### Résumé des résultats :

```
Moyenne (Naturelle) = 12.86 cm, écart-type = 0.21 cm  
Moyenne (LED blanche) = 11.40 cm, écart-type = 0.16 cm  
Moyenne (LED rouge) = 10.23 cm, écart-type = 0.12 cm  
Condition avec la plus grande croissance moyenne : Naturelle
```

```python
import numpy as np
import matplotlib.pyplot as plt

# Données avec valeurs manquantes
hauteurs = np.array([
    [12.5, 13.1, 12.9, 13.0, 12.8],
    [11.2, 11.6, np.nan, 11.5, 11.3],
    [10.4, 10.1, 10.2, np.nan, np.nan]
])
conditions = ["Naturelle", "LED blanche", "LED rouge"]

# Moyenne et écart-type en ignorant les NaN
moyennes = np.nanmean(hauteurs, axis=1)
ecarts_type = np.nanstd(hauteurs, axis=1)

# Affichage du résumé
for i in range(3):
    print(f"Moyenne ({conditions[i]}) = {moyennes[i]:.2f} cm, écart-type = {ecarts_type[i]:.2f} cm")

indice_max = np.argmax(moyennes)
print(f"Condition avec la plus grande croissance moyenne : {conditions[indice_max]}")

# Graphique
x = np.arange(len(conditions))
plt.figure(figsize=(8, 5))
plt.bar(x, moyennes, yerr=ecarts_type, capsize=8, color=["green", "gray", "red"])
plt.xticks(x, conditions)
plt.ylabel("Hauteur moyenne (cm)")
plt.title("Effet de la lumière sur la croissance des plantes")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("graphique_croissance_lumiere.png")
plt.show()
```

### Résultat visuel

![Graphique](./graphique_croissance_lumiere.png?width=45vw)