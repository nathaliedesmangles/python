+++
pre = "<b>3.</b>"
title = " Saisie au clavier, fonctions et débogage"
weight = 303
draft = false
+++


## Exercice #1 : Calcul de la force gravitationnelle

```python
# Demande du nom de l'objet (chaîne de caractères)
nom_objet = input("Entrez le nom de l'objet : ")

# Demande de la masse (nombre décimal)
masse = float(input("Entrez la masse de l'objet en kg : "))

# Déclaration de la constante d'accélération gravitationnelle (en m/s²)
ACCELERATION_GRAVITATIONNELLE = 9.8  # constante en majuscules

# Calcul de la force
force = masse * ACCELERATION_GRAVITATIONNELLE

# Affichage du résultat
print(f"La force de {nom_objet} de {masse:.1f} est de {force:.2f} N.")
```
---

## Exercice #2 : Calcul de la hauteur maximale

```python

# Définition de la fonction pour calculer la hauteur maximale
def hauteur_maximale(vitesse):
    g = 9.81  # accélération gravitationnelle en m/s²
    h = vitesse ** 2 / (2 * g)
    return h

# Saisie de la vitesse initiale (avec conversion en float)
v = float(input("Entrez la vitesse de départ (en m/s) : "))

# Appel de la fonction
hauteur = hauteur_maximale(v)

# Affichage du résultat
print(f"Hauteur maximale : {hauteur} m")

# Affichage arrondi à deux décimales
print(f"Hauteur maximale (arrondie) : {round(hauteur, 2)} m")
```


### Explications

| Ligne              | Erreur                        | Correction          | Explication                                                                             
| ------------------ | ----------------------------- | --------------------| ----------------------------------------- |
| `G = 9,81`         | Virgule au lieu de point      | `g = 9.81`          | En Python, on utilise le point décimal, pas la virgule.                             |
| `vitesse^2`        | Mauvais opérateur d’exponentiation | `vitesse ** 2` | `^` signifie "bitwise XOR", pas "puissance" en Python.|
| `2 * G`            | Variable non définie (majuscule)   | `2 * g`        | Python est sensible à la casse : `G ≠ g`.  |
| `input()` non converti       | `v = input(...)`         | `v = float(input(...))` | `input()` renvoie une chaîne de caractères. Il faut la convertir en nombre.   |