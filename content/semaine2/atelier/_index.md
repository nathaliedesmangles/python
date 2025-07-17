+++
title = "Atelier 2"
weight = 102
+++

## Objectifs

* Manipuler des variables. 
* Utiliser des types de données différents.
* Écrire des algorithmes de problèmes scientifiques.
* Traduire un algorithme en code.
* Afficher des résultats.

---

### Exercice 1 - Calcul de probabilité

On choisit un point au hasard dans ce rectangle. Calcule la probabilité que ce point se situe dans la région grise, c’est-à-dire en dehors des cercles.
![Exercice - Calcul de probabilité](./probabilite.png?width=25vw)


* Un rectangle contenant **6 cercles isométriques** (même taille),
* Ils sont organisés en **2 rangées** de **3 cercles**,
* La **hauteur du rectangle est 10 cm**, ce qui correspond à **deux diamètres** de cercles (1 par rangée).

a) Identifier les variables, les constantes et les formules nécessaires  
b) Écrire l'algorithme  
c) Traduire l'algorithme en Python

### Résultat attendu:

```
Probabilité qu’un point tombe dans la région grise : 0.2119 (soit 21.19 %)
```

### Exercice #2 - Expérience en chimie

Un bécher contient 400 mL de solution. La solution s’évapore à raison de 25 mL/min.
La situation est linéaire : on commence à 400 mL, et on perd 25 mL chaque minute.
Donc la fonction est :
```math
$$
q(t) = 400 - 25t
$$
```
où :
* $t$ est le temps en minutes,
* $q(t)$ est la quantité de solution restante (en mL) après $t$ minutes.

On souhaite trouver la quantité de solution qu'il restera après 10 min 15 s

a) Définir les variables, constantes et formules  
b) Écrire l'algorithme  
c) Traduire l'algorithme en Python

**Résultat attendu** :

```
Quantité restante après 10.25 minutes : 143.75 mL.
```

## Exercice #3 - Calcul d'intérêts simple et composé

* Vous avez deux placements avec **le même montant initial** (qu'on peut appeler `montant`).
   * **Premier placement** : intérêt **annuel simple** de **3,2 %** pendant **10 ans**.
   * **Deuxième placement** : intérêt **composé** à **1,6 % tous les 6 mois**, donc **2 fois par an**, pendant **10 ans**.

i) On cherche **l’écart en % entre les deux montants finaux** au bout de 10 ans.  
ii) En déduire quel est le meilleur placement sur 10 ans.

**Hypothèse** : Comme le montant initial est le **même**, on peut le fixer à 100 \$ pour faciliter le calcul de l’écart en **pourcentage** à la fin.

a) Définir les variables, constantes et formules  
b) Écrire l'algorithme  
c) Traduire l'algorithme en Python

**Résultat attendu** (approximatif) :

```
Valeur avec intérêt simple : 132.00 $
Valeur avec intérêt composé : 134.87 $
Écart relatif : 2.17 %
```








