+++
chapter = true
pre = "<b>4.</b>"
title = "Les fonctions"
weight = 104
+++


## Objectifs d'apprentissage

* Utiliser des fonctions prédéfinies
* Définir ses propres fonctions avec `def`
* Utiliser des paramètres pour envoyer des données
* Retourner un résultat avec `return`
* Comprendre la portée locale des variables

---

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


---

## Exercices à faire avant le cours

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