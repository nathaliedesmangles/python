+++
chapter = true
pre = "<b>8.</b>"
title = "Listes et tableaux imbriqués"
weight = 108
+++


## Objectifs d'apprentissage

* Créer des listes
* Accéder à un élément dans une liste ou un tableau 2D (liste de listes)
* Utiliser des boucles imbriquées pour parcourir un tableau
* Ajouter des conditions dans les boucles

---

## 1. Liste simple

Une **liste** est un ensemble de valeurs entre crochets `[]`.

```python
notes = [78, 85, 92]
print(notes[1])  # 85 (indice commence à 0)
```

* Chaque valeur d'une liste est est positionné par indice, en commençant par l'indice 0.


## 2. Liste de listes (tableau 2D)

C’est une **liste dans laquelle chaque élément est lui-même une liste**.

```python
tableau = [
    [1, 2, 3],
    [4, 5, 6]
]
```

**Représentation tabulaire**:
|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 1 | 2 | 3 |
| **1** | 4 | 5 | 6 |

* Chaque élément (sous-liste) est positionné par indice, en commençant par l'indice 0.
* Chaque valeur d'une sous-liste est est positionné par indice, en commençant par l'indice 0.


### Accès à un élément :

```python
print(tableau[1][2])  # 6
```


## 3. Boucles imbriquées pour parcourir un tableau

### Exemple :

```python
for ligne in tableau:
    for valeur in ligne:
        print(valeur)
```

Affiche tous les éléments, un par un.


## 4. Ajouter une condition dans la boucle

### Exemple : afficher seulement les valeurs > 3

```python
for ligne in tableau:
    for valeur in ligne:
        if valeur > 3:
            print(valeur)
```


## Résumé

| Action                | Exemple                 |
| --------------------- | ----------------------- |
| Accès à un élément    | `tableau[1][2]`         |
| Boucle sur tableau 2D | `for ligne in tableau:` |
| Boucle imbriquée      | `for valeur in ligne:`  |
| Condition             | `if valeur > 3:`        |

---

## Exercices guidés

### Exercice 1 – Accès à un élément

**Énoncé :**
Dans la liste suivante, affiche la valeur 7.

```python
t = [[3, 4], [6, 7], [8, 9]]
```

**Solution :**

```python
print(t[1][1])  # 7
```


### Exercice 2 – Afficher tous les éléments

**Énoncé :**
Parcours le tableau `t` et affiche chaque valeur sur une ligne.

**Solution :**

```python
for ligne in t:
    for val in ligne:
        print(val)
```


### Exercice 3 – Afficher les valeurs paires

**Énoncé :**
Affiche seulement les valeurs **paires** du tableau `t`.

**Solution :**

```python
for ligne in t:
    for val in ligne:
        if val % 2 == 0:
            print(val)
```
