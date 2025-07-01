+++
title = "Boucler sur un tableau 2D"
weight = 8
+++


### Qu’est-ce qu’un tableau 2D ?

C’est une **liste de listes**.

Exemple d’un tableau 3 lignes × 4 colonnes rempli de 0 :

```python
tableau = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
```

Chaque **sous-liste** représente une **ligne**.


### Boucler sur les lignes (1 niveau)

```python
for ligne in tableau:
    print(ligne)
```

➡ On affiche chaque **ligne entière**.


### Boucler sur chaque élément (2 niveaux)

Pour accéder **à chaque case** du tableau, on utilise **deux boucles imbriquées** :

```python
for ligne in tableau:
    for case in ligne:
        print(case)
```

➡ On affiche chaque **élément un par un**.


### Avec indices (si on veut connaître les positions)

```python
for i in range(len(tableau)):         # i = index de ligne
    for j in range(len(tableau[i])):  # j = index de colonne
        print(f"Case [{i}][{j}] = {tableau[i][j]}")
```

➡ Cette méthode permet de **savoir à quelle position** se trouve chaque élément.

---

## Exercice guidé 1 – Remplir un tableau 3x3 avec la somme des indices

```python
tableau = []

for i in range(3):
    ligne = []
    for j in range(3):
        ligne.append(i + j)
    tableau.append(ligne)

print(tableau)
```

Résultat :

```
[[0, 1, 2],
 [1, 2, 3],
 [2, 3, 4]]
```


## Exercice guidé 2 – Compter les zéros dans un tableau

```python
tableau = [
    [0, 1, 0],
    [2, 0, 3],
    [0, 4, 5]
]

compteur = 0

for ligne in tableau:
    for case in ligne:
        if case == 0:
            compteur += 1

print("Nombre de zéros :", compteur)
```

➡ Résultat : `Nombre de zéros : 4`


## À retenir

| Structure                  | Utilité                       |
| -------------------------- | ----------------------------- |
| `for ligne in tableau`     | Parcourir chaque ligne        |
| `for case in ligne`        | Parcourir chaque élément      |
| `for i in range(len(...))` | Parcourir avec indices (i, j) |
| `tableau[i][j]`            | Accès à une case spécifique   |


## Exercice – Grille de températures en laboratoire

### Contexte scientifique

Une technicienne en laboratoire a pris des mesures de **températures (°C)** dans 3 chambres de croissance de plantes, à **4 moments différents** dans la journée. Les données sont enregistrées dans un tableau 2D.

```python
# tableau des températures [chambre][moment]
temperatures = [
    [22.1, 22.5, 23.0, 23.2],  # Chambre 1
    [21.8, 22.2, 22.6, 22.9],  # Chambre 2
    [23.5, 23.3, 23.0, 22.8]   # Chambre 3
]
```


### Objectif

1. Afficher chaque température avec la chambre et le moment de mesure.
2. Calculer la **température moyenne de chaque chambre**.
3. Trouver la **température la plus élevée** de toutes les mesures.


### Solution guidée pas à pas

#### 1. Afficher toutes les températures

```python
for i in range(len(temperatures)):  # index des chambres
    for j in range(len(temperatures[i])):  # index des moments
        print(f"Chambre {i+1}, Moment {j+1} : {temperatures[i][j]} °C")
```


#### 2. Moyenne par chambre

```python
for i in range(len(temperatures)):
    moyenne = sum(temperatures[i]) / len(temperatures[i])
    print(f"Moyenne de la chambre {i+1} : {moyenne:.2f} °C")
```


#### 3. Température maximale

```python
max_temp = temperatures[0][0]  # on part du premier élément

for ligne in temperatures:
    for temp in ligne:
        if temp > max_temp:
            max_temp = temp

print("Température maximale enregistrée :", max_temp, "°C")
```


### Variante possible


* ajouter une 4e chambre,
* de détecter la **température minimale**,
* ou de colorer en rouge les températures > 23 °C avec un message spécial.


