+++
pre = "<b>7.</b>"
title = " Tableaux NumPy et droite de régression"
weight = 207
draft = false
+++


## Exercice 1 – Solubilité d’un sel

```python
import numpy as np

sol = np.array([32.0, 35.5, np.nan, 37.2, 39.0])

# 1. Affiche les valeurs de solubilité
print("Solubilités :", sol)

# 2. Moyenne sans NaN
moyenne = np.nanmean(sol)
print("Moyenne sans NaN :", moyenne)

# 3. Écart type
ecart_type = np.nanstd(sol)
print(f"Écart type : {round(ecart_type,2)}" )
```


## Exercice 2 – Températures journalières

```python
temperatures = np.array([
    [12.1, 17.3, 14.2],
    [11.8, 16.9, 13.9],
    [13.0, 18.1, 15.0],
    [12.5, 17.5, 14.7],
    [np.nan, 16.0, 14.0],
    [13.2, 18.0, 15.2],
    [12.0, 17.0, 14.5]
])

# 1. Forme du tableau
print(f"Forme : {temperatures.shape}")

# 2. Moyenne journalière par ligne (axis=1)
moyennes_journalieres = np.nanmean(temperatures, axis=1)
print(f"Moyennes journalières : {moyennes_journalieres}")

# 3. Moyenne des températures du matin (colonne 0), sans NaN
moyenne_matin = np.nanmean(temperatures[:, 0])
print(f"Moyenne du matin : {moyenne_matin}")
```


## Exercice 3 – Analyse d’ADN

```python
ech1 = np.array([3.2, 2.8, 4.1, 3.9, 2.5])
ech2 = np.array([2.9, 3.0, 4.2, 4.0, 2.7])

# 1. Profil combiné
profil_combine = ech1 + ech2
print("Profil combiné :", profil_combine)

# 2. Différence
difference = ech1 - ech2
print("Différence :", difference)

# 3. Moyennes et écarts types
print(f"Moyenne éch1 : {round(np.mean(ech1),2)}")
print(f"Écart type éch1 : {round(np.std(ech1),2)}")

print(f"Moyenne éch2 : {round(np.mean(ech2),2)}")
print(f"Écart type éch2 : {round(np.std(ech2),2)}")
```


## Exercice 4 – Pressions dans un cylindre (avec graphique)

```python
import numpy as np
import matplotlib.pyplot as plt

# Données
hauteur = np.linspace(0, 50, 6)  # [0, 10, 20, 30, 40, 50]
pression = np.array([101.3, 100.0, 98.7, 97.5, 96.2, 95.0])

# 1. Affiche les hauteurs et les pressions
print(f"Hauteur (cm) : {hauteur}" )
print(f"Pression (kPa) : {pression}")

# 2. Variation de pression par tranche de 10 cm
variation = np.diff(pression)  # différences successives
print(f"Variation de pression par 10 cm : {variation}")

# 3. Moyenne de pression
moyenne_pression = np.mean(pression)
print(f"Moyenne de pression : {round(moyenne_pression,2)} kPa")

# 4. Régression linéaire pour Pression = a*Hauteur + b
a, b = np.polyfit(hauteur, pression, 1)

# Tracé
plt.scatter(hauteur, pression, label="Mesures", color="blue")
plt.plot(hauteur, a*hauteur + b, label=f"Régression linéaire: y={a:.2f}x+{b:.2f}", color="red")
plt.xlabel("Hauteur (cm)")
plt.ylabel("Pression (kPa)")
plt.title("Pression en fonction de la hauteur")
plt.legend()
plt.grid(True)
plt.savefig("graphique_pression_regression.png")
plt.show()
```

### Points notables

* `np.diff()` calcule directement les variations successives.
* La régression linéaire avec `np.polyfit(x, y, 1)` donne la **pente a** et **l’ordonnée à l’origine b**.



## Exercice 5 – Croissance d’une plante

```python
# 1. Tableau de la taille de la plante pendant 10 jours (sans engrais)
jours = np.arange(0, 10)  # Jours 0 à 9
taille_sans_engrais = 5 + 2 * jours

# 2. Ajout de 1 cm supplémentaire (avec engrais)
taille_avec_engrais = taille_sans_engrais + 1

# 3. Moyennes
moyenne_sans = np.mean(taille_sans_engrais)
moyenne_avec = np.mean(taille_avec_engrais)

print(f"Taille sans engrais : {taille_sans_engrais}")
print(f"Taille avec engrais : {taille_avec_engrais}")
print(f"Moyenne sans engrais : {moyenne_sans} cm")
print(f"Moyenne avec engrais : {moyenne_avec} cm")
```

### Point notable

* l’utilisation de `np.arange()` permet de générer les jours facilement, et la croissance est calculée par formule.
