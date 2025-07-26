+++
title = "Les tableaux imbriqués"
weight = 72
draft = true
+++


## 1. Qu’est-ce qu’un tableau imbriqué?

- Un **tableau imbriqué** est une **liste qui contient d’autres listes**.

- Cela permet de représenter des données structurées **en deux dimensions** (comme un tableau ou une matrice en sciences).


### Exemple de tableau 2D (2 lignes, 3 colonnes)

```python
notes = [
    [85, 90, 88],   # notes de l'élève 1
    [78, 82, 80]    # notes de l'élève 2
]
```

Ici, `notes[0]` donne la liste `[85, 90, 88]`, et `notes[1][2]` donne la valeur `80` (3e note de l'élève 2).


## 2. Accès aux éléments

```python
print(notes[0])      # Affiche la 1re ligne : [85, 90, 88]
print(notes[1][2])   # Affiche 3e note de l’élève 2 : 80
```

## 3. Modifier un élément

```python
notes[0][1] = 95     # On change la 2e note de l’élève 1
print(notes[0])      # Résultat : [85, 95, 88]
```


## 4. Parcourir un tableau imbriqué avec deux boucles `for`

```python
for ligne in notes:
    for valeur in ligne:
        print(valeur)
```

**Ce que ça fait** : imprime chaque note, une à la fois.


## 5. Application en sciences – Températures sur 3 jours, dans 2 villes

```python
temperatures = [
    [12.4, 13.0, 15.2],  # Ville A
    [11.1, 14.5, 16.3]   # Ville B
]
```

### Moyenne de température par ville :

```python
for ville in temperatures:
    moyenne = sum(ville) / len(ville)
    print("Moyenne:", moyenne)
```


## 6. Créer un tableau vide de 3 lignes et 4 colonnes

```python
tableau = [[0 for _ in range(4)] for _ in range(3)]
print(tableau)
```

Résultat :
`[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`



## À retenir

* Un tableau imbriqué = liste de listes
* On accède à un élément avec deux indices : `liste[i][j]`
* On parcourt avec deux boucles `for`
* Très utile pour représenter des données en 2D (ex. données expérimentales, résultats d'élèves)

