+++
pre = "<b>3.</b>"
title = " Saisie au clavier, fonctions et débogage"
weight = 203
draft = false
+++

## Exercice 1 : La loi d'Ohm

```python
# Étape 1 : Demander la résistance à l'utilisateur (en ohms)
resistance = float(input("Entrer la résistance en ohms : "))

# Étape 2 : Demander le courant à l'utilisateur (en ampères)
courant = float(input("Entrer le courant en ampères : "))

# Étape 3 : Calculer la tension à l'aide de la formule U = R * I
tension = resistance * courant

# Étape 4 : Afficher le résultat
print(f"La tension est de {tension} V")
```


### Exercice 2 : Élément chimique

```python
# Demander à l'utilisateur d'entrer le nom d’un élément chimique
element = input("Entrer le nom d'un élément chimique : ")

# Afficher le message avec l’élément choisi
print(f"L’élément choisi est : {element}")
```


### Exercice 3 : Convertir Celsius en Kelvin

```python
# Définition de la fonction
def convertir_C_en_K(celsius):
    kelvin = celsius + 273.15
    return kelvin    # <---- La fonction se termine ici

# Affichage et appel de la fonction
print(f"Une température de 30°C équivaut à {convertir_C_en_K(30)} K")
```


### Exercice 4 : Calculer une énergie cinétique

```python
# Définition de la fonction
def energie_cinetique(m, v):
    return 0.5 * m * v**2

# Affichage et appel de la fonction
print(f"L'énergie cinétique de l'objet est de {energie_cinetique(2.0, 3.0)} joules")  # 9.0 J
```


### Exercice 5 : Aire d'un cercle

```python
import math

def aire_cercle():
    rayon = float(input("Entrez le rayon du cercle (en cm) : "))
    aire = math.pi * rayon ** 2
    aire_arrondie = round(aire, 2)
    print(f"Aire du cercle de rayon {rayon} cm : {aire_arrondie} cm²")

# Appel de la fonction
aire_cercle()
```


### Exercice 6 : Vérifier la portée locale

```python
def tester_variable():
    prenom = "Nathalie"
    print(f"Dans la fonction tu t'appelles : {prenom}")

tester_variable()
print(f"À l'exterieur de la fonction tu t'appelles : {prenom}")  # NameError: name 'prenom' is not defined attendue
```


### Exercice 7 : Trouvez les erreurs et corrigez-les

Voici les erreurs dans **l’ordre d’apparition dans le code**, **corrigées une à une**, avec explications :

**1. `math` n’est pas importé**

**Erreur** : `NameError: name 'math' is not defined`

**Correction** :

```python
import math
```

Ajout en haut du script.

**2. Formule de l’aire latérale incorrecte**

```python
aire_lateral = math.pi * rayon * math.sqrt(rayon**2 + hauteur)
```

**Erreur** : la formule du cône utilise la **génératrice** ℓ, pas `√(rayon² + hauteur)`. Et ici, `hauteur` est encore une **chaîne de caractères** donc cela causera une **erreur de type** plus loin.

Mais avant d'y toucher, corrigeons d’abord l’erreur **suivante plus urgente** :


**3. `rayon` et `hauteur` sont des chaînes de caractères**

**Erreur** : `TypeError: unsupported operand type(s)` quand on tente un calcul mathématique sur des `str`.

**Correction** :

```python
r = float(input("Entrez le rayon du cône: "))
h = float(input("Entrez la hauteur du cône: "))
```

**4. Mauvais calcul de l’aire latérale**

**Erreur mathématique** : La bonne formule est
```math
$$
\text{Aire latérale} = \pi r \ell \quad \text{avec } \ell = \sqrt{r^2 + h^2}
$$
```
**Correction** :

```python
generatrice = math.sqrt(rayon**2 + hauteur**2)
aire_laterale = math.pi * rayon * generatrice
```

**5. Mauvais nom de variable `aire_latérale` au lieu de `aire_lateral`**

**Erreur** : `NameError: name 'aire_latérale' is not defined` (car on utilise un accent non défini)

**Correction** :

```python
surface = aire_base + aire_lateral
```

**6. Format incorrect de la dernière `print()`**

```python
print("La surface totale du cône est de {resultat} cm²")
```

**Erreur** : la chaîne affiche `{resultat}` littéralement.

**Correction** :

```python
print(f"La surface totale du cône est de {resultat:.2f} cm²")
```

(avec f-string et arrondi à 2 décimales)

**Code final corrigé** :

```python
import math

def surface_cone(rayon, hauteur):
    aire_base = math.pi * rayon ** 2
    generatrice = math.sqrt(rayon**2 + hauteur**2)
    aire_laterale = math.pi * rayon * generatrice
    surface = aire_base + aire_laterale
    return surface

r = float(input("Entrez le rayon du cône: "))
h = float(input("Entrez la hauteur du cône: "))

print("Rayon saisi:", r)
print("Hauteur saisie:", h)

resultat = surface_cone(r, h)

print(f"La surface totale du cône est de {resultat:.2f} cm²")
```

 