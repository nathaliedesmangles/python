+++
pre = "4."
title = " Boucles et débogage simple"
weight = 204
draft = true
+++


## Exercice 1 – **For ou While ?**

### a. Afficher les nombres de 1 à 10

**Boucle : `for`** (on connaît le début et la fin)

```python
for i in range(1, 11):
    print(i)
```

---

### b. Compter jusqu’à 100 par bonds de 10

**Boucle : `for`**

```python
for i in range(0, 101, 10):
    print(i)
```

---

### c. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)

**Boucle : `while`** (on ne connaît pas d’avance le nombre de répétitions, mais on connaît la condition d’arrêt)

```python
hauteur = 100
while hauteur > 0:
    print(f"Hauteur actuelle : {hauteur} m")
    hauteur -= 10
```

---

### d. Lire une température jusqu’à ce qu’elle soit < 0

**Boucle : `while`**

```python
temperature = float(input("Entrez une température : "))
while temperature >= 0:
    temperature = float(input("Entrez une température : "))
print("Température négative détectée. Fin du programme.")
```

---

### e. Tant que l'utilisateur ne tape pas 0

**Boucle : `while`, sans `break`**

```python
valeur = int(input("Entrez un chiffre entre 1 et 10 (0 pour quitter) : "))
while valeur != 0:
    valeur = int(input("Entrez un chiffre entre 1 et 10 (0 pour quitter) : "))
print("Fin du programme.")
```

**Boucle : `while`, avec `break` si nécessaire**

```python
while True:
    valeur = int(input("Entrez un chiffre entre 1 et 10 (0 pour quitter) : "))
    if valeur == 0:
        print("Fin du programme.")
        break
```

---
## Exercice 2 – Table de multiplication sans répétition

```python
n = int(input("Entrez un nombre entre 1 et 12 : "))
for i in range(1, 13):
    print(f"{i} x {n} = {i * n}")
```

## Exercice 2 – Table de multiplication avec répétition

```python
continuer = 1

while continuer != 0:
    n = int(input("Entrez un nombre entre 1 et 12 : "))
    for i in range(1, 13):
        print(f"{i} x {n} = {i * n}")
    
    continuer = input("Voulez-vous une autre table ? (1 = oui; 0 = non) : ")
```

---

## Exercice 3 – Température qui augmente jusqu’à 30 °C

```python
temp = 20.0

while temp < 30:
    print(f"Température actuelle : {temp:.1f} °C")
    temp += 1.5
```

---

## Exercice 4 – Boucle `for` avec `range`

```python
for i in range(1, 11):
    print(f"Échantillon {i}")
```

---

## Exercice 5 – Corriger les erreurs

### Version corrigée :

```python
nom = input("Quel est ton nom? ")
print("Bonjour", nom)

age = int(input("Quel âge as-tu? "))
print("Dans 10 ans, tu auras", age + 10)
```
