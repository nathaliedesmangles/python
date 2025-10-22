+++
pre = "<b>8.</b>"
title = " Tableaux NumPy et droite de régression"
weight = 208
draft = false
+++


## Exercice 1 – Chute libre verticale et régression linéaire

```python
import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.8
h = 20

# Tableau de temps
t = np.linspace(0, 2, 21)

# Position
y = h - 0.5 * g * t**2

print("5 premières valeurs de y :", y[:5])

# Régression linéaire entre 0.5s et 1.5s
masque = (t >= 0.5) & (t <= 1.5)
pente, ordonnee = np.polyfit(t[masque], y[masque], 1)  # degré 1
droite = pente * t + ordonnee

# Graphique
plt.plot(t, y, 'bo-', label="Chute libre")
plt.plot(t, droite, 'r--', label="Régression linéaire (0.5s-1.5s)")
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.title("Chute libre verticale avec régression locale")
plt.show()
```


## Exercice 2 – Mouvement rectiligne uniforme et régression linéaire

```python
import numpy as np
import matplotlib.pyplot as plt

# Vitesse constante
v = 15  

# Temps de 0 à 10 s
t = np.arange(0, 10.5, 0.5)

# Position
x = v * t

print("Dernière position :", x[-1])

# Régression linéaire
a, b = np.polyfit(t, x, 1)
droite = a * t + b

# Graphique
plt.plot(t, x, 'bo', label="Position calculée")
plt.plot(t, droite, 'r--', label="Régression linéaire")
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.title("Mouvement rectiligne uniforme")
plt.legend()
plt.show()
```


## Exercice 3 – Énergie cinétique et barres d'erreur

```python
import numpy as np
import matplotlib.pyplot as plt

# Masse
m = 2.0

# Tableau des vitesses
v = np.arange(0, 21, 2)

# Énergie cinétique
Ec = 0.5 * m * v**2

print("Énergies cinétiques :", Ec)
print("Énergie maximale :", np.max(Ec))
print("Trois dernières valeurs :", Ec[-3:])
print("Vitesses 2 à 8 m/s :", v[1:5])
print("Énergies correspondantes :", Ec[1:5])

# Barres d’erreur (5 % de la valeur)
erreurs = 0.05 * Ec  

# Graphique à barres
plt.bar(v, Ec, yerr=erreurs, capsize=5, color='skyblue', edgecolor='black')
plt.xlabel("Vitesse (m/s)")
plt.ylabel("Énergie cinétique (J)")
plt.title("Énergie cinétique en fonction de la vitesse")
plt.show()
```



## Exercice 4 – Oscillations harmoniques

```python
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
A = 0.1
omega = 2 * np.pi

# Temps
t = np.linspace(0, 2, 101)

# Position
x = A * np.cos(omega * t)

# Valeurs extrêmes
print("Maximum :", np.max(x))
print("Minimum :", np.min(x))

# Tracé de l’oscillation
plt.plot(t, x, 'b-')
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.title("Oscillations harmoniques")
plt.grid(True)
plt.show()
```
