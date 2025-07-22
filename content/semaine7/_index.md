+++
chapter = true
pre = "<b>7.</b>"
title = " Listes, chaînes de caractères et graphiques de base"
weight = 107
draft = false
+++


## Objectifs d'apprentissage

1. **Créer et manipuler des listes** de données numériques ou textuelles en Python (ajout, suppression, parcours, calcul de statistiques simples).
2. **Accéder, modifier et parcourir** les caractères d’une chaîne de caractères.
3. **Appliquer des méthodes de traitement de texte** pour analyser ou transformer des chaînes de caractères (ex. : mise en minuscules, découpage, recherche, comptage).

---

<!--
## Les **listes** de données

Une **liste** est un contenant qui peut regrouper plusieurs valeurs (appelées *éléments*), dans un ordre donné.

### Création de liste

```python
nombres = [4, 7, 9, 12]
notes = [82.5, 76.0, 91.2]
mots = ["chlorophylle", "atome", "protéine"]
```

### Accès à un élément

On accède à un élément avec un **indice** (le premier élément a l’indice 0).

```python
print(nombres[0])  # Affiche 4
print(mots[2])     # Affiche "protéine"
```

### Modifier un élément

```python
nombres[1] = 10  # La liste devient [4, 10, 9, 12]
```

### Ajouter et retirer un élément

```python
nombres.append(15)      # Ajoute 15 à la fin
nombres.remove(10)      # Enlève le 10
```

### Taille de la liste

```python
print(len(notes))  # Affiche 3
```


## Parcourir une liste avec `for`

```python
for note in notes:
    print(note)
```

## Quelques traitements courants sur les listes

| Objectif                        | Code Python                   |
| ------------------------------- | ----------------------------- |
| Calculer une somme              | `s = sum(notes)`              |
| Moyenne                         | `m = sum(notes) / len(notes)` |
| Trouver le max ou le min        | `max(notes)` ou `min(notes)`  |
| Tester la présence d’un élément | `"atome" in mots`             |
| Trier une liste                 | `mots.sort()`                 |


## Calculs dans une liste avec une boucle `for`

### Calculer une somme

On additionne les valeurs une par une dans une boucle.

```python
valeurs = [10, 20, 30, 40]
somme = 0

for v in valeurs:
    somme += v


---


### Exercice 4 – Arrêter une boucle avec `break`

Un étudiant répond à un test. Tu veux simuler les questions jusqu’à la question 10, **mais arrêter dès qu’il donne une mauvaise réponse**.

1. Simule des réponses avec une variable (par exemple, une bonne réponse = "A").
2. Utilise une boucle `for` pour passer les questions.
3. Si la réponse est incorrecte, affiche "Test terminé" et utilise `break`.

print("Somme:", somme)  # Résultat: 100
```

### Calculer une moyenne

Une **moyenne**, c’est la somme divisée par le nombre d’éléments.

```python
moyenne = somme / len(valeurs)
print("Moyenne:", moyenne)  # Résultat: 25.0
```

> Assurez-vous que la liste n’est pas vide avant de faire la division (`len(valeurs) ≠ 0`).


### Trouver le minimum et le maximum

On initialise avec le **premier élément** de la liste, puis on compare.

```python
valeurs = [10, 20, 30, 40]

minimum = valeurs[0]
maximum = valeurs[0]

for v in valeurs:
    if v < minimum:
        minimum = v
    if v > maximum:
        maximum = v

print("Min:", minimum)  # Résultat: 10
print("Max:", maximum)  # Résultat: 40
```

## Chaînes de caractères (str)

Une chaîne de caractères est un **texte** (entre guillemets), que l'on peut manipuler comme une suite de lettres ou une **liste** de lettre.

### Déclaration

```python
message = "Bonjour les biologistes!"
```

### Accès par index

```python
print(message[0])     # 'B'
print(message[-1])    # '!' (le dernier caractère)
```

### Parcourir une chaîne

```python
for lettre in message:
    print(lettre)
```

### Longueur d’une chaîne

```python
len(message)  # Nombre de caractères
```


## Traitements utiles sur les chaînes

| Objectif                                     | Code Python                           |
| -------------------------------------------- | ------------------------------------- |
| Passer en minuscules                         | `message.lower()`                     |
| Passer en majuscules                         | `message.upper()`                     |
| Enlever les espaces autour                   | `texte.strip()`                       |
| Séparer une chaîne en morceaux               | `message.split(" ")`                  |
| Remplacer un mot                             | `message.replace("Bonjour", "Salut")` |
| Trouver la position d’un mot/lettre          | `message.find("bio")`                 |
| Compter le nombre de fois qu’un mot apparaît | `message.count("e")`                  |


## Exemples simples d’utilisation

**À FAIRE: Énoncés es 2 exercices, solutions**

### Exemple 1 : Moyenne des notes

```python
notes = [89, 73, 94, 85]
moyenne = sum(notes) / len(notes)
print("Moyenne:", moyenne)
```

### Exemple 2 : Nombre de G et C dans une séquence d’ADN

```python
sequence = "ATGCGGTAAC"
gc = sequence.count("G") + sequence.count("C")
pourcentage_gc = gc / len(sequence) * 100
print("Pourcentage GC:", pourcentage_gc)
```

de la leçon

Apprendre à tracer des graphiques simples en 2D à partir de données scientifiques à l’aide de la bibliothèque `matplotlib`.



## Contexte

Les scientifiques visualisent souvent des données sous forme de graphiques pour interpréter plus facilement des tendances, des anomalies ou des corrélations. Python permet de produire des graphiques de haute qualité grâce à la bibliothèque `matplotlib`.

Dans cette leçon, on apprend à créer des graphiques de base : courbe, points, étiquettes et titres. On travaille dans **Jupyter Notebook** à l’intérieur de l’environnement **Anaconda**.


## Notions abordées

1. **Importation de la bibliothèque**

   ```python
   import matplotlib.pyplot as plt
   ```

2. **Tracé simple d’une courbe**

   ```python
   x = [0, 1, 2, 3, 4]
   y = [0, 1, 4, 9, 16]
   plt.plot(x, y)
   plt.show()
   ```

3. **Ajout de titres et étiquettes**

   ```python
   plt.title("Croissance quadratique")
   plt.xlabel("Temps (s)")
   plt.ylabel("Distance (m)")
   ```

4. **Personnalisation de la courbe**

   * Style de ligne, couleur, marqueur

   ```python
   plt.plot(x, y, color='green', linestyle='--', marker='o')
   ```

5. **Tracer plusieurs courbes sur un même graphique**

   ```python
   plt.plot(x, y, label="objet A")
   plt.plot(x, [i**1.5 for i in x], label="objet B")
   plt.legend()
   ```

6. **Enregistrement du graphique**

   ```python
   plt.savefig("mon_graphique.png")
   ```


## Exercice pratique

**Titre :** Température d’un liquide en fonction du temps
**But :** À partir des données fournies, tracer la courbe de température d’un liquide chauffé pendant 10 minutes.

**Données :**

```python
temps = [0, 2, 4, 6, 8, 10]
temperature = [20, 35,  fifty, 65, 72, 74]  # Erreur volontaire à corriger
```

## Résultat attendu

Un graphique clair et lisible du type :

* Titre : Température du liquide en fonction du temps
* Axe X : Temps (min)
* Axe Y : Température (°C)
* Ligne rouge en pointillés avec des cercles
* Fichier PNG enregistré dans le dossier de travail
---


{{% notice style="cyan" title="À retenir" %}}
* Une **liste** permet de stocker plusieurs valeurs.
* On peut **ajouter, enlever, parcourir et modifier** les éléments d’une liste.
* Une **chaîne de caractères** est une séquence de lettres manipulable comme une liste.
* Il existe de nombreuses **fonctions utiles** pour manipuler du texte (majuscules, recherche, découpage…).
{{% /notice %}}

---

Voici une **leçon essentielle sur `matplotlib` appliquée à l’analyse de solubilité**, destinée à des étudiants de 1re session en sciences de la nature. Elle couvre **juste ce qu’il faut** pour produire des graphiques propres et utiles dans un rapport scientifique (ex. variation de la solubilité d’un sel selon la température). Tous les messages d’affichage utilisent des **f-strings avec `print`**.

---

# 🧪 Leçon : Visualiser la solubilité avec `matplotlib`

## 🎯 Objectif

Savoir tracer rapidement des graphiques pour :

* Visualiser la **solubilité en fonction de la température**.
* Comparer plusieurs composés sur le même graphique.
* Ajouter un titre, des étiquettes d’axes, une légende.
* (Facultatif) Ajouter des barres d’erreur et sauvegarder une figure.

---

## 1. Importer `matplotlib`

```python
import matplotlib.pyplot as plt
```

---

## 2. Données d’exemple : température vs solubilité

```python
temperature = [0, 10, 20, 30, 40, 50]
solubilite = [14, 18, 23, 28, 35, 42]
print(f"Données chargées : {len(temperature)} points de température et {len(solubilite)} points de solubilité.")
```

---

## 3. Nuage de points (scatter)

```python
plt.scatter(temperature, solubilite)
plt.title("Solubilité du sel X en fonction de la température")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d'eau)")
plt.grid(True)
plt.show()

print(f"Nuage de points affiché pour {len(temperature)} mesures.")
```

---

## 4. Relier les points (courbe simple)

Utile si les mesures suivent un ordre naturel (ici, température croissante).

```python
plt.plot(temperature, solubilite, marker="o")
plt.title("Solubilité du sel X (courbe)")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d'eau)")
plt.grid(True)
plt.show()

print(f"Courbe affichée avec {len(temperature)} points reliés.")
```

---

## 5. Comparer deux composés sur un même graphique

```python
temp = [0, 20, 40, 60]
sel_A = [15, 21, 30, 38]
sel_B = [30, 32, 33, 33.5]

plt.plot(temp, sel_A, marker="o", label="Sel A")
plt.plot(temp, sel_B, marker="s", label="Sel B")
plt.title("Comparaison de solubilité : Sel A vs Sel B")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d'eau)")
plt.legend()
plt.grid(True)
plt.show()

print(f"Graphique comparatif affiché pour {len(temp)} températures et 2 composés.")
```

---

## 6. Ajouter des barres d’erreur (incertitude expérimentale)

Supposons une incertitude ±2 g/100g.

```python
temperature = [0, 10, 20, 30, 40, 50]
solubilite = [14, 18, 23, 28, 35, 42]
incertitude = [2, 2, 2, 2, 2, 2]

plt.errorbar(temperature, solubilite, yerr=incertitude, fmt="o-", capsize=5)
plt.title("Solubilité avec incertitude expérimentale (±2 g)")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d'eau)")
plt.grid(True)
plt.show()

print(f"Graphique avec barres d'erreur ±{incertitude[0]} g affiché.")
```

---

## 7. Ajouter une droite de tendance (par régression linéaire)

On suppose que vous avez calculé la pente et l’intercept (ex. via `scipy.stats.linregress`).

```python
import numpy as np
from scipy import stats

temperature = np.array([0, 10, 20, 30, 40, 50])
solubilite = np.array([14, 18, 23, 28, 35, 42])

reg = stats.linregress(temperature, solubilite)
print(f"Pente : {reg.slope:.2f} g/°C")
print(f"Intercept : {reg.intercept:.2f} g à 0°C")

solubilite_pred = reg.slope * temperature + reg.intercept

plt.scatter(temperature, solubilite, label="Mesures")
plt.plot(temperature, solubilite_pred, label="Tendance linéaire")
plt.title("Solubilité vs Température avec droite de tendance")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d'eau)")
plt.legend()
plt.grid(True)
plt.show()

print(f"Droite de tendance tracée avec R²={reg.rvalue**2:.3f}.")
```

---

## 8. Sauvegarder une figure

Toujours appeler `plt.savefig()` **avant** `plt.show()` si vous voulez enregistrer le fichier sans le vider dans certains environnements.

```python
plt.scatter(temperature, solubilite)
plt.title("Solubilité du sel X")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d'eau)")
plt.grid(True)
plt.savefig("solubilite_selX.png")
plt.show()

print(f"Figure sauvegardée sous solubilite_selX.png")
```

---

## ✍️ Exercices pratiques

### 🔹 Exercice 1 – Solubilité simple

Données :

```python
temp = [0, 10, 20, 30, 40, 50]
sol = [10, 14, 18, 25, 32, 40]
```

Tâches :

1. Trace un nuage de points.
2. Ajoute un titre et des étiquettes d’axes.
3. Affiche un `print` confirmant le nombre de points.

---

### 🔹 Exercice 2 – Courbe + barres d’erreur

Données : mêmes que ci-dessus, incertitude ±1.5 g.
Tâches :

1. Trace une courbe reliée (points + ligne).
2. Ajoute des barres d’erreur.
3. Affiche un message avec l’incertitude utilisée.

---

### 🔹 Exercice 3 – Deux sels

Données :

```python
temp = [0, 20, 40, 60]
sel_A = [15, 21, 30, 38]
sel_B = [30, 32, 33, 33.5]
```

Tâches :

1. Trace les deux séries sur le même graphique (marqueurs différents).
2. Ajoute une légende.
3. Imprime un message indiquant lequel semble le plus sensible à la température (inspection visuelle).

---

### 🔹 Exercice 4 – Régression + prévision

Données :

```python
temperature = [0, 10, 20, 30, 40, 50]
solubilite = [14, 18, 23, 28, 35, 42]
```

Tâches :

1. Calcule la régression linéaire (`linregress`).
2. Trace les points + la droite.
3. Calcule la solubilité prévue à 60 °C.
4. `print` la valeur prévue avec deux décimales.

---

### 🔹 Exercice 5 – Figure pour rapport

Crée un graphique propre (titre, axes, grille, légende) et sauvegarde-le sous `"rapport_solubilite.png"`.
Affiche ensuite un message confirmant la sauvegarde.

---

-->
### Exercices à faire avant le cours

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **deuxième examen** (25%)

1. Lire la matière sur [Tableaux NumPy](../semaine9/)
2. Faire les [exercices se trouvant à la fin de la leçon 9](../semaine9/#exercices-à-faire-avant-le-cours)



