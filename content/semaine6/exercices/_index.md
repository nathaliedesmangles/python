+++
title = "Exercices - Boucles imbriquées avec une liste de listes"
weight = 106.3
draft = false
+++

<!--

### Exercice 1 : Table de nombres

1. Créer une boucle `for` qui répète 3 fois.
2. À l’intérieur de cette boucle, ajouter une autre boucle qui parcourt les nombres de 1 à 3.
3. Affiche les nombres sur la même ligne, séparés par un espace (avec `print(..., end=" ")`).
4. Ajouter un `print()` à la fin de la boucle pour passer à la ligne suivante.

**Résultat attendu** :
```
1 2 3 
1 2 3 
1 2 3
```
-->
## Niveau 1 – Manipuler et afficher

### Exercice 1 : Liste d’animaux

1. Crée la liste suivante :

   ```python
   animaux = [["chat", "chien"], ["lion", "tigre"], ["souris", "rat"]]
   ```
2. Créer une première boucle pour parcourir chaque sous-liste.
3. À l’intérieur, créer une deuxième boucle pour parcourir les animaux de la sous-liste.
4. Afficher chaque animal sur la même ligne (`print(animal, end=" ")`.
5. Passer à la ligne quand tu as fini une sous-liste.

**Résultat attendu** :
```
chat chien 
lion tigre 
souris rat
```

---

## Niveau 2 – Comprendre la structure

### Exercice 2 : Noms et prénoms

1. Crée les deux listes :

   ```python
   prenoms = ["Alain", "Judith", "Pierre"]
   noms = ["Durand", "Martin", "Lefebvre"]
   ```
2. Crée une boucle pour parcourir la liste des prénoms.
3. À l’intérieur, ajoute une deuxième boucle pour parcourir la liste des noms.
4. Affiche la combinaison prénom + nom à chaque tour.

**Résultat attendu** :
```
Alain Durand
Alain Martin
Alain Lefebvre
Judith Durand
Judith Martin
Judith Lefebvre
Pierre Durand
Pierre Martin
Pierre Lefebvre
```

### Exercice 3 : Tableau de notes

1. Crée la liste des notes :

   ```python
    notes = [
       [60, 75, 70],   # Étudiant 1
       [45, 50, 65],   # Étudiant 2
       [80, 90, 85]    # Étudiant 3
    ]

   ```
2. Crée une boucle pour parcourir les sous-listes (chaque étudiant).
3. À l’intérieur, ajoute une boucle pour parcourir les notes de cet étudiant.
4. Affiche les notes sur la même ligne.

**Résultat attendu** :
```
Toutes les notes :
60 75 70 
45 50 65 
80 90 85 

Moyenne de chaque étudiant :
Étudiant 1 : 68.33
Étudiant 2 : 53.33
Étudiant 3 : 85.00

Moyenne de la classe : 68.89
```

---

## Niveau 3 – Introduire de la logique

### Exercice 4 : Ajouter un texte

1. Crée la liste des matières :

   ```python
   matieres = ["Math", "Physique", "Chimie"]
   ```
2. Reprends la liste des notes de l’exercice 4.
3. Parcours chaque étudiant avec une première boucle.
4. Pour chaque étudiant, affiche : `Étudiant 1 :` puis `Étudiant 2 :`, etc.
5. Ajoute une deuxième boucle pour parcourir les notes de l’étudiant.
6. Associe chaque note à la matière correspondante grâce à l’index.
7. Affiche les couples `Matière=Note`.

**Résultat attendu** :
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
<!--
### Exercice 6 : Étoiles

1. Crée une boucle qui va de 1 à 4.
2. À l’intérieur, crée une deuxième boucle qui répète autant de fois que le numéro de la ligne.
3. À chaque répétition, affiche une étoile `*` suivi d'un espace `" "`.
4. Ajoute un `print()` pour passer à la ligne suivante.

**Résultat attendu** :
```
* 
* * 
* * * 
* * * * 
```

---

## Niveau 4 – Applications concrètes

### Exercice 7 : Grille de multiplication

1. Crée une boucle extérieure qui va de 1 à 5.
2. À l’intérieur, crée une boucle intérieure qui va aussi de 1 à 5.
3. Multiplie les deux nombres (extérieur × intérieur).
4. Affiche le résultat sur la même ligne.
5. Passe à la ligne après chaque ligne complète.

**Résultat attendu** :
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

1. Crée la liste suivante :

   ```python
   groupes = [
     ["André", "Robert", "Chloé"],
     ["David", "Emma", "Farid"]
   ]
   ```
2. Crée une boucle pour parcourir les groupes.
3. Affiche `Groupe 1 :` puis `Groupe 2 :` selon l’index.
4. À l’intérieur, crée une boucle pour afficher les noms des étudiants du groupe.

**Résultat attendu** :
```
Groupe 1 :
André
Robert
Chloé

Groupe 2 :
David
Emma
Farid
```
<!--
### Exercice 9 : Matrice identité

1. Crée une boucle extérieure qui va de 0 à 3 (pour les lignes).
2. À l’intérieur, crée une boucle intérieure qui va aussi de 0 à 3 (pour les colonnes).
3. Si l’indice de la ligne est égal à l’indice de la colonne, affiche `1`.
4. Sinon, affiche `0`.
5. Passe à la ligne après chaque ligne complète.

**Résultat attendu** :
```
1 0 0 0 
0 1 0 0 
0 0 1 0 
0 0 0 1 
```

---


### Défi : Table de conversion Celsius → Fahrenheit

1. Crée une liste de températures Celsius `[0, 10, 20, 30]`.
2. Crée une boucle extérieure qui parcourt cette liste.
3. À l’intérieur, calcule la température en Fahrenheit avec la formule :

   ```
   F = C * 9/5 + 32
   ```
4. Affiche les deux valeurs côte à côte.

**Résultat attendu** :
```
0 °C = 32.0 °F
10 °C = 50.0 °F
20 °C = 68.0 °F
30 °C = 86.0 °F
```
-->