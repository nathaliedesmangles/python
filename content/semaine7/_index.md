+++
chapter = true
pre = "<b>7.</b>"
title = " Listes, chaînes de caractères et graphiques de base"
weight = 107
draft = false
+++


## Objectifs

* Comprendre ce qu’est une **liste** en Python.
* Savoir créer, modifier et parcourir une **liste simple**.
* Manipuler des **listes imbriquées** (listes dans un liste).
* Appliquer les notions des listes simples sur les chaines de caractères.  
* Créer, afficher, embellir et enregistrer des graphiques simples avec la bibliothèque `matplotlib`.
* Connaître les principales **fonctions utiles** pour les **listes/chaines** et **graphiques** de base.

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

## Parcourir une liste

Avec une boucle `for` :

```python
for fruit in fruits:
    print(f"J'aime les {fruit}")

# Affiche:
J'aime les pomme
J'aime les poire
J'aime les cerise
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
* `len(fruits)` vaut 3.
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

---

## Visualiser les données avec Matplotlib (graphiques de base)

Pour pouvoir visualiser des données sous forme de graphiques, nous utiliserons le module `pyplot` de la bibliothèque `matplotlib`.

### Importer `matplotlib.pyplot`

La partie de `matplotlib` qu'on utilise le plus pour créer des graphiques s'appelle `pyplot`.

```python
import matplotlib.pyplot as plt
```

On utilise souvent l’abréviation `plt` pour simplifier l’écriture.


### Tracer une courbe simple avec `plot()`

La fonction `plot()` prend deux listes (ou deux tableaux) :

* La première représente l’axe **x**
* La seconde représente l’axe **y**

```python
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
```

{{% notice style="cyan" title="Sachez qu'..." %}}
À ce stade, rien ne s'affiche encore. Il faut une dernière commande pour voir le graphique.
{{% /notice %}}


### Afficher le graphique avec `show()`

La commande `show()` sert à **afficher la figure** dans une nouvelle fenêtre.

```python
plt.show()
```

**Résultat** : Une courbe représentant les points (0,0), (1,1), (2,4), (3,9), (4,16).
![Figure 1](./Figure_1.png?width=45vw)
---

### Exemple complet

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()
```

### Personnaliser le trait de la courbe (Style de ligne, couleur, marqueur)

```python
plt.plot(x, y, color='green', linestyle='--', marker='o')
```

**Résultat**
![Figure 2](./Figure_2.png?width=45vw)


### Options les plus courantes pour la méthode `plt.plot()`

| **Option**           | **Description**                             | **Exemple**              |
| -------------------- | ------------------------------------------- | ------------------------ |
| `color` ou `c`       | Couleur de la courbe                        | `color='red'` ou `c='r'` |
| `linestyle` ou `ls`  | Style de ligne : continue, pointillée, etc. | `ls='--'`                |
| `linewidth` ou `lw`  | Épaisseur de la ligne                       | `lw=2`                   |
| `marker`             | Symbole pour marquer les points             | `marker='o'`             |
| `markersize` ou `ms` | Taille des marqueurs                        | `ms=8`                   |
| `label`              | Nom de la courbe (pour la légende)          | `label='x²'`             |
| `alpha`              | Transparence (0 = invisible, 1 = opaque)    | `alpha=0.7`              |

```python
plt.plot(x, y, color='blue', linestyle='--', marker='o', label='x²', linewidth=2)
plt.legend()
```

Cela trace une courbe en **bleu**, avec une **ligne pointillée**, des **cercles aux points**, une **légende "x²"**, et une **ligne épaisse**.


### Ajouter un titre, des étiquettes et une grille

* `plt.title("Courbe de y = x²")` : Ajoute un **titre** au graphique.
* `plt.xlabel("x")` et `plt.ylabel("y")` : Donnent un **nom à l’axe horizontal** (ici, "x") et un **nom à l’axe vertical** (ici, "y").
* `plt.grid()` : Affiche une **grille** pour mieux lire les valeurs sur le graphique (optionnel mais utile).


```python
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)

plt.title("Courbe de y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()
```

**Résultat**
![Figure 3](./Figure_3.png?width=45vw)

### Tracer plusieurs courbes sur un même graphique et ajouter une légende

* Il suffit d'utiliser autant de `plt.plot()` qu'il y a de courbes à tracer.
* La fonction `plt.legend()` affiche une **légende** sur le graphique.
* Elle permet d’**identifier** les courbes ou les éléments tracés, à condition qu’ils aient été nommés avec `label=`.

```python
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 2, 3, 4, 8]

plt.plot(x, y1, label="objet A")
plt.plot(x, y2, label="objet B")

plt.title("Deux courbes sur le même graphique")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()  # Affiche la légende

plt.show()
```

> Cela ajoutera une petite boîte dans le coin du graphique indiquant "Courbe 1" et "Courbe 2".

**Résultat**
![Figure 4](./Figure_4.png?width=45vw)


### Enregistrer un graphique sous forme d'image

La fonction `plt.savefig("figure.png")` **enregistre** le graphique dans un fichier image (ici au format PNG).
Cela permet de conserver ou partager le graphique même sans afficher la fenêtre graphique.

```python
plt.plot(x, y)
plt.savefig("figure.png")
```

> Le fichier "figure.png" sera créé dans le même dossier que le fichier `.ipynb`.


### Fonctions de base pour les graphiques

| Fonction / Méthode             | Rôle principal                                     | Exemple minimal                |
| ------------------------------ | -------------------------------------------------- | ------------------------------ |
| `plt.plot(x, y)`               | Trace une courbe (x, y)                            | `plt.plot(x, y)`               |
| `plt.scatter(x, y)`            | Trace un nuage de points                           | `plt.scatter(x, y)`            |
| `plt.bar(x, y)`                | Trace un diagramme à barres                        | `plt.bar(x, y)`                |
| `plt.hist(data)`               | Trace un histogramme                               | `plt.hist(valeurs)`            |
| `plt.title("titre")`           | Ajoute un titre au graphique                       | `plt.title("Graphique")`       |
| `plt.xlabel("nom de l'axe x")` | Ajoute un titre à l’axe des x                      | `plt.xlabel("Temps (s)")`      |
| `plt.ylabel("nom de l'axe y")` | Ajoute un titre à l’axe des y                      | `plt.ylabel("Vitesse (m/s)")`  |
| `plt.legend()`                 | Affiche une légende pour les courbes nommées       | `plt.legend()`                 |
| `plt.grid(True)`               | Affiche une grille                                 | `plt.grid(True)`               |
| `plt.show()`                   | Affiche le graphique à l’écran (à la fin du tracé) | `plt.show()`                   |
| `plt.savefig("figure.png")`    | Sauvegarde le graphique en image                   | `plt.savefig("mon_graph.png")` |
| `plt.figure(figsize=(w, h))`   | Définit la taille du graphique (en pouces)         | `plt.figure(figsize=(8, 4))`   |

{{% notice style="blue" title="À retenir (graphiques simples)" groupid="notice-toggle" expanded="false" %}}
* **Importer la bibliothèque** : matplotlib.pyplot 
* **Créer les données** sous forme de **listes** ou de **tableaux NumPy**
* **Tracer une courbe** avec `plt.plot(x, y)`
    * `plt.plot()` change selon le type de graphique (voir le tableau [ICI](#fonctions-de-base-pour-les-graphiques)
    * Il existe des options permettant de personnaliser les couleurs, traits, etc.
* **Afficher le graphique** avec `plt.show()`.
* **Ajouter un titre** avec `plt.title("Mon graphique")`
* **Nommer les axes** avec `plt.xlabel("x")` et `plt.ylabel("y")`
* **Afficher une grille** pour mieux lire les valeurs avec `plt.grid()`
* **Ajouter une légende** avec `label="..."` dans `plot()` et `plt.legend()`
* **Tracer plusieurs courbes sur un même graphique** en appelant plusieurs fois `plt.plot(...)` avant `plt.show()`
{{% /notice %}}

## Exercices à faire avant le cours

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

### Graphiques

#### Exercice 7 – Température dans une journée

* Heures : `[0, 4, 8, 12, 16, 20, 24]`
* Températures : `[-5, -2, 3, 7, 6, 1, -2]`

Crée un graphique de température en fonction de l’heure.

Ajoute :

* Un titre `"Température en fonction de l’heure"`
* Les étiquettes `"Heure (h)"` et `"Température (°C)"`
* Une grille

#### Exercice 8 - Comparaison des valeurs mesurées et attendues

On a mesuré la concentration d’un soluté à différentes températures. Les valeurs **attendues** suivent une loi théorique, tandis que les **valeurs mesurées** viennent d’un capteur.

```python
temp = [10, 20, 30, 40, 50]
attendu = [2.1, 3.8, 5.6, 7.3, 9.0]
mesure =  [2.0, 3.9, 5.2, 7.5, 8.8]
```

* Affiche les **valeurs attendues** avec `plt.plot(...)` (ligne noire avec des ronds).
* Affiche les **valeurs mesurées** avec `plt.bar(...)` (barres bleues légèrement transparentes).
* Ajoute un **titre**, une **légende**, les **étiquettes d’axes** et une **grille**.

---

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **deuxième examen** (25%)

1. Lire la matière sur [Tableaux NumPy](../semaine9/)
2. Faire les [exercices se trouvant à la fin de la leçon 9](../semaine9/#exercices-à-faire-avant-le-cours)