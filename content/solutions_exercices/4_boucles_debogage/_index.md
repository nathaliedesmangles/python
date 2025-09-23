+++
pre = "4."
title = " Boucles et débogage simple"
weight = 204
draft = false
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
    
    continuer = int(input("Voulez-vous une autre table ? (1 = oui; 0 = non) : "))
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

### 1re exécution du code

![Erreur de syntaxe](./erreur1.png?width=40vw)

**Explications** :
1. Le message dit : ***Erreur de syntaxe** : Syntaxe invalide. Peut-être vous avez oublié une virgule ?*
2. L’erreur est en lien avec la **syntaxe de print()**

**Correction** : on ajoute une virgule après les guillemets dans `print()`
![Modif-Erreur de syntaxe](./modif1.png?width=40vw)

### 2e exécution du code

![Erreur de syntaxe](./erreur2.png?width=40vw)

**Explications** :
1. Le message dit : ***Erreur de nom** : Le nom de la variable 'nom' n'est pas définit*
2. L’erreur est en lien avec la **le mauvais nom de variable utilisé**

**Correction** : on remplace `name` par `nom` dans le premier `print()`
![Modif-Erreur de nom](./modif2.png?width=30vw)

### 3e exécution du code

![Erreur de syntaxe](./erreur3.png?width=40vw)

**Explications** :
1. Le message dit : ***Erreur de type** : On peut seulement concaténer une variable de type str (pas int) à une autre variable de type str.*
2. L’erreur est en lien avec la **le calcul fait avec la variable `age`**. L'adition est sur une variable `str` et une variable `int`.

**Correction** : on converti l'entrée au clavier (`age`) en entier avec `int()` pour que le calcul puisse se faire dans le `print()`
![Modif-Erreur de type](./modif3.png?width=40vw)

### Version corrigée :

```python
nom = input("Quel est ton nom? ")
print("Bonjour", nom)

age = int(input("Quel âge as-tu? "))
print("Dans 10 ans, tu auras", age + 10)
```
**Résultat** :
```
Bonjour Nath
Dans 10 ans tu auras 25 ans
```