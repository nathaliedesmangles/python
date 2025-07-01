+++
title = "Atelier 4"
weight = 41
+++

## Objectifs pédagogiques

* Utiliser les opérateurs de comparaison et logiques.
* Utiliser les structures conditionnelles `if`, `elif`, `else`.
* Travailler avec les types numériques (`float`, `int`).

---

## Exercice 1

### Contexte

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

### À faire

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

* Utiliser des conditions imbriquées ou combinées (`if ... and ...`, `elif`)
* Pour simplifier, tu peux faire un `if` sur la pression pour définir le point d’ébullition
* Utilise des variables pour stocker les seuils


### Bonus (facultatif)

* Gérer des cas d’erreurs (ex. : pression invalide)
* Afficher une petite phrase plus descriptive selon l’état :
* *"L’eau est sous forme de vapeur."* ou *"L’eau est liquide à cette température et pression."*