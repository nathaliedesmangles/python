+++
chapter = true
pre = "<b>7.</b>"
title = " Listes, chaînes de caractères et graphiques de base"
weight = 107
draft = true
+++


## Objectifs d'apprentissage

1. **Créer et manipuler des listes** de données numériques ou textuelles en Python (ajout, suppression, parcours, calcul de statistiques simples).
2. **Accéder, modifier et parcourir** les caractères d’une chaîne de caractères.
3. **Appliquer des méthodes de traitement de texte** pour analyser ou transformer des chaînes de caractères (ex. : mise en minuscules, découpage, recherche, comptage).

---


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