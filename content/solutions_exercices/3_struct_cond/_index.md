+++
pre = "<b>3.</b>"
title = " Structures conditionnelles"
weight = 203
draft = false
+++


## Exercice 1 : Demi-vie radioactive

```python
# Constantes
masse_initiale = 100  # en grammes
demi_vie = 5          # en années

# Entrée utilisateur
temps_ecoule = float(input("Combien d'années se sont écoulées ? "))

# Calcul
nb_periodes = temps_ecoule / demi_vie
masse_restante = masse_initiale * (0.5) ** nb_periodes

# Affichage conditionnel
if masse_restante < 1:
    print(f"La masse restante est très faible : {masse_restante:.4f} g. L’isotope est presque entièrement désintégré.")
else:
    print(f"Masse restante après {temps_ecoule} ans : {masse_restante:.2f} g.")
```

---

## Exercice 2 : Croissance bactérienne

```python
# Constantes
population_initiale = 500
periode = 3  # heures pour un doublement

# Entrée utilisateur
heures = float(input("Combien d’heures se sont écoulées ? "))

# Calcul
nb_periodes = heures / periode
population_finale = population_initiale * 2 ** nb_periodes

# Affichage conditionnel
if population_finale > 1_000_000:
    print(f"Alerte ! La population bactérienne a explosé : {population_finale:.0f} bactéries.")
else:
    print(f"Population estimée après {heures} heures : {population_finale:.0f} bactéries.")
```



---

## Exercice 3 – Température critique d’un liquide

```python
temperature = float(input("Entrez la température du liquide (en °C) : "))

if temperature < 80:
    print("Température sécuritaire.")
elif temperature == 80:
    print("Limite atteinte.")
else:
    print("Attention : température critique !")
```

---

## Exercice 4 – Classification du pH d’une solution

```python
ph = float(input("Entrez le pH de la solution (entre 0 et 14) : "))

if 0 <= ph < 7:
    print("Solution acide")
elif ph == 7:
    print("Solution neutre")
elif 7 < ph <= 14:
    print("Solution basique")
else:
    print("Valeur de pH invalide")
```

---

## Exercice 5 – Autorisation d’une réaction chimique

```python
temperature = float(input("Température en °C : "))
ph = float(input("pH de la solution : "))

if 25 <= temperature <= 45 and 6 <= ph <= 8:
    print("Réaction possible.")
else:
    print("Conditions non compatibles.")
```