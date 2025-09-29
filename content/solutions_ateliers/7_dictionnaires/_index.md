+++
pre = "7."
title = " Dictionnaires"
weight = 307
draft = false
+++

## Exercice - Physique

```python
import matplotlib.pyplot as plt

# Constante gravitationnelle
g = 9.8  

# Création des dictionnaires
vitesses = {}
positions = {}

for t in range(6):  # temps de 0 à 5
    vitesses[t] = g * t
    positions[t] = 0.5 * g * (t**2)

print("Vitesses :", vitesses)
print("Positions :", positions)

# Préparation des données pour les graphiques
temps = list(vitesses.keys())
valeurs_v = list(vitesses.values())
valeurs_y = list(positions.values())

# Tracé des graphes
plt.plot(temps, valeurs_v, "ro-", label="Vitesse (m/s)")
plt.plot(temps, valeurs_y, "bo-", label="Position (m)")

plt.title("Chute libre (sans frottement)")
plt.xlabel("Temps (s)")
plt.ylabel("Valeurs physiques")
plt.legend()
plt.grid(True)
plt.savefig("chute_libre.png")
plt.show()
```

## Exercice - Mathématiques

```python
import matplotlib.pyplot as plt

# Création des dictionnaires
carres = {}
derivees = {}

for x in range(-5, 6):  # de -5 à +5
    carres[x] = x**2
    derivees[x] = 2*x

print("Carrés :", carres)
print("Dérivées :", derivees)

# Préparation des données pour les graphiques
x_vals = list(carres.keys())
y_carres = list(carres.values())
y_derivees = list(derivees.values())

# Tracé des graphes
plt.plot(x_vals, y_carres, "bo-", label="f(x) = x^2")
plt.plot(x_vals, y_derivees, "ro-", label="f'(x) = 2x")

plt.title("Fonction quadratique et sa dérivée")
plt.xlabel("x")
plt.ylabel("Valeurs")
plt.legend()
plt.grid(True)
plt.savefig("quadratique.png")
plt.show()
```