+++
title = "Atelier 3"
weight = 103
+++

## Objectifs

* Gérer les entrées clavier.
* Utiliser des fonctions prédéfinies.
* Définir et utiliser des fonctions. 
* Comprendre et corriger des messages d’erreurs simples.

---

## Exercice #1 : Calcul de la force gravitationnelle

Écrire une fonction qui:

1. Demande à l’utilisateur d’entrer le nom de l’objet (chaîne de caractères).
2. Demande à l’utilisateur d’entrer la masse de l’objet (nombre décimal, en kg).
3. Défini la constante d’accélération gravitationnelle (9,8 m/s²).
4. Calcule la force en utilisant la formule : `force = masse * accélération`
5. Affiche la force avec une phrase claire, incluant le nom de l’objet et l’unité en N (Newton).

Testez la fonction avec ces deux cas:  

**Cas #1.** Objet: balle et masse: 2,5 Kg

**Sortie attendue** :
```
La force de la balle de 2.5 Kg est de 24.50 N.
```

**Cas #2.** Objet: voiture et masse: 1000,0 Kg

**Sortie attendue** :
```
La force de la voiture de 1000.0 Kg est de 9800.00 N.
```

## Exercice #2 : Calcul de la hauteur maximale

Vous voulez aider un·e physicien·ne à calculer la **hauteur maximale** atteinte par un objet lancé verticalement vers le haut avec une certaine vitesse initiale. 
* Écrire un programme qui demande la **vitesse initiale** au lancement, puis calcule la hauteur maximale atteinte par l’objet (en négligeant la résistance de l’air).

La formule utilisée est :
```math
$$
h_{\text{max}} = \frac{v^2}{2g}
$$
```

avec :

```math
$v$ : vitesse initiale (en m/s) <br>  
$g$ : accélération gravitationnelle = 9.81 m/s²  <br>
$h_{\text{max}}$ : hauteur maximale (en m)  
```

## Partie A – Version à compléter

1. Téléchargez le bloc-notes ci-dessous.  
[Bloc-notes du programme à compléter](https://python-a25.netlify.app/blocnotes/exercice2_partiea.ipynb)

2. Complétez le code

---

## Partie B – Version boguée à corriger

Voici une version contenant **plusieurs erreurs** fréquentes à identifier et corriger :

1. Téléchargez le bloc-notes ci-dessous.  
[Bloc-notes du programme à corriger](https://python-a25.netlify.app/blocnotes/exercice2_partieb.ipynb)

2. **Exécute** le code.
3. Notez tous les **messages d’erreurs** affichés.
4. Pour chaque erreur :
   * **Expliquez** ce qu’elle signifie.
   * **Corrigez** le code en expliquant la modification.
5. Ajoutez une ligne pour afficher la même hauteur **arrondie à deux décimales**.