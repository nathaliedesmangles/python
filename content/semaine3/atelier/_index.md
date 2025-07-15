+++
title = "Atelier 3"
weight = 103
+++

## Objectifs pédagogiques

Être capable de :

* Saisir des données au clavier.
* Convertir des types de données
* Traduire un algorithme simple en code Python
* Repérer et corriger des erreurs dans un script
* Utiliser des fonctions prédéfinies pour faire des calculs ou manipuler des données

---

## Exercice 1 – Traduire un algorithme

Voici un algorithme :

> 1. Demander la distance parcourue (en mètres)
> 2. Demander le temps écoulé (en secondes)
> 3. Calculer la vitesse moyenne (v = d / t)
> 4. Afficher la vitesse moyenne

**Consigne :** Traduis cet algorithme en code Python.

---

## Exercice 2 – Débogage : trouver l’erreur

Voici un script contenant une erreur :

```python
nom = input("Entrez votre nom : )
print("Bonjour", nom)
```

**Consigne :**

1. Copie-colle le code et exécute-le.
2. Observe le message d’erreur.
3. Corrige le code.


## Exercice 3 – Erreur logique : l'aire du rectangle

Voici un script avec une **erreur logique** :

```python
longueur = 4
largeur = 3
aire = longueur + largeur
print("Aire =", aire)
```

**Consigne :**

1. Identifie l’erreur.
2. Corrige-la pour obtenir la bonne aire.
3. Modifie le programme pour demander la longueur et la largeur à l’utilisateur avec `input()`.


## Exercice 4 – Utiliser les fonctions prédéfinies

Écris un programme qui :

1. Demande un mot à l’utilisateur
2. Affiche le mot en majuscules
3. Affiche le nombre de lettres dans ce mot

**Pistes :** `input()`, `print()`, `len()`, `str.upper()`


## Exercice 5 – Utiliser le module `math`

Écris un programme qui :

1. Demande à l’utilisateur de saisir un rayon
2. Calcule l’aire d’un cercle (π × r²)
3. Affiche le résultat arrondi à 2 décimales

**Pistes :** `import math`, `math.pi`, `math.pow()`, `round()`


## Bonus – Exercice de consolidation

Voici un mini-algorithme :

> 1. Demander le nom d’un élément chimique
> 2. Demander sa masse atomique
> 3. Afficher un message :
>    `"L'élément [nom] a une masse atomique de [valeur] u."`

Traduis-le en code Python.

