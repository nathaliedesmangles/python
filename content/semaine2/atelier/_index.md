+++
title = "Atelier 2"
weight = 21
+++

Copier les exercices qui utilisent input pour les mettre dans l'atelier de la semaine 3
Remanier les exercices pour enlever la saisie au clavier

## Objectifs

* Manipuler des variables. 
* Utiliser des types de données différents.
* Afficher des résultats.

## Exercice 1 : Conversion de température

Un thermomètre donne des relevés en Fahrenheit, mais vous devez les convertir en Celsius et Kelvin.

1. Utiliser une variable pour stockez une température en °C.
2. Convertissez cette température en °F et en K.
3. Affichez les trois valeurs avec des messages clairs.

**Formules** :
```math
$ °F = (°C × 9/5) + 32 $  <br> 
$ K = °C + 273.15 $
```

## Exercice 2 : La loi d'Ohm

Un technicien de laboratoire vous demande d'écrire un programme Python pour calculer la tension (U) en volts selon la loi d’Ohm. Il voudrait pouvoir entrer la valeur de la résistance (en ohms) et la valeur du courant (en ampères), puis obtenir la tension.

```math
Loi d’Ohm : $ U = R × I $
```

1. Le programme demande à l'utilisateur d'entrer la valeur de la résistance (en ohms)
2. Le programme demande à l'utilisateur d'entrer la valeur du courant (en ampères)
3. Calculer et afficher la tension à l'aide d'une phrase.
4. Ajouter des explications en commentaire dans le code.

**Résultat attendu** :

```
Entrer la résistance en ohms : 10
Entrer le courant en ampères : 2
La tension est de 20.0 V
```

## Exercice 3 : Calcul de concentration molaire

Un technicien prépare une solution en dissolvant une masse donnée de soluté dans un certain volume de solvant.
Écrire un programme qui calcule la concentration molaire (mol/L) selon la formule :
```math
$ C = n / V $ où  $ n = m / M $
```

* `m` : masse du soluté (en grammes)
* `M` : masse molaire du soluté (en g/mol)
* `V` : volume de la solution (en litres)

**Exemple d’utilisation :**
Entrer la masse, la masse molaire, et le volume. Le programme retourne la concentration.


## Exercice 4 : Vitesse moyenne d’une réaction

Lors d’une expérience de cinétique chimique, on mesure la variation de la concentration d’un réactif au cours du temps.
Écrire un programme qui calcule la vitesse moyenne de disparition selon :

```math
$ v = \frac{\Delta [A]}{\Delta t} $
```

où `[A]` est la concentration du réactif.

**Exemple :**
\[Réactif A] passe de 0.80 mol/L à 0.20 mol/L en 120 secondes. Calculer la vitesse moyenne.







