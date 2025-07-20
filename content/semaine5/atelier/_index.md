+++
title = "Atelier 5"
weight = 105
+++

## Objectifs

* Utiliser les opérateurs de comparaison et logiques.
* Utiliser les structures conditionnelles `if`, `elif`, `else`.
* Travailler avec les types numériques (`float`, `int`).

---

## Exercice

L’état physique de l’eau dépend de la température et de la pression. À **pression atmosphérique normale (1 atm)** :

* L’eau gèle à 0 °C et bout à 100 °C.
* En **altitude**, la pression est plus faible, donc l’eau bout à une température plus basse.
* En **autocuiseur**, la pression est plus élevée, donc l’eau bout à une température plus élevée.

On suppose ici un modèle très simple :

| Pression (atm) | Température d’ébullition (°C) |
| -------------- | ----------------------------- |
| 0.5            | 81                            |
| 1.0            | 100                           |
| 1.5            | 112                           |
| 2.0            | 120                           |

Le point de congélation demeure à 0 °C peu importe la pression.

Écris un programme Python qui :

1. Demande à l’utilisateur d’entrer :

   * La **température de l’eau en °C**
   * La **pression en atm** (choix parmi 0.5, 1.0, 1.5, 2.0)

2. Détermine et affiche l’**état physique de l’eau** : `"solide"`, `"liquide"` ou `"gaz"`.


## Exemples de fonctionnements attendus

```text
Température (°C) : 50
Pression (atm) : 1.0
État de l’eau : liquide
```

```text
Température (°C) : 101
Pression (atm) : 1.0
État de l’eau : gaz
```

```text
Température (°C) : -5
Pression (atm) : 2.0
État de l’eau : solide
```

## Pistes / rappels

* Utiliser des conditions imbriquées ou combinées (`if ... and ...`, `elif`).
* Pour simplifier, vous pouvez faire un `if` sur la pression pour définir le point d’ébullition.
* Utilisez des variables pour stocker les seuils.

## Exemple d’exécution

```
Température de l'eau en °C : 105
Pression en atm (0.5, 1.0, 1.5 ou 2.0) : 1.5
sÉtat de l’eau : liquide
L’eau est liquide à cette température et pression.
```

## Version améliorée

* Gérer des cas d’erreurs (ex. : pression invalide)
* Afficher une petite phrase plus descriptive selon l’état :
* *"L’eau est sous forme de vapeur."* ou *"L’eau est liquide à cette température et pression."*

{{% notice style="magenta" title="Gérer des cas d'erreur: Utiliser la valeur None" groupid="notice-toggle" expanded="false" %}}
## Qu’est-ce que `None` en Python ?

* `None` est une **valeur spéciale** en Python.
* Elle représente **l'absence de valeur** ou **"rien"**.

## Pourquoi utiliser `None` ?

* Pour **vérifier si une variable est encore vide**.
* Pour **initialiser une variable** sans lui donner de valeur tout de suite.
* Pour **indiquer qu’une fonction ne retourne rien**.

---
## Exemple 1 – Vérifier si une variable est vide

```python
reponse = None

if reponse is None:
    print("Aucune réponse reçue.")
```

> Attention : on teste `None` avec `is` et non `==` dans les bonnes pratiques Python :

```python
if variable is None:
   

## Exemple 2 – Variable vide au départ

```python
resultat = None  # on ne connaît pas encore le résultat

# plus tard...
resultat = 42
```

## Exemple 3 – Fonction sans return

```python
def afficher_message():
    print("Bonjour!")

x = afficher_message()
print(x)  # Affiche : None (car la fonction ne retourne rien)
```
{{% /notice %}}