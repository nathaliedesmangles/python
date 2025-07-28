+++
chapter = true
pre = "<b>7.</b>"
title = " Dictionnaires et graphiques de base"
weight = 107
draft = false
+++


## Objectifs

* Créer un dictionnaire simple pour représenter des données associatives (ex. : atome → masse atomique)
* Manipuler des données dans un dictionnaire (accès, ajout, modification, parcours).
* Vérifier la présence d’une clé avec `in`. 
* Créer, afficher, embellir et enregistrer des graphiques simples avec la bibliothèque `matplotlib`.

---

## Qu’est-ce qu’un dictionnaire?

Un **dictionnaire** est une structure de données qui associe des **clés** à des **valeurs**.
Il permet de stocker des informations organisées, un peu comme un mini-fichier Excel, mais avec des étiquettes personnalisées au lieu d’indices numériques.

**Syntaxe de base** :

```python
mon_dictionnaire = {
    "clé1": valeur1,
    "clé2": valeur2
}
```

## Utilisation fréquente en sciences

Les dictionnaires sont utiles pour :

* Associer des symboles d’éléments à des valeurs (masse molaire, charge, état)
* Regrouper des résultats par échantillon (ex. température par lieu)
* Associer des noms de gènes à leur expression

### Exemple

Un dictionnaire contenant les masses molaires de quelques éléments :

```python
masses_molaires = {
    "H": 1.008,
    "O": 15.999,
    "C": 12.011
}
```

## Accéder à une valeur avec une clé

```python
print(masses_molaires["O"])  # Affiche : 15.999
```

> Si la clé n’existe pas, Python déclenche une erreur `KeyError`.

## Ajouter ou modifier une valeur

### Ajouter

```python
masses_molaires["N"] = 14.007
```

### Modifier

```python
masses_molaires["C"] = 12.01  # Correction
```

## Vérifier si une clé est présente

```python
if "H" in masses_molaires:
    print("L’hydrogène est dans le dictionnaire.")
```

## Parcourir un dictionnaire

### Via les clés

```python
for element in masses_molaires:
    print(element)
```

### Via les valeurs

```python
for valeur in masses_molaires.values():
    print(valeur)
```

* `.values()` permet d’obtenir **uniquement les valeurs** du dictionnaire, sans les clés.
* **Utile quand on veut faire un calcul avec les valeurs**, comme une moyenne ou une somme.

```python
for valeur in densites.values():
    print(valeur)
```


### Via les paires clé-valeur :

```python
for element, masse in masses_molaires.items():
    print(f"{element} → {masse}")
```

* `.items()` permet d’obtenir les couples **clé-valeur** sous forme de paires (appelées aussi tuples en Python).
* Utile quand on veut à la fois le **nom (clé)** et la **valeur associée** pour un affichage ou un traitement.

## Supprimer une entrée

```python
del masses_molaires["H"]
```

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

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_listes_chaines_graphes.ipynb)


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