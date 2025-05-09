+++
title = "Activité 2 – Calculs de concentrations et vitesses de réaction"
weight = 21
+++

## Objectif

- Mettre en pratique les opérations arithmétiques et la manipulation de variables en Python dans un contexte scientifique (chimie et physique).

## Compétences exercées

* Déclaration et affectation de variables
* Opérations arithmétiques
* Affichage de résultats avec formatage
* Interprétation scientifique d’un problème

**Contexte :**
Vous travaillez en équipe de 2 ou 3. Chaque équipe reçoit des situations-problèmes à modéliser en Python.

---

## Exercice 1 : Calcul de concentration molaire

**Énoncé :**
Un technicien prépare une solution en dissolvant une masse donnée de soluté dans un certain volume de solvant.
Écrire un programme qui calcule la concentration molaire (mol/L) selon la formule :

$$
C = \frac{n}{V}
\quad \text{où} \quad
n = \frac{m}{M}
$$

* `m` : masse du soluté (en grammes)
* `M` : masse molaire du soluté (en g/mol)
* `V` : volume de la solution (en litres)

**Exemple d’utilisation :**
Entrer la masse, la masse molaire, et le volume. Le programme retourne la concentration.


## Exercice 2 : Vitesse moyenne d’une réaction

**Énoncé :**
Lors d’une expérience de cinétique chimique, on mesure la variation de la concentration d’un réactif au cours du temps.
Écrire un programme qui calcule la vitesse moyenne de disparition selon :

$$
v = \frac{\Delta [A]}{\Delta t}
$$

où `[A]` est la concentration du réactif.

**Exemple :**
\[Réactif A] passe de 0.80 mol/L à 0.20 mol/L en 120 secondes. Calculer la vitesse moyenne.


## Extension (pour les rapides)

Ajouter une vérification pour empêcher la division par zéro et afficher un message d’erreur personnalisé si le volume ou le temps est nul.

