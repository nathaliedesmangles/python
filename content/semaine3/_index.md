+++
chapter = true
pre = "<b>3.</b>"
title = "Entrées/Sorties, algorithme et débogage"
weight = 103
+++

## Objectifs d'apprentissage

* Gérer les entrées (**saisies au clavier**) et les sorties (**affichage**) d'un programme Python.
	* Lire des données entrées par l’utilisateur.
* Comprendre le rôle d'un algorithme.
* Écrire et traduire des algorithmes simples en python.
* Apprendre à comprendre les messages d'erreurs et à déboguer un programme

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

---

### Exercices à faire avant le cours:

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
* `print()` permet d'afficher une réponse, seule ou avec du texte.
{{% /notice %}}