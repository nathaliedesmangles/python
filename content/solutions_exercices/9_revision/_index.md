+++
pre = "<b>9.</b>"
title = " Révision"
weight = 209
+++


## Exercice 1 : Neutralisation acide-base

```python
import matplotlib.pyplot as plt

volumes = []
ph_values = []

v = 0
while True:
    p = 3 + 4 * (1 - 2.718**(-0.8 * v)) #p = ph(v)
    volumes.append(v)
    ph_values.append(p)
    print(f"Volume = {v:.1f} mL --> pH = {p:.2f}")
    if 6.8 <= p <= 7.2:
        break
    v += 0.5

plt.plot(volumes, ph_values, marker='o')
plt.xlabel("Volume de base (mL)")
plt.ylabel("pH")
plt.title("Titrage acide-base")
plt.grid(True)
plt.show()
```


## Exercice 2 : Désintégration radioactive

```python
import numpy as np
import matplotlib.pyplot as plt

# Données connues
q0 = 100
demivie = 20
temps = np.arange(0, 65, 5)
quantites = []

for t in temps:
    q = q0 * 0.5 ** (t / demivie)
    quantites.append(q)

print("Quantités restantes :", quantites)

# Graphique
plt.plot(temps, quantites, marker='o')
plt.xlabel("Temps (s)")
plt.ylabel("Quantité restante")
plt.title("Désintégration radioactive")
plt.grid(True)
plt.show()
```

### Variante

```python
# Ajout du bruit à la courbe
np.random.seed(1)  # Pour reproductibilité
bruit = np.random.uniform(-0.05, 0.05, len(quantites))
quantites_bruitees = [q * (1 + b) for q, b in zip(quantites, bruit)]

plt.plot(temps, quantites, label="Théorique", marker='o')
plt.plot(temps, quantites_bruitees, label="Avec bruit (±5%)", marker='x')
plt.xlabel("Temps (s)")
plt.ylabel("Quantité restante")
plt.title("Désintégration radioactive (comparaison)")
plt.legend()
plt.grid(True)
plt.show()
```


## Exercice 3 : Titrage par conductimétrie

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("conductivite.csv")
print(df)

plt.plot(df["volume"], df["conductivite"], marker='o')
plt.xlabel("Volume (mL)")
plt.ylabel("Conductivité (µS)")
plt.title("Titrage par conductimétrie")
plt.grid(True)
plt.show()

avant = df[df["volume"] <= 10]
apres = df[df["volume"] >= 11]

pente_avant = (avant["conductivite"].iloc[-1] - avant["conductivite"].iloc[0]) / (avant["volume"].iloc[-1] - avant["volume"].iloc[0])
pente_apres = (apres["conductivite"].iloc[-1] - apres["conductivite"].iloc[0]) / (apres["volume"].iloc[-1] - apres["volume"].iloc[0])

print(f"Pente avant équivalence : {pente_avant:.2f} µS/mL")
print(f"Pente après équivalence : {pente_apres:.2f} µS/mL")
print("Le point d'équivalence est estimé autour de 10-11 mL.")
```

### Variante

```python
# Variante 3
# Trouver les deux points entourant le changement de pente
i = df["conductivite"].diff().abs().argmin()
x1, y1 = df.iloc[i]["volume"], df.iloc[i]["conductivite"]
x2, y2 = df.iloc[i+1]["volume"], df.iloc[i+1]["conductivite"]

# Interpolation linéaire : x_equiv ≈ x1 + ((7 - y1) / (y2 - y1)) * (x2 - x1)
x_eq = x1 + ((y1 - y2) / abs(y1 - y2)) * (x2 - x1) / 2
print(f"Volume équivalent estimé par interpolation : {x_eq:.2f} mL")
```

## Exercice 4 : Loi de Beer-Lambert

```python
import numpy as np
import matplotlib.pyplot as plt

concentrations = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25])
absorbances = np.array([0.00, 0.12, 0.24, 0.36, 0.49, 0.61])

plt.errorbar(concentrations, absorbances, yerr=0.02, fmt='o')
plt.xlabel("Concentration (mol/L)")
plt.ylabel("Absorbance")
plt.title("Loi de Beer-Lambert")
plt.grid(True)
plt.show()

coef = np.polyfit(concentrations, absorbances, 1)
pente, intercept = coef
print(f"y = {pente:.2f}x + {intercept:.2f}")

abs_inconnue = 0.55
conc_inconnue = (abs_inconnue - intercept) / pente
print(f"Concentration estimée : {conc_inconnue:.3f} mol/L")
```

### Variante

Déjà inclus dans la solution de base :
```python
plt.errorbar(concentrations, absorbances, yerr=0.02, fmt='o')
```
Mais si on veut définir les barres d’erreur individuellement :
```python
erreurs = np.array([0.01, 0.02, 0.015, 0.01, 0.02, 0.015])
plt.errorbar(concentrations, absorbances, yerr=erreurs, fmt='o', capsize=5)
```

## Exercice 5 – Croissance d’une plante

```python
import numpy as np
import matplotlib.pyplot as plt

angle = 30
masse = 2.0
mu = 0.2
g = 9.81

theta = np.radians(angle)
f_pente = masse * g * np.sin(theta)
f_friction = mu * masse * g * np.cos(theta)
f_nette = f_pente - f_friction
a = f_nette / masse

print(f"Accélération nette : {a:.2f} m/s²")

positions = [0]
vitesses = [0]
temps = [0]

dt = 0.1
for i in range(1, 101):
    t = i * dt
    v = vitesses[-1] + a * dt
    x = positions[-1] + v * dt
    vitesses.append(v)
    positions.append(x)
    temps.append(t)

plt.plot(temps, positions)
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.title("Mouvement sur une rampe inclinée")
plt.grid(True)
plt.show()
```

### Variante

```python
# Variante 5
# Accélération avec friction
a_friction = a

# Accélération sans friction
a_sans = g * np.sin(theta)

# Trajectoire sans friction
positions_sans = [0]
v_sans = [0]
for i in range(1, 101):
    v = v_sans[-1] + a_sans * dt
    x = positions_sans[-1] + v * dt
    v_sans.append(v)
    positions_sans.append(x)

# Trajectoire avec friction déjà calculée précédemment : positions

# Tracer les deux trajectoires
plt.plot(temps, positions, label="Avec friction")
plt.plot(temps, positions_sans, label="Sans friction", linestyle='--')
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.title("Rampe inclinée : friction vs sans friction")
plt.legend()
plt.grid(True)
plt.show()
```
