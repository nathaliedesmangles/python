+++
pre = "<b>11.</b>"
title = " Fonctions personnalisées"
weight = 211
+++


## Exercice 1 : La loi d’Ohm

```python
def calculer_tension():
    # Demande la résistance à l'utilisateur
    R = float(input("Entrer la résistance en ohms : "))
    
    # Demande le courant à l'utilisateur
    I = float(input("Entrer le courant en ampères : "))
    
    # Calcule la tension (U = R * I)
    U = R * I

    # Affiche le résultat
    print(f"La tension est de {U} V")

# Appel de la fonction
calculer_tension()
```

---

## Exercice 2 : Élément chimique

```python
def element_chm(elt):
    # Affiche l'élément chimique choisi
    print(f"L’élément choisi est : {elt}")

# Exemple d’appel
element_chm("oxygène")
```

---

## Exercice 3 : Convertir Celsius en Kelvin

```python
def convertir_C_en_K(celsius):
    # Conversion en Kelvin
    kelvin = celsius + 273.15
    
    # Affiche la conversion
    print(f"Une température de {celsius}°C équivaut à {kelvin} K.")

# Exemple d’appel
convertir_C_en_K(30)
```

---

## Exercice 4 : Calculer une énergie cinétique

```python
def energie_cinetique(m, v):
    # Formule : E_c = 0.5 * m * v²
    E = 0.5 * m * v ** 2
    
    # Affiche le résultat
    print(f"L'énergie cinétique de l'objet est de {E} joules.")

# Exemple d’appel
energie_cinetique(2.0, 3.0)
```

---

## Exercice 5 : Aire d’un cercle

```python
import math  # Import du module math pour utiliser pi

def aire_cercle():
    # Demande le rayon
    rayon = float(input("Entrer le rayon du cercle (en cm) : "))
    
    # Calcule l'aire (pi * r²)
    aire = math.pi * rayon ** 2
    
    # Affiche l'aire arrondie à 2 décimales
    print(f"Aire du cercle de rayon {rayon} cm : {round(aire, 2)} cm²")

# Appel de la fonction
aire_cercle()
```

---

## Exercice 6 : Vérifier la portée locale

```python
def tester_variable():
    # Variable locale à la fonction
    prenom = "Nathalie"
    print(f"Dans la fonction tu t'appelles : {prenom}")

# Appel de la fonction
tester_variable()

# Essai d'accès à une variable locale en dehors de sa portée
# Cela provoquera une erreur
print(f"À l'extérieur de la fonction tu t'appelles : {prenom}")
```

**Résultat attendu :**

```text
NameError: name 'prenom' is not defined
```
