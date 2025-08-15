+++
pre = "<b>2.</b>"
title = " Variables, types, entrées et fonctions"
weight = 202
draft = true
+++


### **Exercice 1 : Distance parcourue**

```python
# Données
vitesse = 6.5  # en m/s
temps_minutes = 12

# Conversion du temps en secondes
temps_secondes = temps_minutes * 60

# Calcul de la distance
distance = vitesse * temps_secondes

# Affichage
print(f"Le cycliste a parcouru {distance} mètres en {temps_minutes} minutes.")
```

**Résultat :**

```
Le cycliste a parcouru 4680.0 mètres en 12 minutes.
```

---

### **Exercice 2 : Conversion de température**

```python
# Donnée
temperature_celsius = 38

# Conversions
temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32
temperature_kelvin = temperature_celsius + 273.15

# Affichage
print(f"Température en Celsius : {temperature_celsius}°C")
print(f"Température en Fahrenheit : {temperature_fahrenheit}°F")
print(f"Température en Kelvin : {temperature_kelvin}K")
```

**Résultat :**

```
Température en Celsius : 38°C
Température en Fahrenheit : 100.4°F
Température en Kelvin : 311.15K
```

---

### **Exercice 3 : Calcul de concentration molaire**

```python
# Données
masse = 10.0      # en g
masse_molaire = 58.5  # en g/mol
volume = 0.25     # en L

# Calcul du nombre de moles
n = masse / masse_molaire

# Calcul de la concentration
concentration = n / volume

# Affichage
print(f"Concentration molaire : {concentration} mol/L")
```

**Résultat :**

```
Concentration molaire : 0.682051282051282 mol/L
```

---

### **Exercice 4 : Vitesse moyenne d’une réaction**

```python
# Données
concentration_initiale = 0.80  # mol/L
concentration_finale = 0.20    # mol/L
temps = 120  # en secondes

# Calcul de la variation de concentration
delta_concentration = concentration_finale - concentration_initiale

# Calcul de la vitesse moyenne
vitesse_moyenne = delta_concentration / temps

# Affichage
print(f"Vitesse moyenne = {vitesse_moyenne:.6f} mol L⁻¹ s⁻¹")
```

**Résultat :**

```
Vitesse moyenne = -0.005000 mol L⁻¹ s⁻¹
```