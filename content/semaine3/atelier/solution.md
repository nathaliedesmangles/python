+++
title = "Solution"
weight = 31
draft = true
+++


## Exercice 1 – Traduire un algorithme

```python
distance = float(input("Entrez la distance parcourue (en mètres) : "))
temps = float(input("Entrez le temps écoulé (en secondes) : "))
vitesse = distance / temps
print("La vitesse moyenne est de", round(vitesse, 2), "m/s")
```


## Exercice 2 – Débogage : trouver l’erreur

### Code corrigé :

```python
nom = input("Entrez votre nom : ")
print("Bonjour", nom)
```


## Exercice 3 – Erreur logique : l'aire du rectangle

### Étape 1 – Correction de la formule :

```python
longueur = 4
largeur = 3
aire = longueur * largeur
print("Aire =", aire)
```

### Étape 2 – Avec saisie de l’utilisateur :

```python
longueur = float(input("Entrez la longueur (en m) : "))
largeur = float(input("Entrez la largeur (en m) : "))
aire = longueur * largeur
print("Aire =", aire, "m²")
```


## Exercice 4 – Fonctions prédéfinies

```python
mot = input("Entrez un mot : ")
mot_maj = mot.upper()
nb_lettres = len(mot)

print("Mot en majuscules :", mot_maj)
print("Nombre de lettres :", nb_lettres)
```


## Exercice 5 – Module `math`

```python
import math

rayon = float(input("Entrez le rayon du cercle : "))
aire = math.pi * math.pow(rayon, 2)
print("Aire du cercle :", round(aire, 2), "unités²")
```


## Bonus – Éléments chimiques

```python
nom = input("Entrez le nom d’un élément chimique : ")
masse = float(input("Entrez sa masse atomique (u) : "))

print("L'élément", nom, "a une masse atomique de", masse, "u.")
```