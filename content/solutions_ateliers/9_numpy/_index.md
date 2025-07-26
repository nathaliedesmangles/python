+++
pre = "<b>9.</b>"
title = " Tableaux NumPy"
weight = 309
+++



```python

import numpy as np

# Étape 1 : Données expérimentales

# np.nan représente les données manquantes

donnees = np.array([
        [12.5, 13.1, 12.9, 13.0, 12.8],         # Naturelle
        [11.2, 11.6, np.nan, 11.5, 11.3],       # LED blanche
        [10.4, 10.1, 10.2, np.nan, np.nan]      # LED rouge
])

conditions = ["Naturelle", "LED blanche", "LED rouge"]

# Étape 2 : Calcul des statistiques

moyennes = np.nanmean(donnees, axis=1)
ecarts_types = np.nanstd(donnees, axis=1)


# Étape 3 : Affichage des résultats

for i in range(len(conditions)):
    print(f"Moyenne ({conditions[i]}) = {moyennes[i]:.2f} cm, écart-type = {ecarts_types[i]:.2f} cm")


# Étape 4 : Comparaison des moyennes

indice_max = np.nanargmax(moyennes)

print(f"Condition avec la plus grande croissance moyenne : {conditions[indice_max]}")
```

