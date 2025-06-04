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


## Les variables et les types et affichage de données de base

- Une variable c'est...


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

Les règles de priorité sont les mêmes qu’en mathématiques.
Utilisez les parenthèses pour clarifier vos intentions.

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


