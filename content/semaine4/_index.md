+++
chapter = true
pre = "<b>4.</b>"
title = " Décider avec `if`, `elif`, `else`, répéter avec `while`"
weight = 104
+++


## Objectifs

* Identifier et utiliser correctement les opérateurs de comparaison et logiques pour évaluer des conditions simples en Python.
* Écrire des structures conditionnelles (`if`, `elif`, `else`) pour contrôler le déroulement d’un programme selon différentes situations.
* Appliquer les structures conditionnelles à des contextes scientifiques simples.
* Répéter des instructions tant qu'une condition est vraie, avec la boucle `while`.
* Interrompre le déroulement d'une boucle.
---


## Les opérateurs de comparaison

Ces opérateurs permettent de comparer des valeurs. Le résultat est **toujours un booléen** : `True` (vrai) ou `False` (faux).

| Opérateur | Signification        | Exemple  | Résultat |
| --------- | -------------------- | -------- | -------- |
| `==`      | égal à               | `5 == 5` | `True`   |
| `!=`      | différent de         | `3 != 4` | `True`   |
| `<`       | plus petit que       | `2 < 5`  | `True`   |
| `<=`      | plus petit ou égal à | `5 <= 5` | `True`   |
| `>`       | plus grand que       | `7 > 4`  | `True`   |
| `>=`      | plus grand ou égal à | `6 >= 9` | `False`  |

> Dans une cellule de Code, testez les exemples du tableau.


## Les opérateurs logiques

Ils permettent de **combiner plusieurs conditions**.

| Opérateur | Signification            | Exemple               | Résultat |
| --------- | ------------------------ | --------------------- | -------- |
| `and`     | et (toutes vraies)       | `(4 < 5) and (6 > 3)` | `True`   |
| `or`      | ou (au moins une vraie)  | `(4 < 5) or (6 < 3)`  | `True`   |
| `not`     | négation                 | `not (4 < 5)`         | `False`  |

> Dans une cellule de Code, testez les exemples du tableau.

## Les structures conditionnelles

Elles permettent **d’exécuter un bloc de code seulement si une condition est vraie**.

### L'instruction *if*

> Pour exécuter du code **si une condition est vraie**.

```python
if condition:
    # Bloc de code exécuté si la condition est vraie
```

**Exemple :**

```python
age = 20
if age >= 18:
    print("Majeur")
```


### L'instruction *if*-*else*

> Pour exécuter du code **si une condition est fausse**.

```python
if condition:
    # Si la condition est vraie
else:
    # Sinon (condition fausse)
```

**Exemple :**

```python
age = 16
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```


### L'instruction *if*-*elif*-*else*

> Pour tester **plusieurs cas différents** et exécuter du code différent selon le cas.

{{% notice style="accent" title="Important" %}}
* **Si la condition du `if` est fausse**, un seul `elif` sera exécuté.  
* **Si et seulement si toutes les conditions** (`if` et tous les `elif`) **sont fausses**, le `else` sera traité.
{{% /notice %}}

```python
if condition1:
    # Si condition1 est vraie
elif condition2:
    # Sinon, si condition2 est vraie
elif condition3:
    # Sinon, si condition3 est vraie
else:
    # Sinon (aucune condition vraie)
```

**Exemple :**

```python
note = 85

if note >= 90:
    print("Excellent")
elif note >= 75:
    print("Très bien")
elif note >= 60:
    print("Passable")
else:
    print("Échec")
```

{{% notice style="accent" title="Important" %}}
* **Les deux-points (`:`)** sont obligatoires à la fin des lignes `if`, `elif` et `else`.
* **L'indentation** est essentielle : elle délimite le bloc de code à exécuter.
{{% /notice %}}

> Dans des cellules de Code dans VS Code, testez les exemples des instructions `if`, `elif` et `else`.

## À quoi servent les boucles ?

Répéter des instructions plusieurs fois, soit un nombre connu (`for`), soit jusqu’à ce qu’une condition soit atteinte (`while`).

## La boucle `while`

Utilisée quand **on ne connaît pas d’avance** combien de fois répéter.

### Syntaxe :

```python
while condition:
    instructions
```

**Exemple** :

```python
compteur = 0
while compteur < 5:
    print("Valeur :", compteur)
    compteur += 1
```

> Tant que la condition (`compteur < 5`) est vraie , on exécute le bloc (`print` et `compteur +=1`).

{{% notice style="accent" title="Important" %}}
Il faut **modifier l'état de la condition dans la boucle** pour éviter une boucle infinie. Dans l'exemple, c'est à ça que sert l'instruction `compteur += 1`
{{% /notice %}}


### Boucle infinie

C'est lorsque la boucle ne s'arrête jamais. Cela peut arriver principalement dans deux situations:

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

#### Arrêter une boucle infinie

> Cliquer dans la case **Arrêter l'exécution des cellules** se trouvant à gauche de la cellule contenant la boucle infinie

![Arrêt d'une boucle infinie dans VS Code Jupyter](./arret_boucle_infinie.png?width=35vw)

## Interrompre une boucle

* `break` : arrête **immédiatement** la boucle.
* `continue` : saute **à l’itération suivante**.

**Exemple avec `break`** :

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

> Affiche 0 à 4. S’arrête à 5.

```python
compteur = 0
while compteur < 10:
    if compteur == 5:
        break
    print("Valeur :", compteur)
    compteur += 1
```

> Affiche : 
``` 
Valeur : 0  
Valeur : 1  
Valeur : 2  
Valeur : 3  
Valeur : 4  
```
### Exemple avec `continue`

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue  # On saute les multiples de 3
    print(i)
```

> Affiche:
```
1
2
4
5
7
8
10
```

{{% notice style="cyan" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* Les **opérateurs de comparaison** comparent des valeurs.
* Les **opérateurs logiques** combinent plusieurs conditions.
* Les **structures conditionnelles** permettent de **réagir à des critères** dans un programme.
* **Les deux-points (`:`)** sont obligatoires à la fin des lignes `if`, `elif` et `else`.
* **L'indentation** (souvent 4 espaces) est essentielle : elle délimite le bloc de code à exécuter.
* Il peut y avoir **autant de `elif` que nécessaire**, mais **un seul `if` et au plus un seul `else`**.
	* `if` vérifie si une condition est vraie, **si et seulement si c'est le cas**, les instructions en dessous seront exécutées.
	* `elif` permet de vérifier une autre condition, **si et seulement si la condition du `if` est fausse ET celle du `elif` est vraie**, les instructions en dessous et décalées seront exécutées.
	* `else` permet de prévoir des instructions à effectuer, **si et seulement si aucune des conditions précédentes n'est vraie**.
* Les boucles permettent d’automatiser les calculs et traitements de données.
* `while` : Utilisée lorsqu'une condition doit être respectée pour que la boucle s'exécute.
   * Équivaut à dire: **TANT QUE** *condition est vraie* **FAIRE...**
{{% /notice %}}

---

### Exercices à faire avant le cours

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_struct_cond.ipynb)

### Partie 1 – Comprendre les opérateurs de comparaison

**1.1** Quelle sera la sortie du code suivant ?

```python
a = 10
b = 7
print(a > b)
print(a == 7)
```

**1.2** Complète avec `True` ou `False` :

| Expression | Résultat |
| ---------- | -------- |
| `5 != 3`   |          |
| `8 <= 8`   |          |
| `4 > 10`   |          |
| `3 == 3`   |          |

---

### Partie 2 – Explorer les opérateurs logiques

**2.1** Écris le résultat de chacune des expressions suivantes :

| Expression             | Résultat |
| ---------------------- | -------- |
| `(5 > 2) and (7 < 10)` |          |
| `(3 != 3) or (6 >= 6)` |          |
| `not (2 < 5)`          |          |

**2.2** Dans quel cas cette condition sera-t-elle vraie ?

```python
(temperature > 30) and (humidite < 50)
```

---

### Partie 3 – Lire et prédire des structures conditionnelles

**3.1** Que va afficher ce code si `temp = 10` ?

```python
if temp > 25:
    print("Il fait chaud.")
elif temp > 15:
    print("Il fait confortable.")
else:
    print("Il fait frais.")
```

**3.2** Le code suivant contient une erreur. Saurais-tu la repérer ?

```python
if vitesse > 80
    print("Trop vite !")
```

---

### Partie 4 – Écrire ses propres conditions

**4.1** Complète ce programme pour qu’il affiche :

* `"Solution acide"` si le pH est plus petit que 7
* `"Solution neutre"` si le pH est égal à 7
* `"Solution basique"` si le pH est plus grand que 7

```python
ph = 6.4

# ton code ici
```

**4.2** Crée une condition `if` qui affiche `"Attention, danger"` seulement si une température dépasse 100 **et** qu'une pression est plus grande que 1.5 atm.

```python
temperature = 110
pression = 1.6

# ton code ici
```

### Partie 5 - Répéter, mais pas à l'infini

#### Exercice – Utiliser `while` pour atteindre un objectif

Une température initiale est de 20 °C. Chaque heure, elle augmente de 1,5 °C.
Écrire un programme qui affiche l’évolution de la température **jusqu’à ce qu’elle atteigne 30 °C**.

1. Crée une variable `temp` avec 20 comme valeur initiale.
2. Utilise une boucle `while` pour vérifier si `temp` est inférieure à 30.
3. À chaque tour, affiche la température.
4. Augmente la température de 1.5.

---

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **premier examen** (20%)

1. Lire la matière sur [Listes, chaines de caractères et boucle for](../semaine6/)
2. Faire les [exercices se trouvant à la fin de la leçon 6](../semaine6/#exercices-à-faire-avant-le-cours)

