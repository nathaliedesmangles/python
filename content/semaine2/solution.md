+++
title = "Solution"
weight = 22
draft = true
+++

## Exercice 1 : conversion de température

```python
# Entrez  la température en Celsius
temp_c = float(input("Entrez la température en Celsius : "))

# Conversion de la température en Fahrenheit et en Kelvin
temp_f = (temp_c * 9/5) + 32
temp_k = temp_c + 273.15

# Affichage des résultats
print("Température en Celsius :", temp_c, "°C")
print("Température en Fahrenheit :", temp_f, "°F")
print("Température en Kelvin :", temp_k, "K")
```

## Exercice 2 : La loi d'Ohm

```python
# Entrez la résistance et le courant
resistance = float(input("Entrer la résistance en ohms : "))	# Conversion nécessaire
courant = float(input("Entrer le courant en ampères : "))	# Conversion nécessaire

# Calcul de la tension selon la loi d’Ohm
tension = courant * resistance

# Affichage du résultat
print("La tension est de " + tension + " V")
```

## Exercice 3 : Calcul de concentration molaire

```python
# Entrer la masse, la masse molaire et le volume
masse = float(input("Masse du soluté (g) : "))
masse_molaire = float(input("Masse molaire (g/mol) : "))
volume = float(input("Volume de solution (L) : "))

# Calculs et traitement du résultat
n = masse / masse_molaire
if volume != 0:
    concentration = n / volume
    print(f"Concentration : {concentration:.3f} mol/L")
else:
    print("Erreur : le volume ne peut pas être zéro.")
```

## Exercice 4 : Vitesse moyenne d’une réaction

```python
# Entrer les concentrations initiale et finale
concentration_initiale = float(input("Concentration initiale (mol/L) : "))
concentration_finale = float(input("Concentration finale (mol/L) : "))
temps = float(input("Temps écoulé (s) : "))

# Calcul et traitement des résultats
variation_concentration = concentration_initiale - concentration_finale
if temps != 0:
    vitesse = variation_concentration / temps
    print(f"Vitesse moyenne : {vitesse:.5f} mol/(L·s)")
else:
    print("Erreur : le temps ne peut pas être zéro.")
```
