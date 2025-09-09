+++
pre = "<b>3.</b>"
title = " Structures conditionnelles"
weight = 303
draft = true
+++


```python
# Demander les données à l'utilisateur
temperature = float(input("Température de l'eau en °C : "))
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
    print("Pression invalide. Veuillez entrer 0.5, 1.0, 1.5 ou 2.0.")
    exit()

# Déterminer l’état de l’eau
if temperature < 0:
    etat = "solide"
    description = "L’eau est sous forme de glace."
elif temperature < ebullition:
    etat = "liquide"
    description = "L’eau est liquide à cette température et pression."
else:
    etat = "gaz"
    description = "L’eau est sous forme de vapeur."

# Affichage
print(f"État de l’eau : {etat}")
print(description)
```

---

## **Exemples de sorties**

### Exemple 1 :

```
Température de l'eau en °C : 50
Pression en atm (0.5, 1.0, 1.5 ou 2.0) : 1.0
État de l’eau : liquide
L’eau est liquide à cette température et pression.
```

### Exemple 2 :

```
Température de l'eau en °C : 101
Pression en atm (0.5, 1.0, 1.5 ou 2.0) : 1.0
État de l’eau : gaz
L’eau est sous forme de vapeur.
```

### Exemple 3 :

```
Température de l'eau en °C : -5
Pression en atm (0.5, 1.0, 1.5 ou 2.0) : 2.0
État de l’eau : solide
L’eau est sous forme de glace.
```