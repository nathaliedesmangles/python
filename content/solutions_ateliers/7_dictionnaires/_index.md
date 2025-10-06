+++
pre = "7."
title = " Dictionnaires"
weight = 307
draft = false
+++

## Exercice - Physique


```python
import matplotlib.pyplot as plt

# 1. Constante gravitationnelle
g = 9.8  # m/s²

# 2. Création des dictionnaires
vitesses = {}
positions = {}

# 3. Remplir les dictionnaires avec les formules physiques
for t in range(6):  # de 0 à 5 secondes
    vitesses[t] = g * t
    positions[t] = 0.5 * g * (t**2)

# 4. Vérifier le contenu
print("Vitesses :", vitesses)
print("Positions :", positions)
```

**Résultat attendu :**
```
Vitesses : {0: 0.0, 1: 9.8, 2: 19.6, 3: 29.4, 4: 39.2, 5: 49.0}
Positions : {0: 0.0, 1: 4.9, 2: 19.6, 3: 44.1, 4: 78.4, 5: 122.5}
```

### 5. Préparation des données pour les graphiques

```python
# Clés triées pour garantir l'ordre
temps = sorted(vitesses.keys())

# Extraction des valeurs à partir des clés triées
valeurs_v = [vitesses[t] for t in temps]
valeurs_y = [positions[t] for t in temps]
```

*(Remarque : on aurait aussi pu utiliser `list(vitesses.values())` directement, mais ici on garantit que les deux listes suivent exactement le même ordre.)*


### 6. Tracé des courbes

```python
# Tracé de la vitesse et de la position
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

### 7. Interprétation

* La **pente de la courbe v(t)** est constante : la vitesse augmente **linéairement** avec le temps. Cela signifie que l’accélération est **constante** (ici égale à `g` = 9,8 m/s²).
* La **courbe y(t)** est **parabolique** : la position augmente de plus en plus vite, car l’objet accélère.
* En résumé, la vitesse croit à un rythme constant, et la position croît **quadratiquement** au fil du temps.


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