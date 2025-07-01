+++
title = "Solution"
weight = 62
+++


## Exercice 1 – Table de multiplication


### Solution de base (avec boucle `for`)

```python
# Demande à l'usager un nombre entre 1 et 12
n = int(input("Entrez un nombre entre 1 et 12 : "))

# Vérifie que le nombre est valide
if 1 <= n <= 12:
    for i in range(1, 13):
        print(f"{i} x {n} = {i * n}")
else:
    print("Le nombre doit être entre 1 et 12.")
```


### **Variante** : ordre croissant ou décroissant

```python
n = int(input("Entrez un nombre entre 1 et 12 : "))

if 1 <= n <= 12:
    ordre = input("Voulez-vous l’ordre croissant (c) ou décroissant (d) ? ")
    if ordre.lower() == 'c':
        for i in range(1, 13):
            print(f"{i} x {n} = {i * n}")
    elif ordre.lower() == 'd':
        for i in range(12, 0, -1):
            print(f"{i} x {n} = {i * n}")
    else:
        print("Choix non reconnu.")
else:
    print("Le nombre doit être entre 1 et 12.")
```

### **Version bonus** : recommencer avec boucle `while`

```python
continuer = "oui"

while continuer.lower() == "oui":
    n = int(input("Entrez un nombre entre 1 et 12 : "))
    if 1 <= n <= 12:
        ordre = input("Ordre croissant (c) ou décroissant (d) ? ")
        if ordre.lower() == 'c':
            for i in range(1, 13):
                print(f"{i} x {n} = {i * n}")
        elif ordre.lower() == 'd':
            for i in range(12, 0, -1):
                print(f"{i} x {n} = {i * n}")
        else:
            print("Choix non reconnu.")
    else:
        print("Le nombre doit être entre 1 et 12.")
    
    continuer = input("Voulez-vous une autre table ? (oui/non) : ")
```

## Exercice 2

**But : utiliser une boucle `while` pour augmenter la température jusqu'à 30 °C**

```python
temp = 20  # température initiale

while temp < 30:
    print("Température actuelle :", temp, "°C")
    temp += 1.5  # on augmente de 1.5 °C par heure
```

### Ce que ça fait :

* Affiche la température de 20 °C à 28.5 °C (inclus).
* S’arrête lorsque temp atteint 30 ou plus.


## Exercice 3

**But : afficher les numéros des échantillons de 1 à 10**

```python
for i in range(1, 11):
    print("Échantillon", i)
```

### Ce que ça fait :

* Affiche :

  ```
  Échantillon 1
  Échantillon 2
  ...
  Échantillon 10
  ```

## Exercice 4 (Semaine 7)

**But : simuler un test qui s’arrête dès qu’il y a une mauvaise réponse**

```python
# On suppose que les bonnes réponses sont "A"
# et que l'étudiant fait une erreur à la 4e question

reponses = ["A", "A", "A", "B", "A", "A", "A", "A", "A", "A"]

for i in range(10):
    print("Question", i + 1)
    if reponses[i] != "A":
        print("Réponse incorrecte. Test terminé.")
        break
    else:
        print("Bonne réponse.")
```

### Ce que ça fait :

* Affiche les 3 premières bonnes réponses.
* À la 4e question, la réponse est fausse → le test s’arrête avec `break`.


## Exercice #4

## Exercice #5

## Exercice 6: Nombres décroissants sur chaque ligne

**Affichage :**

```
321
21
1
```

**Code :**

```python
for i in range(3, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
```

---

## Exercice 7: Triangle inversé aligné à droite

**Affichage :**

```
  1
 12
123
```

**Code :**

```python
n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
```


## Exercice 8: Triangle inversé avec espace et décalage

**Affichage :**

```
123
 12
  1
```


```python
n = 3
for i in range(n, 0, -1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
```


## Exercice 9: Triangle inversé symétrique avec des étoiles `*`

**Affichage :**

```
*****
 ***
  *
```

```python
n = 3
for i in range(n, 0, -1):
    etoiles = "*" * (2 * i - 1)
    espaces = " " * (n - i)
    print(espaces + etoiles)
```


