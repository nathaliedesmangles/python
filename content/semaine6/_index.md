+++
chapter = true
pre = "<b>6.</b>"
title = " Listes, chaînes et visualisation des données"
weight = 106
draft = false
+++


## Objectifs

* Créer, modifier et parcourir une **liste simple**.
* Manipuler des **listes imbriquées** (listes dans un liste).
* Appliquer les notions des listes simples sur les chaines de caractères. 
* Créer, afficher, embellir et enregistrer des graphiques simples avec `matplotlib`.

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}


# Exercices

## Fichier de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier.
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_listes_chaines_graphes.ipynb)
2. Enregistrez le fichier dans votre dossier **exercices** de la semaine en cours.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez le fichier `exercices_listes_chaines_graphes.ipynb`
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.


## Listes

### Exercice 1 :

* Crée une liste contenant 5 animaux. 
* À l'aide d'une boucle `for`, affiche chaque animal avec une phrase du type :
```text
Voici un/une <animal>
```

**Exemple de résultat avec la liste** ["chat", "chien", "lapin", "perroquet", "tigre"] :
```
Voici un/une chat
Voici un/une chien
Voici un/une lapin
Voici un/une perroquet
Voici un/une tigre
```
 
### Exercice 2 :

* Crée une grille de 5 lignes et 4 colonnes (liste de listes) contenant des chiffres. 
* À l'aide d'une boucle `for`, affiche tous les chiffres un par un.

**Résultat attendu** :
```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

### Exercice 3 :

* Demande à l’utilisateur d’entrer 3 prénoms et ajoute-les dans une liste (avec `append()`).
* Affiche chaque prénom en ordre alphabétique croissant (avec `sorted()`).  
* Affiche chaque prénom en ordre alphabétique décroissant (avec `sorted()` et `reverse=True`). 

**Exemple de résultat** :
```
Ordre alphabétique croissant :
Alice
Lise
Pierre
Ordre alphabétique décroissant :
Pierre
Lise
Alice
```


### Exercice 4

On étudie les séquences d’ADN de différents suspects afin de comparer certaines bases. Les séquences sont représentées sous forme de listes imbriquées.

* Crée la liste de séquences pour les 3 suspects:
```python
suspects = [
    ["A", "T", "C", "G"],
    ["G", "A", "T", "G"],
    ["A", "T", "T", "G"]
]
```

* À l'aide des indices `rangée` et `colonne`:
	* Affiche la 2e base de la 1re séquence.
	* Affiche la dernière base de la 3e séquence.

**Résultat attendu** :
```
T
G
```

---

## Chaines de caractères

### Exercice 5 - Créer une liste de nombres à partir d'une liste de mots

* Utiliser une boucle et `len()` pour obtenir le nombre de lettres de chaque mot.
* Pour chacun des mots, ajouter son nombre de lettres dans la liste `nb_lettres` avec `append()`.
* Afficher la liste `nb_lettres`.

```python
mots = ["chlorophylle", "atome", "protéine"]
nb_lettres = []
```

**Résultat attendu** :
```
[12, 5, 8]
```

### Exercice 6 - Convertir en ARN

Une séquence d’ADN est "atgct".

* Mets-la en majuscules (avec `upper()`).
* Remplace les "T" par "U" (avec `replace()`).

**Résultat attendu** :
```
AUGCU
```

---

## Graphiques

### Exercice 7 – Température dans une journée

* À partir des deux listes ci-dessous, crée un graphique de la température en fonction de l’heure. Utilise `plot()` et `show()`
```python
heures = [0, 4, 8, 12, 16, 20, 24]
temperatures = [-5, -2, 3, 7, 6, 1, -2]
```

* Ajoute :
	* Un titre `"Température en fonction de l’heure"`. Utilise `title()`.
	* Les étiquettes `"Heure (h)"` et `"Température (C)"`. Utilise `xlabel()` et `ylabel()`
	* Une grille. Utilise `grid()`

**Graphique attendu** :
![Température heure](./exo7.png?width=40vw)


### Exercice 8 - Comparaison des valeurs mesurées et attendues

On a mesuré la concentration d’un soluté à différentes températures. Les valeurs **attendues** suivent une loi théorique, tandis que les **valeurs mesurées** viennent d’un capteur.

```python
temp = [10, 20, 30, 40, 50]
attendu = [2.1, 3.8, 5.6, 7.3, 9.0]
mesure =  [2.0, 3.9, 5.2, 7.5, 8.8]
```
* Écris un programme qui:
	* Affiche les **valeurs attendues** avec `plt.plot(...)` (ligne noire avec des ronds).
	* Affiche les **valeurs mesurées** avec `plt.bar(...)` (barres bleues légèrement transparentes).
	* Ajoute un **titre**, une **légende**, les **étiquettes d’axes** et une **grille**.

**Graphique attendu** :
![Température heure](./exo8.png?width=40vw)

---

# Cours

## Qu’est-ce qu’une liste ?

Une **liste**, c’est un **conteneur** dans lequel on peut ranger plusieurs éléments (nombres, chaînes, booléens, etc.).

C’est un peu comme une boîte à compartiments.

```python
ma_liste = [3, 7, 42, 5]
```

Chaque élément a une **position** (appelée *indice*).

```python
print(ma_liste[0])  # Affiche 3 (le premier élément)
print(ma_liste[2])  # Affiche 42 (le 3e élément) 
```

{{% notice style="accent" icon="stopwatch" title="Important"%}}
* Notez le décalage entre **l'indice** 0 et la **position** 1 de l'élément (indice 2; position 3).
* Cela est dû au fait que les indices commencent **toujours à 0**.
{{% /notice %}}

## Créer et modifier une liste

### Créer une liste vide

```python
liste_vide = []
```

### Ajouter des éléments avec append()

```python
fruits = ["pomme", "banane"]
fruits.append("cerise")  # ["pomme", "banane", "cerise"]
```

### Remplacer un élément en spécifiant son indice

```python
fruits[1] = "poire"  # ["pomme", "poire", "cerise"]
```

### Supprimer la **première occurrence** d’un élément

```python
fruits = ["pomme", "poire", "cerise", "poire"]
fruits.remove("poire")	# ["pomme", "cerise", "poire"] Seul "poire" à l'indice 1 sera supprimé
```

### Supprimer un élément selon son indice

```python
fruits = ["pomme", "cerise", "poire"]
fruits.pop(1)	# ["pomme", "poire"] "cerise" à l'indice 1 sera supprimé
```


## Parcourir une liste avec la boucle `for`

**Rappel** : La boucle `for` est utilisée quand **on connaît d’avance** combien de fois on doit répéter.

```python
for variable in sequence:
    instructions à répéter jusqu'à la fin de la séquence.
```

{{% notice style="accent" icon="stopwatch" title="Important"%}}
* Jusqu'à présent, on a utilisé `range()` pour générer une **séquence de nombre entiers**.
* À partir de maintenant, la séquence pourra être une **liste (de nombres, de mots, de booléens et de listes)**.
{{% /notice %}}


**Exemple** :

```python
fruits = ["pommes", "poires", "cerises"]	# Une liste contenant 3 noms de fruits

for fruit in fruits:	# Pour chaque fruit de la liste fruit**s**
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
* La fonction `range()` génère des nombres entiers de 0 à 2 (qui est le nombre d'éléments dans la liste - 1, **car le 1er indice est 0**)
* `len(fruits)` vaut 3, le nombre d'éléments dans la liste.
* La variable `i` prendra les valeurs `0, 1 et 2`.
* `fruits[i]` contient un à un les fruits de la liste `fruits`.


## Fonctions utiles sur les listes simples

| Méthode / Fonction       | Description                                    | 
| ------------------------ | ---------------------------------------------- | 
| `append(valeur)`         | Ajoute un élément à la fin                     | 
| `insert(indice, valeur)` | Insère une valeur à une position donnée        |
| `pop(indice)`            | Retire l’élément à l’indice (ou le dernier)    | 
| `remove(valeur)`         | Retire la **première** occurrence d'une valeur | 
| `len()`                  | Donne la longueur de la liste                  | 
| `sorted()`               | Trie la liste sans la modifier                 | 
| `sort()`*                | Trie la liste en la modifiant                  | 
| `reverse()`              | Inverse l’ordre des éléments                   | 
| `in`                     | Vérifie si un élément est dans la liste        | 
| `index(valeur)`          | Renvoie l’indice de la première occurrence     | 
| `count(valeur)`          | Compte combien de fois un élément apparaît     | 
| `max()`                  | Trouver le max                                 | 
| `min()`                  | Trouver le min                                 | 
| `sum()` 		   | Calculer une somme des éléments		    | 

<!--
Très bonne question — c’est une confusion classique 👇

---

### 🔹 `liste.sort()`

* **Méthode d’objet liste** (elle appartient directement aux objets de type `list`)
* **Trie la liste en place**, c’est-à-dire qu’elle **modifie la liste existante**
* **Ne retourne rien** → elle renvoie `None`

```python
nombres = [3, 1, 4, 2]
nombres.sort()     # trie la liste en place
print(nombres)     # [1, 2, 3, 4]
print(type(nombres.sort()))  # NoneType → la méthode ne retourne rien
```

➡️ Comme elle ne retourne rien, **écrire `liste = liste.sort()` remplace ta liste par `None`**, ce qui casse tout :

```python
liste = [3, 1, 2]
liste = liste.sort()   # ERREUR logique : liste devient None
print(liste)           # affiche None
```

---

### 🔹 `sorted(liste)`

* **Fonction intégrée (built-in)**, pas une méthode d’objet
* **Ne modifie pas la liste d’origine**
* **Retourne une nouvelle liste triée**

```python
nombres = [3, 1, 4, 2]
nombres_triees = sorted(nombres)
print(nombres)          # [3, 1, 4, 2]  (inchangée)
print(nombres_triees)   # [1, 2, 3, 4]
```

---

### 🔸 Résumé

| Méthode / Fonction | Modifie la liste originale ? | Retourne une nouvelle liste ? | Valeur de retour |
| ------------------ | ---------------------------- | ----------------------------- | ---------------- |
| `liste.sort()`     | ✅ Oui                        | ❌ Non                         | `None`           |
| `sorted(liste)`    | ❌ Non                        | ✅ Oui                         | Liste triée      |

---

### 💡 Quand utiliser quoi ?

* Si tu **veux trier la liste elle-même**, pour la réutiliser triée → `liste.sort()`
* Si tu **veux garder l’ordre original**, mais avoir une **copie triée** → `sorted(liste)`

---

Souhaites-tu que je te montre aussi comment trier avec une clé (`key=`) ou dans l’ordre inverse (`reverse=True`) avec ces deux fonctions ?

-->

{{% notice style="green" title="Exemples avec les fonctions utiles pour les listes simples" groupid="notice-toggle" expanded="false" %}}
### `append(valeur)`

Ajoute un élément à la fin de la liste.

```python
nombres = [1, 2, 3]
nombres.append(4)
print(nombres)   # [1, 2, 3, 4]
```

---

### `insert(indice, valeur)`

Insère une valeur à une position donnée.

```python
nombres = [1, 2, 3]
nombres.insert(1, 99)  
print(nombres)   # [1, 99, 2, 3]
```

---

### `pop(indice)`

Retire l’élément à l’indice donné (ou le dernier si rien n’est précisé).

```python
nombres = [1, 2, 3]
nombres.pop()      
print(nombres)   # [1, 2]  (le dernier élément a été enlevé)
nombres.pop(0)    
print(nombres)   # [2]     (le premier élément a été enlevé)
```

---

### `remove(valeur)`

Retire la **première occurrence** d'une valeur.

```python
nombres = [1, 2, 3, 2]
nombres.remove(2)  
print(nombres)   # [1, 3, 2]
```

---

### `len(liste)`

Donne la longueur (nombre d’éléments) de la liste.

```python
nombres = [10, 20, 30]
print(len(nombres))  # 3
```

---

### `sorted(liste)`

Renvoie une nouvelle liste triée **sans modifier** la liste originale.

**En ordre croissant (par défaut)** :
```python
nombres = [3, 1, 2]
print(sorted(nombres))  # [1, 2, 3]
print(nombres)          # [3, 1, 2] (pas modifiée)
```

**En ordre décroisant**:
```python
nombres = [5, 1, 4, 3, 2]
nombres_decr = sorted(nombres, reverse=True)
print(nombres_decr )  # [5, 4, 3, 2, 1]
```
---

### `sort()`

Trie la liste **en la modifiant directement**.

```python
nombres = [3, 1, 2]
nombres.sort()
print(nombres)   # [1, 2, 3]
```

---

### `reverse()`

Inverse l’ordre des éléments de la liste.

```python
nombres = [1, 2, 3]
nombres.reverse()
print(nombres)   # [3, 2, 1]
```

---

### `in`

Vérifie si un élément est présent dans la liste.

```python
fruits = ["pomme", "banane", "poire"]
print("pomme" in fruits)   # True
print("raisin" in fruits)  # False
```

---

### `index(valeur)`

Donne l’indice de la **première occurrence** d’une valeur.

```python
fruits = ["pomme", "banane", "poire", "banane"]
print(fruits.index("banane"))  # 1
```

---

### `count(valeur)`

Compte combien de fois une valeur apparaît dans la liste.

```python
fruits = ["pomme", "banane", "poire", "banane"]
print(fruits.count("banane"))  # 2
```

---

### `max(liste)`

Trouve le maximum de la liste (numérique ou alphabétique).

```python
nombres = [5, 8, 2, 10]
print(max(nombres))  # 10
```

---

### `min(liste)`

Trouve le minimum de la liste.

```python
nombres = [5, 8, 2, 10]
print(min(nombres))  # 2
```

---

### `sum(liste)`

Calcul de la somme des éléments (seulement si ce sont des nombres).

```python
nombres = [5, 8, 2, 10]
print(sum(nombres))  # 25
```

Calcul de la moyenne d’une liste de notes

```python
notes = [85, 90, 78]
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne:.2f}")
```
{{% /notice %}}


{{% notice style="accent" icon="stopwatch" title="*Important" %}}
* `mots.sort()` utilisé sur une liste de chaines de caractères trie la liste en respectant l’ordre **Unicode**, ce qui fait que les **mots commençant par une majuscule** sont placés **avant ceux en minuscules**.

**Exemple** :

```python
mots = ["pomme", "Banane", "abricot", "Orange"]
mots.sort()
print(mots)

# Affichage : 
['Banane', 'Orange', 'abricot', 'pomme']	# Notez les positions des éléments `abricot` et `pomme`
```
{{% /notice %}}


## Listes imbriquées (notion avancée)

Une **liste imbriquée**, c’est une liste **qui contient d'autres listes**.

**Exemple** : Une liste contenant trois listes (en math, on parle de **matrices**)

```python
matrice = [
    [1, 2, 3], # 1re liste à l'indice 0 de la liste matrice
    [4, 5, 6], # 2e liste à l'indice 1 de la liste matrice
    [7, 8, 9]  # 3e liste à l'indice 2 de la liste matrice
]
```

### Accéder à un élément précis via les indices

* Il faut préciser les **deux indices**: `[rangée][colonne]`
```python
print(matrice[0][2])  # Affiche 3 qui se trouve sur la première rangée (indice 0) et la 3e colonne (indice 2). 
```

### Parcourir une liste imbriquée avec la boucle for

* Il faut utiliser **deux boucles** `for`.
* La première boucle pour **parcourir chaque rangée une à la fois**.
* La deuxième boucle (à l'intérieur de la première) pour **parcourir les éléments un à un d'une rangée**.

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
{{% notice style="green" title="Afficher les colonnes d'une liste de listes" groupid="notice-toggle" expanded="false" %}}
### Exemple simple

```python
# Grille = liste de listes (3 lignes x 4 colonnes)
grille = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11,12]
]

# Affichage par colonnes
for col in range(len(grille[0])):  # nombre de colonnes
    colonne = []		   # une liste vide pour y ajouter les éléments des colonnes
    for ligne in grille:	   # Pour chaque ligne (sous liste) de la grille, on ajoute l'élément de la colonne
        colonne.append(ligne[col])
    print(colonne)
```

**Résultat :**
```
[1, 5, 9]
[2, 6, 10]
[3, 7, 11]
[4, 8, 12]
```

---

### Avec `zip()` (plus "pythonique")

```python
for colonne in zip(*grille):
    print(list(colonne))
```

Donne exactement le même résultat.
`zip(*grille)` transposera automatiquement les lignes en colonnes.


### Avec la bibliothèque (module) NumPy (dans une prochaine leçon)
À suivre...
{{% /notice  %}}


---

{{% notice style="blue" title="À retenir (listes)" groupid="notice-toggle" expanded="false" %}}
* Une liste permet de **stocker plusieurs valeurs**.
* On accède aux éléments avec des **indices**.
* Le premier élément d'une liste est toujours à l'indice 0.
* La taille (nombre d'éléments) d'une liste s'obtient avec la fonction `len()` et vaut toujours `denier indice + 1`.
* Les listes peuvent être **modifiées** facilement à l'aide de fonctions et en ciblant un élément par son/ses indice.s.
* Une liste peut contenir **d'autres listes** → super utile pour représenter des tableaux ou des grilles.
* Dans le cas d'une **liste de listes**, les éléments sont accédés en spécifiant les **deux indices (rangée, colonne)**.
{{% /notice %}}

---

## Les chaînes de caractères sont des listes

On peut manipuler une chaine de caractère comme une suite de lettres ou une **liste de lettres**.

```python
message = "Bonjour à tous!"
print(message[0])     # 'B' (le premier caractère)
print(message[-1])    # '!' (le dernier caractère)
print(message[-7])    # 'à' (le 7e caractère en partant de la fin)
```
{{% notice style="accent" icon="stopwatch" title="Important" %}}
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
| Enlever les espaces autour                   | `message.strip()`                     |
| Séparer une chaîne en morceaux               | `message.split(" ")`                  |
| Remplacer un mot                             | `message.replace("Bonjour", "Salut")` |
| Trouver la position d’un mot/lettre          | `message.find("bio")`                 |
| Compter le nombre de fois qu’un mot apparaît | `message.count("e")`                  |
| Assembler en une seule chaîne de caractères  | `message.join(chaine)`

{{% notice style="green" title="Exemples avec les fonctions utiles pour les chaines" groupid="notice-toggle" expanded="false" %}}
### `lower()`

Passe tout le texte en **minuscules**.

```python
message = "Bonjour Les Amis"
print(message.lower())  
# "bonjour les amis"
```

---

### `upper()`

Passe tout le texte en **majuscules**.

```python
message = "Bonjour Les Amis"
print(message.upper())  
# "BONJOUR LES AMIS"
```

---

### `strip()`

Enlève les espaces (ou tabulations, sauts de ligne) au **début et à la fin**.

```python
message = "   Bonjour   "
print(message.strip())  
# "Bonjour"
```

---

### `split(séparateur)`

Découpe une chaîne en **morceaux** (liste de mots), selon un séparateur.

```python
message = "pomme,banane,poire"
print(message.split(","))  
# ["pomme", "banane", "poire"]

phrase = "Bonjour les amis"
print(phrase.split(" "))  
# ["Bonjour", "les", "amis"]
```

---

### `replace(ancien, nouveau)`

Remplace une partie du texte par une autre.

```python
message = "Bonjour tout le monde"
print(message.replace("Bonjour", "Salut"))  
# "Salut tout le monde"
```

---

### `find(sous_chaine)`

Trouve la **position (indice)** de la première occurrence.
Renvoie `-1` si le mot n’est pas trouvé.

```python
message = "biologie et chimie"
print(message.find("bio"))   # 0 (commence à l’indice 0)
print(message.find("chimie"))  # 12
print(message.find("physique"))  # -1 (absent)
```

---

### `count(sous_chaine)`

Compte combien de fois une sous-chaîne apparaît.

```python
message = "pomme et poire et pomme"
print(message.count("pomme"))  # 2
print(message.count("e"))      # 5
```

---

### `join(chaine)`

Une chaîne de caractères doit être spécifiée comme **séparateur**.

```python
mots = ["Bonjour", "langage", "Python"]
phrase = " ".join(mots)	  # séparateur est l'espace
print(phrase)	# Bonjour langage Python
```
{{% /notice %}}

{{% notice style="blue" title="À retenir (chaines de caractères)" groupid="notice-toggle" expanded="false" %}}
* Une chaine de caractères se manipule comme une liste simple, dont les éléments sont des caractères (incluant l'espace).  
{{% /notice %}}


## Visualiser les données avec Matplotlib (graphiques de base)

Pour pouvoir visualiser des données sous forme de graphiques, nous utiliserons le module `pyplot` de la bibliothèque `matplotlib`.

### Importer `matplotlib.pyplot`

La partie de `matplotlib` qu'on utilise le plus pour créer des graphiques s'appelle `pyplot`.

```python
import matplotlib.pyplot as plt
```

On utilise l’abréviation `plt` pour simplifier l’écriture.

{{% notice style="accent" title="Exécuter tout vs seulement la cellule" groupid="notice-toggle" expanded="false" %}}

Lorsque vous travaillez dans un bloc-notes Jupyter (**fichier .ipynb**), vous avez deux façons d’exécuter du code :

## 1. Exécuter la cellule
- Lance uniquement **la cellule sélectionnée**.  
- Utile pour tester une portion de code.  
- Exemple : si vous importez `numpy` dans une cellule mais n’exécutez **que** une autre cellule qui l’utilise, vous obtiendrez une erreur (`NameError: name 'plt' is not defined`).  

![Capture d’écran - Bouton Exécuter la cellule](/images/exec_cell.png?width=30vw)

## 2. Exécuter tout
- Lance **tout le bloc-notes de haut en bas**.  
- Assure que tous les imports (`matplotlib`, `numpy`, `pandas`, etc.) sont bien pris en compte avant les instructions suivantes.  
- Utile avant une remise ou pour vérifier que le bloc-notes fonctionne de façon autonome.  

![Capture d’écran - Bouton Exécuter tout](/images/exec_tout.png?width=30vw)

## Bonnes pratiques
- Après avoir écrit ou modifié plusieurs cellules, utilisez **Exécuter tout** pour vérifier la cohérence de votre bloc-notes.  
- Pendant vos tests, utilisez **Exécuter la cellule** pour éviter de tout relancer inutilement.
{{% /notice %}}



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
À ce stade, il se peut que **rien ne s'affiche encore**. Il faut une dernière commande pour voir le graphique.
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


{{% notice style="cyan" title="Colorer chaque point manuellement" groupid="notice-toggle" expanded="false" %}}
On peut utiliser une boucle et tracer chaque point avec une couleur différente :

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [2, 4, 1, 3, 5]
couleurs = ['r', 'g', 'b', 'orange', 'purple']

for i in range(len(x)):
    plt.plot(x[i], y[i], 'o', color=couleurs[i])
    
plt.xlabel("Abscisses")
plt.ylabel("Ordonnées")
plt.title("Colorer chaque point manuellement")
plt.grid(True)

plt.show()
```

* Ici, on trace chaque point séparément ('o' pour le marqueur circulaire).
![Couleurs différentes](./points_couleurs.png?width=35vw)
{{% /notice %}}

### Ajouter un titre, des étiquettes et une grille avec title(), xlabel(), ylabel() et grid()

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

La méthode `grid()` accepte plusieurs paramètres de personnalisation:

| Paramètre     | Description                                                                                               | Valeur par défaut     |
| ------------- | --------------------------------------------------------------------------------------------------------- | --------------------- |
| **which**     | Spécifie si les changements s’appliquent aux lignes de grille **majeures**, **mineures** ou **les deux**. | `major`               |
| **axis**      | Spécifie si les changements s’appliquent à l’axe **x**, **y** ou **les deux**.                            | `both`                |
| **color**     | Définit la couleur des lignes de la grille.                                                               | *(aucune, à définir)* |
| **linestyle** | Définit le style des lignes de la grille (par ex. `'-'`, `'--'`, `':'`).                                  | *(aucune, à définir)* |
| **linewidth** | Définit l’épaisseur des lignes de la grille.                                                              | *(aucune, à définir)* |


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

> Cela ajoutera une zone dans un coin du graphique indiquant "Courbe 1" et "Courbe 2".

**Résultat**
![Figure 4](./Figure_4.png?width=45vw)


### Enregistrer un graphique sous forme d'image avec savefig()

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

---

# Atelier

1. Téléchargez le fichier de départ : [Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_listes_chaines_graphes.ipynb)
2. Déplacez-le dans votre dossier prévu pour **l'atelier de la semaine 6**.
3. Ouvrez votre dossier de travail `programmation-sciences` **à partir de Visual Studio Code**.
   * Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb).

---

## Exercice 

Un chercheur a mesuré la **température moyenne (°C)** de quatre villes pendant une semaine. Les données sont regroupées dans une **liste de listes**. Vous devez analyser et représenter ces données.

1. **Les données**
   * Créez une liste `temperatures` contenant les valeurs suivantes (une sous-liste par ville) :
     * Ville A : `[15, 16, 14, 14, 17, 18, 19]`
     * Ville B : `[22, 23, 21, 20, 24, 25, 26]`
     * Ville C : `[5, 7, 6, 6, 8, 9, 7]`
     * Ville D : `[10, 11, 12, 10, 13, 14, 15]`

   * Créez aussi deux listes :
     * `villes = ["Ville A", "Ville B", "Ville C", "Ville D"]`
     * `jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]`

2. **Afficher les températures**
   * À l’aide de **boucles imbriquées** (`for ... :` dans `for ... :`), affichez les températures de chaque ville.
   * Exemple attendu :
     ```
     Ville A : 15 16 14 14 17 18 19
     Ville B : 22 23 21 20 24 25 26
     ...
     ```

3. **Trouver les valeurs extrêmes**
   * Pour chaque ville, utilisez les fonctions `max()` et `min()` pour trouver la température maximale et minimale.
   * Affichez-les sous forme de phrases complètes, par exemple :
     ```
     La température maximale de Ville A est 19 C
     La température minimale de Ville A est 14 C
     ```

4. **Classer les températures**
   * Pour chaque température de chaque ville, affichez (`if / elif / else`):
     * `"Froide"` si T < 10
     * `"Douce"` si 10 ≤ T ≤ 20
     * `"Chaud"` si T > 20
   
   * Exemple :
     ```
     15 => Douce
     7 => Froide
     23 => Chaud
     ```

5. **Tracer un graphique avec matplotlib**
   * Utilisez une boucle pour tracer la courbe des températures de chaque ville (`plt.plot`).
   * Ajoutez :
     * Un **titre** : `"Températures hebdomadaires"`
     * Les étiquettes des axes (`xlabel`, `ylabel`)
     * Une **grille** (`grid`)
     * Une **légende** (`legend`)
   * Sauvegardez le graphique dans un fichier `"temperatures.png"` (`savefig`)
   * Affichez-le (`show`).


**Résultats attendus** :
```
Ville A : 15 16 14 14 17 18 19 
Ville B : 22 23 21 20 24 25 26 
Ville C : 5 7 6 6 8 9 7 
Ville D : 10 11 12 10 13 14 15 
La température maximale de Ville A est 19 C
La température minimale de Ville A est 14 C
La température maximale de Ville B est 26 C
La température minimale de Ville B est 20 C
La température maximale de Ville C est 9 C
La température minimale de Ville C est 5 C
La température maximale de Ville D est 15 C
La température minimale de Ville D est 10 C

Classification pour Ville A :
15 => Douce
16 => Douce
14 => Douce
14 => Douce
17 => Douce
18 => Douce
19 => Douce

Classification pour Ville B :
22 => Chaud
23 => Chaud
21 => Chaud
20 => Douce
24 => Chaud
25 => Chaud
26 => Chaud

Classification pour Ville C :
5 => Froide
7 => Froide
6 => Froide
6 => Froide
8 => Froide
9 => Froide
7 => Froide

Classification pour Ville D :
10 => Douce
11 => Douce
12 => Douce
10 => Douce
13 => Douce
14 => Douce
15 => Douce
```

![Graphique Temperatures](./temperatures.png?width=40vw)
---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [7. Tableaux numpy et opérations scientifiques](../semaine7/)
2. Faire les exercices de la [prochaine leçon :](../semaine7/#exercices)
