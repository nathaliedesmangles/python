+++
chapter = true
pre = "<b>6.</b>"
title = " Répéter avec `for` et `while`"
weight = 106
draft = true
+++

## Objectifs de la leçon

* Comprendre l’utilité des boucles en programmation.
* Savoir écrire des boucles `while` et `for`.
* Savoir identifier quand utiliser une boucle `for` vs. `while`.
* Interrompre le déroulement d'une boucle.
* Appliquer les boucles à des cas concrets en sciences.

---

## À quoi servent les boucles ?

Elles permettent de répéter des instructions plusieurs fois, soit un nombre connu, soit jusqu’à ce qu’une condition soit atteinte.


## La boucle `while`

Utilisée quand **on ne connaît pas d’avance** combien de fois répéter.

### Syntaxe :

```python
while condition:
    instructions
```

### Exemple :

```python
compteur = 0
while compteur < 5:
    print("Valeur :", compteur)
    compteur += 1
```

Tant que la condition est vraie (`compteur < 5`), on exécute le bloc.  
Il faut **modifier l'état de la condition dans la boucle** pour éviter une boucle infinie.

### Exemples de boucle infinie:

**Cas 1**: oublier de modifier l'état de la condition

```python
temp = 100  # température initiale
while temp > 0:
    print(f"Température : {temp} °C")
    					# temp n'est pas modifié 
```

**Cas 1**: oublier de modifier l'état de la condition
```python
temp = 100  # température initiale
while temp > 0:
    print(f"Température : {temp} °C")
    temp += 10				# Erreur de logique
```

## La boucle `for` avec `range()`

Utilisée quand **on connaît d’avance** combien de fois répéter.

### Syntaxes :

#### Cas #1
```python
for i in range(n):
    instructions
```

* `n` est un entier positif.
* Quelque soit `n`, la boucle sera exécutée `n - 1` fois.

#### Exemple :
```python
for i in range(5):
    print("i =", i)
```

Affiche les valeurs de 0 à 4.

#### Cas #2
```python
for i in range(début, fin):
    instructions
```

* `début` : valeur initiale (optionnel, par défaut = 0)
* `fin` : valeur **non incluse**

#### Exemple :
```python
for i in range(1, 5):
    print("i =", i)
```

Affiche les valeurs de 1 à 4.

#### Cas #3
```python
for i in range(début, fin, pas):
    instructions
```

* `début` : valeur initiale (optionnel, par défaut = 0)
* `fin` : valeur **non incluse**
* `pas` : saut entre chaque valeur (optionnel, par défaut = 1)

### Exemple :
```python
for i in range(0, 5, 2):
    print("i =", i)
```

Affiche les valeurs de 0, 2 et 4.


## Interrompre une boucle

* `break` : arrête **immédiatement** la boucle.
* `continue` : saute **à l’itération suivante**.

### Exemple avec `break` :

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Affiche 0 à 4. S’arrête à 5.

```python
compteur = 0
while compteur < 10:
    if compteur == 5:
        break
    print("Valeur :", compteur)
    compteur += 1
```


## À éviter / pièges fréquents

* Boucle infinie (`while` sans mise à jour de la condition)
* Utiliser `range` sans comprendre que la fin est **exclusive**
* Oublier l’indentation dans le bloc de la boucle

---

## Exercice guidé - Boucle `for` ou `while` ?

Pour chacun des contextes suivants, avant d'écrire le code, répondez à la question: "Quelle boucle devriez-vous utiliser ?":

1. Afficher les nombres de 1 à 10
2. Compter jusqu’à 100 par bonds de 10
3. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)
4. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)
5. Écrire un programme qui :
   a) Affiche deux choix : 1-"Entrez votre prénom" et 2-"Quitter le programme"
   b) Demande à l'utilisateur d'entrer son choix (`1` ou `2`) et tant qu'il choisi l'option 1, le programme lui redemande d'entrer son prénom. Si c'est 2, le programme s'arrête (Vous pouvez utiliser `break` ou afficher un message).

{{% notice style="cyan" title="À retenir" %}}
* Les boucles permettent d’automatiser les calculs et traitements de données en science
* `while` = tant qu’une **condition** est vraie. Quand l’utiliser ? Lorsqu'on ne connait pas d'avance le nombre de répétitions.
* `for` = pour **chaque valeur** dans une séquence. Quand l’utiliser ? Lorsque le nombre de répétitions est connu d'avance.
{{% /notice %}}

