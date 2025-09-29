+++
pre = "<b>7.</b>"
title = " Dictionnaires"
weight = 207
draft = false
+++


## Exercice 1 : Créer un dictionnaire

```python
# Création d'un dictionnaire vide
cubes = {}

# Ajout des clés et valeurs avec une boucle
for i in range(1, 6):
    cubes[i] = i**3

print("Dictionnaire des cubes :", cubes)
```



## Exercice 2 : Extraire clés et valeurs

```python
cles = list(cubes.keys())
valeurs = list(cubes.values())

print("Clés :", cles)
print("Valeurs :", valeurs)
```



## Exercice 3 : Parcourir `items()`

```python
for cle, valeur in cubes.items():
    print(f"Le cube de {cle} est {valeur}")
```



## Exercice 4 : Modifier et supprimer

```python
# 1. Ajouter une nouvelle paire
cubes[6] = 216

# 2. Modifier la valeur associée à la clé 3
cubes[3] = 30

# 3. Supprimer la clé 1
del cubes[1]

print("Dictionnaire final :", cubes)
```