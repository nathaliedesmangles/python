+++
chapter = true
pre = "<b>Semaine 7.</b>"
title = "Listes de données et chaînes de caractères"
weight = 70
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

---


{{% notice style="cyan" title="À retenir" %}}
* Une **liste** permet de stocker plusieurs valeurs.
* On peut **ajouter, enlever, parcourir et modifier** les éléments d’une liste.
* Une **chaîne de caractères** est une séquence de lettres manipulable comme une liste.
* Il existe de nombreuses **fonctions utiles** pour manipuler du texte (majuscules, recherche, découpage…).
{{% /notice %}}