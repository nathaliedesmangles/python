+++
title = "Fonctions personnalisées, docstring et test unitaires et Maths"
weight = 2
+++

Contenu :

* Les **fonctions personnalisées**
* La **documentation (docstring)**
* Les **tests unitaires avec PyTest**
* Les **fonctions arithmétiques intégrées** (`min`, `max`, `sum`, `abs`, etc.)
* Le **module `math`**

---

## Objectifs de la séance (2 heures)

À la fin de cette séance, l’étudiant(e) sera capable de :

* Utiliser les fonctions arithmétiques intégrées et du module `math`
* Créer ses propres fonctions avec paramètres et valeurs de retour
* Documenter ses fonctions avec des `docstrings`
* Écrire des tests unitaires simples avec `pytest`

---

## Déroulement de la séance

### 🔹 0:00 – 0:10 | Accueil et plan de la séance

* Brève discussion : Pourquoi utiliser des fonctions ?
* Présentation du plan :

  1. Fonctions arithmétiques et `math`
  2. Fonctions personnalisées
  3. Docstrings
  4. Tests unitaires

---

### 🔹 0:10 – 0:30 | Bloc 1 — Fonctions arithmétiques et module `math`

#### Fonctions intégrées (10 min)

* Présentation : `min()`, `max()`, `sum()`, `abs()`, `round()`
* **Exemples** :

```python
nombres = [3, 7, -5, 10]
print(min(nombres))  # -5
print(sum(nombres))  # 15
print(abs(-9.2))     # 9.2
```

#### Petit défi (5 min)

Trouver la **valeur moyenne** d'une liste de nombres, sans utiliser de module externe.

#### Module `math` (5 min)

* Importation : `import math`
* Fonctions utiles : `math.sqrt()`, `math.pow()`, `math.log()`, `math.sin()`, `math.pi`, `math.e`

**Exemples** :

```python
import math
print(math.sqrt(25))       # 5.0
print(math.log(100, 10))   # 2.0
print(math.pi)             # 3.1415...
```

---

### 🔹 0:30 – 1:00 | Bloc 2 — Fonctions personnalisées

#### Explication interactive (10 min)

* Syntaxe de `def`
* Paramètres, arguments
* `return` vs affichage

#### Exercice guidé (15 min)

Créer une fonction `energie_cinetique(masse, vitesse)` avec retour de valeur.

#### Exercice autonome (5 min)

Créer une fonction `energie_potentielle(m, h)` avec `g = 9.81`.

---

### 🔹 1:00 – 1:15 | Bloc 3 — Docstrings

#### Présentation (5 min)

* Format standard

```python
def nom_fonction(param):
    """
    Description de la fonction.

    Paramètres:
    - param (type): Description.

    Retour:
    - type: Description.
    """
```

#### Exercice (10 min)

Ajouter une docstring aux fonctions `energie_cinetique` et `energie_potentielle`.

---

### 🔹 1:15 – 1:45 | Bloc 4 — Tests unitaires avec `pytest`

#### ⚙️ Présentation (5 min)

* Pourquoi tester ?
* Syntaxe avec `assert`

#### Exercice guidé (15 min)

Créer un fichier `test_physics.py` :

```python
from mon_module import energie_cinetique

def test_energie_cinetique():
    assert energie_cinetique(2, 3) == 9.0
```

Lancer `pytest` dans le terminal.

#### Défi bonus (10 min)

Tester une fonction utilisant `math.sqrt()` (ex. : vitesse calculée à partir de l’énergie).

---

### 🔹 1:45 – 2:00 | Consolidation, Q\&R

* Résumé des notions vues.
* Questions-réponses.
* Suggestions d’exercices maison :

  * Fonctions pour des calculs en cinématique (ex. accélération)
  * Ajouter docstrings et tests
  * Explorer plus de fonctions dans `math` (ex. trigonométrie)


