+++
chapter = true
pre = "<b>Semaine 4.</b>"
title = "Répéter avec `for` et `while`"
weight = 40
+++

## Objectifs de la leçon

* Comprendre l’utilité des boucles en programmation
* Savoir écrire des boucles `while` et `for`
* Appliquer les boucles à des cas concrets en sciences (répétitions, séries de mesures, simulations)

---

## Pourquoi utiliser une boucle?

Une boucle permet de **répéter automatiquement** une suite d'instructions **tant qu'une condition est vraie** (`while`) ou pour **parcourir une série de valeurs** (`for`).


## La boucle `while`

### Syntaxe de base :

```python
compteur = 0
while compteur < 5:
    print("Compteur =", compteur)
    compteur += 1
```

> Il faut **modifier la condition dans la boucle** pour éviter une boucle infinie.

### Exemple en sciences :

```python
# Simulation d’un refroidissement
temp = 100  # température initiale
while temp > 0:
    print(f"Température : {temp} °C")
    temp -= 10
```


## La boucle `for`

### Syntaxe de base :

```python
for i in range(5):
    print("i =", i)
```

### `range(n)` génère les entiers de 0 à n-1. On peut aussi faire :

```python
for i in range(2, 10, 2):  # de 2 à 8, par pas de 2
    print(i)
```

### Exemple en sciences :

```python
# Affichage de mesures prises chaque seconde
mesures = [22.5, 22.8, 23.0, 23.3, 23.5]
for mesure in mesures:
    print(f"Température mesurée : {mesure} °C")
```


## Comparaison `while` vs `for`

| Situation                            | Utiliser `while` si… | Utiliser `for` si… |
| ------------------------------------ | -------------------- | ------------------ |
| Nombre d’itérations inconnu d’avance | ✅                    | ❌                  |
| Série connue (liste, range)          | ❌                    | ✅                  |

---

## Exercices rapides à faire pendant le cours

**1. Afficher les nombres de 1 à 10**

```python
for i in range(1, 11):
    print(i)
```

**2. Compter jusqu’à 100 par bonds de 10**
**3. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)**
**4. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)**

---

## À éviter / pièges fréquents

* Boucle infinie (`while` sans mise à jour de la condition)
* Utiliser `range` sans comprendre que la fin est **exclusive**
* Oublier l’indentation dans le bloc de la boucle


## À retenir

* `while` = tant qu’une **condition** est vraie
* `for` = pour **chaque valeur** dans une séquence
* Les boucles permettent d’automatiser les calculs et traitements de données en science

