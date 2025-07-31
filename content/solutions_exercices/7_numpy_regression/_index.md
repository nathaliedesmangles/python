+++
pre = "<b>7.</b>"
title = " Tableaux NumPy et droite de régression"
weight = 207
+++


### Exercice 1 – Solubilité d’un sel

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
print("Écart type :", ecart_type)
```

---

### Exercice 2 – Températures journalières

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
print("Forme :", temperatures.shape)

# 2. Moyenne journalière par ligne (axis=1)
moyennes_journalières = np.nanmean(temperatures, axis=1)
print("Moyennes journalières :", moyennes_journalières)

# 3. Moyenne des températures du matin (colonne 0), sans NaN
moyenne_matin = np.nanmean(temperatures[:, 0])
print("Moyenne du matin :", moyenne_matin)
```

---

### Exercice 3 – Analyse d’ADN

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
print("Moyenne éch1 :", np.mean(ech1))
print("Écart type éch1 :", np.std(ech1))

print("Moyenne éch2 :", np.mean(ech2))
print("Écart type éch2 :", np.std(ech2))
```

---

### Exercice 4 – Pressions dans un cylindre

Voici la **solution complète de l’exercice 4 – Pressions dans un cylindre**, incluant le **calcul**, l’**affichage**, et la **visualisation graphique avec une droite de régression linéaire** :

---

### ✅ Exercice 4 – Pressions dans un cylindre (avec graphique)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Données de l'exercice
hauteur = np.linspace(0, 50, 6)  # [0, 10, 20, 30, 40, 50]
pression = np.array([101.3, 100.0, 98.7, 97.5, 96.2, 95.0])

# 1. Affichage des hauteurs et des pressions
print("Hauteurs (cm) :", hauteur)
print("Pressions (kPa) :", pression)

# 2. Variation de pression par tranche de 10 cm
variation = np.diff(pression)
print("Variation de pression (chaque 10 cm) :", variation)

# 3. Moyenne de la pression
moyenne = np.mean(pression)
print("Pression moyenne :", moyenne)

# 4. Régression linéaire (pression en fonction de la hauteur)
slope, intercept, r_value, p_value, std_err = linregress(hauteur, pression)
pression_modele = slope * hauteur + intercept

print(f"Pente de la régression : {slope:.3f} kPa/cm")
print(f"Ordonnée à l'origine : {intercept:.3f} kPa")
print(f"Coefficient de corrélation r : {r_value:.3f}")

# 5. Graphique avec données et droite de régression
plt.figure(figsize=(8, 5))
plt.plot(hauteur, pression, 'o', label="Données mesurées", color='blue')
plt.plot(hauteur, pression_modele, '-', label=f"Régression linéaire\n(pente = {slope:.2f})", color='red')
plt.xlabel("Hauteur (cm)")
plt.ylabel("Pression (kPa)")
plt.title("Pression en fonction de la hauteur")
plt.grid(True)
plt.legend()
plt.savefig("graphique_pression_regression.png")
plt.show()
```

### Résultat visuel :

![Graphique](./graphique_pression_regression.png?width=45vw)

Le graphique généré affiche :

* les points mesurés (ronds bleus),
* la droite de régression (ligne rouge),
* une légende et des axes clairs.

---

### Exercice 5 – Croissance d’une plante

```python
# 1. Croissance sans engrais
jours = np.arange(10)
taille = 5 + jours * 2
print("Taille sans engrais :", taille)

# 2. Avec engrais (+1 cm)
taille_engrais = taille + 1
print("Taille avec engrais :", taille_engrais)

# 3. Moyennes
print("Moyenne sans engrais :", np.mean(taille))
print("Moyenne avec engrais :", np.mean(taille_engrais))
```

