+++
pre = "2."
title = " Variables, types et expressions"
weight = 302
draft = false
+++

## Exercice #1 - Calcul de probabilité

On choisit un point au hasard dans ce rectangle. Calcule la probabilité que ce point se situe dans la région grise, c’est-à-dire en dehors des cercles.
![](../../semaine2/probabilite.png?width=30vw)

* Un rectangle contenant **6 cercles isométriques** (même taille),
* Ils sont organisés en **2 rangées** de **3 cercles**,
* La **hauteur du rectangle est 10 cm**, ce qui correspond à **deux diamètres** de cercles (1 par rangée).

a) Identifier les variables, les constantes et les formules nécessaires  
b) Écrire l'algorithme  
c) Traduire l'algorithme en Python

### Solution

a) Identifier les variables, constantes et formules

   * **Variables d'entrées** : 
     - diametre = hauteur_rect / 2 
     - rayon = diametre / 2 
     - largeur_rect = 3 x diametre
     - aire_rectangle = hauteur_rect x largeur_rect
     - aire_cercle = math.pi x rayon² 
     - aire_totale_cercles = 6 x aire_cercle

   * **Variable de sortie** :
     - prob_grise = 1 - (aire_totale_cercles / aire_rect)

   * **Constantes** : la valeur de PI (module math) `math.pi`

b) Écrire l'algorithme

   1. Définir le diamètre et le rayon d'un cercle.
   2. Définir la largeur du rectangle.
   3. Définir l'aire du rectangle.
   4. Définir l'aire des 6 cercles, pour ce faire :  
	4.1.obtenir le rayon d'un cercle.  
	4.2 calculer l'aire d'un cercle.  
	4.3 calculer l'aire des 6 cercles.  
   5. Calculer la probabilité de tomber dans la région grise.

c) Traduire l'algorithme en Python

```python
import math

# Données
diametre = 5  # cm
rayon = diametre / 2
aire_rectangle = 15 * 10  # cm²
aire_cercle = math.pi * rayon**2
aire_total_cercles = 6 * aire_cercle

# Probabilité
prob_grise = 1 - (aire_total_cercles / aire_rectangle)

# Affichage
print(f"Probabilité qu’un point tombe dans la région grise : {prob_grise:.4f} (soit {prob_grise*100:.2f} %)")
```

---
* Définir le diamètre d'un cercle
Puisqu’il y a 2 rangées verticales et une hauteur totale de 10 cm :

```math
   $$
   \text{diamètre} = \frac{10}{2} = 5 \text{ cm}
   $$
```

* Définir l'aire du rectangle
```math
   Largeur = 3 diamètres = $3 \times 5 = 15$ cm
   Hauteur = 10 cm

   $$
   A_{\text{rectangle}} = 15 \times 10 = 150 \text{ cm}^2
   $$
```

* Définir l'aire des cercles
```math
   Rayon $r = \frac{5}{2} = 2.5$ cm
   Aire d’un cercle :

   $$
   A_{\text{cercle}} = \pi r^2 = \pi \times (2.5)^2 = \pi \times 6.25
   $$

   Il y a 6 cercles :

   $$
   A_{\text{cercles}} = 6 \times \pi \times 6.25
   $$
```

4. **Probabilité de tomber dans la région grise** :

   $$
   P_{\text{grise}} = 1 - \frac{A_{\text{cercles}}}{A_{\text{rectangle}}}
   $$
---

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

### Solution

a) Identifier les variables, constantes et formules

quel est le temps écoulé en minutes ?
> 15 secondes = 0.25 minutes
> Donc $t = 10.25$

b) Écrire l'algorithme
   1. Définir la fonction qui représente 

c) Traduire l'algorithme en Python

```python
# a) Fonction q(t)
def q(t):
    return 400 - 25 * t

# b) Temps écoulé en minutes
temps_minutes = 10 + 15 / 60  # 10 min 15 s = 10.25 min

# Calcul de la quantité restante
quantité_restante = q(temps_minutes)

# Affichage clair
print(f"Après {temps_minutes} minutes, il reste {quantité_restante} mL de solution.")
```

## Exercice #3 - Calcul d'intérêts simple et composé

* Vous avez deux placements avec **le même montant initial** (qu'on peut appeler `montant`).
   * **Premier placement** : intérêt **annuel simple** de **3,2 %** pendant **10 ans**.
   * **Deuxième placement** : intérêt **composé** à **1,6 % tous les 6 mois**, donc **2 fois par an**, pendant **10 ans**.

1. On cherche **l’écart en % entre les deux montants finaux** au bout de 10 ans.  
2. En déduire quel est le meilleur placement sur 10 ans.

**Hypothèse** : Comme le montant initial est le **même**, on peut le fixer à 100 \$ pour faciliter le calcul de l’écart en **pourcentage** à la fin.


### Solution

1. L'écart en % entre les deux montnats

a) Identifier les variables, constantes et formules

b) Écrire l'algorithme

c) Traduire l'algorithme en Python

```python
# Montant initial
montant = 100.0  # Peu importe le montant, car on cherche un écart en %

# Premier placement : intérêt simple annuel
taux_simple_annuel = 0.032  # 3,2 %
duree = 10  # années
valeur_simple = montant * (1 + taux_simple_annuel * duree)

# Deuxième placement : intérêt composé semestriel
taux_compose_semestriel = 0.016  # 1,6 % tous les 6 mois
nombre_periodes = 2 * duree  # 2 périodes par an pendant 10 ans
valeur_composee = montant * (1 + taux_compose_semestriel) ** nombre_periodes

# Calcul de l'écart en pourcentage (par rapport à la valeur du placement simple)
ecart_pourcent = ((valeur_composee - valeur_simple) / valeur_simple) * 100

# Affichage
print(f"Valeur avec intérêt simple : {valeur_simple:.2f} $")
print(f"Valeur avec intérêt composé : {valeur_composee:.2f} $")
print(f"Écart relatif : {ecart_pourcent:.2f} %")
```

2. Déduction: **le placement avec intérêts composés** vaut environ **2,17 % de plus** que celui avec intérêts simples, au bout de 10 ans.

