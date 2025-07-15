+++
title = "Atelier 6"
weight = 106
+++


## Objectifs d’apprentissage

* Utiliser les boucles `for` et `while` pour automatiser des tâches répétitives.
* Appliquer les boucles à une situation scientifique concrète.
* Travailler en collaboration pour planifier une solution et tester différents scénarios.

---

## Exercice 1 – Table de multiplication

> Écrire un programme Python qui affiche la table de multiplication d’un nombre donné par l’usager (entre 1 et 12), jusqu’à 12 × ce nombre.

**Exemple de sortie :**

```
Entrez un nombre entre 1 et 12 : 7
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
...
12 x 7 = 84
```

* Variante : demander à l'usager s’il veut une table en ordre croissant ou décroissant.
* Version bonus : utiliser une boucle `while` pour refaire une autre table tant que l’usager le souhaite.

## Exercice 2 – Utiliser `while` pour atteindre un objectif

Une température initiale est de 20 °C. Chaque heure, elle augmente de 1,5 °C.
Écrire un programme qui affiche l’évolution de la température **jusqu’à ce qu’elle atteigne 30 °C**.

**Aide pas à pas :**

1. Crée une variable `temp` avec 20 comme valeur initiale.
2. Utilise une boucle `while` pour vérifier si `temp` est inférieure à 30.
3. À chaque tour, affiche la température.
4. Augmente la température de 1.5.


## Exercice 3 – Répéter une mesure fixe avec `for`

On veut afficher les numéros de 10 échantillons : `Échantillon 1`, `Échantillon 2`, ..., `Échantillon 10`.

**Aide pas à pas :**

1. Utilise une boucle `for` avec `range(1, 11)`.
2. À chaque tour, affiche `Échantillon` suivi du numéro.


## Exercice 4 – Arrêter une boucle avec `break` (Semaine 7)

Un étudiant répond à un test. Tu veux simuler les questions jusqu’à la question 10, **mais arrêter dès qu’il donne une mauvaise réponse**.

**Aide pas à pas :**

1. Simule des réponses avec une variable (par exemple, une bonne réponse = "A").
2. Utilise une boucle `for` pour passer les questions.
3. Si la réponse est incorrecte, affiche "Test terminé" et utilise `break`.


## Exercice 4 – Motif croissant simple

* Utilise deux boucles `for` imbriquées.
* Aucun `input()` n’est requis.
* Le résultat doit s’afficher exactement comme ci-dessous.

**Affichage attendu :**

```
1
12
123
```


## Exercice 5 – Motif croissant inversé (triangle renversé)

* Utilise une boucle `for` pour afficher un motif décroissant.
* Aucune liste n’est nécessaire.
* Ne pas utiliser de conditions (`if`).

**Affichage attendu :**

```
123
12
1
```

## Exercice 6 – Motif avec nombres décroissants par ligne

* Affiche les nombres dans l’ordre décroissant sur chaque ligne.
* Utilise deux boucles `for` imbriquées.
* Ne pas utiliser de chaînes préfabriquées (ex: `"321"`).

**Affichage attendu :**

```
321
21
1
```

## Exercice 7 – Triangle aligné à droite avec nombres croissants

* Utilise les fonctions `print()` et la multiplication de chaînes (`" " * n`).
* Aligne le motif à droite.
* Ne pas utiliser de fonctions avancées comme `rjust()`.

**Affichage attendu :**

```
  1
 12
123
```

## Exercice 8 – Triangle inversé avec décalage à gauche

* Utilise deux boucles imbriquées et des espaces (`" "`) pour le décalage.
* Le triangle doit se décaler d’une position à droite à chaque ligne.

**Affichage attendu :**

```
123
 12
  1
```


## Exercice 9 – Triangle inversé symétrique d’étoiles

* Le motif doit être centré.
* Le nombre d’étoiles par ligne suit la suite : 5, 3, 1 (soit 2\*i – 1).
* Utilise des boucles pour gérer les espaces et les étoiles.

**Affichage attendu :**

```
*****
 ***
  *
```
