+++
chapter = true
pre = "<b>2.</b>"
title = "Introduction à Python (Variables, types et expressions)"
weight = 102
+++


## Objectifs d'apprentissage

À la fin de cette leçon vous serez en mesure de:

* Définir et utiliser des **variables** en Python.
* Manipuler les **types de base** en Python: `int`, `float`, `str`, `bool`.
	* Afficher les résultats de manière claire et lisible
---

## Variables et types de données de base

Une **variable** est un nom qui permet de **stocker une valeur** pour la réutiliser.

**Exemples :**

```python
age = 17
nom = "Julie"
temperature = 36.6
```

### Types de données courants :

| Type    | Exemple         | Description                     |
| ------- | --------------- | ------------------------------- |
| `int`   | `5`, `-3`       | Nombre entier                   |
| `float` | `3.14`, `-0.5`  | Nombre à virgule flottante      |
| `str`   | `"Bonjour"`     | Chaîne de caractères            |
| `bool`  | `True`, `False` | Valeur booléenne (vrai ou faux) |

### Vérifier le type d’une variable :

```python
age = 18
type_age = type(age)
print(type_age)  # <class 'int'>
```

## Règles de nommage des variables

Bonnes pratiques :

* Utiliser des **noms significatifs** (ex : `masse_corps`, `volume_solution`)
* Commencer par une **lettre** ou un **souligné (\_)**, jamais par un chiffre.
* Éviter les mots réservés de Python (`if`, `for`, `print`, etc.).
* Utiliser des mots séparés par des soulignés (\_).
* Utiliser des mots commençants par une lettre majuscule, sauf le premier mot (ex : `masseCorps`, `volumeSolution`).

Mauvais exemples :

```python
1age = 20       # commence par un chiffre → erreur
print = 8       # print est un mot réservé → erreur
```

## Documentation du code (les commentaires)

On écrit des **commentaires** pour expliquer le code. Python ignore tout ce qui suit `#` sur une ligne.

**Exemples :**

```python
# Calcul de l'aire d'un cercle
rayon = 3
aire = 3.14 * rayon ** 2  # formule de l’aire
```

## Opérateurs arithmétiques

| Opérateur | Signification               | Exemple  | Résultat |
| --------- | --------------------------- | -------- | -------- |
| `+`       | Addition                    | `3 + 2`  | `5`      |
| `-`       | Soustraction                | `7 - 4`  | `3`      |
| `*`       | Multiplication              | `5 * 2`  | `10`     |
| `/`       | Division (résultat décimal) | `6 / 2`  | `3.0`    |
| `//`      | Division entière            | `7 // 2` | `3`      |
| `%`       | Modulo (reste)              | `7 % 2`  | `1`      |
| `**`      | Puissance                   | `3 ** 2` | `9`      |


## Expressions et priorité des opérateurs

Une **expression** est une combinaison de variables, de nombres et d'opérateurs.

### Priorité (ordre d’exécution) des opérateurs :

1. `()` : parenthèses
2. `**` : puissance
3. `*`, `/`, `//`, `%` : multiplication et division
4. `+`, `-` : addition et soustraction

**Exemple :**

```python
resultat = 3 + 4 * 2       # donne 11, pas 14 !
resultat = (3 + 4) * 2     # donne 14 grâce aux ()
```

## Affichage simple des données avec print

On utilise `print()` pour afficher du texte et des valeurs.

```python
prenom = "Nathalie"
age = 18
print("Bonjour", prenom)
print("Tu as", age, "ans.")
```

**NB** : 
* Tout ce qui est du texte fixe (autre que la valeur d'une variable), se met entre guillemets (simples ou doubles).
* On délimite les éléments texte vs variable par une virgule.
* Par défaut, la fonction `print()` ajoute un espace entre chacun des éléments écrit entre ses parenthèses.

---


{{% notice style="cyan" title="À retenir" %}}
* Une variable garde une **valeur**.
* On utilise les **bonnes pratiques** pour nommer nos variables.
* Les **commentaires** servent à documenter le code.
* Les **opérateurs arithmétiques** permettent de faire des calculs.
* Comme en mathématiques, l’ordre des opérations est **important** en Python.
* `print()` permet d'afficher une réponse, seule ou avec du texte.
{{% /notice %}}




