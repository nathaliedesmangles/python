+++
chapter = true
pre = "<b>Semaine 3.</b>"
title = "Entrées/Sorties, Algorithme, débogage et fonctions"
weight = 30
+++

## Objectifs d'apprentissage

* Gérer les entrées (**saisies au clavier**) et les sorties (**affichage**) d'un programme Python.
	* Lire des données entrées par l’utilisateur.
* Comprendre le rôle d'un algorithme.
* Écrire et traduire des algorithmes simples en python.
* Apprendre à comprendre les messages d'erreurs et à déboguer un programme
* Utiliser des fonctions prédéfinies (ex: Module math)
* Définir ses propres fonctions.

---

## Lecture, conversion et affichage soigné des données

### Lire une donnée au clavier

La fonction `input()` permet de lire une donnée saisie au clavier :

```python
nom = input("Quel est ton nom ? ")
```

### Convertir les données

Les données entrées par `input()` sont **toujours** des chaînes (`str`). Il faut donc les **convertir** pour faire des calculs :

**Exemple d'erreur en cas d'oubli de convertir**

```python
note1 = input("Entrez la première note")
note1 = note1	r
note2 = input("Entrez la deuxième note")
note2 = note2

moyenne = (note1 + note2) / 2	==> ERREUR
```

CAPTURE IMAGE ERREUR

#### Comment convertir des données en entier (int) ou en nombre flottant (float)

| Fonction  | Conversion vers… | Exemple                |
| --------- | ---------------- | ---------------------- |
| `int()`   | entier           | `int("5") → 5`         |
| `float()` | décimal          | `float("3.14") → 3.14` |

```python
note1 = input("Entrez la première note")
note1 = int(note1)	# conversion en entier
note2 = input("Entrez la deuxième note")
note2 = int(note2)	# conversion en entier

moyenne = (note1 + note2) / 2
```

### Affichage de résultats

On utilise `print()` pour afficher du texte et des valeurs.

```python
note1 = input("Entrez la première note")
note1 = int(note1)	# conversion en entier
note2 = input("Entrez la deuxième note")
note2 = int(note2)	# conversion en entier

moyenne = (note1 + note2) / 2

print("La moyenne des deux notes", note1, "et", note2, "est:", moyenne)
```

Pour un affichage plus soigné, on peut utiliser les **f-strings** :

```python
print(f"La moyenne des deux notes {note1} et {note2} est: {moyenne}")
```

#### Affichage soigné des résultats numériques

EXEMPLE AVEC ALGO SCIENTIFIQUE

## Traduction de l’algorithme en code Python

**Un algorithme**, c’est une suite d’instructions claires pour résoudre un problème.

### Cas concret

Écrire un programme qui calcule la force d'un objet à l'aide de la formule `F = m x a` où `m` est la masse de l'objet et `a` l'accélération.
Le programme doit demander à l'utilisateur d'entrer au clavier la masse et l'accélération.
À la fin, le programme affiche le résultat de la force.

#### L'algorithme (en français) :

> 1. Demander la masse d’un objet
> 2. Demander l’accélération
> 3. Calculer la force avec la formule `F = m × a`
> 4. Afficher la force

#### Traduction en Python :

```python
masse = float(input("Entrez la masse (kg) : "))
acceleration = float(input("Entrez l'accélération (m/s²) : "))
force = masse * acceleration
print("La force est", force, "N")
```

> Astuce : chaque ligne de l’algorithme devient une ou plusieurs lignes de code.


## Débogage

**Déboguer**, c’est trouver et corriger les erreurs dans le code.

### Types d’erreurs fréquentes :

| Type d’erreur      | Exemple                                      | Solution                             |
| ------------------ | -------------------------------------------- | ------------------------------------ |
| Erreur de syntaxe  | `print("Bonjour'`                            | Corriger la fermeture des guillemets |
| Erreur d’exécution | `valeur = int("abc")`                        | Vérifier le type des entrées         |
| Erreur logique     | `aire = longueur + largeur` (au lieu de `*`) | Vérifier la formule                  |

### Exemples à tester (à copier dans VS Code) :

#### Exemple 1 – Erreur de syntaxe

```python
print("Début du programme)
```

> Que dit le message d'erreur ?
> Corrige la ligne.

#### Exemple 2 – Erreur d’exécution

```python
val = int("bonjour")
```

> Quelle est la cause de l’erreur ?
> Remplace `"bonjour"` par `"12"`.

#### Exemple 3 – Erreur logique

```python
longueur = 5
largeur = 2
aire = longueur + largeur  # erreur de formule
print("Aire =", aire)
```

> Est-ce que le résultat est correct ?
> Corrige la formule avec `*` au lieu de `+`.

### Astuces pour déboguer :

* Lire le message d’erreur affiché
* Ajouter des **print()** pour suivre les valeurs
* Tester une ligne à la fois
* Vérifier les types avec type()

### Exemples concrets

**Message d'erreur affiché**

**Utilisation de print()**

**Exploration des variables, ligne par ligne**

## Utilisation de fonctions prédéfinies

Python offre déjà plein de **fonctions toutes prêtes** (*prédéfinies*).

### Exemples utiles :

| Fonction  | Utilité                                 | Exemple                         |
| --------- | --------------------------------------- | ------------------------------- |
| `print()` | Afficher un message                     | `print("Bonjour !")`            |
| `input()` | Demander une donnée à l’utilisateur     | `nom = input("Votre nom :")`    |
| `int()`   | Convertir en entier                     | `val = int("5")`                |
| `float()` | Convertir en nombre décimal             | `val = float("3.14")`           |
| `round()` | Arrondir un nombre                      | `round(2.718, 2)` → `2.72`      |
| `len()`   | Compter les éléments d’une chaîne/liste | `len("atomes")` → `6`           |
| `type()`  | Afficher le type d’une variable         | `type(3.5)` → `<class 'float'>` |

> On **appelle** une fonction en écrivant son nom suivi de parenthèses.

### Fonctions du module `math`

Pour accéder à des fonctions mathématiques plus avancées, on utilise le **module `math`**.

```python
import math
```

| Fonction         | Description        | Exemple                         |
| ---------------- | ------------------ | ------------------------------- |
| `math.sqrt(x)`   | Racine carrée      | `math.sqrt(16)` → `4.0`         |
| `math.pow(x, y)` | Puissance          | `math.pow(2, 3)` → `8.0`        |
| `math.pi`        | La constante π     | `math.pi` → `3.14159...`        |
| `math.sin(x)`    | Sinus (en radians) | `math.sin(math.pi / 2)` → `1.0` |
| `math.log(x)`    | Logarithme naturel | `math.log(10)`                  |

### Exercices à faire :

a) Écrire l'algorithme correspondant au code ci-dessous :

```python
import math

r = float(input("Entrez le rayon du cercle : "))
aire = math.pi * math.pow(r, 2)
print("Aire du cercle :", round(aire, 2), "unités²")
```


b) Traduisez l’algorithme suivant en code Python :

> 1. Demander le nom d’un élément chimique
> 2. Afficher un message disant "L’élément choisi est \[nom]"

{{% notice style="cyan" title="À retenir" %}}
* `input()` permet de lire une donnée (toujours une chaîne).
* Il faut convertir avec `int()` ou `float()` pour faire des calculs.
* `print()` permet d'afficher une réponse, seule ou avec du texte et .
{{% /notice %}}