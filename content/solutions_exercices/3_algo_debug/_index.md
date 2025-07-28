+++
pre = "<b>3.</b>"
title = " Saisie au clavier, fonctions et débogage"
weight = 203
draft = false
+++


## Exercice 1 : Demi-vie radioactive

```python
# Données initiales
masse_initiale = 100  # en grammes
demi_vie = 5  # en années

# Entrée de l'utilisateur
annees = int(input("Combien d'années se sont écoulées ? "))

# Calcul du nombre de périodes de demi-vie
nb_periodes = annees // demi_vie

# Calcul de la masse restante
masse_restante = masse_initiale * (0.5) ** nb_periodes

# Affichage du résultat
print(f"Après {annees} ans, il reste environ {masse_restante:.2f} g de l'isotope.")
```



## Exercice 2 : Croissance bactérienne

```python
# Données initiales
population_initiale = 500
temps_doublement = 3  # en heures

# Entrée de l'utilisateur
heures = int(input("Combien d'heures se sont écoulées ? "))

# Calcul du nombre de périodes de doublement
nb_periodes = heures // temps_doublement

# Calcul de la population après croissance
population_finale = population_initiale * (2 ** nb_periodes)

# Affichage du résultat
print(f"Après {heures} heures, la population est estimée à {population_finale} bactéries.")
```

### Exercice 3 : Trouvez les erreurs et corrigez-les

Voici les erreurs dans **l’ordre d’apparition dans le code**, **corrigées une à une**, avec explications :

**1. `math` n’est pas importé**

**Erreur** : `NameError: name 'math' is not defined`

**Correction** :

```python
import math
```

Ajout en haut du script.

**2. Formule de l’aire latérale incorrecte**

```python
aire_lateral = math.pi * rayon * math.sqrt(rayon**2 + hauteur)
```

**Erreur** : la formule du cône utilise la **génératrice** ℓ, pas `√(rayon² + hauteur)`. Et ici, `hauteur` est encore une **chaîne de caractères** donc cela causera une **erreur de type** plus loin.

Mais avant d'y toucher, corrigeons d’abord l’erreur **suivante plus urgente** :


**3. `rayon` et `hauteur` sont des chaînes de caractères**

**Erreur** : `TypeError: unsupported operand type(s)` quand on tente un calcul mathématique sur des `str`.

**Correction** :

```python
r = float(input("Entrez le rayon du cône: "))
h = float(input("Entrez la hauteur du cône: "))
```

**4. Mauvais calcul de l’aire latérale**

**Erreur mathématique** : La bonne formule est
```math
$$
\text{Aire latérale} = \pi r \ell \quad \text{avec } \ell = \sqrt{r^2 + h^2}
$$
```
**Correction** :

```python
generatrice = math.sqrt(rayon**2 + hauteur**2)
aire_laterale = math.pi * rayon * generatrice
```

**5. Mauvais nom de variable `aire_latérale` au lieu de `aire_lateral`**

**Erreur** : `NameError: name 'aire_latérale' is not defined` (car on utilise un accent non défini)

**Correction** :

```python
surface = aire_base + aire_lateral
```

**6. Format incorrect de la dernière `print()`**

```python
print("La surface totale du cône est de {resultat} cm²")
```

**Erreur** : la chaîne affiche `{resultat}` littéralement.

**Correction** :

```python
print(f"La surface totale du cône est de {resultat:.2f} cm²")
```

(avec f-string et arrondi à 2 décimales)

**Code final corrigé** :

```python
import math

def surface_cone(rayon, hauteur):
    aire_base = math.pi * rayon ** 2
    generatrice = math.sqrt(rayon**2 + hauteur**2)
    aire_laterale = math.pi * rayon * generatrice
    surface = aire_base + aire_laterale
    return surface

r = float(input("Entrez le rayon du cône: "))
h = float(input("Entrez la hauteur du cône: "))

print("Rayon saisi:", r)
print("Hauteur saisie:", h)

resultat = surface_cone(r, h)

print(f"La surface totale du cône est de {resultat:.2f} cm²")
```