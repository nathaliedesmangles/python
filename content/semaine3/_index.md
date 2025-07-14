+++
chapter = true
pre = "<b>3.</b>"
title = "Saisie au clavier, débogage et fonctions"
weight = 103
+++

## Objectifs d'apprentissage

* Gérer les entrées (**saisies au clavier**) d'un programme Python.
	* Lire des données entrées par l’utilisateur.
* Utiliser des fonctions prédéfinies
* Définir ses propres fonctions avec `def`
   * Utiliser des paramètres pour envoyer des données
   * Retourner un résultat avec `return`
   * Comprendre la portée locale des variables
* Apprendre à comprendre les messages d'erreurs et à déboguer un programme

---

## Lecture et conversion de données

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

print(f"La moyenne des deux notes {note1} et {note2} est: {moyenne}")
```

## Débogage

**Déboguer**, c’est trouver et corriger les erreurs dans le code.

### Types d’erreurs fréquentes :

| Type d’erreur      | Exemple                                      | Solution                             |
| ------------------ | -------------------------------------------- | ------------------------------------ |
| Erreur de syntaxe  | `print("Bonjour'`                            | Corriger la fermeture des guillemets |
| Erreur d’exécution | `valeur = int("abc")`                        | Vérifier le type des entrées         |
| Erreur logique     | `aire = longueur + largeur` (au lieu de `*`) | Vérifier la formule                  |

## Qu’est-ce qu’une fonction ?

* Une fonction est un **bloc de code réutilisable**. On peut lui donner des **paramètres** (valeurs en entrée) et elle peut renvoyer un **résultat**. 
* Si une fonction renvoie un résultat, il devra être stocké dans  une variable pour pouvoir être utilisé ailleurs dans le code.

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

### Quelques fonctions du module `math`

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


## Définir une fonction avec `def`

### Syntaxe de base :

```python
def nom_fonction(param1, param2):
    instructions
    return résultat
```

### Exemple :

```python
def aire_rectangle(longueur, largeur):
    aire = longueur * largeur
    return aire
```

> Cette fonction reçoit deux valeurs, calcule l’aire et la retourne.


## Appeler une fonction

### Exemple :

```python
a = aire_rectangle(5, 2)
print("Aire :", a)
```


## Le mot-clé `return`

* Il **renvoie un résultat** à l’endroit où la fonction a été appelée.
* Dès que `return` est exécuté, la fonction **s’arrête**.

### Exemple :

```python
def carre(x):
    return x * x
```


## La portée locale des variables

Les **variables créées dans une fonction** (ex: `aire`) **n’existent que dans la fonction**.

### Exemple :

```python
def test():
    x = 10
    return x

print(test())  # OK
print(x)       # Erreur : x n'existe pas ici
```


{{% notice style="cyan" title="À retenir" %}}
| Élément       | Rôle                                                        |
| ------------- | ----------------------------------------------------------- |
| `def`         | Définir une fonction                                        |
| Paramètres    | Donner des valeurs à la fonction                            |
| `return`      | Retourner un résultat (`resultat = fonction()` ou <br> `print(fonction())`)             |
| Portée locale | Les variables dans une fonction n’existent qu’à l’intérieur |
{{% /notice %}}


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

{{% notice style="cyan" title="À retenir" %}}
* `input()` permet de lire une donnée (toujours une chaîne).
* Il faut convertir avec `int()` ou `float()` pour faire des calculs.
* `print()` permet d'afficher une réponse, seule ou avec du texte.
{{% /notice %}}


---

### Exercices à faire avant le cours:


{{% notice style="cyan" title="Appel de fonction" %}}
Pour chacun des exercices ci-dessous, utilisez (appelez) la fonction crée.
{{% /notice %}}

### Exercice 1 - Élément chimique

Écrire une fonction `element_chimique()` qui :
* Demande à l'utilisateur d'entrer le nom d’un élément chimique.
* Affiche un message disant "L’élément choisi est \[nom]"

### Exercice 2 - Aire d'un cercle

Écrire une fonction `aire_cercle()` qui :
* Demande à l'utilisateur d'entrer le rayon du cercle (en cm).
* Calcule l'aire du cercle (utiliser le **module math** pour PI et le rayon².)
* Affiche l'aire du cercle, arrondie à 2 décimales (utiliser la fonction `round`).

**Exemple d'affichage attendu (rayon de 5 cm)** :
```python
Aire du cercle de rayon 5 cm : 78.54 cm²
```

### Exercice 3 - Convertir Celsius en Kelvin

Crée une fonction nommée `convertir_C_en_K` qui :

* prend une température en °C en paramètre
* retourne la température en Kelvin (formule : K = C + 273.15)

**Solution :**

```python
def convertir_C_en_K(celsius):
    kelvin = celsius + 273.15
    return kelvin

print(convertir_C_en_K(25))  # 298.15
```

### Exercice 4 – Calculer une énergie cinétique

Crée une fonction `energie_cinetique(m, v)` qui calcule :

```math
$E_c = \frac{1}{2} \cdot m \cdot v^2$
```

**Solution :**

```python
def energie_cinetique(m, v):
    return 0.5 * m * v**2

print(energie_cinetique(2.0, 3.0))  # 9.0
```

### Exercice 5 – Vérifier la portée locale

Crée une fonction `tester_variable()` qui crée une variable `x = 10` et l’affiche dans la fonction.
Essaye ensuite d’afficher `x` **à l’extérieur de la fonction**.

**Solution :**

```python
def tester_variable():
    x = 10
    print("Dans la fonction :", x)

tester_variable()
print("À l’extérieur :", x)  # Erreur attendue
```
