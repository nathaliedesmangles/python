+++
title = "Exercices - Boucles imbriquées avec une liste de listes (solutions)"
weight = 106.4
draft = true
+++


## Niveau 1 – Manipuler et afficher
<!--
### Exercice 1 : Table de nombres

```python
for i in range(3):  # 3 lignes
    for j in range(1, 4):  # nombres de 1 à 3
        print(j, end=" ")
    print()  # saut de ligne à la fin de chaque ligne
```

**Explication :**

* La première boucle `for i in range(3)` crée 3 lignes.
* La deuxième boucle `for j in range(1, 4)` parcourt les nombres de 1 à 3.
* `print(j, end=" ")` permet d’afficher sur la même ligne.
* `print()` seul sert à passer à la ligne suivante.
-->

### Exercice 1 : Liste d’animaux

```python
animaux = [["chat", "chien"], ["lion", "tigre"], ["souris", "rat"]]

for sous_liste in animaux:   # on parcourt les sous-listes
    for animal in sous_liste:  # on parcourt chaque animal dans la sous-liste
        print(animal, " ")	# un espace sépare le noms des animaux
    print()  # saut de ligne après chaque sous-liste
```

**Explication :**

* La première boucle prend chaque sous-liste (par exemple `["chat", "chien"]`).
* La deuxième boucle affiche chaque élément de la sous-liste.
* On ajoute un `print()` pour séparer visuellement les groupes.

---

## Niveau 2 – Comprendre la structure

### Exercice 2 : Noms et prénoms

```python
prenoms = ["Alain", "Judith", "Pierre"]
noms = ["Durand", "Martin", "Lefebvre"]

for prenom in prenoms:
    for nom in noms:
        print(prenom, nom)
```

**Explication :**

* La boucle extérieure choisit un prénom.
* La boucle intérieure combine ce prénom avec tous les noms.
* Cela crée toutes les combinaisons possibles.


### Exercice 3 : Tableau de notes

```python
notes = [
    [60, 75, 14],   # Étudiant 1
    [45, 50, 65],   # Étudiant 2
    [80, 90, 85]    # Étudiant 3
]

# Afficher toutes les notes
print("Toutes les notes :")
for etudiant in notes:
    for note in etudiant:
        print(note, end=" ")	# un espace sépare les notes d'un étudiant
    print()  # saut de ligne après chaque étudiant

# Calculer la moyenne de chaque étudiant
print()		# Saut de ligne
print("Moyenne de chaque étudiant :")
for i in range(len(notes)):
    somme = 0
    for note in notes[i]:
        somme += note
    moyenne = somme / len(notes[i])
    print(f"Étudiant {i+1} : {moyenne:.2f}")

# Calculer la moyenne générale de la classe
somme_totale = 0
nombre_notes = 0
for etudiant in notes:
    for note in etudiant:
        somme_totale += note
        nombre_notes += 1

moyenne_classe = somme_totale / nombre_notes
print()	# saut de ligne
print(f"Moyenne de la classe : {moyenne_classe:.2f}")
```

**Explication :**

* La première double boucle affiche toutes les notes, regroupées par étudiant.
* La deuxième partie calcule la moyenne **par étudiant** en faisant la somme des notes et en divisant par leur nombre.
* La dernière partie calcule la moyenne **de la classe entière** en additionnant toutes les notes et en comptant leur nombre.

---

## Niveau 3 – Introduire de la logique

### Exercice 4 : Ajouter un texte

```python
matieres = ["Math", "Physique", "Chimie"]

notes = [
    [12, 15, 14],   # Étudiant 1
    [9, 10, 13],    # Étudiant 2
    [16, 18, 17]    # Étudiant 3
]

for i in range(len(notes)):  # i = index de l'étudiant
    print(f"Étudiant {i+1} :")
    for j in range(len(notes[i])):  # j = index de la note
        print(f"{matieres[j]} = {notes[i][j]}")
    print()
```

**Explication :**

* `i` sert à savoir quel étudiant est en cours.
* `j` sert à associer la note à la bonne matière.
* On utilise deux indices pour parcourir la structure.

**Résultat attendu :**

```
Étudiant 1 :
Math = 12
Physique = 15
Chimie = 14

Étudiant 2 :
Math = 9
Physique = 10
Chimie = 13

Étudiant 3 :
Math = 16
Physique = 18
Chimie = 17
```

---

<!--

### Exercice 6 : Étoiles

```python
for i in range(1, 5):  # lignes de 1 à 4
    for j in range(i):  # répète i fois
        print("*", end=" ")
    print()  # nouvelle ligne
```

**Explication :**

* La ligne 1 affiche 1 étoile, la ligne 2 affiche 2 étoiles, etc.
* `end=" "` évite le saut de ligne automatique.

**Résultat :**
```
* 
* * 
* * * 
* * * * 
```

---

<!--
### Exercice 7 : Grille de multiplication

```python
for i in range(1, 6):  # lignes
    for j in range(1, 6):  # colonnes
        print(i * j, end="\t")  # tabulation pour aligner
    print()
```

**Explication :**

* Chaque ligne correspond à un multiplicateur `i`.
* Chaque colonne correspond à un multiplicateur `j`.
* Le produit est affiché sous forme de tableau.

**Résultat :**

```
1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25
```
-->

## Niveau 4 – Applications concrètes

### Exercice 5 : Présence en classe

```python
groupes = [
  ["André", "Robert", "Chloé"],
  ["David", "Emma", "Farid"]
]

for i in range(len(groupes)):
    print(f"Groupe {i+1} :")
    for nom in groupes[i]:
        print(nom)
    print()
```

**Explication :**

* La première boucle gère les groupes.
* La deuxième boucle affiche les noms des étudiants de chaque groupe.

**Résultat :**

```
Groupe 1 :
Alice
Bob
Chloé

Groupe 2 :
David
Emma
Farid
```
<!--
---

### Exercice 9 : Matrice identité

```python
for i in range(4):  # lignes
    for j in range(4):  # colonnes
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
```

**Explication :**

* Dans une matrice identité, les diagonales sont remplies de 1.
* Les autres cases sont remplies de 0.

**Résultat :**

```
1 0 0 0 
0 1 0 0 
0 0 1 0 
0 0 0 1 
```

---

## Niveau 5 – Défis

### Défi 1 : Triangle de nombres

```python
for i in range(1, 5):  # 4 lignes
    for j in range(1, i+1):  # va jusqu’au numéro de la ligne
        print(j, end=" ")
    print()
```

**Explication :**

* La ligne 1 affiche "1".
* La ligne 2 affiche "1 2".
* La ligne 3 affiche "1 2 3", etc.

**Résultat :**

```
1 
1 2 
1 2 3 
1 2 3 4 
```

---

### Défi 2 : Table de conversion Celsius → Fahrenheit

```python
celsius = [0, 10, 20, 30]

for C in celsius:
    F = C * 9/5 + 32
    print(f"{C} °C = {F} °F")
```

**Explication :**

* On applique la formule de conversion pour chaque valeur.
* La boucle parcourt la liste `celsius`.

**Résultat :**

```
0 °C = 32.0 °F
10 °C = 50.0 °F
20 °C = 68.0 °F
30 °C = 86.0 °F
```

---

## Niveau 3 – Exercices intermédiaires

### Exercice 6 – Carré numérique

*Objectif :* Créer une grille carrée avec des nombres.

```python
n = 4
for i in range(1, n + 1):        # pour chaque ligne
    ligne = []                   # on prépare une liste vide
    for j in range(1, n + 1):    # on ajoute les nombres de 1 à n
        ligne.append(j)
    print(ligne)                 # on affiche la ligne complète
```

**Explication :**

* La boucle `for i` gère les lignes.
* La boucle `for j` ajoute les nombres dans la ligne.
* On affiche chaque ligne à la fin.

---

### Exercice 7 – Grille d'étoiles

*Objectif :* Afficher une grille carrée remplie d’étoiles.

```python
n = 5
for i in range(n):               # répéter pour chaque ligne
    ligne = []
    for j in range(n):           # ajouter une étoile dans la ligne
        ligne.append("*")
    print(" ".join(ligne))       # afficher la ligne avec des espaces
```

**Explication :**

* On utilise deux boucles pour créer une grille `n × n`.
* La fonction `" ".join(ligne)` transforme la liste en chaîne de caractères avec des espaces.

---

### Exercice 8 – Matrice identité simplifiée

*Objectif :* Créer une matrice identité avec des 1 sur la diagonale et 0 ailleurs.

```python
n = 4
for i in range(n):               # lignes
    ligne = []
    for j in range(n):           # colonnes
        if i == j:               # condition pour la diagonale
            ligne.append(1)
        else:
            ligne.append(0)
    print(ligne)
```

**Explication :**

* Quand `i == j`, on est sur la diagonale → on met 1.
* Sinon, on met 0.

---

## Niveau 4 – Exercices avancés

### Exercice 9 – Table de multiplication

*Objectif :* Construire une table de multiplication.

```python
n = 5
for i in range(1, n + 1):        # chaque ligne correspond à un nombre
    ligne = []
    for j in range(1, n + 1):    # multiplication avec les colonnes
        ligne.append(i * j)
    print(ligne)
```

**Explication :**

* `i` est le multiplicateur des lignes.
* `j` varie de 1 à n pour donner tous les produits.

---

### Exercice 10 – Triangle numérique

*Objectif :* Afficher un triangle où chaque ligne contient les nombres croissants.

```python
n = 5
for i in range(1, n + 1):        # nombre de lignes
    ligne = []
    for j in range(1, i + 1):    # de 1 jusqu’à i
        ligne.append(j)
    print(ligne)
```

**Explication :**

* Chaque ligne s’allonge d’un nombre supplémentaire.
* La boucle interne dépend de `i`, donc plus on descend, plus il y a de nombres.

---

### Exercice 11 – Triangle d’étoiles centré

*Objectif :* Afficher un triangle isocèle d’étoiles.

```python
n = 5
for i in range(1, n + 1):
    espace = " " * (n - i)         # espaces pour centrer
    etoiles = "*" * (2 * i - 1)    # formule pour obtenir 1, 3, 5, ...
    print(espace + etoiles + espace)
```

**Explication :**

* On ajoute des espaces pour centrer les étoiles.
* La largeur augmente de 2 à chaque ligne (`2*i - 1`).

---

## Niveau 5 – Défis

### Exercice 12 – Damier noir et blanc

*Objectif :* Construire un damier avec alternance X et O.

```python
n = 8
for i in range(n):                 # lignes
    ligne = []
    for j in range(n):             # colonnes
        if (i + j) % 2 == 0:       # somme paire → X
            ligne.append("X")
        else:                      # somme impaire → O
            ligne.append("O")
    print(" ".join(ligne))
```

**Explication :**

* Le damier alterne grâce à `(i + j) % 2`.
* Pair → `X`, impair → `O`.

---

### Exercice 13 – Triangle de Pascal simplifié

*Objectif :* Générer les 5 premières lignes du triangle de Pascal.

```python
n = 5
triangle = []

for i in range(n):
    ligne = [1] * (i + 1)               # on commence avec des 1
    for j in range(1, i):
        ligne[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(ligne)

for ligne in triangle:
    print(ligne)
```

**Explication :**

* Chaque ligne commence et finit par 1.
* Les autres valeurs sont la somme des deux nombres au-dessus.

---

### Exercice 14 – Mot croisé

*Objectif :* Écrire un mot horizontalement et verticalement dans une grille.

```python
mot = "PYTHON"
n = len(mot)

for i in range(n):
    ligne = []
    for j in range(n):
        if i == j:                   # diagonale
            ligne.append(mot[i])
        elif i == n // 2:            # ligne centrale
            ligne.append(mot[j])
        elif j == n // 2:            # colonne centrale
            ligne.append(mot[i])
        else:
            ligne.append(".")
    print(" ".join(ligne))
```

**Explication :**

* Diagonale : lettres du mot.
* Ligne centrale : mot écrit en entier.
* Colonne centrale : mot écrit verticalement.
* Sinon, on met un `.` pour remplir.

-->

