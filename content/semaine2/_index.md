+++
chapter = true
pre = "<b>Semaine 2.</b>"
title = "Introduction à Python (variables, types, entrée/sortie)"
weight = 20
+++


## Objectifs d'apprentissage

À la fin de cette leçon vous serez en mesure de:

* Définir et utiliser des **variables** en Python.
* Manipuler les **types de base** en Python: `int`, `float`, `str`, `bool`.
	* Afficher les résultats de manière claire et lisible
* Gérer les entrées (**saisies au clavier**) et les sorties (**affichage**) d'un programme Python.
	* Lire des données entrées par l’utilisateur.
---

## Les variables et les types et affichage de données de base

Lorsqu’on écrit de vrais programmes, on a souvent besoin de **stocker des valeurs ou des résultats de calculs en mémoire**.

### Qu’est-ce qu’une variable ?

- Les variables sont utilisées pour stocker ces valeurs ou résultats, pour pouvoir **les réutiliser** plus tard. Imaginez une boîte dans laquelle vous rangez quelque chose : c’est ça, une variable.

{{% notice style="cyan" title="Sachez que" %}}
De manière générale, il est **recommandé** de **donner un nom évocateur** à une variable, afin de mieux comprendre ce qu’elle contient.
{{% /notice %}}

### Définir une variable et lui attribuer une valeur

- En Python, on utilise le symbole `=` (appelé **opérateur d'affectation**) pour attribuer une valeur à une variable. Il est préférable de mettre un espace avant et après le `=`.
- Il est aussi possible de chaîner des affectations, par exemple : `a = b = 2`. Ici les variables `a` et `b` valent toutes les deux `2`.

**Exemple de définition d'une variable** 

```python
jour_de_la_semaine = "Lundi"
```

**Explication du code**

- Ici, la **valeur textuelle** `"Lundi"` est enregistrée en mémoire. On peut la réutiliser en appelant le nom de la variable, par exemple :

```python
print(jour_de_la_semaine)  # Résultat qui s'affiche: Lundi
```

- La variable `jour_de_la_semaine` contient une valeur de type ***`str`*** (**chaîne de caractères**) :

```python
print(type(jour_de_la_semaine))  # <class 'str'>
```

- On peut **toujours modifier la valeur** d’une variable :

```python
jour_de_la_semaine = "Mardi"
```

Maintenant, la variable contient une nouvelle valeur :

```python
print(jour_de_la_semaine)  # Résultat qui s'affiche: Mardi
```

Il est aussi possible d’**attribuer la valeur d’une variable à une autre variable** :

```python
nombre1 = 10
nombre2 = nombre2  		# nombre2 vaut aussi 10
```

Python permet aussi d’**assigner des valeurs de types différents à une même variable**. Par exemple :

```python
mois = "Décembre"
print(type(mois))  # <class 'str'>
```

Puis :

```python
mois = 12
print(type(mois))  # <class 'int'>
```

Cela fonctionne parce que Python est un langage à **typage dynamique**. C'est-à-dire, que la variable prends **automatiquement** le **type de la valeur** qui lui est assignée.

> <span style="color:red;"><b>Ne pas abuser du typage dynamique</b></span> : dans un long programme, on peut oublier qu’on a changé le type d’une variable, ce qui peut provoquer des erreurs difficiles à trouver.

### Règles pour nommer les variables

Comme mentionné plus haut, chaque variable a un nom qui la distingue des autres. Voici les **règles à respecter** :

* Les noms sont **sensibles à la casse** (`mois` ≠ `Mois`).
* Un nom doit **commencer par une lettre ou un trait de soulignement**, et peut contenir des lettres, chiffres ou traits de soulignement (ex. : `utilisateur_nom`, `score1`, `_compteur`).
* Un nom **ne peut pas commencer par un chiffre** (ex. : `2q` est <span style="color:red;"><b>invalide</b></span>).
* Un nom **ne doit pas être un mot réservé (mot-clé)** du langage.

> <span style="color:red;"><b>Ne brisez pas ces règles, sinon votre programme ne fonctionnera pas</b></span>.

### Exercices 

1. **Définir une chaîne de caractères**
   - Créez une variable appelée `fete` avec la valeur `"Journée du roulé à la cannelle"`, qui doit être une chaîne de caractères.

```python
# définir une nouvelle variable ici
fete = "Journée du roulé à la cannelle"
```
2. Assignez la chaîne de caractères `"Python"` à la variable `prenom`.
3. À la ligne 10, remplacez la valeur de la variable `prenom` par votre vrai prénom.
4. Utilisez une affectation chaînée pour stocker la valeur 13 dans `age_jumeau1` et `age_jumeau2` à la ligne 15.

## Les variables non définies

NOTICE
Si vous essayez d’utiliser une variable **non définie**, Python renverra une erreur :

```python
print(nom_du_mois)  # NameError: name 'nom_du_mois' is not defined
```

### Exercices

1. Définissez la variable `cours`, sans lui donner de valeur. Ensuite utilisez `print()` pour afficher sa valeur. Que se passe t-il?
2. Définissez la variable `maVariable` en lui donnant la valeur ``. Ensuite, afficher la valeur de la variable `MaVariable`. Qu'observez-vous ? Comment pouvez-vous l'expliquer ?

## Les types des variables


## La conversion des types de variables



## Les opérations arithmétiques en Python

Python peut effectuer toutes les opérations de base :

| Opération        | Symbole | Exemple   | Résultat |
| ---------------- | ------- | --------- | -------- |
| Addition         | `+`     | `2 + 3`   | `5`      |
| Soustraction     | `-`     | `7 - 2`   | `5`      |
| Multiplication   | `*`     | `4 * 5`   | `20`     |
| Division         | `/`     | `10 / 4`  | `2.5`    |
| Division entière | `//`    | `10 // 4` | `2`      |
| Modulo           | `%`     | `10 % 4`  | `2`      |
| Puissance        | `**`    | `2 ** 3`  | `8`      |

- Les règles de priorité sont les mêmes qu’en mathématiques.
- Utilisez les parenthèses pour clarifier vos intentions.

### Exercices 

0. Définissez la variables `nombre_initial` avec la valeur `9.0`
1. Diviser la valeur stockée dans `nombre_initial` par 2 et stocker le résultat dans la variable `resultat_division`.
2. Calculer le reste d’une telle division et stocker le résultat dans la variable `reste_division`.
3. Multiplier `resultat_division` par 2 et stocker le résultat dans la variable `resultat_multiplication`.
4. Ajouter `reste_division` à `resultat_multiplication` et stocker le résultat dans la variable `somme_finale`.
5. Soustraire `resultat_multiplication` de `nombre_initial` et stocker le résultat dans la variable `difference`.
6. Effectuer une division entière de `nombre_initial` par 2 et stocker le résultat dans la variable `division_entiere`.
7. Élever `resultat_multiplication` à la puissance 3 et stocker le résultat dans la variable `puissance_trois`.
8. Affichez toutes les variables à l'aide de print(). Résultat attendu
```

```

## Affectations raccourcies

- Une **affectation raccourcie** est une instruction unique qui combine une opération binaire et une affectation, comme `+=`, `-=`, etc.

Une expression d’affectation raccourcie comme `nombre += 1` peut être réécrite en `nombre = nombre + 1` pour obtenir le même résultat.

### Exercices

1. Utilisez une affectation raccourcie pour ajouter `5` à la variable `nombre` et la mettre à jour.
number = 9.0
print("number = " + str(number))

number -= 2
print("number = " + str(number))

number += 5

print("number = " + str(number))


### **Opérateurs booléens**

Un **booléen** est un type de valeur qui ne peut être que **Vrai** (`True`) ou **Faux** (`False`).
L’opérateur `==` (égalité) compare deux variables pour vérifier si elles sont égales.
Vous en apprendrez davantage sur les opérateurs booléens dans une tâche ultérieure.

Pour une explication plus structurée et détaillée, vous pouvez consulter cette page de la base de connaissances Hyperskill.

---

### **Tâche**

* Vérifiez si la variable `deux` est égale à `trois`.
* Vérifiez si la variable `est_egal` porte un nom trompeur.
* Vérifiez si la variable `est_faux` contient effectivement un mensonge.

Utilisez l’opérateur `==`.
Utilisez la valeur `True`.
Utilisez la valeur `False`.

---

**Exemple de code en français :**

```python
deux = 2
trois = 3

est_egal = (deux == trois)      # False
print(est_egal)

est_faux = (est_egal == False)  # True
print(est_faux)
```

## Comparison operators

---

### Conclusion

Dans cette leçon, nous avons découvert ce que sont les **variables** en Python. Nous avons vu comment les **définir**, leur **assigner des valeurs**, et les **règles à suivre pour les nommer**. Ces notions vous seront très utiles pour bien progresser dans l’apprentissage de Python !

---


## Les entrées de l'utilisateur (via le clavier)

Pour demander une valeur à l’utilisateur :

```python
nom = input("Quel est ton nom? ")
```

Par défaut, `input()` retourne une chaîne de caractères (`str`).
Pour effectuer des calculs, vous devez convertir en nombre :

```python
masse = float(input("Entrer la masse en grammes : "))
```

Utilisez `int()` pour les entiers et `float()` pour les décimaux.

## Les sorties (affichage)

```python
print("Bonjour", nom)
print("La concentration est", concentration, "mol/L")
```

Pour un affichage plus précis :

```python
print(f"La concentration est de {concentration:.2f} mol/L")
```

Ici, `:.2f` signifie : afficher avec 2 chiffres après la virgule.

## Erreurs courantes et comment les éviter

| Type d’erreur         | Exemple                            | Explication                   |
| --------------------- | ---------------------------------- | ----------------------------- |
| **SyntaxError**       | `print("Bonjour"`                  | Parenthèse fermante manquante |
| **TypeError**         | `"masse" + 10`                     | Mélange de texte et de nombre |
| **ZeroDivisionError** | `10 / 0`                           | Division par zéro             |
| **ValueError**        | `float("abc")`                     | Conversion invalide           |
| **NameError**         | `print(resultat)` sans déclaration | Variable non définie          |

**Conseil :** Lisez toujours attentivement le message d’erreur. Python vous indique généralement la ligne concernée et le type de problème.


## En résumé

* Python sait calculer, mais il faut lui donner des consignes claires.
* Toujours convertir les entrées `input()` si vous voulez faire des calculs.
* Utilisez `print()` pour afficher vos résultats avec clarté.
* Ne vous découragez pas face aux erreurs : elles sont des occasions d’apprentissage.

---

# Atelier à faire en classe (2 périodes)

## Exercice 1

## Exercice 2

## Exercice 3
