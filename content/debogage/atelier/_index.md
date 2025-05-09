+++
title = "Activité - Corriger un script scientifique erroné"
weight = 2
+++


## Objectifs pédagogiques

* Identifier et corriger des erreurs fréquentes : types de données, concaténation, calculs
* Introduire la validation minimale des entrées
* Revoir les conventions de nommage et la clarté du code

---

## Préambule

**Thème : Loi d’Ohm (U = R × I)**
**Durée prévue :** 60 à 90 minutes
**Travail en équipe de 2 ou 3**

## Contexte

Un technicien de laboratoire a tenté d’écrire un programme Python pour calculer la tension (U) en volts selon la loi d’Ohm. Il voulait que l’utilisateur entre la valeur de la résistance (en ohms) et du courant (en ampères), puis obtenir la tension. Malheureusement, le script contient plusieurs erreurs.

Vous devez lire, exécuter et corriger le script pour qu’il fonctionne correctement et respecte les bonnes pratiques vues en classe.

## Script initial (erroné)

```python
# Calcul de la tension selon la loi d’Ohm
resistance = input("Entrer la résistance en ohms : ")
courant = input("Entrer le courant en ampères : ")

tension = courant * resistance

print("La tension est de " + tension + " V")
```

## Consignes

1. Exécuter le script tel quel et observer les messages d’erreurs.
2. Identifier au moins **trois problèmes** différents dans le code.
3. Corriger le script pour qu’il fonctionne correctement et soit lisible.
4. Ajouter une explication en commentaire pour chaque correction.
5. Faire valider votre version corrigée avec une autre équipe.
6. Proposer une amélioration facultative (ex. : arrondir le résultat, afficher les unités, utiliser `f-strings`).

## Résultat attendu

Un script fonctionnel, lisible, commenté, et capable de produire une sortie comme :

```
Entrer la résistance en ohms : 10
Entrer le courant en ampères : 2
La tension est de 20.0 V
```

