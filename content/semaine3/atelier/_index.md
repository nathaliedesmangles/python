+++
title = "Activité 3 - État physique de l’eau selon la température et la pression"
weight = 31
+++

## Objectifs pédagogiques

* Utiliser les structures conditionnelles `if`, `elif`, `else`
* Travailler avec les types numériques (`float`, `int`)
* Comprendre l’effet de la pression sur les températures de fusion et d’ébullition

---

## Énoncé

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

## Tâche demandée

Écris un programme Python qui :

1. Demande à l’utilisateur d’entrer :

   * La **température de l’eau en °C**
   * La **pression en atm** (choix parmi 0.5, 1.0, 1.5, 2.0)
2. Détermine et affiche l’**état physique de l’eau** : `"solide"`, `"liquide"` ou `"gaz"`.


## Exemples de fonctionnement attendus

```text
Température (°C) : 50
Pression (atm) : 1.0
→ État de l’eau : liquide
```

```text
Température (°C) : 101
Pression (atm) : 1.0
→ État de l’eau : gaz
```

```text
Température (°C) : -5
Pression (atm) : 2.0
→ État de l’eau : solide
```

## Pistes / rappels

* Utiliser des conditions imbriquées ou combinées (`if ... and ...`, `elif`)
* Pour simplifier, tu peux faire un `if` ou un `match` sur la pression pour définir le point d’ébullition
* Utilise des variables pour stocker les seuils

---

### Extension (facultatif)

* Gérer des cas d’erreurs (ex. : pression invalide)
* Afficher une petite phrase plus descriptive selon l’état :
  *"L’eau est sous forme de vapeur."* ou *"L’eau est liquide à cette température et pression."*

<!---

## Solution Python – État de l’eau selon température et pression**

```python
# Demander les données à l'utilisateur
temp = float(input("Température de l'eau en °C : "))
pression = float(input("Pression en atm (0.5, 1.0, 1.5 ou 2.0) : "))

# Déterminer le point d’ébullition selon la pression
if pression == 0.5:
    ebullition = 81
elif pression == 1.0:
    ebullition = 100
elif pression == 1.5:
    ebullition = 112
elif pression == 2.0:
    ebullition = 120
else:
    print("Pression invalide. Choisissez 0.5, 1.0, 1.5 ou 2.0.")
    ebullition = None

# Vérifier l’état de l’eau seulement si la pression est valide
if ebullition is not None:
    if temp < 0:
        etat = "solide"
        message = "L’eau est sous forme de glace."
    elif temp < ebullition:
        etat = "liquide"
        message = "L’eau est liquide à cette température et pression."
    else:
        etat = "gaz"
        message = "L’eau est sous forme de vapeur."

    print(f"→ État de l’eau : {etat}")
    print(message)
```

## Exemple d’exécution dans Jupyter Notebook

```
Température de l'eau en °C : 105
Pression en atm (0.5, 1.0, 1.5 ou 2.0) : 1.5
→ État de l’eau : liquide
L’eau est liquide à cette température et pression.
```

-->
