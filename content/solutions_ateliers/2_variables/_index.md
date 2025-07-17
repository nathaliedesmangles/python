+++
pre = "<b>2.</b>"
title = " Variables, types de données et algorithme"
weight = 302
draft = false
+++

## Exercice #1 - Calcul de probabilité

a) Identifier les variables, constantes et formules

   * **Variables d'entrées** : 
     - diametre = hauteur_rect / 2 
     - rayon = diametre / 2 
     - largeur_rect = 3 x diametre
     - aire_rectangle = hauteur_rect x largeur_rect
     - aire_cercle = math.pi x rayon² 
     - aire_totale_cercles = 6 x aire_cercle

   * **Variable de sortie** :
     - prob_grise = 1 - (aire_totale_cercles / aire_rectangle)

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

### Exercice #2 - Expérience en chimie

a) Définir les variables, constantes et formules

**Constantes :**

* `Q0 = 400` (volume initial, en mL)
* `V = 25` (vitesse d’évaporation, en mL/min)

**Variables :**

* `t_min = 10` (minutes)
* `t_sec = 15` (secondes)
* `t` : temps total en **minutes**, donc `t = t_min + t_sec / 60`

**Formule :**

```math
$ q(t) = Q0 - V * t $
```

b) Écrire l'algorithme (en français)

1. Initialiser le volume initial `Q0` à 400
2. Initialiser la vitesse d’évaporation `V` à 25
3. Définir le temps écoulé `t` en minutes : `10 + 15/60`
4. Calculer la quantité de solution restante avec la formule `q = Q0 - V * t`
5. Afficher le résultat


c) Traduction en Python

```python
# Constantes
Q0 = 400         # volume initial en mL
V = 25           # vitesse d'évaporation en mL/min

# Temps écoulé
t_min = 10       # minutes
t_sec = 15       # secondes
t = t_min + t_sec / 60  # conversion en minutes

# Calcul
q = Q0 - V * t

# Affichage
print(f"Quantité restante après {t} minutes : {q} mL")```
```
---


## Exercice #3 - Calcul d'intérêts simple et composé

i) **L'écart en % entre les deux montants finaux**

a) Définir les variables, constantes et formules

**Constantes** :

* `montant = 100`  (valeur initiale, arbitraire mais identique)
* `t = 10` (durée en années)

**Placement 1** — intérêt simple :

* taux annuel = `3.2 %` = `0.032`
* Formule :
  $M_{\text{simple}} = montant \times (1 + taux \times temps)$

**Placement 2** — intérêt composé semestriel :

* taux semestriel = `1.6 %` = `0.016`
* nombre de périodes = `2 × 10 = 20`
* Formule :
```math
  $M_{\text{composé}} = montant \times (1 + taux)^{nombre\_de\_périodes}$
```

**Écart relatif en %** :

```math
* $\text{écart} = \frac{M_{\text{composé}} - M_{\text{simple}}}{M_{\text{simple}}} \times 100$
```

b) Algorithme

1. Définir les constantes : montant, temps, taux simple, taux composé
2. Calculer le montant final avec intérêt simple
3. Calculer le montant final avec intérêt composé
4. Calculer l’écart relatif en pourcentage
5. Afficher les résultats


c) Traduction en Python

```python
# Constantes
montant = 100
t = 10

# Placement 1 : intérêt simple
taux_simple = 0.032
valeur_simple = montant * (1 + taux_simple * t)

# Placement 2 : intérêt composé
taux_compose = 0.016  # tous les 6 mois
n = 2 * t  # 2 périodes par année pendant 10 ans
valeur_composee = montant * (1 + taux_compose) ** n

# Écart relatif en %
ecart = (valeur_composee - valeur_simple) / valeur_simple * 100

# Affichage
print(f"Valeur avec intérêt simple : {valeur_simple:.2f} $")
print(f"Valeur avec intérêt composé : {valeur_composee:.2f} $")
print(f\"Écart relatif : {ecart:.2f} %\")
```

ii) **Déduction**

* Le placement **composé** est **plus avantageux** après 10 ans, malgré un taux plus bas, grâce à l'effet des intérêts composés.
**Le placement avec intérêts composés** vaut environ **2,17 % de plus** que celui avec intérêts simples, au bout de 10 ans.

