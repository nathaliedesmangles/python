+++
title = "Activité 6 - modélisation d’une loi physique (loi d’Ohm, chute libre)."
weight = 61
+++


## Objectif de l’atelier

Apprendre à créer une **fonction Python** qui modélise une **loi physique simple** et l’utiliser pour explorer des situations concrètes dans un contexte scientifique.

---

## Consignes

* Travaillez **à deux ou trois**, discutez de chaque étape.
* Testez vos fonctions avec **plusieurs valeurs**.
* Commentez brièvement votre code.
* Ajoutez une **brève conclusion** à la fin du notebook :

  * Qu’avez-vous observé?
  * Quelle relation la fonction exprime-t-elle?


## Livrable

À la fin de la séance, vous devez avoir un **fichier `.ipynb` propre, documenté, et fonctionnel** avec :

* La fonction Python créée
* L’affichage des résultats
* Une conclusion en 2-3 phrases

## Choix de la loi physique

Choisissez **un seul** des deux modèles suivants à implémenter :

### Option A – Loi d’Ohm (électricité)

Formule :
  **V = R × I**

> V = tension (en volts)
> R = résistance (en ohms)
> I = courant (en ampères)

**À faire :**

1. Créez une fonction nommée `calcul_tension(R, I)` qui retourne la tension.
2. Affichez un tableau des tensions pour un courant qui varie de 0 à 2 A, par pas de 0.1 A, pour une résistance de 10 ohms.
3. Gérez les cas d’entrée invalides (ex. : valeurs négatives).

### Option B – Chute libre (sans frottement)

Formule :
  **h(t) = h₀ – ½·g·t²**
  (g = 9.8 m/s²)

> h(t) = hauteur à un instant t
> h₀ = hauteur initiale
> t = temps en secondes

**À faire :**

1. Créez une fonction nommée `calcul_position(h0, t)` qui retourne la hauteur à l’instant t.
2. Simulez la chute d’un objet depuis une hauteur de 20 m, à chaque 0.5 s, jusqu’à ce qu’il touche le sol.
3. Affichez les résultats sous forme de tableau (temps et hauteur).
4. Arrêtez la simulation automatiquement quand l’objet atteint le sol.



