+++
title = "Solution"
weight = 42
+++

## État de l’eau selon température et pression

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
sÉtat de l’eau : liquide
L’eau est liquide à cette température et pression.
```
