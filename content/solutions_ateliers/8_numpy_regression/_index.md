+++
pre = "<b>8.</b>"
title = " Tableaux NumPy et droite de régression"
weight = 308
draft = false
+++


## Exercice 1

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

# Moyenne et écart-type en ignorant les données manquantes (NaN)
moyennes = np.nanmean(hauteurs, axis=1)
ecarts_type = np.nanstd(hauteurs, axis=1)

# Affichage du résumé
# Pour chaque hauteur: conditions; moyennes et écarts-type
for i in range(3):
    print(f"Moyenne ({conditions[i]}) = {moyennes[i]:.2f} cm, écart-type = {ecarts_type[i]:.2f} cm")

indice_max = np.argmax(moyennes)
print(f"Condition avec la plus grande croissance moyenne : {conditions[indice_max]}")

# Graphique
x = np.arange(len(conditions))
plt.figure(figsize=(8, 5))

# Traçage du graphique à barres et barres d'erreur
plt.bar(x, moyennes, yerr=ecarts_type, capsize=8, color=["green", "gray", "red"])
plt.xticks(x, conditions)

plt.ylabel("Hauteur moyenne (cm)")
plt.title("Effet de la lumière sur la croissance des plantes")

# Quadrillage horizontal seulement
plt.grid(axis="y") 

# Pour que les paramètres (titre, étiquettes, graduations) 
# s'intègre bien dans la zone de la figure
plt.tight_layout()
	
plt.savefig("graphique_croissance_lumiere.png")
plt.show()
```


## Exercice 2

```python
import numpy as np
import matplotlib.pyplot as plt

# Données expérimentales
temps = np.array([0, 1, 2, 3, 4])
distance = np.array([0, 0.9, 1.8, 2.9, 4.1])

# Régression linéaire (degré 1 = droite)
a, b = np.polyfit(temps, distance, 1)

print(f"Pente a = {a:.2f} m/s")
print(f"Ordonnée à l’origine b = {b:.2f} m")

# Calcul des valeurs prédites par la droite
distance_predite = a * temps + b


# Calcul du coefficient de détermination R²
distance_moy = np.mean(distance)
ss_tot = np.sum((distance - distance_moy)**2)
ss_res = np.sum((distance - distance_predite)**2)
r2 = 1 - (ss_res / ss_tot)
print(f"Coefficient de détermination R² = {r2:.3f}")

# Tracé du graphique
plt.scatter(temps, distance, color='blue', label='Données expérimentales')
plt.plot(temps, distance_predite, color='red', label='Droite de régression')

plt.xlabel("Temps (s)")
plt.ylabel("Distance (m)")
plt.title("Mouvement rectiligne uniforme - Régression linéaire")
plt.legend()
plt.grid(True)
plt.show()
```

**Interprétation scientifique** :

* La pente (1.02 m/s) correspond à la vitesse moyenne du chariot.
* Le R² ≈ 1.0 indique que le mouvement est quasiment parfaitement linéaire, donc le chariot avance à vitesse constante.
* L’ordonnée à l’origine (-0.01 m) est très petite : le chariot part pratiquement du point zéro.