+++
chapter = true
pre = "<b>3.</b>"
title = " Saisie au clavier, fonctions et débogage"
weight = 103
+++

## Objectifs d'apprentissage

* Gérer les entrées (**saisies au clavier**) d'un programme Python.
* Utiliser des fonctions **prédéfinies**.
* Définir ses propres fonctions avec `def` (paramètres, `return`, portée locale)
* Comprendre les messages d'erreurs et à apprendre à déboguer un programme.

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
note2 = input("Entrez la deuxième note")

moyenne = (note1 + note2) / 2	==> ERREUR
```

![Erreur de type](./erreur_type.png)

{{% notice style="accent" title="Important" %}}
L'erreur est causée par le fait que la fonction `input()`, transforme toutes les saisies au clavier en **chaine de caractères (`str`)**.
Si on tape **95** au clavier, pour Python ça devient **"95"**.
{{% /notice %}}

#### Comment convertir des données en entier (*int*) ou en nombre flottant (*float*)

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
> La **conversion des deux notes en entier**, fait en sorte que Python arrive à faire le calcul sans problème.


## Qu’est-ce qu’une fonction ?


{{% notice style="cyan" title="Analogie dans la vie de touts les jours" %}}


{{% /notice %}}

* Une fonction est un **bloc de code réutilisable**. On peut lui donner des **paramètres** (valeurs en entrée) et elle peut renvoyer un **résultat**. 
* Si une fonction renvoie un résultat, il devra être stocké dans  une variable pour pouvoir être utilisé ailleurs dans le code.

### Utilisation de fonctions prédéfinies

Python offre plein de **fonctions toutes prêtes** (*prédéfinies*).

**Exemples de fonctions prédéfinies** :

| Fonction  | Utilité                                 | Exemple                         |
| --------- | --------------------------------------- | ------------------------------- |
| `print()` | Afficher un message                     | `print("Bonjour !")`            |
| `input()` | Demander une donnée à l’utilisateur     | `nom = input("Votre nom :")`    |
| `int()`   | Convertir en entier                     | `val = int("5")`                |
| `float()` | Convertir en nombre décimal             | `val = float("3.14")`           |
| `round()` | Arrondir un nombre                      | `round(2.718, 2)` → `2.72`      |
| `len()`   | Compter les éléments d’une chaîne/liste | `len("atomes")` → `6`           |
| `type()`  | Afficher le type d’une variable         | `type(3.5)` → `<class 'float'>` |

> On utilise une fonction en l'**appelant**. On l'appelle en écrivant son nom suivi de parenthèses.

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


## Création de fonction avec `def`

**Rappel** : 
> Une fonction peut:
   > 1. Afficher un résultat (ex: `print()`)
   > 2. Retourner un résultat (ex: `input()`)


### Comment créer et utiliser une fonction ?

1. On utilise le mot clé `def`.
2. Suivi du nom de la fonction.
3. Suivi de parenthèses `()`.
4. suivi de deux-points `:`.
5. Les instructions de la fonction sont sur les lignes d'en dessous, décalées. Ce décalage, permet à Python de reconnaitre le code à exécuter.

{{% notice style="accent" title="Important" %}}
* Les règles de **nomenclature des variables**, s'appliquent aussi aux noms de fonctions.
* Entre les parenthèses, on peut indiquer des **paramètres ou pas**, mais les **parenthèses sont obligatoires**.
{{% /notice %}}

#### Syntaxes générales

**Une fonction qui affiche le résultat** :
```python
def nom_fonction(param1, param2):
    instructions
    print(résultat)
```

**Exemple** :

```python
def aire_rectangle(longueur, largeur):
    aire = longueur * largeur
    print(f"L'aire du rectangle de longueur {longueur} et de largeur {largeur} est {aire} cm^2")
```

> Cette fonction reçoit deux valeurs (longueur et largeur du rectangle), calcule l’aire du rectangle et **affiche** l'aire.

**Une fonction qui retourne le résultat** :

```python
def nom_fonction(param1, param2):
    instructions
    return résultat
```

**Exemple** :

```python
def aire_rectangle(longueur, largeur):
    aire = longueur * largeur
    return aire
```

> Cette fonction reçoit deux valeurs (longueur et largeur du rectangle), calcule l’aire du rectangle et la **retourne**.

#### Le mot-clé `return`

* Il **renvoie un résultat** à l’endroit où la fonction a été utilisée (appelée).
* Dès que `return` est exécuté, la fonction **s’arrête**.


#### Appeler (utiliser) une fonction

**Utilisation de la fonction `aire_rectangle()` qui **affiche** l'aire**

```python
aire_rectangle(5, 2)
```

> Ici, 5 est la valeur pour la longueur et 2 celle de la largeur.

**Utilisation de la fonction `aire_rectangle()` qui **retourne** l'aire**

```python
surface = aire_rectangle(5, 2)
print("L'aire du rectangle est : {surface}")
```
> Notez la différence: Ici, **il faut stocker le résultat de la fonction dans une variable**.

### La portée locale des variables

Les **variables créées **à l'intérieur** d'une fonction** (ex: `aire`) **n’existent que dans la fonction**.

**Exemple** :

```python
def test():
    x = 10  <---- On peut utiliser x qu'à l'intérieur de la fonction.
    return x <---- Après cette ligne, x n'existe plus. 

print(test())  # OK, affiche 10
print(x)       # Erreur : x n'existe pas ici
```
![Erreur de nom](./erreur_name.png?width=35vw)


## Trouver facilement les sources des erreurs dans nos programmes (débogage)

**Déboguer**, c’est trouver les causes des erreurs dans le cod, afin de les corriger rapidement.

### Types d’erreurs fréquentes

* **Erreur de syntaxe** : La syntaxe de Python n'est pas respectée. Ex.: `print("Bonjour'`
* **Erreur d’exécution** : Le mauvais type de données est utilisé. Ex.: `valeur = int("abc")`
* **Erreur logique** : Les instructions ne correspondent pas à la logique imposée par le problème. Ex.: `aire = longueur + largeur`
 

### Quelques habitudes à avoir pour déboguer :

* Lire le message d’erreur affiché
* Ajouter des **print()** pour suivre les valeurs
* Tester une ligne à la fois
* Est-ce que le résultat est correct ?
* Vérifier les types avec type()


### Exemple de code présentant des erreurs

**Énoncé du problème**

Ce programme est censé calculer le temps nécessaire pour qu’un objet tombe d’une certaine hauteur `h` en chute libre (sans frottement), en utilisant la formule :

```math
$$
t = \sqrt{\frac{2h}{g}}
$$
où $g = 9.8 \, m/s^2$ est l’accélération gravitationnelle.
```
> Malheureusement, le programme contient des erreurs. Utilise des `print()` pour comprendre ce qui ne fonctionne pas, puis corrige le code.

---

**Code à déboguer**

```python
import math

def temps_chute(hauteur):
    g = "9.8"
    t = math.sqrt(2 * hauteur / g)
    return t

h = input("Entrez la hauteur de chute en mètres: ")

print("Hauteur entrée:", h)

temps = temps_chute(h)

print("Le temps de chute est", temps "secondes.")
```

---

{{% notice style="magenta" title="Correction attendue" groupid="notice-toggle" expanded="false" %}}

**Erreurs intégrées** :

1. `g = "9.8"` : valeur gravitationnelle en chaîne de caractères → provoquera une erreur de type.
2. `input()` retourne une chaîne → doit être convertie en `float()`.
3. Il manque une virgule dans le `print()` final.
4. Le type de la variable `hauteur` dans `temps_chute()` est incorrect (chaîne).
5. Possibilité d’ajouter un `print()` intermédiaire dans `temps_chute()` pour voir la valeur de `t`.

```python
import math

def temps_chute(hauteur):
    g = 9.8
    t = math.sqrt(2 * hauteur / g)
    return t

h = float(input("Entrez la hauteur de chute en mètres: "))

print("Hauteur entrée:", h)

temps = temps_chute(h)

print("Le temps de chute est", temps, "secondes.")
```
{{% /notice %}}

{{% notice style="cyan" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* Python fourni des fonctions prédéfinies, prêtes à être utiliser (ex: les fonctions du module `math`)
* `input()` permet de lire une donnée (toujours une chaîne).
* Il faut convertir avec `int()` ou `float()` pour faire des calculs.
* `def` : sert à définir une fonction 
* nom_fonction(paramètres) : Les paramètres sont les variables représentant les données dont la fonction a besoin pour obtenir le résultat.                   
* `return` : Permet à la fonction de retourner un résultat (`resultat = fonction()` ou <br> `print(fonction())`)
* Portée locale : Signifie que les variables dans une fonction n’existent qu’à l’intérieur de .elle-ci|
* Pour utiliser une fonction prédéfinie ou personnalisé, il faut écrire sont nom, les parenthèses et les paramètres si elle en a.
{{% /notice %}}

---

### Exercices à faire avant le cours


{{% notice style="magenta" title="Appel de fonction" groupid="notice-toggle" expanded="false" %}}
Pour chacun des exercices ci-dessous, utilisez (appelez) la fonction crée.
{{% /notice %}}

## Exercice 1 : La loi d'Ohm

Un technicien de laboratoire vous demande d'écrire un programme Python pour calculer la tension (U) en volts selon la loi d’Ohm. Il voudrait pouvoir entrer la valeur de la résistance (en ohms) et la valeur du courant (en ampères), puis obtenir la tension.

```math
Loi d’Ohm : $ U = R × I $
```

1. Le programme demande à l'utilisateur d'entrer la valeur de la résistance (en ohms)
2. Le programme demande à l'utilisateur d'entrer la valeur du courant (en ampères)
3. Calculer et afficher la tension à l'aide d'une phrase.
4. Ajouter des explications en commentaire dans le code.

**Résultat attendu** :

```
Entrer la résistance en ohms : 10
Entrer le courant en ampères : 2
La tension est de 20.0 V
```

### Exercice 2 : Élément chimique

Écrire une fonction `element_chimique()` qui :
* Demande à l'utilisateur d'entrer le nom d’un élément chimique.
* Affiche un message disant "L’élément choisi est \[nom]"

### Exercice 3 : Aire d'un cercle

Écrire une fonction `aire_cercle()` qui :
* Demande à l'utilisateur d'entrer le rayon du cercle (en cm).
* Calcule l'aire du cercle (utiliser le **module math** pour PI et le rayon².)
* Affiche l'aire du cercle, arrondie à 2 décimales (utiliser la fonction `round`).

**Exemple d'affichage attendu (rayon de 5 cm)** :
```python
Aire du cercle de rayon 5 cm : 78.54 cm²
```

### Exercice 4 : Convertir Celsius en Kelvin

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

### Exercice 5 : Calculer une énergie cinétique

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

### Exercice 6 : Vérifier la portée locale

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
### Exercice 7 : Trouvez les erreurs et corrigez les

**Énoncé du problème** :

> Ce programme est censé calculer la surface d’un cône droit à partir du rayon et de la hauteur entrés par l’utilisateur. La formule utilisée est :
```math
$$
\text{Surface} = \pi \cdot r \cdot (r + \sqrt{r^2 + h^2})
$$
```
> Toutefois, plusieurs erreurs se sont glissées dans le programme. Utilise des instructions `print()` pour comprendre les erreurs, puis corrige-les une à une.


### Code à déboguer et corriger

```python
import math

def surface_cone(rayon, hauteur):
    aire_base = math.pi * rayon ** 2
    aire_lateral = math.pi * rayon * math.sqrt(rayon**2 + hauteur)
    surface = aire_base + aire_latérale
    return surface

r = input("Entrez le rayon du cône: ")
h = input("Entrez la hauteur du cône: ")

print("Rayon saisi:", r)
print("Hauteur saisie:", h)

resultat = surface_cone(r, h)

print("La surface totale du cône est de", resultat "cm²")
```
---

{{% notice style="magenta" title="Correction attendue" groupid="notice-toggle" expanded="false" %}}
**Erreurs à corriger, dans l'ordre**:  
1. `input()` retourne une **chaîne de caractères** → nécessite une conversion `float()`.
2. Erreur dans le calcul de `aire_lateral`: `hauteur` au lieu de `hauteur**2`.
3. Nom de variable mal orthographié : `aire_latérale` ≠ `aire_lateral` (accent).
4. Manque une virgule dans le `print()` final.
5. Nom de variables non explicites et parfois contradictoires (`r`, `rayon`), ce qui peut déstabiliser.

```python
import math

def surface_cone(rayon, hauteur):
    aire_base = math.pi * rayon ** 2
    aire_lateral = math.pi * rayon * math.sqrt(rayon**2 + hauteur**2)
    surface = aire_base + aire_lateral
    return surface

r = float(input("Entrez le rayon du cône: "))
h = float(input("Entrez la hauteur du cône: "))

print("Rayon saisi:", r)
print("Hauteur saisie:", h)

resultat = surface_cone(r, h)

print("La surface totale du cône est de", resultat, "cm²")
```
{{% /notice %}}

---

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **premier examen** (15%)

1. Lire la matière sur [Décider avec if, elif, else et les opérateurs](../semaine5/)
2. Faire les [exercices se trouvant à la fin de la leçon 5](../semaine5/#exercices-à-faire-avant-le-cours)