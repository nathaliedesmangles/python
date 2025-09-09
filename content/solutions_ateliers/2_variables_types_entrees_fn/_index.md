+++
pre = "<b>2.</b>"
title = " Variables, types, entrées et fonction"
weight = 302
draft = true
+++


## Exercice #1 - Expérience en chimie

```python
# Constantes
q_initiale = 400        # en mL
t_minutes = 10 + 15/60  # conversion des 15 s en minutes => 10.25 minutes
taux_evaporation = 25   # en mL/min

# Formule : q(t) = 400 - 25 * t
quantite_restante = q_initiale - taux_evaporation * t_minutes

print(f"Quantité restante après {t_minutes} minutes : {quantite_restante:.2f} mL.")
```

**Résultat attendu** :

```
Quantité restante après 10.25 minutes : 143.75 mL.
```

---

## Exercice #2 - Calcul de la force gravitationnelle

```python
objet = input("Nom de l'objet : ")
masse = float(input("Masse de l'objet (en kg) : "))
g = 9.8  # accélération gravitationnelle en m/s²
force = masse * g
print(f"La force de la {objet} de {masse:.1f} Kg est de {force:.2f} N.")

# Tests
# Test 1
# >>> balle, 2.5
# Test 2
# >>> voiture, 1000.0
```

**Résultats attendus** :

```
La force de la balle de 2.5 Kg est de 24.50 N.
La force de la voiture de 1000.0 Kg est de 9800.00 N.
```

---

## Exercice #3 - Calcul d'intérêts simple et composé

```python
# Montant initial
montant = 100

# Intérêt simple : 3.2 % par an pendant 10 ans
taux_simple = 0.032
duree = 10
valeur_simple = montant * (1 + taux_simple * duree)

# Intérêt composé : 1.6 % deux fois par an pendant 10 ans
taux_composé = 0.016  # tous les 6 mois
periodes = 2 * duree  # 2 fois par an pendant 10 ans
valeur_composée = montant * (1 + taux_composé) ** periodes

# Écart en pourcentage
écart = ((valeur_composée - valeur_simple) / valeur_simple) * 100

# Affichage des résultats
print(f"Valeur avec intérêt simple : {valeur_simple:.2f} $")
print(f"Valeur avec intérêt composé : {valeur_composée:.2f} $")
print(f"Écart relatif : {écart:.2f} %")
```

**Résultats attendus** :

```
Valeur avec intérêt simple : 132.00 $
Valeur avec intérêt composé : 137.36 $
Écart relatif : 4.06 %
```

---

### Exercice #4 - Calcul de la hauteur maximale

```python
# Demander la vitesse initiale à l'utilisateur
vitesse_initiale = float(input("Entrez la vitesse initiale (en m/s) : "))
g = 9.81  # accélération gravitationnelle en m/s²

# Calcul de la hauteur maximale
h_max = (vitesse_initiale ** 2) / (2 * g)

# Affichage
print(f"La hauteur maximale atteinte est de {h_max:.2f} mètres.")
```

**Test suggestion** :

```
v = 20 m/s → h ≈ 20.39 m
```

---

### Exercice #5 - Calcul de probabilité géométrique (Facultatif)

**Hypothèses :**

* Le rectangle fait **10 cm** de haut.
* Cela représente **2 diamètres**, donc **diamètre = 5 cm** → rayon = 2.5 cm.
* Chaque cercle a une aire : πr² = π × 2.5² ≈ 19.63 cm²
* Il y a **6 cercles**, donc aire totale des cercles ≈ 6 × 19.63

```python
import math

# Dimensions
hauteur = 10
diametre = hauteur / 2        # car 2 diamètres = 10 cm
rayon = diametre / 2          # donc rayon = 2.5 cm
largeur = 3 * diametre        # 3 cercles côte à côte → largeur = 15 cm

# Aire du rectangle
aire_rectangle = largeur * hauteur

# Aire totale des 6 cercles
aire_cercle = math.pi * rayon ** 2
aire_cercles = 6 * aire_cercle

# Aire grise = tout sauf les cercles
aire_grise = aire_rectangle - aire_cercles

# Probabilité = aire grise / aire totale
probabilite = aire_grise / aire_rectangle

print(f"Probabilité qu’un point tombe dans la région grise : {probabilite:.4f} (soit {probabilite*100:.2f} %)")
```

**Résultat attendu** :

```
Probabilité qu’un point tombe dans la région grise : 0.2119 (soit 21.19 %)
```