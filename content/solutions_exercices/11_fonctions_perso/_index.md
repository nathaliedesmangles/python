+++
pre = "<b>11.</b>"
title = " Fonctions personnalisées"
weight = 211
draft = false
+++


## Exercice 1 : La loi d’Ohm

```python
def calculer_tension():
    """
    Calcule la tension électrique à partir de la résistance et du courant.

    Demande à l'utilisateur d'entrer la résistance (en ohms) et le courant (en ampères),
    puis applique la loi d'Ohm : U = R * I.

    Affiche la tension calculée à l'écran.

    Exemple :
        >>> calculer_tension()
        Entrer la résistance en ohms : 10
        Entrer le courant en ampères : 2
        La tension est de 20.0 V
    """
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


## Exercice 2 : Élément chimique

```python
def element_chm(elt):
    """
    Affiche le nom d’un élément chimique choisi.

    Args:
        elt (str): Nom ou symbole de l’élément chimique.

    Exemple :
        >>> element_chm("Oxygène")
        L’élément choisi est : Oxygène
    """

    # Affiche l'élément chimique choisi
    print(f"L’élément choisi est : {elt}")

# Exemple d’appel
element_chm("oxygène")
```


## Exercice 3 : Convertir Celsius en Kelvin

```python
def convertir_C_en_K(celsius):
    """
    Convertit une température en degrés Celsius vers Kelvin.

    Formule utilisée : K = °C + 273.15

    Args:
        celsius (float): Température en degrés Celsius.

    Affiche :
        La température équivalente en Kelvin.

    Exemple :
        >>> convertir_C_en_K(25)
        Une température de 25°C équivaut à 298.15 K.
    """

    # Conversion en Kelvin
    kelvin = celsius + 273.15
    
    # Affiche la conversion
    print(f"Une température de {celsius}°C équivaut à {kelvin} K.")

# Exemple d’appel
convertir_C_en_K(30)
```


## Exercice 4 : Calculer une énergie cinétique

```python
def energie_cinetique(m, v):
    """
    Calcule et affiche l'énergie cinétique d'un objet.

    Formule utilisée : E_c = 0.5 * m * v²

    Args:
        m (float): Masse de l’objet en kilogrammes.
        v (float): Vitesse de l’objet en mètres par seconde.

    Affiche :
        L’énergie cinétique en joules.

    Exemple :
        >>> energie_cinetique(2, 3)
        L'énergie cinétique de l'objet est de 9.0 joules.
    """

    # Formule : E_c = 0.5 * m * v²
    E = 0.5 * m * v ** 2
    
    # Affiche le résultat
    print(f"L'énergie cinétique de l'objet est de {E} joules.")

# Exemple d’appel
energie_cinetique(2.0, 3.0)
```


## Exercice 5 : Aire d’un cercle

```python
import math  # Import du module math pour utiliser pi

def aire_cercle():
    """
    Calcule l’aire d’un cercle à partir de son rayon.

    Demande à l’utilisateur le rayon du cercle (en cm), puis calcule l’aire
    selon la formule : Aire = π * r².

    Affiche l’aire arrondie à deux décimales.

    Exemple :
        >>> aire_cercle()
        Entrer le rayon du cercle (en cm) : 3
        Aire du cercle de rayon 3.0 cm : 28.27 cm²
    """

    # Demande le rayon
    rayon = float(input("Entrer le rayon du cercle (en cm) : "))
    
    # Calcule l'aire (pi * r²)
    aire = math.pi * rayon ** 2
    
    # Affiche l'aire arrondie à 2 décimales
    print(f"Aire du cercle de rayon {rayon} cm : {round(aire, 2)} cm²")

# Appel de la fonction
aire_cercle()
```


## Exercice 6 : Vérifier la portée locale

```python
def tester_variable():
    """
    Montre l’utilisation d’une variable locale dans une fonction.

    Définit une variable locale 'prenom' et l’affiche pour illustrer la portée
    des variables (scope) en Python.

    Exemple :
        >>> tester_variable()
        Dans la fonction tu t'appelles : Nathalie
    """
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










