+++
pre = "<b>4.</b>"
title = " Fonctions"
weight = 204
+++

## Exercice 1 - Élément chimique

Écrire une fonction `element_chimique()` qui :
* Demande à l'utilisateur d'entrer le nom d’un élément chimique.
* Affiche un message disant "L’élément choisi est \[nom]"

**Solution :**

```python
def element_chimique():
   element = input("Entrez le nom d'un élément chimique : "))
   print("L’élément choisi est", element)

# Appel de la fonction
element_chimique()
```

## Exercice 2 - Aire d'un cercle

1. Écrire une fonction `aire_cercle()` qui :
   * demande à l'utilisateur d'entrer le rayon du cercle (en cm).
   * calcule l'aire du cercle (utiliser le **module math** pour PI et le rayon².)
   * affiche l'aire du cercle, arrondie à 2 décimales (utiliser la fonction `round`).

**Exemple d'affichage attendu (rayon de 5 cm)** :
```python
Aire du cercle de rayon 5 cm : 78.54 cm²
```

**Solution :**

```python
import math

def aire_cercle():
   r = float(input("Entrez le rayon du cercle : "))
   aire = math.pi * math.pow(r, 2)
   print("Aire du cercle :", round(aire, 2), "cm²")

# Appel de la fonction
aire_cercle()
```

## Exercice 3 - Convertir Celsius en Kelvin

Crée une fonction nommée `convertir_C_en_K` qui :

* prend une température en °C en paramètre.
* retourne la température en Kelvin (formule : K = C + 273.15)

**Solution :**

```python
def convertir_C_en_K(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Appel de la fonction
print(convertir_C_en_K(25))  # 298.15
```

## Exercice 4 – Calculer une énergie cinétique

Crée une fonction `energie_cinetique(m, v)` qui calcule :

```math
$E_c = \frac{1}{2} \cdot m \cdot v^2$
```
**Solution :**

```python
def energie_cinetique(m, v):
    return 0.5 * m * v**2

# Appel de la fonction
print(energie_cinetique(2.0, 3.0))  # 9.0
```

## Exercice 5 – Vérifier la portée locale

Crée une fonction `tester_variable()` qui crée une variable `x = 10` et l’affiche dans la fonction.
Essaye ensuite d’afficher `x` **à l’extérieur de la fonction**.

**Solution :**

```python
def tester_variable():
    x = 10
    print("Dans la fonction :", x)

# Appel de la fonction
tester_variable()
print("À l’extérieur :", x)  # Erreur attendue
```