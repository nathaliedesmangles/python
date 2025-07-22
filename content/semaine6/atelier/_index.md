+++
title = "Atelier 6"
weight = 106
draft = false
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

* **Variante 1**: demander à l'usager s’il veut une table en ordre croissant ou décroissant.
* **Variante 2** : utiliser une boucle `while` pour refaire une autre table tant que l’usager le souhaite.


## Exercice 2 – Motif croissant simple

* Utilise deux boucles `for` imbriquées.
* Ne pas utiliser de conditions (`if`).
* Aucun `input()` n’est requis.
* Le résultat doit s’afficher exactement comme ci-dessous.

**Affichage attendu :**
```
1
12
123
```


## Exercice 3 – Motif croissant inversé (triangle renversé)

* Utilise une boucle `for` pour afficher un motif décroissant.
* Ne pas utiliser de conditions (`if`).
* Aucun `input()` n’est requis.
* Le résultat doit s’afficher exactement comme ci-dessous.

**Affichage attendu :**
```
123
12
1
```

## Exercice 4 – Triangle inversé symétrique d’étoiles

* Le motif doit être centré.
* Le nombre d’étoiles par ligne suit la suite : 5, 3, 1 (soit `(2 x i) – 1`).
* Utilise des boucles pour gérer les espaces et les étoiles.
* Ne pas utiliser de conditions (`if`).
* Aucun `input()` n’est requis.

**Affichage attendu :**
```
*****
 ***
  *
```

