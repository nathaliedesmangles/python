+++
pre = "6."
title = " Listes, chaines et visualisation des données"
weight = 306
draft = false
+++


```python
import matplotlib.pyplot as plt

# Données
temperatures = [
    [15, 16, 14, 14, 17, 18, 19],  # Ville A
    [22, 23, 21, 20, 24, 25, 26],  # Ville B
    [5, 7, 6, 6, 8, 9, 7],         # Ville C
    [10, 11, 12, 10, 13, 14, 15]   # Ville D
]

villes = ["Ville A", "Ville B", "Ville C", "Ville D"]
jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

# 1. Affichage des températures
for i in range(len(villes)):
    print(villes[i], ":", end=" ")
    for j in range(len(temperatures[i])):
        print(temperatures[i][j], end=" ")
    print()  # retour à la ligne

# 2. Min et max
for i in range(len(villes)):
    tmax = max(temperatures[i])
    tmin = min(temperatures[i])
    print(f"La température maximale de {villes[i]} est {tmax} °C")
    print(f"La température minimale de {villes[i]} est {tmin} °C")

# 3. Classification des températures
for i in range(len(villes)):
    print(f"\nClassification pour {villes[i]} :")
    for j in range(len(temperatures[i])):
        t = temperatures[i][j]
        if t < 10:
            print(t, "=> Froide")
        elif 10 <= t <= 20:
            print(t, "=> Douce")
        else:
            print(t, "=> Chaud")

# 4. Graphique
for i in range(len(villes)):
    plt.plot(jours, temperatures[i], label=villes[i])

plt.title("Températures hebdomadaires")
plt.xlabel("Jour")
plt.ylabel("Température (°C)")
plt.grid(True)
plt.legend()
plt.savefig("temperatures.png")
plt.show()
```

