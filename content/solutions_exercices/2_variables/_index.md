+++
pre = "<b>2.</b>"
title = " Variables, types de données et algorithme"
weight = 202
draft = false
+++

## Exercice 1 : Conversion de température

```python
# 1. Stocker la température en degrés Celsius
temp_celsius = 25  # Exemple : 25 °C

# 2. Convertir en Fahrenheit et en Kelvin
temp_fahrenheit = (temp_celsius * 9/5) + 32
temp_kelvin = temp_celsius + 273.15

# 3. Afficher les trois valeurs avec des messages clairs
print("Température en Celsius :", temp_celsius, "°C")
print("Température en Fahrenheit :", temp_fahrenheit, "°F")
print("Température en Kelvin :", temp_kelvin, "K")
```

## Exercice 2 : Calcul de concentration molaire

```python
# Données connues
m = 10.0   # masse du soluté en grammes
M = 58.5   # masse molaire du soluté en g/mol (ex. NaCl)
V = 0.25   # volume de la solution en litres

# Calcul du nombre de moles
n = m / M

# Calcul de la concentration molaire
C = n / V

# Affichage du résultat
print("Concentration molaire :", C, "mol/L")
```
---

## Exercice 3 : Vitesse moyenne d’une réaction

```python
# données de l'exemple
A_initial = 0.80  # [A] initial en mol/L
A_final   = 0.20  # [A] final en mol/L
t_initial = 0     # temps initial en secondes (optionnel ici)
t_final   = 120   # temps final en secondes

# calcul de la vitesse moyenne
vitesse = (A_final - A_initial) / (t_final - t_initial)

print(f"Vitesse moyenne = {vitesse:.6f} mol L⁻¹ s⁻¹")
```

## Exercice 4 : Distance parcourue

### 1. **Algorithme en phrases**

1. Définir la vitesse en m/s
2. Définir le temps en minutes
3. Convertir le temps en secondes
4. Calculer la distance parcourue avec la formule :
```math
  $$
  d = v \times t
  $$
```
5. Afficher le résultat avec une phrase complète


### 2. **Traduction en Python**

```python
# vitesse en m/s (type: float)
vitesse = 6.5

# temps en minutes (type: int ou float)
temps_minutes = 12

# conversion en secondes
temps_secondes = temps_minutes * 60  # type: int

# calcul de la distance (type: float)
distance = vitesse * temps_secondes

# affichage du résultat
print(f"Le cycliste a parcouru {distance} mètres en {temps_minutes} minutes.")
```


