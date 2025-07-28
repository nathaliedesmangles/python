+++
chapter = true
pre = "<b>6.</b>"
title = " Listes et chaînes de caractères et boucle for"
weight = 106
draft = false
+++

## Objectifs

À la fin de cette leçon, vous devrez être capable de :

* Créer, modifier et parcourir une **liste simple**.
* Manipuler des **listes imbriquées** (listes dans un liste).
* Appliquer les notions des listes simples sur les chaines de caractères. 
* Savoir identifier quand utiliser une boucle `for` vs. `while`.

---

## Qu’est-ce qu’une liste ?

Une **liste**, c’est un **conteneur** dans lequel on peut ranger plusieurs éléments (nombres, chaînes, booléens, etc.).

C’est un peu comme une boîte à compartiments.

```python
ma_liste = [3, 7, 42, 5]
```

Chaque élément a une **position** (appelée *indice*).

```python
print(ma_liste[0])  # Affiche 3 (le premier élément)
print(ma_liste[2])  # Affiche 42
```

## Créer et modifier une liste

### Créer une liste vide

```python
liste_vide = []
```

### Ajouter des éléments

```python
fruits = ["pomme", "banane"]
fruits.append("cerise")  # ["pomme", "banane", "cerise"]
```

### Remplacer un élément

```python
fruits[1] = "poire"  # ["pomme", "poire", "cerise"]
```

## Parcourir une liste avec la boucle `for`

La boucle `for` est utilisée quand **on connaît d’avance** combien de fois on doit répéter.

Avec une boucle `for`. La syntaxe générale de la boucle est:

```python
for variable in sequence:
    instructions à répéter jusqu'à la fin de la séquence.
```

**Exemple** :

```python
fruits = ["pommes", "poires", "cerises"]

for fruit in fruits:
    print(f"J'aime les {fruit}")

# Affiche:
J'aime les pommes
J'aime les poires
J'aime les cerises
```

**Explication** : 
* La variable `fruit` prendra comme valeur, les éléments de la liste `fruits` un à un.

Avec les indices :

```python
for i in range(len(fruits)):
    print(f"L'indice {i} contient : {fruits[i]}")

# Affiche:
L'indice 0 contient : pomme
L'indice 1 contient : poire
L'indice 2 contient : cerise
```
**Explication** : 
* La fonction `` génère des nombres entiers de 0 à 2 (qui est le nombre d'éléments dans la liste - 1)
* `len(fruits)` vaut 3, le nombre d'éléments dans la liste.
* La variable `i` prendra les valeurs `0, 1 et 2`.
* `fruits[i]` contient un à un les fruits de la liste `fruits`.


## Fonctions utiles sur les listes simples

| Méthode / Fonction       | Description                                    | Exemple                      |
| ------------------------ | ---------------------------------------------- | ---------------------------- |
| `append(valeur)`         | Ajoute un élément à la fin                     | `ma_liste.append(10)`        |
| `insert(indice, valeur)` | Insère une valeur à une position donnée        | `ma_liste.insert(1, 99)`     |
| `pop(indice)`            | Retire l’élément à l’indice (ou le dernier)    | `ma_liste.pop()`             |
| `remove(valeur)`         | Retire la **première** occurrence d'une valeur | `ma_liste.remove(42)`        |
| `len()`                  | Donne la longueur de la liste                  | `len(ma_liste)`              |
| `sorted()`               | Trie la liste sans la modifier                 | `sorted(ma_liste)`           |
| `sort()`*                | Trie la liste en la modifiant                  | `ma_liste.sort()`            |
| `reverse()`              | Inverse l’ordre des éléments                   | `ma_liste.reverse()`         |
| `in`                     | Vérifie si un élément est dans la liste        | `"pomme" in fruits` → `True` |
| `index(valeur)`          | Renvoie l’indice de la première occurrence     | `fruits.index("poire")`      |
| `count(valeur)`          | Compte combien de fois un élément apparaît     | `fruits.count("poire")`      |
| `max()`                  | Trouver le max                                 | `max(ma_liste)`              |
| `min()`                  | Trouver le min                                 | `min(ma_liste)`              |
| `sum()` 		   | Calculer une somme des éléments		    | `s = sum(ma_liste)`

**Exemple** : Calcul de la moyenne d’une liste de notes

```python
notes = [85, 90, 78]
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne:.2f}")
```

{{% notice style="accent" title="*Important" %}}
* `mots.sort()` utilisé sur une liste de chaines de caractères trie la liste en respectant l’ordre **Unicode**, ce qui fait que les **mots commençant par une majuscule** sont placés **avant ceux en minuscules**.

```python
mots = ["pomme", "Banane", "abricot", "Orange"]
mots.sort()
print(mots)

# Affichage : 
['Banane', 'Orange', 'abricot', 'pomme']
```
{{% /notice %}}


## Listes imbriquées

Une **liste imbriquée**, c’est une liste **qui contient d'autres listes**.

**Exemple** : Une liste contenant trois listes

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Accéder à un élément précis

* Il faut préciser les **deux indices**: `[rangée][colonne]`
```python
print(matrice[0][2])  # Affiche 3 qui se trouve sur la première rangée (indice 0) et la 3e colonne (indice 2). 
```

### Parcourir une liste imbriquée

* Il faut utiliser **deux boucles** `for`.
* La première boucle pour **parcourir chaque rangée une à la fois**.
* La deuxième boucle (à l'intérieur de la première) pour parcourir les éléments d'une rangée.

```python
for ligne in matrice:
    for valeur in ligne:
        print(valeur)
```

**Exemple** : afficher une grille 3x3

```python
grille = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

for ligne in grille:
    for valeur in ligne:
        print(valeur)

# Affiche:
X
O
X
O
X
O
O
X
X
```

---

{{% notice style="blue" title="À retenir (listes)" groupid="notice-toggle" expanded="false" %}}
* Une liste permet de **stocker plusieurs valeurs**.
* On accède aux éléments avec des **indices**.
* Les listes peuvent être **modifiées** facilement.
* Une liste peut contenir **d'autres listes** → super utile pour représenter des tableaux ou des grilles.
{{% /notice %}}

---

## Les chaînes de caractères sont des listes

On peut manipuler une chaine de caractère comme une suite de lettres ou une **liste** de lettres.

```python
message = "Bonjour à tous!"
print(message[0])     # 'B' (le premier caractère)
print(message[-1])    # '!' (le dernier caractère)
print(message[-7])    # 'à' 
```
{{% notice style="cyan" title="Sachez que..." %}}
Les espaces comptent dans le calcul du nombre de caractères dans une chaine.
{{% /notice %}}

### Parcourir une chaîne

```python
for lettre in message:
    print(lettre)
```

### Longueur d’une chaîne

```python
len(message)  # Nombre de caractères, incluant les espaces
```

### Fonctions utiles sur les chaînes

| Objectif                                     | Code Python                           |
| -------------------------------------------- | ------------------------------------- |
| Passer en minuscules                         | `message.lower()`                     |
| Passer en majuscules                         | `message.upper()`                     |
| Enlever les espaces autour                   | `texte.strip()`                       |
| Séparer une chaîne en morceaux               | `message.split(" ")`                  |
| Remplacer un mot                             | `message.replace("Bonjour", "Salut")` |
| Trouver la position d’un mot/lettre          | `message.find("bio")`                 |
| Compter le nombre de fois qu’un mot apparaît | `message.count("e")`                  |

{{% notice style="blue" title="À retenir (chaines de caractères)" groupid="notice-toggle" expanded="false" %}}
* Une chaine de caractères se manipule comme une liste simple, dont les éléments sont des caractères (incluant l'espace).  
{{% /notice %}}

## La boucle `for` avec `range()`

Utilisée quand **on connaît d’avance** combien de fois répéter.

### Syntaxe :

```python
for i in range(début, fin, pas):
    instructions
```

* `début` : valeur initiale (optionnel, par défaut = 0)
* `fin` : valeur **non incluse**
* `pas` : saut entre chaque valeur (optionnel, par défaut = 1)

**Exemple** :

```python
for i in range(0, 5):
    print("i =", i)
```

> Affiche les valeurs de 0 à 4.



{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* `for` avec `range()` : Utilisée lorsque le nombre de répétitions est connu d'avance.  
   * Équivaut à dire:  
      * **POUR CHAQUE** *tour de boucle* **FAIRE...** ou
      * **POUR CHAQUE** *valeur d'une séquence* **FAIRE...**
{{% /notice %}}


---

## Exercices à faire avant le cours

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_boucles.ipynb)


### Listes

#### Exercice 1 :

* Crée une liste contenant 5 animaux. Affiche chaque animal avec une phrase du type :
```text
Voici un/une <animal>
```
 
#### Exercice 2 :

* Crée une grille de 5 lignes et 4 colonnes (liste de listes) contenant des chiffres. 
* Affiche tous les chiffres un par un.

#### Exercice 3 :

* Demande à l’utilisateur d’entrer 3 noms et stocke-les dans une liste.
* Affiche chaque animal en ordre alphabétique croissant.  
* Affiche chaque animal en ordre alphabétique décroissant. 

#### Exercice 4

* Crée une liste de séquences :
```python
suspects = [
    ["A", "T", "C", "G"],
    ["G", "A", "T", "G"],
    ["A", "T", "T", "G"]
]
```
* Affiche la 2e base de la 1re séquence.
* Affiche la dernière base de la 3e séquence.

---

### Chaines de caractères

#### Exercice 5 - Créer une liste de nombres à partir d'une liste de mots

* Utiliser une boucle pour obtenir le nombre de lettres de chaque mot
* Pour chacun des mots, ajouter son nombre de lettres dans la liste `nb_lettres`.

```python
mots = ["chlorophylle", "atome", "protéine"]
nb_lettres = []
```

#### Exercice 6 - Convertir en ARN

Une séquence d’ADN est "ATGCT".

* Mets-la en minuscules.
* Remplace les "t" par "u".

---

===

### Exercice 1 - For ou While ?

Pour chacun des contextes suivants, avant d'écrire le code, répondez à la question: "Quelle boucle devriez-vous utiliser ?":

a. Afficher les nombres de 1 à 10  
b. Compter jusqu’à 100 par bonds de 10  
c. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)  
d. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)  
e. Écrire un programme qui :  
&nbsp;&nbsp;&nbsp;&nbsp; i. Affiche deux choix :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. "Entrez votre prénom"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2."Quitter le programme"  
&nbsp;&nbsp;&nbsp;&nbsp; ii. Demande à l'utilisateur d'entrer son choix (`1` ou `2`) et tant qu'il choisi l'option 1, le programme lui redemande d'entrer son prénom. Si c'est 2, le programme s'arrête (Vous pouvez utiliser `break` ou afficher un message).  


### Exercice 3 – Répéter une mesure fixe avec `for`

On veut afficher les numéros de 10 échantillons : `Échantillon 1`, `Échantillon 2`, ..., `Échantillon 10`.

1. Utilise une boucle `for` avec `range(1, 11)`.
2. À chaque tour, affiche `Échantillon` suivi du numéro.

---

## À faire avant le prochain cours

1. Lire la matière sur [Listes, chaines et graphiques de base](../semaine7/)
2. Faire les [exercices se trouvant à la fin de la leçon 7](../semaine7/#exercices-à-faire-avant-le-cours)
